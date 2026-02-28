# QUDT Schema Fixes

## Overview

The QUDT LinkML schema had several critical issues preventing generation. This document describes the problems encountered and fixes applied.

## Issues Fixed

### 1. Circular References (Infinite Recursion)

**Problem:** The schema contained circular `is_a` and `mixins` references causing infinite recursion during schema resolution.

**Fixes:**
- **EnumeratedValue** (line 276): Removed self-reference in mixins - class had itself as a mixin
- **Enumeration** (line 307): Removed self-reference in mixins - class had itself as a mixin
- **NumericUnion** (line 397): Removed `is_a: numericUnion` - referenced non-existent lowercase variant
- **Statement** (line 791): Removed `is_a: Statement` - class inherited from itself
- **literal slot** (line 1618): Removed `is_a: literal` - slot inherited from itself

**Why:** Circular inheritance creates infinite loops during schema traversal, causing RecursionError.

### 2. Undefined Type Ranges

**Problem:** Slots referenced range types that don't exist in LinkML or the schema.

**Fixes:**
- **HTML** → **string** (lines 1440, 1567): Changed undefined `HTML` type to built-in `string`
- **anyURI** → **uri** (lines 1632, 1644, 1658, 1662): Changed XML Schema type to LinkML built-in
- **xsd:float** → **float**: Changed XSD types to LinkML built-in types
- **xsd:boolean** → **boolean**
- **xsd:double** → **double**
- **xsd:decimal** → **decimal**

**Why:** LinkML uses its own built-in types. XSD types need to be mapped to LinkML equivalents.

### 3. Invalid Class Inheritance

**Problem:** Classes inheriting from types instead of other classes.

**Fixes:**
- **LatexString** (line 981): Removed `is_a: string` - `string` is a type, not a class

**Why:** Classes can only inherit from other classes, not from primitive types.

### 4. Invalid Slot References

**Problem:** Slots referencing non-existent parent slots.

**Fixes:**
- **ucumCode** (line 1589): Removed `is_a: notation` - `notation` slot doesn't exist

**Why:** Slot inheritance requires the parent slot to be defined.

### 5. Missing Base Class

**Problem:** Multiple classes inherited from `Thing` but it wasn't defined.

**Fixes:**
- Added `Thing` class as root class with `class_uri: owl:Thing`
- Added `owl` prefix to support OWL vocabulary references

**Why:** All classes referencing `Thing` as parent need it to be defined in the schema.

### 6. Missing Directory Structure

**Problem:** Generation attempted to write to non-existent directory.

**Fixes:**
- Created `src/linkml_qudt/datamodel/` directory

**Why:** The justfile expects this directory to exist for generated Python models.

## Result

After these fixes, `just gen-project` runs successfully and generates all artifacts including Python models, JSON Schema, OWL, GraphQL, and documentation. Minor warnings remain about undefined prefixes (dc, dtype, vaem, rdfs, rdf) but these don't prevent generation.
