# Environment variables with defaults
schema_name := 'linkml_qudt'
source_schema_dir := "src" / schema_name / "schema"

# Kroki server URL for diagram generation (leave empty to use default)
kroki_server := "https://kroki.r4.v-lad.org"

# Directory variables
pymodel := "src" / schema_name / "datamodel"
source_schema_path := source_schema_dir / schema_name + ".yaml"
dest := "project"
gen_project_excludes := "-X graphql -X markdown -X excel"

# List all commands as default command. The prefix "_" hides the command.
_default:
    @just --list

# Clean all generated files
[group('project management')]
clean: _clean_project
  rm -rf tmp
  rm -rf docs/elements
  rm -rf datadict

# (Re-)Generate project and documentation locally
[group('model development')]
site: gen-project gen-schema

# Deploy documentation site to Github Pages
[group('deployment')]
deploy: site
  mkd-gh-deploy

# Run all tests
[group('model development')]
test: _test-schema _test-examples

# Run linting
[group('model development')]
lint:
  uv run --group dev linkml-lint {{source_schema_dir}}

# Generate md documentation for the schema
[group('model development')]
gen-schema:
  -mkdir -p docs/schema
  uv run --group dev gen-yaml {{source_schema_path}} > "docs/schema/{{schema_name}}.yaml"

# Build docs and run test server
[group('model development')]
testdoc: _serve

gen-python:
  uv run --group dev gen-project -d  {{pymodel}} -I python {{source_schema_path}}
  uv run --group dev gen-pydantic {{source_schema_path}} > {{pymodel}}/{{schema_name}}_pydantic.py

# Generate project files including Python data model
[group('model development')]
gen-project: gen-python
  mkdir -p {{dest}}/owl
  uv run --group dev gen-owl {{source_schema_path}} > {{dest}}/owl/{{schema_name}}.owl.ttl || true
  mkdir -p {{dest}}/typescript
  uv run --group dev gen-typescript {{source_schema_path}} > {{dest}}/typescript/{{schema_name}}.ts || true
  mkdir -p datadict/images
  uv run --group dev gen-markdown-datadict --debug --anchor-style mkdocs \
    {{ if kroki_server != "" { "--kroki-server " + kroki_server } else { "" } }} \
    --diagram-dir datadict/images \
    --pretty-format-svg {{source_schema_path}} > datadict/datadict.md

# Locally serve data dictionary
[group('model development')]
serve-data-dict: gen-project
  cd datadict
  uv run --group dev grip --wide --with-mermaid --case-insensitive-anchors datadict.md localhost:6420 --norefresh


# Serve documentation site locally
[group('documentation')]
serve-docs: gen-project
  uv run --group dev mkdocs serve

# Build documentation site
[group('documentation')]
build-docs: gen-project
  uv run --group dev mkdocs build

# Deploy documentation site to GitHub Pages
[group('documentation')]
deploy-docs:
  uv run --group dev mkdocs gh-deploy --force

# Test schema generation
_test-schema:
  uv run --group dev gen-project -C config.yaml  {{gen_project_excludes}} -d tmp {{source_schema_path}}


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

# Run documentation server
_serve:
  uv run --group dev mkdocs serve

_export-datadict-html:
  @echo "Exporting enhanced data dictionary to HTML..."
  cd datadict && uv run --group dev grip --with-mermaid --case-insensitive-anchors datadict.md --export datadict.html
  @echo "Generated: datadict/datadict.html (with visual Mermaid diagrams)"

_clean_project:
    #!/usr/bin/env python3
    import shutil, pathlib
    # remove the generated project files
    for d in pathlib.Path("project").iterdir():
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
