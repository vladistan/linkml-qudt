# QUDT LinkML Model

## Welcome

This is a **LinkML model** for the [QUDT (Quantities, Units, Dimensions and Types)](https://qudt.org) ontology. QUDT provides a comprehensive vocabulary for describing physical quantities, units of measure, and their relationships in a machine-readable format.

!!! warning "Early Stage Project"
    This is a **first draft attempt** at converting the QUDT ontology to LinkML. It likely contains issues and limitations. In a very likely
    event you find a problem please file a [GitHub Issue](https://github.com/vladistan/linkml-qudt/issues) here. Or submit a pull request with your suggested improvement!

## Quick Links

<div class="grid cards" markdown>

- :material-book-open-variant: **[About This Project](about.md)**

    Learn about the conversion process, tools used, and known limitations

- :material-file-document: **[Data Dictionary](datadict.md)**

    Browse the comprehensive data dictionary with class diagrams and documentation

- :material-github: **[GitHub Repository](https://github.com/vladistan/linkml-qudt)**

    Access the source code, issues, and contribute

</div>

## What is QUDT?

QUDT is an ontology that provides:

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

## Get Started

### Installation

```bash
# Clone the repository
git clone https://github.com/vladistan/linkml-qudt.git
cd linkml-qudt

# Install dependencies
uv sync --group dev

```

### Explore the Model

- **[Browse the Data Dictionary](datadict.md)** - Visual exploration with class diagrams
- **[Read About the Project](about.md)** - Details about the conversion process and known issues
- **[GitHub Repository](https://github.com/vladistan/linkml-qudt)** -- Source code 

## Resources

- [QUDT Website](https://qudt.org)
- [LinkML Documentation](https://linkml.io)
