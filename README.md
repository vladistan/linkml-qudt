# QUDT LinkML Model

## Overview

This is a **first draft attempt** to create a [LinkML](https://linkml.io) model from the [QUDT (Quantities, Units, Dimensions and Types)](https://qudt.org) ontology. QUDT is a comprehensive ontology that provides a structured vocabulary for describing physical quantities, units of measure, and their relationships.

**This is an initial attempt and likely contains numerous issues.** Suggestions and contributions on how to make this more useful are very welcome!

## Original QUDT Files

The original QUDT ontology files are vendored in the `original/` directory:

- [original/qudt.ttl](https://github.com/vladistan/linkml-qudt/blob/main/original/qudt.ttl) - QUDT ontology in Turtle format
- [original/qudt.ofn](https://github.com/vladistan/linkml-qudt/blob/main/original/qudt.ofn) - QUDT ontology in OWL Functional Syntax

## Important Files (Start Here)

- **[Data Dictionary](datadict.md)** - Single page data dictionary (Look here first)
- **[src/linkml_qudt/schema/linkml_qudt.yaml](https://github.com/vladistan/linkml-qudt/blob/main/src/linkml_qudt/schema/linkml_qudt.yaml)** - The main LinkML schema
- **[src/linkml_qudt/datamodel/linkml_qudt_pydantic.py](https://github.com/vladistan/linkml-qudt/blob/main/src/linkml_qudt/datamodel/linkml_qudt_pydantic.py)** - Pydantic v2 model

### Additional Generated Artifacts

The `project/` directory contains various generated artifacts:

- [project/jsonld/](https://github.com/vladistan/linkml-qudt/tree/main/project/jsonld) - JSON-LD context and schema
- [project/jsonschema/](https://github.com/vladistan/linkml-qudt/tree/main/project/jsonschema) - JSON Schema validation files
- [project/owl/](https://github.com/vladistan/linkml-qudt/tree/main/project/owl) - OWL/RDF representation (Turtle format)
- [project/shacl/](https://github.com/vladistan/linkml-qudt/tree/main/project/shacl) - SHACL validation shapes
- [project/shex/](https://github.com/vladistan/linkml-qudt/tree/main/project/shex) - ShEx schemas
- [project/protobuf/](https://github.com/vladistan/linkml-qudt/tree/main/project/protobuf) - Protocol Buffers definitions
- [project/sqlschema/](https://github.com/vladistan/linkml-qudt/tree/main/project/sqlschema) - SQL DDL schemas
- [project/typescript/](https://github.com/vladistan/linkml-qudt/tree/main/project/typescript) - TypeScript type definitions
- [project/prefixmap/](https://github.com/vladistan/linkml-qudt/tree/main/project/prefixmap) - Prefix mappings
- [src/linkml_qudt/datamodel/linkml_qudt.py](https://github.com/vladistan/linkml-qudt/blob/main/src/linkml_qudt/datamodel/linkml_qudt.py) - Python dataclasses

## Conversion Process

This LinkML model was created through a two-step automated conversion
process. First, the [ROBOT](http://robot.obolibrary.org/) tool was
used to convert the published QUDT ontology files to OWL Functional
Syntax (OFN) format. Then, [Schema
Automator](https://github.com/linkml/schema-automator) was applied
to generate the LinkML model from the OFN representation.

### Manual Corrections Applied

Unfortunately, the automated conversion process did not yield a usable LinkML schema. The generated output had several structural and type issues. The following corrections were made
to make the schema useful.

- Replaced auto-generated types with LinkML standard types (e.g., `string`, `uriList`, `stringList`)
- Added standard ontology prefixes (`owl`, `rdf`, `rdfs`, `dc`, `dcterms`, `prov`, `voag`, `vaem`, `dtype`)
- Fixed issues with the `PhysicalConstant` class definition
- General cleanup and normalization of schema structure
- Removed redundant `Thing` mixin from `Comment` class (already directly inherited)


## Known Issues & Limitations

**This is a first draft with known limitations:**

- The automated conversion may not have captured all semantic nuances from the QUDT ontology
- Some complex OWL patterns may not translate perfectly to LinkML
- Not all QUDT constraints may be fully represented
- The model may require additional validation rules
- Some class hierarchies may need refinement
- Some attributes did not transfer from the original ontology. For example all most of the DublinCore metatadata attributes are missing from the LinkML model.  Looks like they could be added with an addtional automated step.
- So far only classess from main ontology were transferred. We need to transfer individuals.

## Development

### Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

### Installation

```bash
# Install dependencies
uv sync --group dev

```

### Regenerate Artifacts

```bash
# Regenerate all project artifacts
just gen-project

# Regenerate with Kroki diagrams (requires Kroki server)
just gen-project-kroki-files
```

### Documentation Website

This project includes a static documentation website built with MkDocs:

```bash
# Serve documentation locally (auto-updates on file changes)
just serve-docs

# Build static site to site/ directory
just build-docs

# Deploy to GitHub Pages
just deploy-docs
```

The documentation site includes:
- **Home** - Overview and quick links
- **About** - This README content
- **Data Dictionary** - Comprehensive model documentation with diagrams
- **Schema** - Direct access to the LinkML YAML schema

Visit the live site at: https://vladistan.github.io/linkml-qudt

## Contributing

**We welcome contributions!** This is an early draft and there's much room for improvement. Areas where help is particularly appreciated:

- ✅ Improving the schema structure and class hierarchies
- ✅ Adding better documentation and examples
- ✅ Identifying and fixing conversion issues
- ✅ Adding validation rules and constraints
- ✅ Creating example data and use cases
- ✅ Improving alignment with QUDT semantics
- ✅ Testing and validation

Please open an issue or pull request if you have suggestions or improvements!

## Related Resources

- **LinkML**: https://linkml.io
- **LinkML Documentation**: https://linkml.io/linkml/
- **QUDT**: https://qudt.org
- **ROBOT**: http://robot.obolibrary.org/
- **Schema Automator**: https://github.com/linkml/schema-automator

## License

The QUDT ontology is licensed under [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). Please refer to the [QUDT license page](https://qudt.org/pages/QUDToverviewPage.html) for details.

This LinkML model derivative is provided as-is for community use and improvement.

## Contact

For questions or suggestions about this LinkML model, please open an issue in this repository.

For questions about QUDT itself, please refer to the [QUDT community resources](https://qudt.org).
