# QUDT LinkML Model

[![Documentation](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://vladistan.github.io/linkml-qudt/)
[![Open in Codespaces](https://img.shields.io/badge/Open%20in-Codespaces-blue?logo=github)](https://codespaces.new/vladistan/linkml-qudt)

A [LinkML](https://linkml.io) model for the [QUDT (Quantities, Units, Dimensions and Types)](https://qudt.org) ontology.

> **⚠️ Early Stage Project**: This is a first draft attempt at converting the QUDT ontology to LinkML. It likely contains issues and limitations. Please report problems via [GitHub Issues](https://github.com/vladistan/linkml-qudt/issues)!

## Quick Links

- 📘 **[Documentation Site](https://vladistan.github.io/linkml-qudt/)** - Full documentation with interactive diagrams
- 📊 **[Data Dictionary](https://vladistan.github.io/linkml-qudt/datadict/)** - Browse all classes and slots
- 📄 **[Schema File](src/linkml_qudt/schema/linkml_qudt.yaml)** - Main LinkML schema
- 🐍 **[Pydantic Models](src/linkml_qudt/datamodel/linkml_qudt_pydantic.py)** - Type-safe Python models

## What This Provides

- QUDT main ontology class hierarchy in LinkML format
- Generated artifacts in multiple formats:
  - Python dataclasses and Pydantic models
  - JSON Schema, TypeScript, SQL DDL
  - OWL/RDF, SHACL, ShEx (OWL is regenerated from LinkML)
  - Protocol Buffers, Prefix maps
- Documentation
- Validation tools and examples (TODO)

See the **[project/](project/)** directory for all generated artifacts.

## Development

### Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv)

### Installation

```bash
# Install dependencies
uv sync --group dev

```

### Regenerate Artifacts

```bash
# Regenerate all project artifacts
just gen-project
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

Visit the live site at: **https://vladistan.github.io/linkml-qudt**

## Contributing

**We welcome contributions!** This is an early draft and there's much room for improvement. Areas where help is particularly appreciated:

- Improving the schema structure and class hierarchies
- Adding better documentation and examples
- Identifying and fixing conversion issues
- Adding validation rules and constraints
- Creating example data and use cases
- Improving alignment with QUDT semantics
- Testing and validation

Please open an issue or pull request if you have suggestions or improvements!

## Resources

- [LinkML](https://linkml.io) - Modeling language framework
- [QUDT](https://qudt.org) - Quantities, Units, Dimensions and Types ontology
- [Documentation Site](https://vladistan.github.io/linkml-qudt) - Full project documentation

## License

The QUDT ontology is licensed under [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). Please refer to the [QUDT license page](https://qudt.org/pages/QUDToverviewPage.html) for details.

This LinkML model derivative is provided as-is for community use and improvement.

## Questions?

- **This LinkML model**: [Open an issue](https://github.com/vladistan/linkml-qudt/issues)
- **QUDT ontology**: [QUDT community resources](https://qudt.org)
