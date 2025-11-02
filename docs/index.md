# QUDT LinkML Model

## Welcome

This is a **LinkML model** for the [QUDT (Quantities, Units, Dimensions and Types)](https://qudt.org) ontology. QUDT provides a comprehensive vocabulary for describing physical quantities, units of measure, and their relationships in a machine-readable format.

!!! warning "Early Stage Project"
    This is a **first draft attempt** at converting the QUDT ontology to LinkML. It likely contains issues and limitations. We welcome suggestions and contributions!

## Quick Links

<div class="grid cards" markdown>

- :material-book-open-variant: **[About This Project](about.md)**

    Learn about the conversion process, tools used, and known limitations

- :material-file-document: **[Data Dictionary](datadict.md)**

    Browse the comprehensive data dictionary with class diagrams and documentation

- :material-code-json: **[Schema](schema.md)**

    View the LinkML YAML schema

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

## Key Features

=== "Python Integration"

    ```python
    from linkml_qudt.datamodel.linkml_qudt_pydantic import Unit, Quantity

    # Create a unit
    meter = Unit(id="http://qudt.org/vocab/unit/M", symbol="m")

    # Work with quantities
    length = Quantity(value=5.0, unit=meter)
    ```

=== "Generated Artifacts"

    - **Pydantic Models** - Type-safe Python models
    - **JSON Schema** - For validation
    - **OWL/RDF** - Semantic web formats
    - **SQL DDL** - Database schemas
    - **TypeScript** - Type definitions
    - **And more...**

=== "Validation"

    ```bash
    # Validate instance data
    linkml-validate -s src/linkml_qudt/schema/linkml_qudt.yaml data.yaml

    # Generate other formats
    gen-json-schema src/linkml_qudt/schema/linkml_qudt.yaml
    gen-pydantic src/linkml_qudt/schema/linkml_qudt.yaml
    ```

## Get Started

### Installation

```bash
# Clone the repository
git clone https://github.com/vladistan/linkml-qudt.git
cd linkml-qudt

# Install dependencies
uv sync --group dev

# Or with pip
pip install -e .
```

### Explore the Model

- **[Browse the Data Dictionary](datadict.md)** - Visual exploration with class diagrams
- **[Read About the Project](about.md)** - Conversion process and details
- **[View the Schema](schema.md)** - Raw LinkML YAML schema

## Contributing

This is an early-stage project and we welcome contributions! See the [About page](about.md#contributing) for areas where help is needed.

## Resources

- [QUDT Website](https://qudt.org)
- [LinkML Documentation](https://linkml.io)
- [GitHub Repository](https://github.com/vladistan/linkml-qudt)
