# About This Project

## Overview

This is a [LinkML](https://linkml.io) model for the [QUDT (Quantities, Units, Dimensions and Types)](https://qudt.org) ontology. QUDT is a comprehensive ontology that provides a structured vocabulary for describing physical quantities, units of measure, and their relationships.

!!! warning "Early Stage Project"
    This is a **first draft attempt** at converting the QUDT ontology to LinkML. It likely contains issues and limitations. In a very likely event you find a problem please file a [GitHub Issue](https://github.com/vladistan/linkml-qudt/issues) here. Or submit a pull request with your suggested improvement!

## What is QUDT?

QUDT provides a comprehensive vocabulary for:

- **Quantity Kinds** - Observable properties that can be measured (e.g., length, mass, temperature)
- **Units** - Standard units of measurement (e.g., meter, kilogram, kelvin)
- **Dimensions** - Fundamental dimensions (e.g., length, mass, time)
- **Relationships** - Connections between quantities, units, and dimensions

## What is LinkML?

[LinkML](https://linkml.io) is a modeling language for describing data structures and schemas. It provides:

- **Multiple serialization formats** - Generate JSON Schema, Pydantic, Python, TypeScript, SQL, and more
- **Validation** - Validate data against schemas
- **Documentation** - Auto-generate comprehensive documentation
- **Interoperability** - Bridge between different data formats and systems

## Key Features

This LinkML model provides:

- Comprehensive class hierarchy from QUDT
- Generated artifacts in multiple formats (Python, TypeScript, JSON Schema, OWL, etc.)
- Interactive documentation with diagrams
- Pydantic v2 models for type-safe Python development

## Conversion Process

This LinkML model was created through an automated conversion process with the following steps:

- Used [ROBOT](http://robot.obolibrary.org/) tool to convert the published QUDT ontology files to OWL Functional Syntax (OFN) format
- Applied [Schema Automator](https://github.com/linkml/schema-automator) to generate the LinkML model from the OFN representation
- Made manual corrections to address issues in the automated conversion (see below)

### Manual Corrections Applied

Unfortunately, the automated conversion process did not yield a usable LinkML schema. The generated output had several structural and type issues. The following corrections were made to make the schema useful:

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
- Most Dublin Core metadata attributes are missing from the LinkML model (could be added with an additional automated step)
- Only classes from main ontology were transferred; individuals need to be transferred

## Project Files

The project repository contains:

- **Main Schema**: [src/linkml_qudt/schema/linkml_qudt.yaml](https://github.com/vladistan/linkml-qudt/blob/main/src/linkml_qudt/schema/linkml_qudt.yaml)
- **Pydantic Model**: [src/linkml_qudt/datamodel/linkml_qudt_pydantic.py](https://github.com/vladistan/linkml-qudt/blob/main/src/linkml_qudt/datamodel/linkml_qudt_pydantic.py)
- **Python Dataclasses**: [src/linkml_qudt/datamodel/linkml_qudt.py](https://github.com/vladistan/linkml-qudt/blob/main/src/linkml_qudt/datamodel/linkml_qudt.py)
- **Generated Artifacts**: [project/](https://github.com/vladistan/linkml-qudt/tree/main/project) - JSON Schema, OWL, TypeScript, etc.
- **Original QUDT Files**: [original/](https://github.com/vladistan/linkml-qudt/tree/main/original) - Vendored QUDT ontology files

## Contributing

**We welcome contributions!** This is an early draft and there's much room for improvement. Areas where help is particularly appreciated:

- Improving the schema structure and class hierarchies
- Adding better documentation and examples
- Identifying and fixing conversion issues
- Adding validation rules and constraints
- Creating example data and use cases
- Improving alignment with QUDT semantics
- Testing and validation

Please open an [issue](https://github.com/vladistan/linkml-qudt/issues) or [pull request](https://github.com/vladistan/linkml-qudt/pulls) if you have suggestions or improvements!

## Resources

- **QUDT Website**: [qudt.org](https://qudt.org)
- **LinkML Documentation**: [linkml.io](https://linkml.io)
- **GitHub Repository**: [vladistan/linkml-qudt](https://github.com/vladistan/linkml-qudt)
- **ROBOT Tool**: [robot.obolibrary.org](http://robot.obolibrary.org/)
- **Schema Automator**: [github.com/linkml/schema-automator](https://github.com/linkml/schema-automator)

## License

The QUDT ontology is licensed under [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). Please refer to the [QUDT license page](https://qudt.org/pages/QUDToverviewPage.html) for details.

This LinkML model derivative is provided as-is for community use and improvement.

## Contact

For questions or suggestions about this LinkML model, please open an [issue in the GitHub repository](https://github.com/vladistan/linkml-qudt/issues).

For questions about QUDT itself, please refer to the [QUDT community resources](https://qudt.org).
