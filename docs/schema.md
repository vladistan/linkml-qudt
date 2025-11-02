# LinkML Schema

## Overview

The QUDT LinkML schema is the core definition file that describes all classes, slots, enumerations, and types in the QUDT model.

## Schema File

**Location**: [`src/linkml_qudt/schema/linkml_qudt.yaml`](https://github.com/vladistan/linkml-qudt/blob/main/src/linkml_qudt/schema/linkml_qudt.yaml)

## Schema Metadata

```yaml
name: qudt
description: qudt
id: http://qudt.org/3.1.6/schema/qudt
imports:
  - linkml:types
```

## Key Components

### Prefixes

The schema uses standard ontology prefixes:

- `qudt:` - QUDT namespace
- `owl:` - Web Ontology Language
- `rdf:` - RDF namespace
- `rdfs:` - RDF Schema
- `dc:`, `dcterms:` - Dublin Core
- `prov:` - Provenance ontology
- And more...

### Main Class Hierarchy

The schema defines a comprehensive class hierarchy starting from `Thing` (owl:Thing):

- **Quantities** - AbstractQuantityKind, QuantityKind, etc.
- **Units** - Unit, DerivedUnit, PrefixedUnit, etc.
- **Dimensions** - DimensionVector, QuantityKindDimensionVector
- **Constants** - PhysicalConstant, ConstantValue
- **Systems** - SystemOfQuantityKinds, SystemOfUnits
- **Enumerations** - Various encoding types, alignment types, etc.

### View Full Schema

For the complete schema definition, you can:

1. **[View on GitHub](https://github.com/vladistan/linkml-qudt/blob/main/src/linkml_qudt/schema/linkml_qudt.yaml)** - Browse the YAML file online

2. **Clone the repository** and view locally:
   ```bash
   git clone https://github.com/vladistan/linkml-qudt.git
   cd linkml-qudt
   cat src/linkml_qudt/schema/linkml_qudt.yaml
   ```

3. **[Browse the Data Dictionary](datadict.md)** - Human-friendly documentation with diagrams

## Using the Schema

### Validation

```bash
# Validate instance data
linkml-validate -s src/linkml_qudt/schema/linkml_qudt.yaml data.yaml
```

### Generate Code

```bash
# Python dataclasses
gen-python src/linkml_qudt/schema/linkml_qudt.yaml > model.py

# Pydantic models
gen-pydantic src/linkml_qudt/schema/linkml_qudt.yaml > model_pydantic.py

# JSON Schema
gen-json-schema src/linkml_qudt/schema/linkml_qudt.yaml > schema.json

# TypeScript types
gen-typescript src/linkml_qudt/schema/linkml_qudt.yaml > model.ts
```

### Generate Documentation

```bash
# Markdown documentation
gen-doc -d docs src/linkml_qudt/schema/linkml_qudt.yaml

# Data dictionary with diagrams
gen-markdown-datadict src/linkml_qudt/schema/linkml_qudt.yaml > datadict.md
```

## Conversion History

This schema was created through automated conversion from the QUDT OWL ontology using:

- [ROBOT](http://robot.obolibrary.org/) - Ontology transformation
- [Schema Automator](https://github.com/linkml/schema-automator) - OWL to LinkML conversion

Manual corrections were then applied. See the [About page](about.md#manual-corrections-applied) for details.

## Schema Development

To modify the schema:

1. Edit `src/linkml_qudt/schema/linkml_qudt.yaml`
2. Regenerate artifacts:
   ```bash
   just gen-project
   ```
3. Run tests:
   ```bash
   just test
   ```
4. Lint the schema:
   ```bash
   just lint
   ```

## Related Files

- **[Data Dictionary](datadict.md)** - Human-readable documentation
- **[About](about.md)** - Project overview and conversion details
- **Generated Artifacts** - See the `project/` directory for all generated formats
