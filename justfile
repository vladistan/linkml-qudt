# Environment variables with defaults
schema_name := 'linkml_qudt'
source_schema_dir := "src" / schema_name / "schema"
gen_project_excludes := "-X graphql -X markdown -X excel"

# Directory variables
src := "src"
dest := "project"
pymodel := src / schema_name / "datamodel"
source_schema_path := source_schema_dir / schema_name + ".yaml"
docdir := "docs/elements"  # Directory for generated documentation
merged_schema_path := "docs/schema" / schema_name + ".yaml"

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
  rm -rf docs/elements

# (Re-)Generate project and documentation locally

[group('model development')]
site: gen-project

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
  uv run --group dev gen-doc -d {{docdir}} {{source_schema_path}}




# Build docs and run test server
[group('model development')]
testdoc: update-docs _serve

gen-python:
  uv run --group dev gen-project -d  {{pymodel}} -I python {{source_schema_path}}
  uv run --group dev gen-pydantic {{source_schema_path}} > {{pymodel}}/{{schema_name}}_pydantic.py

# Generate project files including Python data model
[group('model development')]
gen-project:
  uv run --group dev gen-project {{gen_project_excludes}} -d {{dest}} {{source_schema_path}}
  uv run --group dev gen-pydantic {{source_schema_path}} > {{pymodel}}/{{schema_name}}_pydantic.py
  mv {{dest}}/*.py {{pymodel}}
  mkdir -p {{dest}}/owl
  uv run --group dev gen-owl {{source_schema_path}} > {{dest}}/owl/{{schema_name}}.owl.ttl || true ; \
  mkdir -p {{dest}}/typescript
  uv run --group dev gen-typescript {{source_schema_path}} > {{dest}}/typescript/{{schema_name}}.ts || true ; \
  uv run --group dev gen-markdown-datadict --debug --anchor-style mkdocs {{source_schema_path}} > {{dest}}/datadict.md

# Generate project with SVG diagrams rendered via Kroki server
[group('model development')]
gen-project-kroki kroki_server="https://kroki.r4.v-lad.org":
  uv run --group dev gen-project {{gen_project_excludes}} -d {{dest}} {{source_schema_path}}
  uv run --group dev gen-pydantic {{source_schema_path}} > {{pymodel}}/{{schema_name}}_pydantic.py
  mv {{dest}}/*.py {{pymodel}}
  mkdir -p {{dest}}/owl
  uv run --group dev gen-owl {{source_schema_path}} > {{dest}}/owl/{{schema_name}}.owl.ttl || true ; \
  mkdir -p {{dest}}/typescript
  uv run --group dev gen-typescript {{source_schema_path}} > {{dest}}/typescript/{{schema_name}}.ts || true ; \
  uv run --group dev gen-markdown-datadict --debug --anchor-style mkdocs --kroki-server {{kroki_server}} {{source_schema_path}} > {{dest}}/datadict.md

# Generate project with SVG diagrams saved as separate files
[group('model development')]
gen-project-kroki-files kroki_server="https://kroki.r4.v-lad.org" diagram_dir="project/images":
  uv run --group dev gen-project {{gen_project_excludes}} -d {{dest}} {{source_schema_path}}
  uv run --group dev gen-pydantic {{source_schema_path}} > {{pymodel}}/{{schema_name}}_pydantic.py
  mv {{dest}}/*.py {{pymodel}}
  mkdir -p {{dest}}/owl
  uv run --group dev gen-owl {{source_schema_path}} > {{dest}}/owl/{{schema_name}}.owl.ttl || true ; \
  mkdir -p {{dest}}/typescript
  uv run --group dev gen-typescript {{source_schema_path}} > {{dest}}/typescript/{{schema_name}}.ts || true ; \
  uv run --group dev gen-markdown-datadict --debug --anchor-style mkdocs --kroki-server {{kroki_server}} --diagram-dir {{diagram_dir}} --pretty-format-svg {{source_schema_path}} > {{dest}}/datadict.md

# Generate project with SVG diagrams with clickable links (for GitHub Pages or other hosted docs)
[group('model development')]
gen-project-kroki-linked kroki_server="https://kroki.r4.v-lad.org" diagram_dir="project/images" base_url="https://example.com/schema":
  uv run --group dev gen-project {{gen_project_excludes}} -d {{dest}} {{source_schema_path}}
  uv run --group dev gen-pydantic {{source_schema_path}} > {{pymodel}}/{{schema_name}}_pydantic.py
  mv {{dest}}/*.py {{pymodel}}
  mkdir -p {{dest}}/owl
  uv run --group dev gen-owl {{source_schema_path}} > {{dest}}/owl/{{schema_name}}.owl.ttl || true ; \
  mkdir -p {{dest}}/typescript
  uv run --group dev gen-typescript {{source_schema_path}} > {{dest}}/typescript/{{schema_name}}.ts || true ; \
  uv run --group dev gen-markdown-datadict --debug --anchor-style mkdocs --kroki-server {{kroki_server}} --diagram-dir {{diagram_dir}} --add-svg-links {{base_url}} --pretty-format-svg {{source_schema_path}} > {{dest}}/datadict.md

# Locally serve data dictionary
[group('model development')]
serve-data-dict:
  cd {{dest}} && uv run --group dev grip --wide --with-mermaid --case-insensitive-anchors datadict.md localhost:6419 --norefresh

# Update documentation site content (symlink README and datadict to docs/)
[group('documentation')]
update-docs:
  rm -f docs/about.md docs/datadict.md
  ln -s ../README.md docs/about.md
  ln -s ../{{dest}}/datadict.md docs/datadict.md
  rm -rf docs/images
  ln -s ../{{dest}}/images docs/images

# Serve documentation site locally
[group('documentation')]
serve-docs: update-docs
  uv run --group dev mkdocs serve

# Build documentation site
[group('documentation')]
build-docs: update-docs
  uv run --group dev mkdocs build

# Deploy documentation site to GitHub Pages
[group('documentation')]
deploy-docs: update-docs
  uv run --group dev mkdocs gh-deploy --force

#gen-project

# Status
[group('project management')]
status:
  @echo "Project: {{schema_name}}"
  @echo "Source: {{source_schema_path}}"


# Test schema generation
_test-schema:
  uv run --group dev gen-project {{gen_project_excludes}} -d tmp {{source_schema_path}}

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
