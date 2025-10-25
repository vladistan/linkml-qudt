# Environment variables with defaults
schema_name := 'linkml_qudt'
source_schema_dir := "src" / schema_name / "schema"
config_yaml := ""
gen_doc_args := ""
gen_java_args := ""
gen_owl_args := ""
gen_pydantic_args := ""
gen_ts_args := ""

# Directory variables
src := "src"
dest := "project"
pymodel := src / schema_name / "datamodel"
source_schema_path := source_schema_dir / schema_name + ".yaml"
docdir := "docs/elements"  # Directory for generated documentation
merged_schema_path := "docs/schema/{{schema_name}}.yaml"

# List all commands as default command. The prefix "_" hides the command.
_default:
    @just --list

# Install project dependencies
[group('project management')]
install:
  uv sync --group dev

# Clean all generated files
[group('project management')]
clean: _clean_project
  rm -rf tmp
  rm -rf {{docdir}}/*.md

# (Re-)Generate project and documentation locally

[group('model development')]
site: gen-project gen-doc

# Deploy documentation site to Github Pages
[group('deployment')]
deploy: site
  mkd-gh-deploy


# Run all tests
[group('model development')]
test: _test-schema _test-python _test-examples

# Run linting
[group('model development')]
lint:
  uv run --group dev linkml-lint {{source_schema_dir}}


# Generate md documentation for the schema
[group('model development')]
gen-doc: _gen-yaml
  uv run --group dev gen-doc {{gen_doc_args}} -d {{docdir}} {{source_schema_path}}

# Build docs and run test server
[group('model development')]
testdoc: gen-doc _serve

gen-python:
  uv run --group dev gen-project -d  {{pymodel}} -I python {{source_schema_path}}
  uv run --group dev gen-pydantic {{gen_pydantic_args}} {{source_schema_path}} > {{pymodel}}/{{schema_name}}_pydantic.py

# Generate project files including Python data model
[group('model development')]
gen-project:
  uv run --group dev gen-project {{config_yaml}} -d {{dest}} {{source_schema_path}}
  uv run --group dev gen-pydantic {{gen_pydantic_args}} {{source_schema_path}} > {{pymodel}}/{{schema_name}}_pydantic.py
  mv {{dest}}/*.py {{pymodel}}
  mkdir -p {{dest}}/owl
  uv run --group dev gen-owl {{gen_owl_args}} {{source_schema_path}} > {{dest}}/owl/{{schema_name}}.owl.ttl || true ; \
  mkdir -p {{dest}}/typescript
  uv run --group dev gen-typescript {{gen_ts_args}} {{source_schema_path}} > {{dest}}/typescript/{{schema_name}}.ts || true ; \
  uv run --group dev gen-markdown-datadict {{source_schema_path}} > {{dest}}/datadict.md

# Locally serve data dictionary
[group('model development')]
serve-data-dict: gen-project
  cd {{dest}} && uv run --user-content --wide --group dev grip --with-mermaid --case-insensitive-anchors datadict.md localhost:6419 --norefresh


# Status
[group('project management')]
status:
  @echo "Project: {{schema_name}}"
  @echo "Source: {{source_schema_path}}"


# Test schema generation
_test-schema:
  uv run --group dev gen-project {{config_yaml}} -d tmp {{source_schema_path}}

# Run Python unit tests with pytest
_test-python: gen-python
  uv run python -m pytest

# Run example tests
_test-examples: _ensure_examples_output
  uv run --group dev linkml-run-examples \
    --input-formats json \
    --input-formats yaml \
    --output-formats json \
    --output-formats yaml \
    --counter-example-input-directory tests/data/invalid \
    --input-directory tests/data/valid \
    --output-directory examples/output \
    --schema {{source_schema_path}} > examples/output/README.md

# Generate merged model
_gen-yaml:
  -mkdir -p docs/schema
  uv run --group dev gen-yaml {{source_schema_path}} > {{merged_schema_path}}

# Run documentation server
_serve:
  uv run --group dev mkdocs serve

_export-datadict-html:
  @echo "Exporting enhanced data dictionary to HTML..."
  cd {{dest}} && uv run --group dev grip --with-mermaid --case-insensitive-anchors datadict.md --export datadict.html
  @echo "Generated: {{dest}}/datadict.html (with visual Mermaid diagrams)"

_clean_project:
    #!/usr/bin/env python3
    import shutil, pathlib
    # remove the generated project files
    for d in pathlib.Path("{{dest}}").iterdir():
      if d.is_dir():
        shutil.rmtree(d, ignore_errors=True)
    # remove the generated python data model
    for d in pathlib.Path("{{pymodel}}").iterdir():
      if d.name == "__init__.py":
        continue
      print(f'removing "{d}"')
      if d.is_dir():
        shutil.rmtree(d, ignore_errors=True)
      else:
        d.unlink()

_ensure_examples_output:  # Ensure a clean examples/output directory exists
  -mkdir -p examples/output
  -rm -rf examples/output/*
