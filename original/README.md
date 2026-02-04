# QUDT Vocabulary Files

Downloaded from [QUDT.org](http://qudt.org/) on 2026-02-04.

## Files

| File | Source URL | Description |
|------|------------|-------------|
| `qudt-shacl.ttl` | http://qudt.org/schema/shacl/qudt | Main QUDT Ontology |
| `datatype.ttl` | https://qudt.org/schema/datatype/ | QUDT Datatype Ontology |
| `units.ttl` | http://qudt.org/vocab/unit | QUDT Units Vocabulary |
| `quantitykind.ttl` | http://qudt.org/vocab/quantitykind | QUDT QuantityKinds Vocabulary |
| `dimensionvector.ttl` | http://qudt.org/vocab/dimensionvector | QUDT DimensionVectors Vocabulary |
| `constant.ttl` | http://qudt.org/vocab/constant | QUDT Physical Constants Vocabulary |
| `sou.ttl` | http://qudt.org/vocab/sou | QUDT Systems of Units Vocabulary |
| `soqk.ttl` | http://qudt.org/vocab/soqk | QUDT Systems of Quantity Kinds Vocabulary |

## Usage in Pokemon

The Pokemon knowledge graph uses only a small subset of QUDT:
- `qudt:Quantity` class (for Berry sizes)
- `qudt:value`, `qudt:unit`, `qudt:quantityValue`, `qudt:hasQuantityKind` predicates
- Units: `unit/MilliM`, `unit/M`, `unit/KiloM`
- QuantityKind: `quantitykind/Height`
