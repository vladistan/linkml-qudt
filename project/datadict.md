
# QUDT


**metamodel version:** 1.7.0

**version:** None


qudt


## Class Diagram

![class_diagram](images/class_diagram.svg)

## ERD Diagram

![erd_diagram](images/erd_diagram.svg)

## Base Classes


Foundational classes in the hierarchy (root classes and direct children of Thing):

| Class | Description |
| --- | --- |
| [Aspect](#aspect) |  |
| [Class](#class) |  |
| [Concept](#concept) |  |
| [Resource](#resource) |  |
| [StringEncodingType](#stringencodingtype) |  |
| [Thing](#thing) | The root class for all QUDT concepts |

## Standalone Classes


These classes are completely isolated with no relationships and are not used as base classes:

| Class | Description |
| --- | --- |
| [AspectClass](#aspectclass) |  |
| [CatalogEntry](#catalogentry) |  |
| [Comment](#comment) |  |
| [DateTimeStringEncodingType](#datetimestringencodingtype) |  |
| [LatexString](#latexstring) |  |
| [List](#list) |  |
| [NISTSP811Comment](#nistsp811comment) |  |
| [Ontology](#ontology) |  |
| [SignednessType](#signednesstype) |  |
| [Statement](#statement) |  |
| [SymmetricRelation](#symmetricrelation) |  |
| [Verifiable](#verifiable) |  |
| [GDay](#gday) |  |
| [GMonth](#gmonth) |  |
| [GMonthDay](#gmonthday) |  |
| [GYear](#gyear) |  |
| [GYearMonth](#gyearmonth) |  |
| [ValueUnion](#valueunion) |  |

## Classes


### AbstractQuantityKind




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
AbstractQuantityKind:
  is_a: Concept
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - AbstractQuantityKind_broader
  - AbstractQuantityKind_altSymbol
  - AbstractQuantityKind_latexSymbol
  - AbstractQuantityKind_symbol
  slot_usage:
    broader:
      range: QuantityKind
    altSymbol:
      required: false
    latexSymbol:
      required: false
    symbol:
      multivalued: false

```
</details>

![class_abstractquantitykind_erd](images/class_abstractquantitykind_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |
| **[altSymbol](#altsymbol)** | <sub>0..\*</sub> | None |  |
| **[latexSymbol](#latexsymbol)** | <sub>0..\*</sub> | None |  |
| **[symbol](#symbol)** | <sub>0..1</sub> | None |  |

#### Parents

 * [Concept](#concept)

#### Children

 * [UserQuantityKind](#userquantitykind)

#### Used as mixin by

 * [QuantityKind](#quantitykind)




### AngleUnit




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
AngleUnit:
  is_a: DimensionlessUnit
  slots:
  - Verifiable_wikidataMatch
  - Verifiable_dbpediaMatch
  - Verifiable_isoNormativeReference
  - Verifiable_normativeReference
  - hasReciprocalUnit
  - isUnitOfSystem
  - omUnit
  - unitFor
  - Unit_applicableSystem
  - Unit_definedUnitOfSystem
  - Unit_derivedCoherentUnitOfSystem
  - Unit_derivedUnitOfSystem
  - Unit_exactMatch
  - Unit_hasDimensionVector
  - Unit_hasFactorUnit
  - Unit_hasQuantityKind
  - Unit_iec61360Code
  - Unit_prefix
  - Unit_qkdvDenominator
  - Unit_qkdvNumerator
  - Unit_scalingOf
  - Unit_ucumCode
  - Unit_udunitsCode
  - Unit_uneceCommonCode
  - Unit_altSymbol
  - Unit_latexDefinition
  - Unit_latexSymbol
  - Unit_siUnitsExpression
  - Unit_symbol
  - Unit_conversionMultiplier
  - Unit_conversionMultiplierSN
  - Unit_conversionOffset
  - Unit_conversionOffsetSN
  - Unit_factorUnitScalar
  - Unit_mathMLdefinition
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription

```
</details>

![class_angleunit_erd](images/class_angleunit_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[altSymbol](#altsymbol)** | <sub>0..\*</sub> | None |  |
| **[applicableSystem](#applicablesystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[conversionMultiplier](#conversionmultiplier)** | <sub>0..1</sub> | None |  |
| **[conversionMultiplierSN](#conversionmultipliersn)** | <sub>0..1</sub> | None |  |
| **[conversionOffset](#conversionoffset)** | <sub>0..1</sub> | None |  |
| **[conversionOffsetSN](#conversionoffsetsn)** | <sub>0..1</sub> | None |  |
| **[dbpediaMatch](#dbpediamatch)** | <sub>0..\*</sub> | uri |  |
| **[definedUnitOfSystem](#definedunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[derivedCoherentUnitOfSystem](#derivedcoherentunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[derivedUnitOfSystem](#derivedunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[exactMatch](#exactmatch)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[factorUnitScalar](#factorunitscalar)** | <sub>0..1</sub> | None |  |
| **[hasDimensionVector](#hasdimensionvector)** | <sub>0..1</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[hasFactorUnit](#hasfactorunit)** | <sub>0..\*</sub> | [Class](#class) |  |
| **[hasQuantityKind](#hasquantitykind)** | <sub>0..\*</sub> | [QuantityKind](#quantitykind) |  |
| **[hasReciprocalUnit](#hasreciprocalunit)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[iec61360Code](#iec61360code)** | <sub>0..\*</sub> | string |  |
| **[isUnitOfSystem](#isunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[isoNormativeReference](#isonormativereference)** | <sub>0..\*</sub> | None |  |
| **[latexDefinition](#latexdefinition)** | <sub>0..\*</sub> | None |  |
| **[latexSymbol](#latexsymbol)** | <sub>0..\*</sub> | None |  |
| **[mathMLdefinition](#mathmldefinition)** | <sub>0..1</sub> | None |  |
| **[normativeReference](#normativereference)** | <sub>0..\*</sub> | None |  |
| **[omUnit](#omunit)** | <sub>0..\*</sub> | None |  |
| **[prefix](#prefix)** | <sub>0..\*</sub> | [Prefix](#prefix) |  |
| **[qkdvDenominator](#qkdvdenominator)** | <sub>0..1</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[qkdvNumerator](#qkdvnumerator)** | <sub>0..1</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[scalingOf](#scalingof)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[siUnitsExpression](#siunitsexpression)** | <sub>0..\*</sub> | None |  |
| **[symbol](#symbol)** | <sub>0..\*</sub> | None |  |
| **[ucumCode](#ucumcode)** | <sub>0..\*</sub> | [UCUMcs](#ucumcs) |  |
| **[udunitsCode](#udunitscode)** | <sub>0..\*</sub> | string |  |
| **[uneceCommonCode](#unececommoncode)** | <sub>0..\*</sub> | string |  |
| **[unitFor](#unitfor)** | <sub>0..\*</sub> | None |  |
| **[wikidataMatch](#wikidatamatch)** | <sub>0..\*</sub> | uri |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |

#### Parents

 * [DimensionlessUnit](#dimensionlessunit)

#### Children

 * [PlaneAngleUnit](#planeangleunit)
 * [SolidAngleUnit](#solidangleunit)




### Aspect



An aspect is an abstract type class that defines properties that can be reused.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
Aspect:
  is_a: Thing

```
</details>


#### Local class diagram

![class_aspect_local](images/class_aspect_local.svg)

This class has no attributes


#### Parents

 * [Thing](#thing) - The root class for all QUDT concepts

#### Children

 * [DataEncoding](#dataencoding)
 * [Quantifiable](#quantifiable)
 * [Verifiable](#verifiable)




### AspectClass




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
AspectClass:
  is_a: Class

```
</details>


#### Local class diagram

![class_aspectclass_local](images/class_aspectclass_local.svg)

This class has no attributes


#### Parents

 * [Class](#class)




### BaseDimensionMagnitude



<p class=\"lm-para\">A <em>Dimension</em> expresses a magnitude for a base quantiy kind such as mass, length and time.</p>
<p class=\"lm-para\">DEPRECATED - each exponent is expressed as a property. Keep until a validaiton of this has been done.</p>


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
BaseDimensionMagnitude:
  is_a: Concept
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - BaseDimensionMagnitude_hasBaseQuantityKind
  - BaseDimensionMagnitude_vectorMagnitude
  slot_usage:
    hasBaseQuantityKind:
      range: QuantityKind
      required: true
      multivalued: false
    vectorMagnitude:
      range: float
      required: true
      multivalued: false

```
</details>

![class_basedimensionmagnitude_erd](images/class_basedimensionmagnitude_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |
| **[hasBaseQuantityKind](#hasbasequantitykind)** | <sub>1..1</sub> | [QuantityKind](#quantitykind) |  |
| **[vectorMagnitude](#vectormagnitude)** | <sub>1..1</sub> | float |  |

#### Parents

 * [Concept](#concept)




### BinaryPrefix



A <em>Binary Prefix</em> is a prefix for multiples of units in data processing, data transmission, and digital information, notably the bit and the byte, to indicate multiplication by a power of 2.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
BinaryPrefix:
  is_a: Prefix
  slots:
  - Verifiable_wikidataMatch
  - Verifiable_dbpediaMatch
  - Verifiable_isoNormativeReference
  - Verifiable_normativeReference
  - Prefix_exactMatch
  - Prefix_ucumCode
  - Prefix_altSymbol
  - Prefix_latexSymbol
  - Prefix_symbol
  - Prefix_prefixMultiplier
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription

```
</details>

![class_binaryprefix_erd](images/class_binaryprefix_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[altSymbol](#altsymbol)** | <sub>0..\*</sub> | None |  |
| **[dbpediaMatch](#dbpediamatch)** | <sub>0..\*</sub> | uri |  |
| **[exactMatch](#exactmatch)** | <sub>0..\*</sub> | [Prefix](#prefix) |  |
| **[isoNormativeReference](#isonormativereference)** | <sub>0..\*</sub> | None |  |
| **[latexSymbol](#latexsymbol)** | <sub>0..\*</sub> | None |  |
| **[normativeReference](#normativereference)** | <sub>0..\*</sub> | None |  |
| **[prefixMultiplier](#prefixmultiplier)** | <sub>0..1</sub> | None |  |
| **[symbol](#symbol)** | <sub>0..\*</sub> | None |  |
| **[ucumCode](#ucumcode)** | <sub>0..\*</sub> | [UCUMcs-term](#ucumcs-term) |  |
| **[wikidataMatch](#wikidatamatch)** | <sub>0..\*</sub> | uri |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |

#### Parents

 * [Prefix](#prefix)




### BitEncodingType




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
BitEncodingType:
  is_a: Encoding
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - Encoding_bits
  - Encoding_bytes

```
</details>

![class_bitencodingtype_erd](images/class_bitencodingtype_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[bits](#bits)** | <sub>0..1</sub> | None |  |
| **[bytes](#bytes)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |

#### Parents

 * [Encoding](#encoding)




### BooleanEncodingType




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
BooleanEncodingType:
  is_a: Encoding
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - Encoding_bits
  - Encoding_bytes

```
</details>

![class_booleanencodingtype_erd](images/class_booleanencodingtype_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[bits](#bits)** | <sub>0..1</sub> | None |  |
| **[bytes](#bytes)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |

#### Parents

 * [Encoding](#encoding)




### ByteEncodingType




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
ByteEncodingType:
  is_a: Encoding
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - Encoding_bits
  - Encoding_bytes

```
</details>

![class_byteencodingtype_erd](images/class_byteencodingtype_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[bits](#bits)** | <sub>0..1</sub> | None |  |
| **[bytes](#bytes)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |

#### Parents

 * [Encoding](#encoding)




### CardinalityType




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
CardinalityType:
  is_a: EnumeratedValue
  slots:
  - Verifiable_wikidataMatch
  - Verifiable_dbpediaMatch
  - Verifiable_isoNormativeReference
  - Verifiable_normativeReference
  - EnumeratedValue_altSymbol
  - EnumeratedValue_description
  - EnumeratedValue_abbreviation
  - EnumeratedValue_symbol
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_deprecated
  - Concept_plainTextDescription
  - CardinalityType_literal
  slot_usage:
    literal:
      multivalued: false

```
</details>

![class_cardinalitytype_erd](images/class_cardinalitytype_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[altSymbol](#altsymbol)** | <sub>0..\*</sub> | None |  |
| **[dbpediaMatch](#dbpediamatch)** | <sub>0..\*</sub> | uri |  |
| **[isoNormativeReference](#isonormativereference)** | <sub>0..\*</sub> | None |  |
| **[normativeReference](#normativereference)** | <sub>0..\*</sub> | None |  |
| **[symbol](#symbol)** | <sub>0..1</sub> | None |  |
| **[wikidataMatch](#wikidatamatch)** | <sub>0..\*</sub> | uri |  |
| **[literal](#literal)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |

#### Parents

 * [EnumeratedValue](#enumeratedvalue)

#### Referenced by:

 *  **[Datatype](#datatype)** : cardinality  <sub>0..\*</sub> 




### CatalogEntry




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
CatalogEntry: {}

```
</details>


This class has no attributes





### CharEncodingType




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
CharEncodingType:
  is_a: Encoding
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - Encoding_bits
  - Encoding_bytes

```
</details>

![class_charencodingtype_erd](images/class_charencodingtype_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[bits](#bits)** | <sub>0..1</sub> | None |  |
| **[bytes](#bytes)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |

#### Parents

 * [Encoding](#encoding)




### Citation



Provides a simple way of making citations.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
Citation:
  is_a: Concept
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - Citation_description
  - Citation_url
  slot_usage:
    description:
      required: true
      multivalued: false
    url:
      multivalued: false

```
</details>

![class_citation_erd](images/class_citation_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>1..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |
| **[url](#url)** | <sub>0..1</sub> | None |  |

#### Parents

 * [Concept](#concept)




### Class




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
Class: {}

```
</details>

![class_class_erd](images/class_class_erd.svg)

This class has no attributes


#### Children

 * [AspectClass](#aspectclass)

#### Referenced by:

 *  **[Unit](#unit)** : hasFactorUnit  <sub>0..\*</sub> 




### Comment




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
Comment:
  is_a: Verifiable
  slots:
  - Verifiable_wikidataMatch
  - Verifiable_dbpediaMatch
  - Verifiable_isoNormativeReference
  - Verifiable_normativeReference
  - Comment_rationale
  - Comment_description
  slot_usage:
    rationale:
      required: false
    description:
      multivalued: false

```
</details>


#### Local class diagram

![class_comment_local](images/class_comment_local.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[dbpediaMatch](#dbpediamatch)** | <sub>0..\*</sub> | uri |  |
| **[isoNormativeReference](#isonormativereference)** | <sub>0..\*</sub> | None |  |
| **[normativeReference](#normativereference)** | <sub>0..\*</sub> | None |  |
| **[wikidataMatch](#wikidatamatch)** | <sub>0..\*</sub> | uri |  |
| **[rationale](#rationale)** | <sub>0..\*</sub> | string |  |

#### Parents

 * [Verifiable](#verifiable)

#### Children

 * [NISTSP811Comment](#nistsp811comment)




### Concept



The root class for all QUDT concepts.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
Concept:
  is_a: Thing
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  slot_usage:
    hasRule:
      range: Rule
    isReplacedBy:
      multivalued: false
    description:
      multivalued: false
    abbreviation:
      multivalued: false
    deprecated:
      multivalued: false
    id:
      multivalued: false
    plainTextDescription:
      multivalued: false

```
</details>

![class_concept_erd](images/class_concept_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |

#### Parents

 * [Thing](#thing) - The root class for all QUDT concepts

#### Children

 * [AbstractQuantityKind](#abstractquantitykind)
 * [BaseDimensionMagnitude](#basedimensionmagnitude)
 * [Citation](#citation)
 * [DataItem](#dataitem)
 * [Datatype](#datatype)
 * [Discipline](#discipline)
 * [Encoding](#encoding)
 * [EnumeratedQuantity](#enumeratedquantity)
 * [Enumeration](#enumeration)
 * [Figure](#figure)
 * [MathsFunctionType](#mathsfunctiontype)
 * [Organization](#organization)
 * [QuantityKindDimensionVector](#quantitykinddimensionvector)
 * [Scale](#scale)
 * [Symbol](#symbol)
 * [SystemOfQuantityKinds](#systemofquantitykinds)

#### Used as mixin by

 * [EnumeratedValue](#enumeratedvalue)
 * [NumericUnion](#numericunion)
 * [Prefix](#prefix)
 * [Quantity](#quantity)
 * [QuantityValue](#quantityvalue)
 * [Rule](#rule)
 * [SystemOfUnits](#systemofunits)
 * [Unit](#unit)

#### Referenced by:





### ConstantValue



Used to specify the values of a constant.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
ConstantValue:
  is_a: QuantityValue
  slots:
  - Quantifiable_dataEncoding
  - Quantifiable_datatype
  - Quantifiable_relativeStandardUncertainty
  - Quantifiable_standardUncertainty
  - Quantifiable_standardUncertaintySN
  - Quantifiable_value
  - Quantifiable_valueSN
  - QuantityValue_hasUnit
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - ConstantValue_exactConstant
  slot_usage:
    exactConstant:
      required: false

```
</details>

![class_constantvalue_erd](images/class_constantvalue_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[dataEncoding](#dataencoding)** | <sub>0..1</sub> | [DataEncoding](#dataencoding) |  |
| **[datatype](#datatype)** | <sub>0..1</sub> | [Datatype](#datatype) |  |
| **[hasUnit](#hasunit)** | <sub>0..1</sub> | [Unit](#unit) |  |
| **[relativeStandardUncertainty](#relativestandarduncertainty)** | <sub>0..1</sub> | double |  |
| **[standardUncertainty](#standarduncertainty)** | <sub>0..1</sub> | decimal |  |
| **[standardUncertaintySN](#standarduncertaintysn)** | <sub>0..\*</sub> | double |  |
| **[value](#value)** | <sub>0..1</sub> | None |  |
| **[valueSN](#valuesn)** | <sub>0..1</sub> | None |  |
| **[exactConstant](#exactconstant)** | <sub>0..\*</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |

#### Parents

 * [QuantityValue](#quantityvalue)




### ContextualUnit




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
ContextualUnit:
  is_a: Unit
  slots:
  - Verifiable_wikidataMatch
  - Verifiable_dbpediaMatch
  - Verifiable_isoNormativeReference
  - Verifiable_normativeReference
  - hasReciprocalUnit
  - isUnitOfSystem
  - omUnit
  - unitFor
  - Unit_applicableSystem
  - Unit_definedUnitOfSystem
  - Unit_derivedCoherentUnitOfSystem
  - Unit_derivedUnitOfSystem
  - Unit_exactMatch
  - Unit_hasDimensionVector
  - Unit_hasFactorUnit
  - Unit_hasQuantityKind
  - Unit_iec61360Code
  - Unit_prefix
  - Unit_qkdvDenominator
  - Unit_qkdvNumerator
  - Unit_scalingOf
  - Unit_ucumCode
  - Unit_udunitsCode
  - Unit_uneceCommonCode
  - Unit_altSymbol
  - Unit_latexDefinition
  - Unit_latexSymbol
  - Unit_siUnitsExpression
  - Unit_symbol
  - Unit_conversionMultiplier
  - Unit_conversionMultiplierSN
  - Unit_conversionOffset
  - Unit_conversionOffsetSN
  - Unit_factorUnitScalar
  - Unit_mathMLdefinition
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - ContextualUnit_broader
  slot_usage:
    broader:
      range: Unit

```
</details>

![class_contextualunit_erd](images/class_contextualunit_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[altSymbol](#altsymbol)** | <sub>0..\*</sub> | None |  |
| **[applicableSystem](#applicablesystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[conversionMultiplier](#conversionmultiplier)** | <sub>0..1</sub> | None |  |
| **[conversionMultiplierSN](#conversionmultipliersn)** | <sub>0..1</sub> | None |  |
| **[conversionOffset](#conversionoffset)** | <sub>0..1</sub> | None |  |
| **[conversionOffsetSN](#conversionoffsetsn)** | <sub>0..1</sub> | None |  |
| **[dbpediaMatch](#dbpediamatch)** | <sub>0..\*</sub> | uri |  |
| **[definedUnitOfSystem](#definedunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[derivedCoherentUnitOfSystem](#derivedcoherentunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[derivedUnitOfSystem](#derivedunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[exactMatch](#exactmatch)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[factorUnitScalar](#factorunitscalar)** | <sub>0..1</sub> | None |  |
| **[hasDimensionVector](#hasdimensionvector)** | <sub>0..1</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[hasFactorUnit](#hasfactorunit)** | <sub>0..\*</sub> | [Class](#class) |  |
| **[hasQuantityKind](#hasquantitykind)** | <sub>0..\*</sub> | [QuantityKind](#quantitykind) |  |
| **[hasReciprocalUnit](#hasreciprocalunit)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[iec61360Code](#iec61360code)** | <sub>0..\*</sub> | string |  |
| **[isUnitOfSystem](#isunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[isoNormativeReference](#isonormativereference)** | <sub>0..\*</sub> | None |  |
| **[latexDefinition](#latexdefinition)** | <sub>0..\*</sub> | None |  |
| **[latexSymbol](#latexsymbol)** | <sub>0..\*</sub> | None |  |
| **[mathMLdefinition](#mathmldefinition)** | <sub>0..1</sub> | None |  |
| **[normativeReference](#normativereference)** | <sub>0..\*</sub> | None |  |
| **[omUnit](#omunit)** | <sub>0..\*</sub> | None |  |
| **[prefix](#prefix)** | <sub>0..\*</sub> | [Prefix](#prefix) |  |
| **[qkdvDenominator](#qkdvdenominator)** | <sub>0..1</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[qkdvNumerator](#qkdvnumerator)** | <sub>0..1</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[scalingOf](#scalingof)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[siUnitsExpression](#siunitsexpression)** | <sub>0..\*</sub> | None |  |
| **[symbol](#symbol)** | <sub>0..\*</sub> | None |  |
| **[ucumCode](#ucumcode)** | <sub>0..\*</sub> | [UCUMcs](#ucumcs) |  |
| **[udunitsCode](#udunitscode)** | <sub>0..\*</sub> | string |  |
| **[uneceCommonCode](#unececommoncode)** | <sub>0..\*</sub> | string |  |
| **[unitFor](#unitfor)** | <sub>0..\*</sub> | None |  |
| **[wikidataMatch](#wikidatamatch)** | <sub>0..\*</sub> | uri |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |

#### Parents

 * [Unit](#unit)




### CountingUnit



Used for all units that express counts. Examples are Atomic Number, Number, Number per Year, Percent and Sample per Second.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
CountingUnit:
  is_a: DimensionlessUnit
  slots:
  - Verifiable_wikidataMatch
  - Verifiable_dbpediaMatch
  - Verifiable_isoNormativeReference
  - Verifiable_normativeReference
  - hasReciprocalUnit
  - isUnitOfSystem
  - omUnit
  - unitFor
  - Unit_applicableSystem
  - Unit_definedUnitOfSystem
  - Unit_derivedCoherentUnitOfSystem
  - Unit_derivedUnitOfSystem
  - Unit_exactMatch
  - Unit_hasDimensionVector
  - Unit_hasFactorUnit
  - Unit_hasQuantityKind
  - Unit_iec61360Code
  - Unit_prefix
  - Unit_qkdvDenominator
  - Unit_qkdvNumerator
  - Unit_scalingOf
  - Unit_ucumCode
  - Unit_udunitsCode
  - Unit_uneceCommonCode
  - Unit_altSymbol
  - Unit_latexDefinition
  - Unit_latexSymbol
  - Unit_siUnitsExpression
  - Unit_symbol
  - Unit_conversionMultiplier
  - Unit_conversionMultiplierSN
  - Unit_conversionOffset
  - Unit_conversionOffsetSN
  - Unit_factorUnitScalar
  - Unit_mathMLdefinition
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription

```
</details>

![class_countingunit_erd](images/class_countingunit_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[altSymbol](#altsymbol)** | <sub>0..\*</sub> | None |  |
| **[applicableSystem](#applicablesystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[conversionMultiplier](#conversionmultiplier)** | <sub>0..1</sub> | None |  |
| **[conversionMultiplierSN](#conversionmultipliersn)** | <sub>0..1</sub> | None |  |
| **[conversionOffset](#conversionoffset)** | <sub>0..1</sub> | None |  |
| **[conversionOffsetSN](#conversionoffsetsn)** | <sub>0..1</sub> | None |  |
| **[dbpediaMatch](#dbpediamatch)** | <sub>0..\*</sub> | uri |  |
| **[definedUnitOfSystem](#definedunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[derivedCoherentUnitOfSystem](#derivedcoherentunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[derivedUnitOfSystem](#derivedunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[exactMatch](#exactmatch)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[factorUnitScalar](#factorunitscalar)** | <sub>0..1</sub> | None |  |
| **[hasDimensionVector](#hasdimensionvector)** | <sub>0..1</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[hasFactorUnit](#hasfactorunit)** | <sub>0..\*</sub> | [Class](#class) |  |
| **[hasQuantityKind](#hasquantitykind)** | <sub>0..\*</sub> | [QuantityKind](#quantitykind) |  |
| **[hasReciprocalUnit](#hasreciprocalunit)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[iec61360Code](#iec61360code)** | <sub>0..\*</sub> | string |  |
| **[isUnitOfSystem](#isunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[isoNormativeReference](#isonormativereference)** | <sub>0..\*</sub> | None |  |
| **[latexDefinition](#latexdefinition)** | <sub>0..\*</sub> | None |  |
| **[latexSymbol](#latexsymbol)** | <sub>0..\*</sub> | None |  |
| **[mathMLdefinition](#mathmldefinition)** | <sub>0..1</sub> | None |  |
| **[normativeReference](#normativereference)** | <sub>0..\*</sub> | None |  |
| **[omUnit](#omunit)** | <sub>0..\*</sub> | None |  |
| **[prefix](#prefix)** | <sub>0..\*</sub> | [Prefix](#prefix) |  |
| **[qkdvDenominator](#qkdvdenominator)** | <sub>0..1</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[qkdvNumerator](#qkdvnumerator)** | <sub>0..1</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[scalingOf](#scalingof)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[siUnitsExpression](#siunitsexpression)** | <sub>0..\*</sub> | None |  |
| **[symbol](#symbol)** | <sub>0..\*</sub> | None |  |
| **[ucumCode](#ucumcode)** | <sub>0..\*</sub> | [UCUMcs](#ucumcs) |  |
| **[udunitsCode](#udunitscode)** | <sub>0..\*</sub> | string |  |
| **[uneceCommonCode](#unececommoncode)** | <sub>0..\*</sub> | string |  |
| **[unitFor](#unitfor)** | <sub>0..\*</sub> | None |  |
| **[wikidataMatch](#wikidatamatch)** | <sub>0..\*</sub> | uri |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |

#### Parents

 * [DimensionlessUnit](#dimensionlessunit)




### CurrencyUnit



Currency Units have their own subclass of unit because: (a) they have additonal properites such as 'country' and (b) their URIs do not conform to the same rules as other units.

Used for all units that express currency.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
CurrencyUnit:
  is_a: DimensionlessUnit
  slots:
  - Verifiable_wikidataMatch
  - Verifiable_dbpediaMatch
  - Verifiable_isoNormativeReference
  - Verifiable_normativeReference
  - hasReciprocalUnit
  - isUnitOfSystem
  - omUnit
  - unitFor
  - Unit_applicableSystem
  - Unit_definedUnitOfSystem
  - Unit_derivedCoherentUnitOfSystem
  - Unit_derivedUnitOfSystem
  - Unit_exactMatch
  - Unit_hasDimensionVector
  - Unit_hasFactorUnit
  - Unit_hasQuantityKind
  - Unit_iec61360Code
  - Unit_prefix
  - Unit_qkdvDenominator
  - Unit_qkdvNumerator
  - Unit_scalingOf
  - Unit_ucumCode
  - Unit_udunitsCode
  - Unit_uneceCommonCode
  - Unit_altSymbol
  - Unit_latexDefinition
  - Unit_latexSymbol
  - Unit_siUnitsExpression
  - Unit_symbol
  - Unit_conversionMultiplier
  - Unit_conversionMultiplierSN
  - Unit_conversionOffset
  - Unit_conversionOffsetSN
  - Unit_factorUnitScalar
  - Unit_mathMLdefinition
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - CurrencyUnit_currencyCode
  - CurrencyUnit_currencyExponent
  slot_usage:
    currencyCode:
      multivalued: false
    currencyExponent:
      multivalued: false

```
</details>

![class_currencyunit_erd](images/class_currencyunit_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[altSymbol](#altsymbol)** | <sub>0..\*</sub> | None |  |
| **[applicableSystem](#applicablesystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[conversionMultiplier](#conversionmultiplier)** | <sub>0..1</sub> | None |  |
| **[conversionMultiplierSN](#conversionmultipliersn)** | <sub>0..1</sub> | None |  |
| **[conversionOffset](#conversionoffset)** | <sub>0..1</sub> | None |  |
| **[conversionOffsetSN](#conversionoffsetsn)** | <sub>0..1</sub> | None |  |
| **[dbpediaMatch](#dbpediamatch)** | <sub>0..\*</sub> | uri |  |
| **[definedUnitOfSystem](#definedunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[derivedCoherentUnitOfSystem](#derivedcoherentunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[derivedUnitOfSystem](#derivedunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[exactMatch](#exactmatch)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[factorUnitScalar](#factorunitscalar)** | <sub>0..1</sub> | None |  |
| **[hasDimensionVector](#hasdimensionvector)** | <sub>0..1</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[hasFactorUnit](#hasfactorunit)** | <sub>0..\*</sub> | [Class](#class) |  |
| **[hasQuantityKind](#hasquantitykind)** | <sub>0..\*</sub> | [QuantityKind](#quantitykind) |  |
| **[hasReciprocalUnit](#hasreciprocalunit)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[iec61360Code](#iec61360code)** | <sub>0..\*</sub> | string |  |
| **[isUnitOfSystem](#isunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[isoNormativeReference](#isonormativereference)** | <sub>0..\*</sub> | None |  |
| **[latexDefinition](#latexdefinition)** | <sub>0..\*</sub> | None |  |
| **[latexSymbol](#latexsymbol)** | <sub>0..\*</sub> | None |  |
| **[mathMLdefinition](#mathmldefinition)** | <sub>0..1</sub> | None |  |
| **[normativeReference](#normativereference)** | <sub>0..\*</sub> | None |  |
| **[omUnit](#omunit)** | <sub>0..\*</sub> | None |  |
| **[prefix](#prefix)** | <sub>0..\*</sub> | [Prefix](#prefix) |  |
| **[qkdvDenominator](#qkdvdenominator)** | <sub>0..1</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[qkdvNumerator](#qkdvnumerator)** | <sub>0..1</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[scalingOf](#scalingof)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[siUnitsExpression](#siunitsexpression)** | <sub>0..\*</sub> | None |  |
| **[symbol](#symbol)** | <sub>0..\*</sub> | None |  |
| **[ucumCode](#ucumcode)** | <sub>0..\*</sub> | [UCUMcs](#ucumcs) |  |
| **[udunitsCode](#udunitscode)** | <sub>0..\*</sub> | string |  |
| **[uneceCommonCode](#unececommoncode)** | <sub>0..\*</sub> | string |  |
| **[unitFor](#unitfor)** | <sub>0..\*</sub> | None |  |
| **[wikidataMatch](#wikidatamatch)** | <sub>0..\*</sub> | uri |  |
| **[currencyCode](#currencycode)** | <sub>0..1</sub> | None |  |
| **[currencyExponent](#currencyexponent)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |

#### Parents

 * [DimensionlessUnit](#dimensionlessunit)




### DataEncoding



<p><em>Data Encoding</em> expresses the properties that specify how data is represented at the bit and byte level. These properties are applicable to describing raw data.</p>


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
DataEncoding:
  is_a: Aspect
  slots:
  - DataEncoding_bitOrder
  - DataEncoding_encoding
  - DataEncoding_byteOrder
  slot_usage:
    bitOrder:
      range: EndianType
      multivalued: false
    encoding:
      range: Encoding
      multivalued: false
    byteOrder:
      multivalued: false

```
</details>

![class_dataencoding_erd](images/class_dataencoding_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[bitOrder](#bitorder)** | <sub>0..1</sub> | [EndianType](#endiantype) |  |
| **[byteOrder](#byteorder)** | <sub>0..1</sub> | [EndianType](#endiantype) |  |
| **[encoding](#encoding)** | <sub>0..1</sub> | [Encoding](#encoding) |  |

#### Parents

 * [Aspect](#aspect)

#### Referenced by:

 *  **[Quantifiable](#quantifiable)** : dataEncoding  <sub>0..\*</sub> 




### DataItem




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
DataItem:
  is_a: Concept
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - DataItem_value
  slot_usage:
    value:
      range: string
      multivalued: false

```
</details>

![class_dataitem_erd](images/class_dataitem_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |
| **[value](#value)** | <sub>0..1</sub> | string |  |

#### Parents

 * [Concept](#concept)




### Datatype




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
Datatype:
  is_a: Concept
  slots:
  - guidance
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - Datatype_basis
  - Datatype_cardinality
  - Datatype_orderedType
  - Datatype_ansiSQLName
  - Datatype_cName
  - Datatype_oracleSQLName
  - Datatype_protocolBuffersName
  - Datatype_pythonName
  - Datatype_vbName
  - Datatype_bounded
  - Datatype_id
  - Datatype_javaName
  - Datatype_jsName
  - Datatype_matlabName
  - Datatype_microsoftSQLServerName
  - Datatype_mySQLName
  - Datatype_odbcName
  - Datatype_oleDBName
  slot_usage:
    basis:
      range: Datatype
      multivalued: false
    cardinality:
      range: CardinalityType
      multivalued: false
    orderedType:
      range: OrderedType
      multivalued: false
    ansiSQLName:
      multivalued: false
    cName:
      multivalued: false
    oracleSQLName:
      multivalued: false
    protocolBuffersName:
      multivalued: false
    pythonName:
      multivalued: false
    vbName:
      multivalued: false
    bounded:
      multivalued: false
    id:
      multivalued: false
    javaName:
      multivalued: false
    jsName:
      multivalued: false
    matlabName:
      multivalued: false
    microsoftSQLServerName:
      multivalued: false
    mySQLName:
      multivalued: false
    odbcName:
      multivalued: false
    oleDBName:
      multivalued: false

```
</details>

![class_datatype_erd](images/class_datatype_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |
| **[ansiSQLName](#ansisqlname)** | <sub>0..1</sub> | string |  |
| **[basis](#basis)** | <sub>0..1</sub> | [Datatype](#datatype) |  |
| **[bounded](#bounded)** | <sub>0..1</sub> | None |  |
| **[cName](#cname)** | <sub>0..1</sub> | string |  |
| **[cardinality](#cardinality)** | <sub>0..1</sub> | [CardinalityType](#cardinalitytype) |  |
| **[javaName](#javaname)** | <sub>0..1</sub> | None |  |
| **[jsName](#jsname)** | <sub>0..1</sub> | None |  |
| **[matlabName](#matlabname)** | <sub>0..1</sub> | None |  |
| **[microsoftSQLServerName](#microsoftsqlservername)** | <sub>0..1</sub> | None |  |
| **[mySQLName](#mysqlname)** | <sub>0..1</sub> | None |  |
| **[odbcName](#odbcname)** | <sub>0..1</sub> | None |  |
| **[oleDBName](#oledbname)** | <sub>0..1</sub> | None |  |
| **[oracleSQLName](#oraclesqlname)** | <sub>0..1</sub> | string |  |
| **[orderedType](#orderedtype)** | <sub>0..1</sub> | [OrderedType](#orderedtype) |  |
| **[protocolBuffersName](#protocolbuffersname)** | <sub>0..1</sub> | string |  |
| **[pythonName](#pythonname)** | <sub>0..1</sub> | string |  |
| **[vbName](#vbname)** | <sub>0..1</sub> | string |  |

#### Parents

 * [Concept](#concept)

#### Children

 * [ScalarDatatype](#scalardatatype)

#### Referenced by:

 *  **[Datatype](#datatype)** : basis  <sub>0..\*</sub> 
 *  **[Quantifiable](#quantifiable)** : datatype  <sub>0..\*</sub> 
 *  **[ScalarDatatype](#scalardatatype)** : rdfsDatatype  <sub>0..\*</sub> 




### DateTimeStringEncodingType




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
DateTimeStringEncodingType:
  is_a: StringEncodingType
  slots:
  - DateTimeStringEncodingType_allowedPattern
  slot_usage:
    allowedPattern:
      required: true

```
</details>


#### Local class diagram

![class_datetimestringencodingtype_local](images/class_datetimestringencodingtype_local.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[allowedPattern](#allowedpattern)** | <sub>1..\*</sub> | None |  |

#### Parents

 * [StringEncodingType](#stringencodingtype)




### DecimalPrefix



A <em>Decimal Prefix</em> is a prefix for multiples of units that are powers of 10.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
DecimalPrefix:
  is_a: Prefix
  slots:
  - Verifiable_wikidataMatch
  - Verifiable_dbpediaMatch
  - Verifiable_isoNormativeReference
  - Verifiable_normativeReference
  - Prefix_exactMatch
  - Prefix_ucumCode
  - Prefix_altSymbol
  - Prefix_latexSymbol
  - Prefix_symbol
  - Prefix_prefixMultiplier
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription

```
</details>

![class_decimalprefix_erd](images/class_decimalprefix_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[altSymbol](#altsymbol)** | <sub>0..\*</sub> | None |  |
| **[dbpediaMatch](#dbpediamatch)** | <sub>0..\*</sub> | uri |  |
| **[exactMatch](#exactmatch)** | <sub>0..\*</sub> | [Prefix](#prefix) |  |
| **[isoNormativeReference](#isonormativereference)** | <sub>0..\*</sub> | None |  |
| **[latexSymbol](#latexsymbol)** | <sub>0..\*</sub> | None |  |
| **[normativeReference](#normativereference)** | <sub>0..\*</sub> | None |  |
| **[prefixMultiplier](#prefixmultiplier)** | <sub>0..1</sub> | None |  |
| **[symbol](#symbol)** | <sub>0..\*</sub> | None |  |
| **[ucumCode](#ucumcode)** | <sub>0..\*</sub> | [UCUMcs-term](#ucumcs-term) |  |
| **[wikidataMatch](#wikidatamatch)** | <sub>0..\*</sub> | uri |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |

#### Parents

 * [Prefix](#prefix)




### DerivedUnit



A DerivedUnit is a type specification for units that are derived from other units.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
DerivedUnit:
  is_a: Unit
  slots:
  - Verifiable_wikidataMatch
  - Verifiable_dbpediaMatch
  - Verifiable_isoNormativeReference
  - Verifiable_normativeReference
  - hasReciprocalUnit
  - isUnitOfSystem
  - omUnit
  - unitFor
  - Unit_applicableSystem
  - Unit_definedUnitOfSystem
  - Unit_derivedCoherentUnitOfSystem
  - Unit_derivedUnitOfSystem
  - Unit_exactMatch
  - Unit_hasDimensionVector
  - Unit_hasFactorUnit
  - Unit_hasQuantityKind
  - Unit_iec61360Code
  - Unit_prefix
  - Unit_qkdvDenominator
  - Unit_qkdvNumerator
  - Unit_scalingOf
  - Unit_ucumCode
  - Unit_udunitsCode
  - Unit_uneceCommonCode
  - Unit_altSymbol
  - Unit_latexDefinition
  - Unit_latexSymbol
  - Unit_siUnitsExpression
  - Unit_symbol
  - Unit_conversionMultiplier
  - Unit_conversionMultiplierSN
  - Unit_conversionOffset
  - Unit_conversionOffsetSN
  - Unit_factorUnitScalar
  - Unit_mathMLdefinition
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription

```
</details>

![class_derivedunit_erd](images/class_derivedunit_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[altSymbol](#altsymbol)** | <sub>0..\*</sub> | None |  |
| **[applicableSystem](#applicablesystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[conversionMultiplier](#conversionmultiplier)** | <sub>0..1</sub> | None |  |
| **[conversionMultiplierSN](#conversionmultipliersn)** | <sub>0..1</sub> | None |  |
| **[conversionOffset](#conversionoffset)** | <sub>0..1</sub> | None |  |
| **[conversionOffsetSN](#conversionoffsetsn)** | <sub>0..1</sub> | None |  |
| **[dbpediaMatch](#dbpediamatch)** | <sub>0..\*</sub> | uri |  |
| **[definedUnitOfSystem](#definedunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[derivedCoherentUnitOfSystem](#derivedcoherentunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[derivedUnitOfSystem](#derivedunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[exactMatch](#exactmatch)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[factorUnitScalar](#factorunitscalar)** | <sub>0..1</sub> | None |  |
| **[hasDimensionVector](#hasdimensionvector)** | <sub>0..1</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[hasFactorUnit](#hasfactorunit)** | <sub>0..\*</sub> | [Class](#class) |  |
| **[hasQuantityKind](#hasquantitykind)** | <sub>0..\*</sub> | [QuantityKind](#quantitykind) |  |
| **[hasReciprocalUnit](#hasreciprocalunit)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[iec61360Code](#iec61360code)** | <sub>0..\*</sub> | string |  |
| **[isUnitOfSystem](#isunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[isoNormativeReference](#isonormativereference)** | <sub>0..\*</sub> | None |  |
| **[latexDefinition](#latexdefinition)** | <sub>0..\*</sub> | None |  |
| **[latexSymbol](#latexsymbol)** | <sub>0..\*</sub> | None |  |
| **[mathMLdefinition](#mathmldefinition)** | <sub>0..1</sub> | None |  |
| **[normativeReference](#normativereference)** | <sub>0..\*</sub> | None |  |
| **[omUnit](#omunit)** | <sub>0..\*</sub> | None |  |
| **[prefix](#prefix)** | <sub>0..\*</sub> | [Prefix](#prefix) |  |
| **[qkdvDenominator](#qkdvdenominator)** | <sub>0..1</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[qkdvNumerator](#qkdvnumerator)** | <sub>0..1</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[scalingOf](#scalingof)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[siUnitsExpression](#siunitsexpression)** | <sub>0..\*</sub> | None |  |
| **[symbol](#symbol)** | <sub>0..\*</sub> | None |  |
| **[ucumCode](#ucumcode)** | <sub>0..\*</sub> | [UCUMcs](#ucumcs) |  |
| **[udunitsCode](#udunitscode)** | <sub>0..\*</sub> | string |  |
| **[uneceCommonCode](#unececommoncode)** | <sub>0..\*</sub> | string |  |
| **[unitFor](#unitfor)** | <sub>0..\*</sub> | None |  |
| **[wikidataMatch](#wikidatamatch)** | <sub>0..\*</sub> | uri |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |

#### Parents

 * [Unit](#unit)




### DimensionlessUnit



A Dimensionless Unit is a quantity for which all the exponents of the factors corresponding to the base quantities in its quantity dimension are zero.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
DimensionlessUnit:
  is_a: Unit
  slots:
  - Verifiable_wikidataMatch
  - Verifiable_dbpediaMatch
  - Verifiable_isoNormativeReference
  - Verifiable_normativeReference
  - hasReciprocalUnit
  - isUnitOfSystem
  - omUnit
  - unitFor
  - Unit_applicableSystem
  - Unit_definedUnitOfSystem
  - Unit_derivedCoherentUnitOfSystem
  - Unit_derivedUnitOfSystem
  - Unit_exactMatch
  - Unit_hasDimensionVector
  - Unit_hasFactorUnit
  - Unit_hasQuantityKind
  - Unit_iec61360Code
  - Unit_prefix
  - Unit_qkdvDenominator
  - Unit_qkdvNumerator
  - Unit_scalingOf
  - Unit_ucumCode
  - Unit_udunitsCode
  - Unit_uneceCommonCode
  - Unit_altSymbol
  - Unit_latexDefinition
  - Unit_latexSymbol
  - Unit_siUnitsExpression
  - Unit_symbol
  - Unit_conversionMultiplier
  - Unit_conversionMultiplierSN
  - Unit_conversionOffset
  - Unit_conversionOffsetSN
  - Unit_factorUnitScalar
  - Unit_mathMLdefinition
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription

```
</details>

![class_dimensionlessunit_erd](images/class_dimensionlessunit_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[altSymbol](#altsymbol)** | <sub>0..\*</sub> | None |  |
| **[applicableSystem](#applicablesystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[conversionMultiplier](#conversionmultiplier)** | <sub>0..1</sub> | None |  |
| **[conversionMultiplierSN](#conversionmultipliersn)** | <sub>0..1</sub> | None |  |
| **[conversionOffset](#conversionoffset)** | <sub>0..1</sub> | None |  |
| **[conversionOffsetSN](#conversionoffsetsn)** | <sub>0..1</sub> | None |  |
| **[dbpediaMatch](#dbpediamatch)** | <sub>0..\*</sub> | uri |  |
| **[definedUnitOfSystem](#definedunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[derivedCoherentUnitOfSystem](#derivedcoherentunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[derivedUnitOfSystem](#derivedunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[exactMatch](#exactmatch)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[factorUnitScalar](#factorunitscalar)** | <sub>0..1</sub> | None |  |
| **[hasDimensionVector](#hasdimensionvector)** | <sub>0..1</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[hasFactorUnit](#hasfactorunit)** | <sub>0..\*</sub> | [Class](#class) |  |
| **[hasQuantityKind](#hasquantitykind)** | <sub>0..\*</sub> | [QuantityKind](#quantitykind) |  |
| **[hasReciprocalUnit](#hasreciprocalunit)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[iec61360Code](#iec61360code)** | <sub>0..\*</sub> | string |  |
| **[isUnitOfSystem](#isunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[isoNormativeReference](#isonormativereference)** | <sub>0..\*</sub> | None |  |
| **[latexDefinition](#latexdefinition)** | <sub>0..\*</sub> | None |  |
| **[latexSymbol](#latexsymbol)** | <sub>0..\*</sub> | None |  |
| **[mathMLdefinition](#mathmldefinition)** | <sub>0..1</sub> | None |  |
| **[normativeReference](#normativereference)** | <sub>0..\*</sub> | None |  |
| **[omUnit](#omunit)** | <sub>0..\*</sub> | None |  |
| **[prefix](#prefix)** | <sub>0..\*</sub> | [Prefix](#prefix) |  |
| **[qkdvDenominator](#qkdvdenominator)** | <sub>0..1</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[qkdvNumerator](#qkdvnumerator)** | <sub>0..1</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[scalingOf](#scalingof)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[siUnitsExpression](#siunitsexpression)** | <sub>0..\*</sub> | None |  |
| **[symbol](#symbol)** | <sub>0..\*</sub> | None |  |
| **[ucumCode](#ucumcode)** | <sub>0..\*</sub> | [UCUMcs](#ucumcs) |  |
| **[udunitsCode](#udunitscode)** | <sub>0..\*</sub> | string |  |
| **[uneceCommonCode](#unececommoncode)** | <sub>0..\*</sub> | string |  |
| **[unitFor](#unitfor)** | <sub>0..\*</sub> | None |  |
| **[wikidataMatch](#wikidatamatch)** | <sub>0..\*</sub> | uri |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |

#### Parents

 * [Unit](#unit)

#### Children

 * [AngleUnit](#angleunit)
 * [CountingUnit](#countingunit)
 * [CurrencyUnit](#currencyunit)
 * [LogarithmicUnit](#logarithmicunit)




### Discipline




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
Discipline:
  is_a: Concept
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription

```
</details>

![class_discipline_erd](images/class_discipline_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |

#### Parents

 * [Concept](#concept)




### Encoding




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
Encoding:
  is_a: Concept
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - Encoding_bits
  - Encoding_bytes
  slot_usage:
    bits:
      multivalued: false
    bytes:
      multivalued: false

```
</details>

![class_encoding_erd](images/class_encoding_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |
| **[bits](#bits)** | <sub>0..1</sub> | None |  |
| **[bytes](#bytes)** | <sub>0..1</sub> | None |  |

#### Parents

 * [Concept](#concept)

#### Children

 * [BitEncodingType](#bitencodingtype)
 * [BooleanEncodingType](#booleanencodingtype)
 * [ByteEncodingType](#byteencodingtype)
 * [CharEncodingType](#charencodingtype)
 * [FloatingPointEncodingType](#floatingpointencodingtype)
 * [IntegerEncodingType](#integerencodingtype)

#### Referenced by:

 *  **[DataEncoding](#dataencoding)** : encoding  <sub>0..\*</sub> 




### EndianType




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
EndianType:
  is_a: EnumeratedValue
  slots:
  - Verifiable_wikidataMatch
  - Verifiable_dbpediaMatch
  - Verifiable_isoNormativeReference
  - Verifiable_normativeReference
  - EnumeratedValue_altSymbol
  - EnumeratedValue_description
  - EnumeratedValue_abbreviation
  - EnumeratedValue_symbol
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_deprecated
  - Concept_plainTextDescription

```
</details>

![class_endiantype_erd](images/class_endiantype_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[altSymbol](#altsymbol)** | <sub>0..\*</sub> | None |  |
| **[dbpediaMatch](#dbpediamatch)** | <sub>0..\*</sub> | uri |  |
| **[isoNormativeReference](#isonormativereference)** | <sub>0..\*</sub> | None |  |
| **[normativeReference](#normativereference)** | <sub>0..\*</sub> | None |  |
| **[symbol](#symbol)** | <sub>0..1</sub> | None |  |
| **[wikidataMatch](#wikidatamatch)** | <sub>0..\*</sub> | uri |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |

#### Parents

 * [EnumeratedValue](#enumeratedvalue)

#### Referenced by:

 *  **[DataEncoding](#dataencoding)** : bitOrder  <sub>0..\*</sub> 
 *  **[DataEncoding](#dataencoding)** : byteOrder  <sub>0..\*</sub> 




### EnumeratedQuantity




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
EnumeratedQuantity:
  is_a: Concept
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - EnumeratedQuantity_enumeratedValue
  - EnumeratedQuantity_enumeration
  slot_usage:
    enumeratedValue:
      range: EnumeratedValue
    enumeration:
      range: Enumeration

```
</details>

![class_enumeratedquantity_erd](images/class_enumeratedquantity_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |
| **[enumeratedValue](#enumeratedvalue)** | <sub>0..\*</sub> | [EnumeratedValue](#enumeratedvalue) |  |
| **[enumeration](#enumeration)** | <sub>0..\*</sub> | [Enumeration](#enumeration) |  |

#### Parents

 * [Concept](#concept)




### EnumeratedValue




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
EnumeratedValue:
  is_a: Verifiable
  mixins:
  - Concept
  slots:
  - Verifiable_wikidataMatch
  - Verifiable_dbpediaMatch
  - Verifiable_isoNormativeReference
  - Verifiable_normativeReference
  - EnumeratedValue_altSymbol
  - EnumeratedValue_description
  - EnumeratedValue_abbreviation
  - EnumeratedValue_symbol
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_deprecated
  - Concept_plainTextDescription
  slot_usage:
    altSymbol:
      required: false
    description:
      multivalued: false
    abbreviation:
      multivalued: false
    symbol:
      multivalued: false

```
</details>

![class_enumeratedvalue_erd](images/class_enumeratedvalue_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[dbpediaMatch](#dbpediamatch)** | <sub>0..\*</sub> | uri |  |
| **[isoNormativeReference](#isonormativereference)** | <sub>0..\*</sub> | None |  |
| **[normativeReference](#normativereference)** | <sub>0..\*</sub> | None |  |
| **[wikidataMatch](#wikidatamatch)** | <sub>0..\*</sub> | uri |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[altSymbol](#altsymbol)** | <sub>0..\*</sub> | None |  |
| **[symbol](#symbol)** | <sub>0..1</sub> | None |  |

#### Parents

 * [Verifiable](#verifiable)

#### Children

 * [CardinalityType](#cardinalitytype)
 * [EndianType](#endiantype)
 * [OrderedType](#orderedtype)
 * [QuantityType](#quantitytype)
 * [RuleType](#ruletype)
 * [ScaleType](#scaletype)
 * [TransformType](#transformtype)

#### Uses

 *  mixin: [Concept](#concept)

#### Referenced by:

 *  **[EnumeratedQuantity](#enumeratedquantity)** : enumeratedValue  <sub>0..\*</sub> 
 *  **[Enumeration](#enumeration)** : default  <sub>0..\*</sub> 
 *  **[Enumeration](#enumeration)** : element  <sub>1..\*</sub> 




### Enumeration



<p>An enumeration is a set of literals from which a single value is selected. Each literal can have a tag as an integer within a standard encoding appropriate to the range of integer values. Consistency of enumeration types will allow them, and the enumerated values, to be referred to unambiguously either through symbolic name or encoding. Enumerated values are also controlled vocabularies and as such need to be standardized. Without this consistency enumeration literals can be stated differently and result in  data conflicts and misinterpretations.</p>

<p>The tags are a set of positive whole numbers, not necessarily contiguous and having no numerical significance, each corresponding to the associated literal identifier. An order attribute can also be given on the enumeration elements. An enumeration can itself be a member of an enumeration. This allows enumerations to be enumerated in a selection. Enumerations are also subclasses of <em>Scalar Datatype</em>. This allows them to be used as the reference of a datatype specification.</p>


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
Enumeration:
  is_a: Concept
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_deprecated
  - Concept_plainTextDescription
  - Enumeration_default
  - Enumeration_element
  - Enumeration_abbreviation
  slot_usage:
    default:
      range: EnumeratedValue
      multivalued: false
    element:
      range: EnumeratedValue
      required: true
    abbreviation:
      multivalued: false

```
</details>

![class_enumeration_erd](images/class_enumeration_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[default](#default)** | <sub>0..1</sub> | [EnumeratedValue](#enumeratedvalue) |  |
| **[element](#element)** | <sub>1..\*</sub> | [EnumeratedValue](#enumeratedvalue) |  |

#### Parents

 * [Concept](#concept)

#### Used as mixin by

 * [EnumerationScale](#enumerationscale)

#### Referenced by:

 *  **[EnumeratedQuantity](#enumeratedquantity)** : enumeration  <sub>0..\*</sub> 
 *  **[SystemOfQuantityKinds](#systemofquantitykinds)** : baseDimensionEnumeration  <sub>0..\*</sub> 




### EnumerationScale




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
EnumerationScale:
  is_a: Scale
  mixins:
  - Enumeration
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - Scale_permissibleMaths
  - Scale_permissibleTransformation
  - Scale_scaleType
  - Scale_dataStructure
  - Enumeration_default
  - Enumeration_element

```
</details>

![class_enumerationscale_erd](images/class_enumerationscale_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[dataStructure](#datastructure)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[permissibleMaths](#permissiblemaths)** | <sub>0..\*</sub> | [MathsFunctionType](#mathsfunctiontype) |  |
| **[permissibleTransformation](#permissibletransformation)** | <sub>0..\*</sub> | [TransformType](#transformtype) |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |
| **[scaleType](#scaletype)** | <sub>0..1</sub> | [ScaleType](#scaletype) |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |

#### Parents

 * [Scale](#scale)

#### Uses

 *  mixin: [Enumeration](#enumeration)




### Figure




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
Figure:
  is_a: Concept
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - Figure_imageLocation
  - Figure_figureCaption
  - Figure_figureLabel
  - Figure_height
  - Figure_image
  - Figure_landscape
  - Figure_width
  slot_usage:
    imageLocation:
      required: true
      multivalued: false
    figureCaption:
      multivalued: false
    figureLabel:
      multivalued: false
    height:
      multivalued: false
    image:
      multivalued: false
    landscape:
      multivalued: false
    width:
      multivalued: false

```
</details>

![class_figure_erd](images/class_figure_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |
| **[figureCaption](#figurecaption)** | <sub>0..1</sub> | None |  |
| **[figureLabel](#figurelabel)** | <sub>0..1</sub> | None |  |
| **[height](#height)** | <sub>0..1</sub> | None |  |
| **[image](#image)** | <sub>0..1</sub> | None |  |
| **[imageLocation](#imagelocation)** | <sub>1..1</sub> | None |  |
| **[landscape](#landscape)** | <sub>0..1</sub> | None |  |
| **[width](#width)** | <sub>0..1</sub> | None |  |

#### Parents

 * [Concept](#concept)

#### Referenced by:





### FloatingPointEncodingType




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
FloatingPointEncodingType:
  is_a: Encoding
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - Encoding_bits
  - Encoding_bytes

```
</details>

![class_floatingpointencodingtype_erd](images/class_floatingpointencodingtype_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[bits](#bits)** | <sub>0..1</sub> | None |  |
| **[bytes](#bytes)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |

#### Parents

 * [Encoding](#encoding)




### IntegerEncodingType




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
IntegerEncodingType:
  is_a: Encoding
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - Encoding_bits
  - Encoding_bytes

```
</details>

![class_integerencodingtype_erd](images/class_integerencodingtype_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[bits](#bits)** | <sub>0..1</sub> | None |  |
| **[bytes](#bytes)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |

#### Parents

 * [Encoding](#encoding)




### IntervalScale



<p>The interval type allows for the degree of difference between items, but not the ratio between them. Examples include temperature with the Celsius scale, which has two defined points (the freezing and boiling point of water at specific conditions) and then separated into 100 intervals, date when measured from an arbitrary epoch (such as AD), percentage such as a percentage return on a stock,[16] location in Cartesian coordinates, and direction measured in degrees from true or magnetic north. Ratios are not meaningful since 20 °C cannot be said to be \"twice as hot\" as 10 °C, nor can multiplication/division be carried out between any two dates directly. However, ratios of differences can be expressed; for example, one difference can be twice another. Interval type variables are sometimes also called \"scaled variables\", but the formal mathematical term is an affine space (in this case an affine line).</p>
<p>Characteristics: median, percentile &amp; Monotonic increasing (order (&lt;) &amp; totally ordered set</p>

median, percentile & Monotonic increasing (order (<)) & totally ordered set


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
IntervalScale:
  is_a: Scale
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - Scale_permissibleMaths
  - Scale_permissibleTransformation
  - Scale_scaleType
  - Scale_dataStructure

```
</details>

![class_intervalscale_erd](images/class_intervalscale_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[dataStructure](#datastructure)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[permissibleMaths](#permissiblemaths)** | <sub>0..\*</sub> | [MathsFunctionType](#mathsfunctiontype) |  |
| **[permissibleTransformation](#permissibletransformation)** | <sub>0..\*</sub> | [TransformType](#transformtype) |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |
| **[scaleType](#scaletype)** | <sub>0..1</sub> | [ScaleType](#scaletype) |  |

#### Parents

 * [Scale](#scale)




### LatexString



A type of string in which some characters may be wrapped with '$' and '$ characters for LaTeX rendering.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
LatexString: {}

```
</details>


This class has no attributes





### List




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
List: {}

```
</details>


This class has no attributes





### LogarithmicUnit



Logarithmic units are abstract mathematical units that can be used to express any quantities (physical or mathematical) that are defined on a logarithmic scale, that is, as being proportional to the value of a logarithm function. Examples of logarithmic units include common units of information and entropy, such as the bit, and the byte, as well as units of relative signal strength magnitude such as the decibel.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
LogarithmicUnit:
  is_a: DimensionlessUnit
  slots:
  - Verifiable_wikidataMatch
  - Verifiable_dbpediaMatch
  - Verifiable_isoNormativeReference
  - Verifiable_normativeReference
  - hasReciprocalUnit
  - isUnitOfSystem
  - omUnit
  - unitFor
  - Unit_applicableSystem
  - Unit_definedUnitOfSystem
  - Unit_derivedCoherentUnitOfSystem
  - Unit_derivedUnitOfSystem
  - Unit_exactMatch
  - Unit_hasDimensionVector
  - Unit_hasFactorUnit
  - Unit_hasQuantityKind
  - Unit_iec61360Code
  - Unit_prefix
  - Unit_qkdvDenominator
  - Unit_qkdvNumerator
  - Unit_scalingOf
  - Unit_ucumCode
  - Unit_udunitsCode
  - Unit_uneceCommonCode
  - Unit_altSymbol
  - Unit_latexDefinition
  - Unit_latexSymbol
  - Unit_siUnitsExpression
  - Unit_symbol
  - Unit_conversionMultiplier
  - Unit_conversionMultiplierSN
  - Unit_conversionOffset
  - Unit_conversionOffsetSN
  - Unit_factorUnitScalar
  - Unit_mathMLdefinition
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription

```
</details>

![class_logarithmicunit_erd](images/class_logarithmicunit_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[altSymbol](#altsymbol)** | <sub>0..\*</sub> | None |  |
| **[applicableSystem](#applicablesystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[conversionMultiplier](#conversionmultiplier)** | <sub>0..1</sub> | None |  |
| **[conversionMultiplierSN](#conversionmultipliersn)** | <sub>0..1</sub> | None |  |
| **[conversionOffset](#conversionoffset)** | <sub>0..1</sub> | None |  |
| **[conversionOffsetSN](#conversionoffsetsn)** | <sub>0..1</sub> | None |  |
| **[dbpediaMatch](#dbpediamatch)** | <sub>0..\*</sub> | uri |  |
| **[definedUnitOfSystem](#definedunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[derivedCoherentUnitOfSystem](#derivedcoherentunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[derivedUnitOfSystem](#derivedunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[exactMatch](#exactmatch)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[factorUnitScalar](#factorunitscalar)** | <sub>0..1</sub> | None |  |
| **[hasDimensionVector](#hasdimensionvector)** | <sub>0..1</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[hasFactorUnit](#hasfactorunit)** | <sub>0..\*</sub> | [Class](#class) |  |
| **[hasQuantityKind](#hasquantitykind)** | <sub>0..\*</sub> | [QuantityKind](#quantitykind) |  |
| **[hasReciprocalUnit](#hasreciprocalunit)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[iec61360Code](#iec61360code)** | <sub>0..\*</sub> | string |  |
| **[isUnitOfSystem](#isunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[isoNormativeReference](#isonormativereference)** | <sub>0..\*</sub> | None |  |
| **[latexDefinition](#latexdefinition)** | <sub>0..\*</sub> | None |  |
| **[latexSymbol](#latexsymbol)** | <sub>0..\*</sub> | None |  |
| **[mathMLdefinition](#mathmldefinition)** | <sub>0..1</sub> | None |  |
| **[normativeReference](#normativereference)** | <sub>0..\*</sub> | None |  |
| **[omUnit](#omunit)** | <sub>0..\*</sub> | None |  |
| **[prefix](#prefix)** | <sub>0..\*</sub> | [Prefix](#prefix) |  |
| **[qkdvDenominator](#qkdvdenominator)** | <sub>0..1</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[qkdvNumerator](#qkdvnumerator)** | <sub>0..1</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[scalingOf](#scalingof)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[siUnitsExpression](#siunitsexpression)** | <sub>0..\*</sub> | None |  |
| **[symbol](#symbol)** | <sub>0..\*</sub> | None |  |
| **[ucumCode](#ucumcode)** | <sub>0..\*</sub> | [UCUMcs](#ucumcs) |  |
| **[udunitsCode](#udunitscode)** | <sub>0..\*</sub> | string |  |
| **[uneceCommonCode](#unececommoncode)** | <sub>0..\*</sub> | string |  |
| **[unitFor](#unitfor)** | <sub>0..\*</sub> | None |  |
| **[wikidataMatch](#wikidatamatch)** | <sub>0..\*</sub> | uri |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |

#### Parents

 * [DimensionlessUnit](#dimensionlessunit)




### MathsFunctionType




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
MathsFunctionType:
  is_a: Concept
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription

```
</details>

![class_mathsfunctiontype_erd](images/class_mathsfunctiontype_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |

#### Parents

 * [Concept](#concept)

#### Referenced by:

 *  **[ScaleType](#scaletype)** : permissibleMaths  <sub>0..\*</sub> 
 *  **[Scale](#scale)** : permissibleMaths  <sub>0..\*</sub> 




### NISTSP811Comment




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
NIST_SP811_Comment:
  is_a: Comment
  slots:
  - Verifiable_wikidataMatch
  - Verifiable_dbpediaMatch
  - Verifiable_isoNormativeReference
  - Verifiable_normativeReference
  - Comment_rationale
  - Comment_description

```
</details>


#### Local class diagram

![class_nist_sp811_comment_local](images/class_nist_sp811_comment_local.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[dbpediaMatch](#dbpediamatch)** | <sub>0..\*</sub> | uri |  |
| **[isoNormativeReference](#isonormativereference)** | <sub>0..\*</sub> | None |  |
| **[normativeReference](#normativereference)** | <sub>0..\*</sub> | None |  |
| **[rationale](#rationale)** | <sub>0..\*</sub> | string |  |
| **[wikidataMatch](#wikidatamatch)** | <sub>0..\*</sub> | uri |  |

#### Parents

 * [Comment](#comment)




### NominalScale



A nominal scale differentiates between items or subjects based only on their names or (meta-)categories and other qualitative classifications they belong to; thus dichotomous data involves the construction of classifications as well as the classification of items. Discovery of an exception to a classification can be viewed as progress. Numbers may be used to represent the variables but the numbers do not have numerical value or relationship: For example, a Globally unique identifier. Examples of these classifications include gender, nationality, ethnicity, language, genre, style, biological species, and form. In a university one could also use hall of affiliation as an example.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
NominalScale:
  is_a: Scale
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - Scale_permissibleMaths
  - Scale_permissibleTransformation
  - Scale_scaleType
  - Scale_dataStructure

```
</details>

![class_nominalscale_erd](images/class_nominalscale_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[dataStructure](#datastructure)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[permissibleMaths](#permissiblemaths)** | <sub>0..\*</sub> | [MathsFunctionType](#mathsfunctiontype) |  |
| **[permissibleTransformation](#permissibletransformation)** | <sub>0..\*</sub> | [TransformType](#transformtype) |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |
| **[scaleType](#scaletype)** | <sub>0..1</sub> | [ScaleType](#scaletype) |  |

#### Parents

 * [Scale](#scale)




### NumericUnion




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
NumericUnion:
  mixins:
  - Concept
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription

```
</details>

![class_numericunion_erd](images/class_numericunion_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |

#### Uses

 *  mixin: [Concept](#concept)

#### Referenced by:





### Ontology




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
Ontology: {}

```
</details>


This class has no attributes


#### Referenced by:





### OrderedType




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
OrderedType:
  is_a: EnumeratedValue
  slots:
  - Verifiable_wikidataMatch
  - Verifiable_dbpediaMatch
  - Verifiable_isoNormativeReference
  - Verifiable_normativeReference
  - EnumeratedValue_altSymbol
  - EnumeratedValue_description
  - EnumeratedValue_abbreviation
  - EnumeratedValue_symbol
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_deprecated
  - Concept_plainTextDescription
  - OrderedType_literal
  slot_usage:
    literal:
      multivalued: false

```
</details>

![class_orderedtype_erd](images/class_orderedtype_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[altSymbol](#altsymbol)** | <sub>0..\*</sub> | None |  |
| **[dbpediaMatch](#dbpediamatch)** | <sub>0..\*</sub> | uri |  |
| **[isoNormativeReference](#isonormativereference)** | <sub>0..\*</sub> | None |  |
| **[normativeReference](#normativereference)** | <sub>0..\*</sub> | None |  |
| **[symbol](#symbol)** | <sub>0..1</sub> | None |  |
| **[wikidataMatch](#wikidatamatch)** | <sub>0..\*</sub> | uri |  |
| **[literal](#literal)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |

#### Parents

 * [EnumeratedValue](#enumeratedvalue)

#### Referenced by:

 *  **[Datatype](#datatype)** : orderedType  <sub>0..\*</sub> 




### OrdinalScale



The ordinal type allows for rank order (1st, 2nd, 3rd, etc.) by which data can be sorted, but still does not allow for relative degree of difference between them. Examples include, on one hand, dichotomous data with dichotomous (or dichotomized) values such as 'sick' vs. 'healthy' when measuring health, 'guilty' vs. 'innocent' when making judgments in courts, 'wrong/false' vs. 'right/true' when measuring truth value, and, on the other hand, non-dichotomous data consisting of a spectrum of values, such as 'completely agree', 'mostly agree', 'mostly disagree', 'completely disagree' when measuring opinion.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
OrdinalScale:
  is_a: Scale
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - Scale_permissibleMaths
  - Scale_permissibleTransformation
  - Scale_scaleType
  - Scale_dataStructure
  - OrdinalScale_order
  slot_usage:
    order:
      required: true
      multivalued: false

```
</details>

![class_ordinalscale_erd](images/class_ordinalscale_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[dataStructure](#datastructure)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[permissibleMaths](#permissiblemaths)** | <sub>0..\*</sub> | [MathsFunctionType](#mathsfunctiontype) |  |
| **[permissibleTransformation](#permissibletransformation)** | <sub>0..\*</sub> | [TransformType](#transformtype) |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |
| **[scaleType](#scaletype)** | <sub>0..1</sub> | [ScaleType](#scaletype) |  |
| **[order](#order)** | <sub>1..1</sub> | None |  |

#### Parents

 * [Scale](#scale)




### Organization




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
Organization:
  is_a: Concept
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - Organization_url
  slot_usage:
    url:
      required: false

```
</details>

![class_organization_erd](images/class_organization_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |
| **[url](#url)** | <sub>0..\*</sub> | None |  |

#### Parents

 * [Concept](#concept)




### PhysicalConstant



A physical constant is a physical quantity that is generally believed to be both universal in nature and constant in time. It can be contrasted with a mathematical constant, which is a fixed numerical value but does not directly involve any physical measurement. There are many physical constants in science, some of the most widely recognized being the speed of light in vacuum c, Newton's gravitational constant G, Planck's constant h, the electric permittivity of free space ε0, and the elementary charge e. Physical constants can take many dimensional forms, or may be dimensionless depending on the system of quantities and units used.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
PhysicalConstant:
  is_a: Quantity
  slots:
  - Quantifiable_dataEncoding
  - Quantifiable_datatype
  - Quantifiable_hasUnit
  - Quantifiable_relativeStandardUncertainty
  - Quantifiable_standardUncertainty
  - Quantifiable_standardUncertaintySN
  - Quantifiable_value
  - Quantifiable_valueSN
  - Quantity_hasQuantityKind
  - Quantity_quantityValue
  - Quantity_isDeltaQuantity
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - PhysicalConstant_applicableSystem
  - PhysicalConstant_applicableUnit
  - PhysicalConstant_dbpediaMatch
  - PhysicalConstant_exactMatch
  - PhysicalConstant_hasDimensionVector
  - PhysicalConstant_ucumCode
  - PhysicalConstant_exactConstant
  - PhysicalConstant_altSymbol
  - PhysicalConstant_isoNormativeReference
  - PhysicalConstant_latexSymbol
  - PhysicalConstant_normativeReference
  - PhysicalConstant_symbol
  - PhysicalConstant_latexDefinition
  - PhysicalConstant_mathMLdefinition
  slot_usage:
    applicableSystem:
      range: SystemOfUnits
    applicableUnit:
      range: Unit
    dbpediaMatch:
      range: uri
    exactMatch:
      range: PhysicalConstant
    hasDimensionVector:
      range: QuantityKindDimensionVector
    ucumCode:
      required: false
    exactConstant:
      range: boolean
    altSymbol:
      required: false
    isoNormativeReference:
      required: false
    latexSymbol:
      required: false
    normativeReference:
      required: false
    symbol:
      required: false
    latexDefinition:
      multivalued: false
    mathMLdefinition:
      multivalued: false

```
</details>

![class_physicalconstant_erd](images/class_physicalconstant_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[dataEncoding](#dataencoding)** | <sub>0..1</sub> | [DataEncoding](#dataencoding) |  |
| **[datatype](#datatype)** | <sub>0..1</sub> | [Datatype](#datatype) |  |
| **[hasQuantityKind](#hasquantitykind)** | <sub>0..\*</sub> | [QuantityKind](#quantitykind) |  |
| **[hasUnit](#hasunit)** | <sub>0..1</sub> | [Unit](#unit) |  |
| **[isDeltaQuantity](#isdeltaquantity)** | <sub>0..\*</sub> | boolean |  |
| **[quantityValue](#quantityvalue)** | <sub>0..\*</sub> | [QuantityValue](#quantityvalue) |  |
| **[relativeStandardUncertainty](#relativestandarduncertainty)** | <sub>0..1</sub> | double |  |
| **[standardUncertainty](#standarduncertainty)** | <sub>0..1</sub> | decimal |  |
| **[standardUncertaintySN](#standarduncertaintysn)** | <sub>0..\*</sub> | double |  |
| **[value](#value)** | <sub>0..1</sub> | None |  |
| **[valueSN](#valuesn)** | <sub>0..1</sub> | None |  |
| **[altSymbol](#altsymbol)** | <sub>0..\*</sub> | None |  |
| **[applicableSystem](#applicablesystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[applicableUnit](#applicableunit)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[dbpediaMatch](#dbpediamatch)** | <sub>0..\*</sub> | uri |  |
| **[exactConstant](#exactconstant)** | <sub>0..\*</sub> | boolean |  |
| **[exactMatch](#exactmatch)** | <sub>0..\*</sub> | [PhysicalConstant](#physicalconstant) |  |
| **[hasDimensionVector](#hasdimensionvector)** | <sub>0..\*</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[isoNormativeReference](#isonormativereference)** | <sub>0..\*</sub> | None |  |
| **[latexDefinition](#latexdefinition)** | <sub>0..1</sub> | None |  |
| **[latexSymbol](#latexsymbol)** | <sub>0..\*</sub> | None |  |
| **[mathMLdefinition](#mathmldefinition)** | <sub>0..1</sub> | None |  |
| **[normativeReference](#normativereference)** | <sub>0..\*</sub> | None |  |
| **[symbol](#symbol)** | <sub>0..\*</sub> | None |  |
| **[ucumCode](#ucumcode)** | <sub>0..\*</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |

#### Parents

 * [Quantity](#quantity)

#### Referenced by:

 *  **[PhysicalConstant](#physicalconstant)** : exactMatch  <sub>0..\*</sub> 
 *  **[SystemOfUnits](#systemofunits)** : applicablePhysicalConstant  <sub>0..\*</sub> 




### PlaneAngleUnit




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
PlaneAngleUnit:
  is_a: AngleUnit
  slots:
  - Verifiable_wikidataMatch
  - Verifiable_dbpediaMatch
  - Verifiable_isoNormativeReference
  - Verifiable_normativeReference
  - hasReciprocalUnit
  - isUnitOfSystem
  - omUnit
  - unitFor
  - Unit_applicableSystem
  - Unit_definedUnitOfSystem
  - Unit_derivedCoherentUnitOfSystem
  - Unit_derivedUnitOfSystem
  - Unit_exactMatch
  - Unit_hasDimensionVector
  - Unit_hasFactorUnit
  - Unit_hasQuantityKind
  - Unit_iec61360Code
  - Unit_prefix
  - Unit_qkdvDenominator
  - Unit_qkdvNumerator
  - Unit_scalingOf
  - Unit_ucumCode
  - Unit_udunitsCode
  - Unit_uneceCommonCode
  - Unit_altSymbol
  - Unit_latexDefinition
  - Unit_latexSymbol
  - Unit_siUnitsExpression
  - Unit_symbol
  - Unit_conversionMultiplier
  - Unit_conversionMultiplierSN
  - Unit_conversionOffset
  - Unit_conversionOffsetSN
  - Unit_factorUnitScalar
  - Unit_mathMLdefinition
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription

```
</details>

![class_planeangleunit_erd](images/class_planeangleunit_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[altSymbol](#altsymbol)** | <sub>0..\*</sub> | None |  |
| **[applicableSystem](#applicablesystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[conversionMultiplier](#conversionmultiplier)** | <sub>0..1</sub> | None |  |
| **[conversionMultiplierSN](#conversionmultipliersn)** | <sub>0..1</sub> | None |  |
| **[conversionOffset](#conversionoffset)** | <sub>0..1</sub> | None |  |
| **[conversionOffsetSN](#conversionoffsetsn)** | <sub>0..1</sub> | None |  |
| **[dbpediaMatch](#dbpediamatch)** | <sub>0..\*</sub> | uri |  |
| **[definedUnitOfSystem](#definedunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[derivedCoherentUnitOfSystem](#derivedcoherentunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[derivedUnitOfSystem](#derivedunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[exactMatch](#exactmatch)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[factorUnitScalar](#factorunitscalar)** | <sub>0..1</sub> | None |  |
| **[hasDimensionVector](#hasdimensionvector)** | <sub>0..1</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[hasFactorUnit](#hasfactorunit)** | <sub>0..\*</sub> | [Class](#class) |  |
| **[hasQuantityKind](#hasquantitykind)** | <sub>0..\*</sub> | [QuantityKind](#quantitykind) |  |
| **[hasReciprocalUnit](#hasreciprocalunit)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[iec61360Code](#iec61360code)** | <sub>0..\*</sub> | string |  |
| **[isUnitOfSystem](#isunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[isoNormativeReference](#isonormativereference)** | <sub>0..\*</sub> | None |  |
| **[latexDefinition](#latexdefinition)** | <sub>0..\*</sub> | None |  |
| **[latexSymbol](#latexsymbol)** | <sub>0..\*</sub> | None |  |
| **[mathMLdefinition](#mathmldefinition)** | <sub>0..1</sub> | None |  |
| **[normativeReference](#normativereference)** | <sub>0..\*</sub> | None |  |
| **[omUnit](#omunit)** | <sub>0..\*</sub> | None |  |
| **[prefix](#prefix)** | <sub>0..\*</sub> | [Prefix](#prefix) |  |
| **[qkdvDenominator](#qkdvdenominator)** | <sub>0..1</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[qkdvNumerator](#qkdvnumerator)** | <sub>0..1</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[scalingOf](#scalingof)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[siUnitsExpression](#siunitsexpression)** | <sub>0..\*</sub> | None |  |
| **[symbol](#symbol)** | <sub>0..\*</sub> | None |  |
| **[ucumCode](#ucumcode)** | <sub>0..\*</sub> | [UCUMcs](#ucumcs) |  |
| **[udunitsCode](#udunitscode)** | <sub>0..\*</sub> | string |  |
| **[uneceCommonCode](#unececommoncode)** | <sub>0..\*</sub> | string |  |
| **[unitFor](#unitfor)** | <sub>0..\*</sub> | None |  |
| **[wikidataMatch](#wikidatamatch)** | <sub>0..\*</sub> | uri |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |

#### Parents

 * [AngleUnit](#angleunit)




### Prefix




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
Prefix:
  is_a: Verifiable
  mixins:
  - Concept
  slots:
  - Verifiable_wikidataMatch
  - Verifiable_dbpediaMatch
  - Verifiable_isoNormativeReference
  - Verifiable_normativeReference
  - Prefix_exactMatch
  - Prefix_ucumCode
  - Prefix_altSymbol
  - Prefix_latexSymbol
  - Prefix_symbol
  - Prefix_prefixMultiplier
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  slot_usage:
    exactMatch:
      range: Prefix
    ucumCode:
      range: UCUMcs-term
    altSymbol:
      required: false
    latexSymbol:
      required: false
    symbol:
      required: false
    prefixMultiplier:
      multivalued: false

```
</details>

![class_prefix_erd](images/class_prefix_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[dbpediaMatch](#dbpediamatch)** | <sub>0..\*</sub> | uri |  |
| **[isoNormativeReference](#isonormativereference)** | <sub>0..\*</sub> | None |  |
| **[normativeReference](#normativereference)** | <sub>0..\*</sub> | None |  |
| **[wikidataMatch](#wikidatamatch)** | <sub>0..\*</sub> | uri |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[altSymbol](#altsymbol)** | <sub>0..\*</sub> | None |  |
| **[exactMatch](#exactmatch)** | <sub>0..\*</sub> | [Prefix](#prefix) |  |
| **[latexSymbol](#latexsymbol)** | <sub>0..\*</sub> | None |  |
| **[prefixMultiplier](#prefixmultiplier)** | <sub>0..1</sub> | None |  |
| **[symbol](#symbol)** | <sub>0..\*</sub> | None |  |
| **[ucumCode](#ucumcode)** | <sub>0..\*</sub> | [UCUMcs-term](#ucumcs-term) |  |

#### Parents

 * [Verifiable](#verifiable)

#### Children

 * [BinaryPrefix](#binaryprefix)
 * [DecimalPrefix](#decimalprefix)

#### Uses

 *  mixin: [Concept](#concept)

#### Referenced by:

 *  **[Prefix](#prefix)** : exactMatch  <sub>0..\*</sub> 
 *  **[SystemOfUnits](#systemofunits)** : prefix  <sub>0..\*</sub> 
 *  **[Unit](#unit)** : prefix  <sub>0..\*</sub> 




### Quantifiable



<p><em>Quantifiable</em> ascribes to some thing the capability of being measured, observed, or counted.</p>


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
Quantifiable:
  is_a: Aspect
  slots:
  - Quantifiable_dataEncoding
  - Quantifiable_datatype
  - Quantifiable_hasUnit
  - Quantifiable_relativeStandardUncertainty
  - Quantifiable_standardUncertainty
  - Quantifiable_standardUncertaintySN
  - Quantifiable_value
  - Quantifiable_valueSN
  slot_usage:
    dataEncoding:
      range: DataEncoding
      multivalued: false
    datatype:
      range: Datatype
      multivalued: false
    hasUnit:
      range: Unit
      multivalued: false
    relativeStandardUncertainty:
      range: double
      multivalued: false
    standardUncertainty:
      range: decimal
      multivalued: false
    standardUncertaintySN:
      range: double
    value:
      multivalued: false
    valueSN:
      multivalued: false

```
</details>

![class_quantifiable_erd](images/class_quantifiable_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[dataEncoding](#dataencoding)** | <sub>0..1</sub> | [DataEncoding](#dataencoding) |  |
| **[datatype](#datatype)** | <sub>0..1</sub> | [Datatype](#datatype) |  |
| **[hasUnit](#hasunit)** | <sub>0..1</sub> | [Unit](#unit) |  |
| **[relativeStandardUncertainty](#relativestandarduncertainty)** | <sub>0..1</sub> | double |  |
| **[standardUncertainty](#standarduncertainty)** | <sub>0..1</sub> | decimal |  |
| **[standardUncertaintySN](#standarduncertaintysn)** | <sub>0..\*</sub> | double |  |
| **[value](#value)** | <sub>0..1</sub> | None |  |
| **[valueSN](#valuesn)** | <sub>0..1</sub> | None |  |

#### Parents

 * [Aspect](#aspect)

#### Children

 * [Quantity](#quantity)
 * [QuantityValue](#quantityvalue)




### Quantity



<p class=\"lm-para\">A <b>quantity</b> is the measurement of an observable property of a particular object, event, or physical system. 
  A quantity is always associated with the context of measurement (i.e. the thing measured, the measured value, the accuracy of measurement, etc.) whereas the 
  underlying <b>quantity kind</b> is independent of any particular measurement. Thus, length is a quantity kind while the height of a rocket is a specific 
  quantity of length; its magnitude that may be expressed in meters, feet, inches, etc. Examples of physical quantities include physical constants, such as 
  the speed of light in a vacuum, Planck's constant, the electric permittivity of free space, and the fine structure constant. </p>
<p class=\"lm-para\">In other words, quantities are quantifiable aspects of the world, such as the duration of a movie, the distance between two points, 
velocity of a car, the pressure of the atmosphere, and a person's weight; and units are used to describe their numerical measure.</p> 
<p class=\"lm-para\">Many <b>quantity kinds</b> are related to each other by various physical laws, and as a result, the associated units of some quantity 
kinds can be expressed as products (or ratios) of powers of other quantity kinds (e.g., momentum is mass times velocity and velocity is defined as distance 
divided by time). In this way, some quantities can be calculated from other measured quantities using their associations to the quantity kinds in these 
expressions. These quantity kind relationships are also discussed in dimensional analysis. Those that cannot be so expressed can be regarded 
as \"fundamental\" in this sense.</p>
<p class=\"lm-para\">A quantity is distinguished from a \"quantity kind\" in that the former carries a value and the latter is a type specifier.</p>


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
Quantity:
  is_a: Quantifiable
  mixins:
  - Concept
  slots:
  - Quantifiable_dataEncoding
  - Quantifiable_datatype
  - Quantifiable_hasUnit
  - Quantifiable_relativeStandardUncertainty
  - Quantifiable_standardUncertainty
  - Quantifiable_standardUncertaintySN
  - Quantifiable_value
  - Quantifiable_valueSN
  - Quantity_hasQuantityKind
  - Quantity_quantityValue
  - Quantity_isDeltaQuantity
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  slot_usage:
    hasQuantityKind:
      range: QuantityKind
      required: false
    quantityValue:
      range: QuantityValue
    isDeltaQuantity:
      range: boolean

```
</details>

![class_quantity_erd](images/class_quantity_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[dataEncoding](#dataencoding)** | <sub>0..1</sub> | [DataEncoding](#dataencoding) |  |
| **[datatype](#datatype)** | <sub>0..1</sub> | [Datatype](#datatype) |  |
| **[hasUnit](#hasunit)** | <sub>0..1</sub> | [Unit](#unit) |  |
| **[relativeStandardUncertainty](#relativestandarduncertainty)** | <sub>0..1</sub> | double |  |
| **[standardUncertainty](#standarduncertainty)** | <sub>0..1</sub> | decimal |  |
| **[standardUncertaintySN](#standarduncertaintysn)** | <sub>0..\*</sub> | double |  |
| **[value](#value)** | <sub>0..1</sub> | None |  |
| **[valueSN](#valuesn)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasQuantityKind](#hasquantitykind)** | <sub>0..\*</sub> | [QuantityKind](#quantitykind) |  |
| **[isDeltaQuantity](#isdeltaquantity)** | <sub>0..\*</sub> | boolean |  |
| **[quantityValue](#quantityvalue)** | <sub>0..\*</sub> | [QuantityValue](#quantityvalue) |  |

#### Parents

 * [Quantifiable](#quantifiable)

#### Children

 * [PhysicalConstant](#physicalconstant)

#### Uses

 *  mixin: [Concept](#concept)

#### Referenced by:





### QuantityKind



A <b>Quantity Kind</b> is any observable property that can be  measured and quantified numerically. Familiar examples include physical properties such as length, mass, time, force, energy, power, electric charge, etc. Less familiar examples include currency, interest rate, price to earning ratio, and information capacity.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
QuantityKind:
  is_a: Verifiable
  mixins:
  - AbstractQuantityKind
  slots:
  - Verifiable_wikidataMatch
  - Verifiable_dbpediaMatch
  - Verifiable_isoNormativeReference
  - Verifiable_normativeReference
  - belongsToSystemOfQuantities
  - QuantityKind_dimensionVectorForSI
  - QuantityKind_exactMatch
  - QuantityKind_hasDimensionVector
  - QuantityKind_iec61360Code
  - QuantityKind_applicableCGSUnit
  - QuantityKind_applicableISOUnit
  - QuantityKind_applicableImperialUnit
  - QuantityKind_applicableSIUnit
  - QuantityKind_applicableUSCustomaryUnit
  - QuantityKind_applicableUnit
  - QuantityKind_qkdvDenominator
  - QuantityKind_qkdvNumerator
  - QuantityKind_latexDefinition
  - QuantityKind_mathMLdefinition
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - AbstractQuantityKind_broader
  - AbstractQuantityKind_altSymbol
  - AbstractQuantityKind_latexSymbol
  - AbstractQuantityKind_symbol
  slot_usage:
    dimensionVectorForSI:
      range: QuantityKindDimensionVector_SI
      multivalued: false
    exactMatch:
      range: QuantityKind
    hasDimensionVector:
      range: QuantityKindDimensionVector
    iec61360Code:
      range: string
    applicableCGSUnit:
      required: false
    applicableISOUnit:
      required: false
    applicableImperialUnit:
      required: false
    applicableSIUnit:
      required: false
    applicableUSCustomaryUnit:
      required: false
    applicableUnit:
      required: false
    qkdvDenominator:
      multivalued: false
    qkdvNumerator:
      multivalued: false
    latexDefinition:
      multivalued: false
    mathMLdefinition:
      multivalued: false

```
</details>

![class_quantitykind_erd](images/class_quantitykind_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[dbpediaMatch](#dbpediamatch)** | <sub>0..\*</sub> | uri |  |
| **[isoNormativeReference](#isonormativereference)** | <sub>0..\*</sub> | None |  |
| **[normativeReference](#normativereference)** | <sub>0..\*</sub> | None |  |
| **[wikidataMatch](#wikidatamatch)** | <sub>0..\*</sub> | uri |  |
| **[applicableCGSUnit](#applicablecgsunit)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[applicableISOUnit](#applicableisounit)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[applicableImperialUnit](#applicableimperialunit)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[applicableSIUnit](#applicablesiunit)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[applicableUSCustomaryUnit](#applicableuscustomaryunit)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[applicableUnit](#applicableunit)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[belongsToSystemOfQuantities](#belongstosystemofquantities)** | <sub>0..\*</sub> | [SystemOfQuantityKinds](#systemofquantitykinds) |  |
| **[dimensionVectorForSI](#dimensionvectorforsi)** | <sub>0..1</sub> | [QuantityKindDimensionVectorSI](#quantitykinddimensionvectorsi) |  |
| **[exactMatch](#exactmatch)** | <sub>0..\*</sub> | [QuantityKind](#quantitykind) |  |
| **[hasDimensionVector](#hasdimensionvector)** | <sub>0..\*</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[iec61360Code](#iec61360code)** | <sub>0..\*</sub> | string |  |
| **[latexDefinition](#latexdefinition)** | <sub>0..1</sub> | None |  |
| **[mathMLdefinition](#mathmldefinition)** | <sub>0..1</sub> | None |  |
| **[qkdvDenominator](#qkdvdenominator)** | <sub>0..1</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[qkdvNumerator](#qkdvnumerator)** | <sub>0..1</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |

#### Parents

 * [Verifiable](#verifiable)

#### Uses

 *  mixin: [AbstractQuantityKind](#abstractquantitykind)

#### Referenced by:

 *  **[AbstractQuantityKind](#abstractquantitykind)** : broader  <sub>0..1</sub> 
 *  **[BaseDimensionMagnitude](#basedimensionmagnitude)** : hasBaseQuantityKind  <sub>1..\*</sub> 
 *  **[QuantityKindDimensionVector](#quantitykinddimensionvector)** : hasReferenceQuantityKind  <sub>0..\*</sub> 
 *  **[QuantityKind](#quantitykind)** : exactMatch  <sub>0..\*</sub> 
 *  **[QuantityType](#quantitytype)** : value  <sub>0..\*</sub> 
 *  **[Quantity](#quantity)** : hasQuantityKind  <sub>0..\*</sub> 
 *  **[SystemOfQuantityKinds](#systemofquantitykinds)** : hasBaseQuantityKind  <sub>0..\*</sub> 
 *  **[SystemOfQuantityKinds](#systemofquantitykinds)** : hasQuantityKind  <sub>0..\*</sub> 
 *  **[SystemOfQuantityKinds](#systemofquantitykinds)** : systemDerivedQuantityKind  <sub>0..\*</sub> 
 *  **[Unit](#unit)** : hasQuantityKind  <sub>0..\*</sub> 
 *  **[UserQuantityKind](#userquantitykind)** : hasQuantityKind  <sub>1..\*</sub> 




### QuantityKindDimensionVector



<p class=\"lm-para\">A  <em>Quantity Kind Dimension Vector</em> describes the dimensionality of a quantity kind in the context of a system of units. In the SI system of units, the dimensions of a quantity kind are expressed as a product of the basic physical dimensions mass ($M$), length ($L$), time ($T$) current ($I$), amount of substance ($N$), luminous intensity ($J$) and absolute temperature ($\\theta$) as $dim \\, Q = L^{\\alpha} \\, M^{\\beta} \\, T^{\\gamma} \\, I ^{\\delta} \\, \\theta ^{\\epsilon} \\, N^{\\eta} \\, J ^{\\nu}$.</p>

<p class=\"lm-para\">The rational powers of the dimensional exponents, $\\alpha, \\, \\beta, \\, \\gamma, \\, \\delta, \\, \\epsilon, \\, \\eta, \\, \\nu$, are positive, negative, or zero.</p>

<p class=\"lm-para\">For example, the dimension of the physical quantity kind $\\it{speed}$ is $\\boxed{length/time}$, $L/T$ or $LT^{-1}$, and the dimension of the physical quantity kind force is $\\boxed{mass \\times acceleration}$ or $\\boxed{mass \\times (length/time)/time}$, $ML/T^2$ or $MLT^{-2}$ respectively.</p>


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
QuantityKindDimensionVector:
  is_a: Concept
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - QuantityKindDimensionVector_hasReferenceQuantityKind
  - QuantityKindDimensionVector_latexSymbol
  - QuantityKindDimensionVector_dimensionExponentForAmountOfSubstance
  - QuantityKindDimensionVector_dimensionExponentForElectricCurrent
  - QuantityKindDimensionVector_dimensionExponentForLength
  - QuantityKindDimensionVector_dimensionExponentForLuminousIntensity
  - QuantityKindDimensionVector_dimensionExponentForMass
  - QuantityKindDimensionVector_dimensionExponentForThermodynamicTemperature
  - QuantityKindDimensionVector_dimensionExponentForTime
  - QuantityKindDimensionVector_dimensionlessExponent
  - QuantityKindDimensionVector_latexDefinition
  slot_usage:
    hasReferenceQuantityKind:
      range: QuantityKind
    latexSymbol:
      required: false
    dimensionExponentForAmountOfSubstance:
      required: true
      multivalued: false
    dimensionExponentForElectricCurrent:
      required: true
      multivalued: false
    dimensionExponentForLength:
      required: true
      multivalued: false
    dimensionExponentForLuminousIntensity:
      required: true
      multivalued: false
    dimensionExponentForMass:
      required: true
      multivalued: false
    dimensionExponentForThermodynamicTemperature:
      required: true
      multivalued: false
    dimensionExponentForTime:
      required: true
      multivalued: false
    dimensionlessExponent:
      required: true
      multivalued: false
    latexDefinition:
      multivalued: false

```
</details>

![class_quantitykinddimensionvector_erd](images/class_quantitykinddimensionvector_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |
| **[dimensionExponentForAmountOfSubstance](#dimensionexponentforamountofsubstance)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForElectricCurrent](#dimensionexponentforelectriccurrent)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForLength](#dimensionexponentforlength)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForLuminousIntensity](#dimensionexponentforluminousintensity)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForMass](#dimensionexponentformass)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForThermodynamicTemperature](#dimensionexponentforthermodynamictemperature)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForTime](#dimensionexponentfortime)** | <sub>1..1</sub> | None |  |
| **[dimensionlessExponent](#dimensionlessexponent)** | <sub>1..1</sub> | None |  |
| **[hasReferenceQuantityKind](#hasreferencequantitykind)** | <sub>0..\*</sub> | [QuantityKind](#quantitykind) |  |
| **[latexDefinition](#latexdefinition)** | <sub>0..1</sub> | None |  |
| **[latexSymbol](#latexsymbol)** | <sub>0..\*</sub> | None |  |

#### Parents

 * [Concept](#concept)

#### Children

 * [QuantityKindDimensionVectorCGS](#quantitykinddimensionvectorcgs)
 * [QuantityKindDimensionVectorISO](#quantitykinddimensionvectoriso)
 * [QuantityKindDimensionVectorImperial](#quantitykinddimensionvectorimperial)
 * [QuantityKindDimensionVectorSI](#quantitykinddimensionvectorsi)

#### Referenced by:

 *  **[PhysicalConstant](#physicalconstant)** : hasDimensionVector  <sub>0..\*</sub> 
 *  **[QuantityKind](#quantitykind)** : hasDimensionVector  <sub>0..\*</sub> 
 *  **[QuantityKind](#quantitykind)** : qkdvDenominator  <sub>0..\*</sub> 
 *  **[QuantityKind](#quantitykind)** : qkdvNumerator  <sub>0..\*</sub> 
 *  **[Unit](#unit)** : hasDimensionVector  <sub>0..\*</sub> 
 *  **[Unit](#unit)** : qkdvDenominator  <sub>0..\*</sub> 
 *  **[Unit](#unit)** : qkdvNumerator  <sub>0..\*</sub> 




### QuantityKindDimensionVectorCGS



A <em>CGS Dimension Vector</em> is used to specify the dimensions for a C.G.S. quantity kind.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
QuantityKindDimensionVector_CGS:
  is_a: QuantityKindDimensionVector
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - QuantityKindDimensionVector_hasReferenceQuantityKind
  - QuantityKindDimensionVector_latexSymbol
  - QuantityKindDimensionVector_dimensionExponentForAmountOfSubstance
  - QuantityKindDimensionVector_dimensionExponentForElectricCurrent
  - QuantityKindDimensionVector_dimensionExponentForLength
  - QuantityKindDimensionVector_dimensionExponentForLuminousIntensity
  - QuantityKindDimensionVector_dimensionExponentForMass
  - QuantityKindDimensionVector_dimensionExponentForThermodynamicTemperature
  - QuantityKindDimensionVector_dimensionExponentForTime
  - QuantityKindDimensionVector_dimensionlessExponent
  - QuantityKindDimensionVector_latexDefinition

```
</details>

![class_quantitykinddimensionvector_cgs_erd](images/class_quantitykinddimensionvector_cgs_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[dimensionExponentForAmountOfSubstance](#dimensionexponentforamountofsubstance)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForElectricCurrent](#dimensionexponentforelectriccurrent)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForLength](#dimensionexponentforlength)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForLuminousIntensity](#dimensionexponentforluminousintensity)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForMass](#dimensionexponentformass)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForThermodynamicTemperature](#dimensionexponentforthermodynamictemperature)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForTime](#dimensionexponentfortime)** | <sub>1..1</sub> | None |  |
| **[dimensionlessExponent](#dimensionlessexponent)** | <sub>1..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasReferenceQuantityKind](#hasreferencequantitykind)** | <sub>0..\*</sub> | [QuantityKind](#quantitykind) |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[latexDefinition](#latexdefinition)** | <sub>0..1</sub> | None |  |
| **[latexSymbol](#latexsymbol)** | <sub>0..\*</sub> | None |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |

#### Parents

 * [QuantityKindDimensionVector](#quantitykinddimensionvector)

#### Children

 * [QuantityKindDimensionVectorCGS-EMU](#quantitykinddimensionvectorcgs-emu)
 * [QuantityKindDimensionVectorCGS-ESU](#quantitykinddimensionvectorcgs-esu)
 * [QuantityKindDimensionVectorCGS-GAUSS](#quantitykinddimensionvectorcgs-gauss)
 * [QuantityKindDimensionVectorCGS-LH](#quantitykinddimensionvectorcgs-lh)




### QuantityKindDimensionVectorCGS-EMU



A <em>CGS EMU Dimension Vector</em> is used to specify the dimensions for EMU C.G.S. quantity kind.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
QuantityKindDimensionVector_CGS-EMU:
  is_a: QuantityKindDimensionVector_CGS
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - QuantityKindDimensionVector_hasReferenceQuantityKind
  - QuantityKindDimensionVector_latexSymbol
  - QuantityKindDimensionVector_dimensionExponentForAmountOfSubstance
  - QuantityKindDimensionVector_dimensionExponentForElectricCurrent
  - QuantityKindDimensionVector_dimensionExponentForLength
  - QuantityKindDimensionVector_dimensionExponentForLuminousIntensity
  - QuantityKindDimensionVector_dimensionExponentForMass
  - QuantityKindDimensionVector_dimensionExponentForThermodynamicTemperature
  - QuantityKindDimensionVector_dimensionExponentForTime
  - QuantityKindDimensionVector_dimensionlessExponent
  - QuantityKindDimensionVector_latexDefinition

```
</details>

![class_quantitykinddimensionvector_cgs-emu_erd](images/class_quantitykinddimensionvector_cgs-emu_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[dimensionExponentForAmountOfSubstance](#dimensionexponentforamountofsubstance)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForElectricCurrent](#dimensionexponentforelectriccurrent)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForLength](#dimensionexponentforlength)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForLuminousIntensity](#dimensionexponentforluminousintensity)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForMass](#dimensionexponentformass)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForThermodynamicTemperature](#dimensionexponentforthermodynamictemperature)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForTime](#dimensionexponentfortime)** | <sub>1..1</sub> | None |  |
| **[dimensionlessExponent](#dimensionlessexponent)** | <sub>1..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasReferenceQuantityKind](#hasreferencequantitykind)** | <sub>0..\*</sub> | [QuantityKind](#quantitykind) |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[latexDefinition](#latexdefinition)** | <sub>0..1</sub> | None |  |
| **[latexSymbol](#latexsymbol)** | <sub>0..\*</sub> | None |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |

#### Parents

 * [QuantityKindDimensionVectorCGS](#quantitykinddimensionvectorcgs)




### QuantityKindDimensionVectorCGS-ESU



A <em>CGS ESU Dimension Vector</em> is used to specify the dimensions for ESU C.G.S. quantity kind.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
QuantityKindDimensionVector_CGS-ESU:
  is_a: QuantityKindDimensionVector_CGS
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - QuantityKindDimensionVector_hasReferenceQuantityKind
  - QuantityKindDimensionVector_latexSymbol
  - QuantityKindDimensionVector_dimensionExponentForAmountOfSubstance
  - QuantityKindDimensionVector_dimensionExponentForElectricCurrent
  - QuantityKindDimensionVector_dimensionExponentForLength
  - QuantityKindDimensionVector_dimensionExponentForLuminousIntensity
  - QuantityKindDimensionVector_dimensionExponentForMass
  - QuantityKindDimensionVector_dimensionExponentForThermodynamicTemperature
  - QuantityKindDimensionVector_dimensionExponentForTime
  - QuantityKindDimensionVector_dimensionlessExponent
  - QuantityKindDimensionVector_latexDefinition

```
</details>

![class_quantitykinddimensionvector_cgs-esu_erd](images/class_quantitykinddimensionvector_cgs-esu_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[dimensionExponentForAmountOfSubstance](#dimensionexponentforamountofsubstance)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForElectricCurrent](#dimensionexponentforelectriccurrent)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForLength](#dimensionexponentforlength)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForLuminousIntensity](#dimensionexponentforluminousintensity)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForMass](#dimensionexponentformass)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForThermodynamicTemperature](#dimensionexponentforthermodynamictemperature)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForTime](#dimensionexponentfortime)** | <sub>1..1</sub> | None |  |
| **[dimensionlessExponent](#dimensionlessexponent)** | <sub>1..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasReferenceQuantityKind](#hasreferencequantitykind)** | <sub>0..\*</sub> | [QuantityKind](#quantitykind) |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[latexDefinition](#latexdefinition)** | <sub>0..1</sub> | None |  |
| **[latexSymbol](#latexsymbol)** | <sub>0..\*</sub> | None |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |

#### Parents

 * [QuantityKindDimensionVectorCGS](#quantitykinddimensionvectorcgs)




### QuantityKindDimensionVectorCGS-GAUSS



A <em>CGS GAUSS Dimension Vector</em> is used to specify the dimensions for Gaussioan C.G.S. quantity kind.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
QuantityKindDimensionVector_CGS-GAUSS:
  is_a: QuantityKindDimensionVector_CGS
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - QuantityKindDimensionVector_hasReferenceQuantityKind
  - QuantityKindDimensionVector_latexSymbol
  - QuantityKindDimensionVector_dimensionExponentForAmountOfSubstance
  - QuantityKindDimensionVector_dimensionExponentForElectricCurrent
  - QuantityKindDimensionVector_dimensionExponentForLength
  - QuantityKindDimensionVector_dimensionExponentForLuminousIntensity
  - QuantityKindDimensionVector_dimensionExponentForMass
  - QuantityKindDimensionVector_dimensionExponentForThermodynamicTemperature
  - QuantityKindDimensionVector_dimensionExponentForTime
  - QuantityKindDimensionVector_dimensionlessExponent
  - QuantityKindDimensionVector_latexDefinition

```
</details>

![class_quantitykinddimensionvector_cgs-gauss_erd](images/class_quantitykinddimensionvector_cgs-gauss_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[dimensionExponentForAmountOfSubstance](#dimensionexponentforamountofsubstance)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForElectricCurrent](#dimensionexponentforelectriccurrent)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForLength](#dimensionexponentforlength)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForLuminousIntensity](#dimensionexponentforluminousintensity)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForMass](#dimensionexponentformass)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForThermodynamicTemperature](#dimensionexponentforthermodynamictemperature)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForTime](#dimensionexponentfortime)** | <sub>1..1</sub> | None |  |
| **[dimensionlessExponent](#dimensionlessexponent)** | <sub>1..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasReferenceQuantityKind](#hasreferencequantitykind)** | <sub>0..\*</sub> | [QuantityKind](#quantitykind) |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[latexDefinition](#latexdefinition)** | <sub>0..1</sub> | None |  |
| **[latexSymbol](#latexsymbol)** | <sub>0..\*</sub> | None |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |

#### Parents

 * [QuantityKindDimensionVectorCGS](#quantitykinddimensionvectorcgs)




### QuantityKindDimensionVectorCGS-LH



A <em>CGS LH Dimension Vector</em> is used to specify the dimensions for Lorentz-Heaviside C.G.S. quantity kind.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
QuantityKindDimensionVector_CGS-LH:
  is_a: QuantityKindDimensionVector_CGS
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - QuantityKindDimensionVector_hasReferenceQuantityKind
  - QuantityKindDimensionVector_latexSymbol
  - QuantityKindDimensionVector_dimensionExponentForAmountOfSubstance
  - QuantityKindDimensionVector_dimensionExponentForElectricCurrent
  - QuantityKindDimensionVector_dimensionExponentForLength
  - QuantityKindDimensionVector_dimensionExponentForLuminousIntensity
  - QuantityKindDimensionVector_dimensionExponentForMass
  - QuantityKindDimensionVector_dimensionExponentForThermodynamicTemperature
  - QuantityKindDimensionVector_dimensionExponentForTime
  - QuantityKindDimensionVector_dimensionlessExponent
  - QuantityKindDimensionVector_latexDefinition

```
</details>

![class_quantitykinddimensionvector_cgs-lh_erd](images/class_quantitykinddimensionvector_cgs-lh_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[dimensionExponentForAmountOfSubstance](#dimensionexponentforamountofsubstance)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForElectricCurrent](#dimensionexponentforelectriccurrent)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForLength](#dimensionexponentforlength)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForLuminousIntensity](#dimensionexponentforluminousintensity)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForMass](#dimensionexponentformass)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForThermodynamicTemperature](#dimensionexponentforthermodynamictemperature)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForTime](#dimensionexponentfortime)** | <sub>1..1</sub> | None |  |
| **[dimensionlessExponent](#dimensionlessexponent)** | <sub>1..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasReferenceQuantityKind](#hasreferencequantitykind)** | <sub>0..\*</sub> | [QuantityKind](#quantitykind) |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[latexDefinition](#latexdefinition)** | <sub>0..1</sub> | None |  |
| **[latexSymbol](#latexsymbol)** | <sub>0..\*</sub> | None |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |

#### Parents

 * [QuantityKindDimensionVectorCGS](#quantitykinddimensionvectorcgs)




### QuantityKindDimensionVectorISO




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
QuantityKindDimensionVector_ISO:
  is_a: QuantityKindDimensionVector
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - QuantityKindDimensionVector_hasReferenceQuantityKind
  - QuantityKindDimensionVector_latexSymbol
  - QuantityKindDimensionVector_dimensionExponentForAmountOfSubstance
  - QuantityKindDimensionVector_dimensionExponentForElectricCurrent
  - QuantityKindDimensionVector_dimensionExponentForLength
  - QuantityKindDimensionVector_dimensionExponentForLuminousIntensity
  - QuantityKindDimensionVector_dimensionExponentForMass
  - QuantityKindDimensionVector_dimensionExponentForThermodynamicTemperature
  - QuantityKindDimensionVector_dimensionExponentForTime
  - QuantityKindDimensionVector_dimensionlessExponent
  - QuantityKindDimensionVector_latexDefinition

```
</details>

![class_quantitykinddimensionvector_iso_erd](images/class_quantitykinddimensionvector_iso_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[dimensionExponentForAmountOfSubstance](#dimensionexponentforamountofsubstance)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForElectricCurrent](#dimensionexponentforelectriccurrent)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForLength](#dimensionexponentforlength)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForLuminousIntensity](#dimensionexponentforluminousintensity)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForMass](#dimensionexponentformass)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForThermodynamicTemperature](#dimensionexponentforthermodynamictemperature)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForTime](#dimensionexponentfortime)** | <sub>1..1</sub> | None |  |
| **[dimensionlessExponent](#dimensionlessexponent)** | <sub>1..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasReferenceQuantityKind](#hasreferencequantitykind)** | <sub>0..\*</sub> | [QuantityKind](#quantitykind) |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[latexDefinition](#latexdefinition)** | <sub>0..1</sub> | None |  |
| **[latexSymbol](#latexsymbol)** | <sub>0..\*</sub> | None |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |

#### Parents

 * [QuantityKindDimensionVector](#quantitykinddimensionvector)




### QuantityKindDimensionVectorImperial




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
QuantityKindDimensionVector_Imperial:
  is_a: QuantityKindDimensionVector
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - QuantityKindDimensionVector_hasReferenceQuantityKind
  - QuantityKindDimensionVector_latexSymbol
  - QuantityKindDimensionVector_dimensionExponentForAmountOfSubstance
  - QuantityKindDimensionVector_dimensionExponentForElectricCurrent
  - QuantityKindDimensionVector_dimensionExponentForLength
  - QuantityKindDimensionVector_dimensionExponentForLuminousIntensity
  - QuantityKindDimensionVector_dimensionExponentForMass
  - QuantityKindDimensionVector_dimensionExponentForThermodynamicTemperature
  - QuantityKindDimensionVector_dimensionExponentForTime
  - QuantityKindDimensionVector_dimensionlessExponent
  - QuantityKindDimensionVector_latexDefinition

```
</details>

![class_quantitykinddimensionvector_imperial_erd](images/class_quantitykinddimensionvector_imperial_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[dimensionExponentForAmountOfSubstance](#dimensionexponentforamountofsubstance)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForElectricCurrent](#dimensionexponentforelectriccurrent)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForLength](#dimensionexponentforlength)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForLuminousIntensity](#dimensionexponentforluminousintensity)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForMass](#dimensionexponentformass)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForThermodynamicTemperature](#dimensionexponentforthermodynamictemperature)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForTime](#dimensionexponentfortime)** | <sub>1..1</sub> | None |  |
| **[dimensionlessExponent](#dimensionlessexponent)** | <sub>1..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasReferenceQuantityKind](#hasreferencequantitykind)** | <sub>0..\*</sub> | [QuantityKind](#quantitykind) |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[latexDefinition](#latexdefinition)** | <sub>0..1</sub> | None |  |
| **[latexSymbol](#latexsymbol)** | <sub>0..\*</sub> | None |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |

#### Parents

 * [QuantityKindDimensionVector](#quantitykinddimensionvector)




### QuantityKindDimensionVectorSI




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
QuantityKindDimensionVector_SI:
  is_a: QuantityKindDimensionVector
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - QuantityKindDimensionVector_hasReferenceQuantityKind
  - QuantityKindDimensionVector_latexSymbol
  - QuantityKindDimensionVector_dimensionExponentForAmountOfSubstance
  - QuantityKindDimensionVector_dimensionExponentForElectricCurrent
  - QuantityKindDimensionVector_dimensionExponentForLength
  - QuantityKindDimensionVector_dimensionExponentForLuminousIntensity
  - QuantityKindDimensionVector_dimensionExponentForMass
  - QuantityKindDimensionVector_dimensionExponentForThermodynamicTemperature
  - QuantityKindDimensionVector_dimensionExponentForTime
  - QuantityKindDimensionVector_dimensionlessExponent
  - QuantityKindDimensionVector_latexDefinition

```
</details>

![class_quantitykinddimensionvector_si_erd](images/class_quantitykinddimensionvector_si_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[dimensionExponentForAmountOfSubstance](#dimensionexponentforamountofsubstance)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForElectricCurrent](#dimensionexponentforelectriccurrent)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForLength](#dimensionexponentforlength)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForLuminousIntensity](#dimensionexponentforluminousintensity)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForMass](#dimensionexponentformass)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForThermodynamicTemperature](#dimensionexponentforthermodynamictemperature)** | <sub>1..1</sub> | None |  |
| **[dimensionExponentForTime](#dimensionexponentfortime)** | <sub>1..1</sub> | None |  |
| **[dimensionlessExponent](#dimensionlessexponent)** | <sub>1..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasReferenceQuantityKind](#hasreferencequantitykind)** | <sub>0..\*</sub> | [QuantityKind](#quantitykind) |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[latexDefinition](#latexdefinition)** | <sub>0..1</sub> | None |  |
| **[latexSymbol](#latexsymbol)** | <sub>0..\*</sub> | None |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |

#### Parents

 * [QuantityKindDimensionVector](#quantitykinddimensionvector)

#### Referenced by:

 *  **[QuantityKind](#quantitykind)** : dimensionVectorForSI  <sub>0..\*</sub> 




### QuantityType




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
QuantityType:
  is_a: EnumeratedValue
  slots:
  - Verifiable_wikidataMatch
  - Verifiable_dbpediaMatch
  - Verifiable_isoNormativeReference
  - Verifiable_normativeReference
  - EnumeratedValue_altSymbol
  - EnumeratedValue_description
  - EnumeratedValue_abbreviation
  - EnumeratedValue_symbol
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_deprecated
  - Concept_plainTextDescription
  - QuantityType_value
  slot_usage:
    value:
      range: QuantityKind

```
</details>

![class_quantitytype_erd](images/class_quantitytype_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[altSymbol](#altsymbol)** | <sub>0..\*</sub> | None |  |
| **[dbpediaMatch](#dbpediamatch)** | <sub>0..\*</sub> | uri |  |
| **[isoNormativeReference](#isonormativereference)** | <sub>0..\*</sub> | None |  |
| **[normativeReference](#normativereference)** | <sub>0..\*</sub> | None |  |
| **[symbol](#symbol)** | <sub>0..1</sub> | None |  |
| **[wikidataMatch](#wikidatamatch)** | <sub>0..\*</sub> | uri |  |
| **[value](#value)** | <sub>0..\*</sub> | [QuantityKind](#quantitykind) |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |

#### Parents

 * [EnumeratedValue](#enumeratedvalue)




### QuantityValue



A <i>Quantity Value</i> expresses the magnitude and kind of a quantity and is given by the product of a numerical value <code>n</code> and a unit of measure <code>U</code>. The number multiplying the unit is referred to as the numerical value of the quantity expressed in that unit. Refer to <a href=\"http://physics.nist.gov/Pubs/SP811/sec07.html\">NIST SP 811 section 7</a> for more on quantity values.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
QuantityValue:
  is_a: Quantifiable
  mixins:
  - Concept
  slots:
  - Quantifiable_dataEncoding
  - Quantifiable_datatype
  - Quantifiable_relativeStandardUncertainty
  - Quantifiable_standardUncertainty
  - Quantifiable_standardUncertaintySN
  - Quantifiable_value
  - Quantifiable_valueSN
  - QuantityValue_hasUnit
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  slot_usage:
    hasUnit:
      multivalued: false

```
</details>

![class_quantityvalue_erd](images/class_quantityvalue_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[dataEncoding](#dataencoding)** | <sub>0..1</sub> | [DataEncoding](#dataencoding) |  |
| **[datatype](#datatype)** | <sub>0..1</sub> | [Datatype](#datatype) |  |
| **[relativeStandardUncertainty](#relativestandarduncertainty)** | <sub>0..1</sub> | double |  |
| **[standardUncertainty](#standarduncertainty)** | <sub>0..1</sub> | decimal |  |
| **[standardUncertaintySN](#standarduncertaintysn)** | <sub>0..\*</sub> | double |  |
| **[value](#value)** | <sub>0..1</sub> | None |  |
| **[valueSN](#valuesn)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasUnit](#hasunit)** | <sub>0..1</sub> | [Unit](#unit) |  |

#### Parents

 * [Quantifiable](#quantifiable)

#### Children

 * [ConstantValue](#constantvalue)

#### Uses

 *  mixin: [Concept](#concept)

#### Referenced by:

 *  **[Quantity](#quantity)** : quantityValue  <sub>0..\*</sub> 




### RatioScale



The ratio type takes its name from the fact that measurement is the estimation of the ratio between a magnitude of a continuous quantity and a unit magnitude of the same kind (Michell, 1997, 1999). A ratio scale possesses a meaningful (unique and non-arbitrary) zero value. Most measurement in the physical sciences and engineering is done on ratio scales. Examples include mass, length, duration, plane angle, energy and electric charge. In contrast to interval scales, ratios are now meaningful because having a non-arbitrary zero point makes it meaningful to say, for example, that one object has \"twice the length\" of another (= is \"twice as long\"). Very informally, many ratio scales can be described as specifying \"how much\" of something (i.e. an amount or magnitude) or \"how many\" (a count). The Kelvin temperature scale is a ratio scale because it has a unique, non-arbitrary zero point called absolute zero.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
RatioScale:
  is_a: Scale
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - Scale_permissibleMaths
  - Scale_permissibleTransformation
  - Scale_scaleType
  - Scale_dataStructure

```
</details>

![class_ratioscale_erd](images/class_ratioscale_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[dataStructure](#datastructure)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[permissibleMaths](#permissiblemaths)** | <sub>0..\*</sub> | [MathsFunctionType](#mathsfunctiontype) |  |
| **[permissibleTransformation](#permissibletransformation)** | <sub>0..\*</sub> | [TransformType](#transformtype) |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |
| **[scaleType](#scaletype)** | <sub>0..1</sub> | [ScaleType](#scaletype) |  |

#### Parents

 * [Scale](#scale)




### Resource




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
Resource: {}

```
</details>


#### Local class diagram

![class_resource_local](images/class_resource_local.svg)

This class has no attributes


#### Children

 * [UCUMcs](#ucumcs)
 * [UCUMcs-term](#ucumcs-term)
 * [ValueUnion](#valueunion)




### Rule




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
Rule:
  is_a: Verifiable
  mixins:
  - Concept
  slots:
  - Verifiable_wikidataMatch
  - Verifiable_dbpediaMatch
  - Verifiable_isoNormativeReference
  - Verifiable_normativeReference
  - Rule_ruleType
  - Rule_rationale
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  slot_usage:
    ruleType:
      range: RuleType
    rationale:
      required: false

```
</details>

![class_rule_erd](images/class_rule_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[dbpediaMatch](#dbpediamatch)** | <sub>0..\*</sub> | uri |  |
| **[isoNormativeReference](#isonormativereference)** | <sub>0..\*</sub> | None |  |
| **[normativeReference](#normativereference)** | <sub>0..\*</sub> | None |  |
| **[wikidataMatch](#wikidatamatch)** | <sub>0..\*</sub> | uri |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[rationale](#rationale)** | <sub>0..\*</sub> | string |  |
| **[ruleType](#ruletype)** | <sub>0..\*</sub> | [RuleType](#ruletype) |  |

#### Parents

 * [Verifiable](#verifiable)

#### Uses

 *  mixin: [Concept](#concept)

#### Referenced by:

 *  **[Concept](#concept)** : hasRule  <sub>0..\*</sub> 




### RuleType




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
RuleType:
  is_a: EnumeratedValue
  slots:
  - Verifiable_wikidataMatch
  - Verifiable_dbpediaMatch
  - Verifiable_isoNormativeReference
  - Verifiable_normativeReference
  - EnumeratedValue_altSymbol
  - EnumeratedValue_description
  - EnumeratedValue_abbreviation
  - EnumeratedValue_symbol
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_deprecated
  - Concept_plainTextDescription

```
</details>

![class_ruletype_erd](images/class_ruletype_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[altSymbol](#altsymbol)** | <sub>0..\*</sub> | None |  |
| **[dbpediaMatch](#dbpediamatch)** | <sub>0..\*</sub> | uri |  |
| **[isoNormativeReference](#isonormativereference)** | <sub>0..\*</sub> | None |  |
| **[normativeReference](#normativereference)** | <sub>0..\*</sub> | None |  |
| **[symbol](#symbol)** | <sub>0..1</sub> | None |  |
| **[wikidataMatch](#wikidatamatch)** | <sub>0..\*</sub> | uri |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |

#### Parents

 * [EnumeratedValue](#enumeratedvalue)

#### Referenced by:

 *  **[Rule](#rule)** : ruleType  <sub>0..\*</sub> 




### ScalarDatatype




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
ScalarDatatype:
  is_a: Datatype
  slots:
  - guidance
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - Datatype_basis
  - Datatype_cardinality
  - Datatype_orderedType
  - Datatype_ansiSQLName
  - Datatype_cName
  - Datatype_oracleSQLName
  - Datatype_protocolBuffersName
  - Datatype_pythonName
  - Datatype_vbName
  - Datatype_bounded
  - Datatype_id
  - Datatype_javaName
  - Datatype_jsName
  - Datatype_matlabName
  - Datatype_microsoftSQLServerName
  - Datatype_mySQLName
  - Datatype_odbcName
  - Datatype_oleDBName
  - ScalarDatatype_rdfsDatatype
  - ScalarDatatype_bits
  - ScalarDatatype_bytes
  - ScalarDatatype_length
  - ScalarDatatype_maxExclusive
  - ScalarDatatype_maxInclusive
  - ScalarDatatype_minExclusive
  - ScalarDatatype_minInclusive
  slot_usage:
    rdfsDatatype:
      range: Datatype
      multivalued: false
    bits:
      multivalued: false
    bytes:
      multivalued: false
    length:
      multivalued: false
    maxExclusive:
      multivalued: false
    maxInclusive:
      multivalued: false
    minExclusive:
      multivalued: false
    minInclusive:
      multivalued: false

```
</details>

![class_scalardatatype_erd](images/class_scalardatatype_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[ansiSQLName](#ansisqlname)** | <sub>0..1</sub> | string |  |
| **[basis](#basis)** | <sub>0..1</sub> | [Datatype](#datatype) |  |
| **[bounded](#bounded)** | <sub>0..1</sub> | None |  |
| **[cName](#cname)** | <sub>0..1</sub> | string |  |
| **[cardinality](#cardinality)** | <sub>0..1</sub> | [CardinalityType](#cardinalitytype) |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[javaName](#javaname)** | <sub>0..1</sub> | None |  |
| **[jsName](#jsname)** | <sub>0..1</sub> | None |  |
| **[matlabName](#matlabname)** | <sub>0..1</sub> | None |  |
| **[microsoftSQLServerName](#microsoftsqlservername)** | <sub>0..1</sub> | None |  |
| **[mySQLName](#mysqlname)** | <sub>0..1</sub> | None |  |
| **[odbcName](#odbcname)** | <sub>0..1</sub> | None |  |
| **[oleDBName](#oledbname)** | <sub>0..1</sub> | None |  |
| **[oracleSQLName](#oraclesqlname)** | <sub>0..1</sub> | string |  |
| **[orderedType](#orderedtype)** | <sub>0..1</sub> | [OrderedType](#orderedtype) |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |
| **[protocolBuffersName](#protocolbuffersname)** | <sub>0..1</sub> | string |  |
| **[pythonName](#pythonname)** | <sub>0..1</sub> | string |  |
| **[vbName](#vbname)** | <sub>0..1</sub> | string |  |
| **[bits](#bits)** | <sub>0..1</sub> | None |  |
| **[bytes](#bytes)** | <sub>0..1</sub> | None |  |
| **[length](#length)** | <sub>0..1</sub> | None |  |
| **[maxExclusive](#maxexclusive)** | <sub>0..1</sub> | None |  |
| **[maxInclusive](#maxinclusive)** | <sub>0..1</sub> | None |  |
| **[minExclusive](#minexclusive)** | <sub>0..1</sub> | None |  |
| **[minInclusive](#mininclusive)** | <sub>0..1</sub> | None |  |
| **[rdfsDatatype](#rdfsdatatype)** | <sub>0..1</sub> | [Datatype](#datatype) |  |

#### Parents

 * [Datatype](#datatype)




### Scale



Scales (also called \"scales of measurement\" or \"levels of measurement\")  are expressions that typically refer to the theory of scale types.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
Scale:
  is_a: Concept
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - Scale_permissibleMaths
  - Scale_permissibleTransformation
  - Scale_scaleType
  - Scale_dataStructure
  slot_usage:
    permissibleMaths:
      range: MathsFunctionType
    permissibleTransformation:
      range: TransformType
    scaleType:
      range: ScaleType
      multivalued: false
    dataStructure:
      multivalued: false

```
</details>

![class_scale_erd](images/class_scale_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |
| **[dataStructure](#datastructure)** | <sub>0..1</sub> | None |  |
| **[permissibleMaths](#permissiblemaths)** | <sub>0..\*</sub> | [MathsFunctionType](#mathsfunctiontype) |  |
| **[permissibleTransformation](#permissibletransformation)** | <sub>0..\*</sub> | [TransformType](#transformtype) |  |
| **[scaleType](#scaletype)** | <sub>0..1</sub> | [ScaleType](#scaletype) |  |

#### Parents

 * [Concept](#concept)

#### Children

 * [EnumerationScale](#enumerationscale)
 * [IntervalScale](#intervalscale)
 * [NominalScale](#nominalscale)
 * [OrdinalScale](#ordinalscale)
 * [RatioScale](#ratioscale)




### ScaleType




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
ScaleType:
  is_a: EnumeratedValue
  slots:
  - Verifiable_wikidataMatch
  - Verifiable_dbpediaMatch
  - Verifiable_isoNormativeReference
  - Verifiable_normativeReference
  - EnumeratedValue_altSymbol
  - EnumeratedValue_description
  - EnumeratedValue_abbreviation
  - EnumeratedValue_symbol
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_deprecated
  - Concept_plainTextDescription
  - ScaleType_permissibleMaths
  - ScaleType_permissibleTransformation
  - ScaleType_dataStructure
  slot_usage:
    permissibleMaths:
      range: MathsFunctionType
    permissibleTransformation:
      range: TransformType
    dataStructure:
      multivalued: false

```
</details>

![class_scaletype_erd](images/class_scaletype_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[altSymbol](#altsymbol)** | <sub>0..\*</sub> | None |  |
| **[dbpediaMatch](#dbpediamatch)** | <sub>0..\*</sub> | uri |  |
| **[isoNormativeReference](#isonormativereference)** | <sub>0..\*</sub> | None |  |
| **[normativeReference](#normativereference)** | <sub>0..\*</sub> | None |  |
| **[symbol](#symbol)** | <sub>0..1</sub> | None |  |
| **[wikidataMatch](#wikidatamatch)** | <sub>0..\*</sub> | uri |  |
| **[dataStructure](#datastructure)** | <sub>0..1</sub> | None |  |
| **[permissibleMaths](#permissiblemaths)** | <sub>0..\*</sub> | [MathsFunctionType](#mathsfunctiontype) |  |
| **[permissibleTransformation](#permissibletransformation)** | <sub>0..\*</sub> | [TransformType](#transformtype) |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |

#### Parents

 * [EnumeratedValue](#enumeratedvalue)

#### Referenced by:

 *  **[Scale](#scale)** : scaleType  <sub>0..\*</sub> 




### SignednessType




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
SignednessType: {}

```
</details>


This class has no attributes





### SolidAngleUnit




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
SolidAngleUnit:
  is_a: AngleUnit
  slots:
  - Verifiable_wikidataMatch
  - Verifiable_dbpediaMatch
  - Verifiable_isoNormativeReference
  - Verifiable_normativeReference
  - hasReciprocalUnit
  - isUnitOfSystem
  - omUnit
  - unitFor
  - Unit_applicableSystem
  - Unit_definedUnitOfSystem
  - Unit_derivedCoherentUnitOfSystem
  - Unit_derivedUnitOfSystem
  - Unit_exactMatch
  - Unit_hasDimensionVector
  - Unit_hasFactorUnit
  - Unit_hasQuantityKind
  - Unit_iec61360Code
  - Unit_prefix
  - Unit_qkdvDenominator
  - Unit_qkdvNumerator
  - Unit_scalingOf
  - Unit_ucumCode
  - Unit_udunitsCode
  - Unit_uneceCommonCode
  - Unit_altSymbol
  - Unit_latexDefinition
  - Unit_latexSymbol
  - Unit_siUnitsExpression
  - Unit_symbol
  - Unit_conversionMultiplier
  - Unit_conversionMultiplierSN
  - Unit_conversionOffset
  - Unit_conversionOffsetSN
  - Unit_factorUnitScalar
  - Unit_mathMLdefinition
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription

```
</details>

![class_solidangleunit_erd](images/class_solidangleunit_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[altSymbol](#altsymbol)** | <sub>0..\*</sub> | None |  |
| **[applicableSystem](#applicablesystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[conversionMultiplier](#conversionmultiplier)** | <sub>0..1</sub> | None |  |
| **[conversionMultiplierSN](#conversionmultipliersn)** | <sub>0..1</sub> | None |  |
| **[conversionOffset](#conversionoffset)** | <sub>0..1</sub> | None |  |
| **[conversionOffsetSN](#conversionoffsetsn)** | <sub>0..1</sub> | None |  |
| **[dbpediaMatch](#dbpediamatch)** | <sub>0..\*</sub> | uri |  |
| **[definedUnitOfSystem](#definedunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[derivedCoherentUnitOfSystem](#derivedcoherentunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[derivedUnitOfSystem](#derivedunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[exactMatch](#exactmatch)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[factorUnitScalar](#factorunitscalar)** | <sub>0..1</sub> | None |  |
| **[hasDimensionVector](#hasdimensionvector)** | <sub>0..1</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[hasFactorUnit](#hasfactorunit)** | <sub>0..\*</sub> | [Class](#class) |  |
| **[hasQuantityKind](#hasquantitykind)** | <sub>0..\*</sub> | [QuantityKind](#quantitykind) |  |
| **[hasReciprocalUnit](#hasreciprocalunit)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[iec61360Code](#iec61360code)** | <sub>0..\*</sub> | string |  |
| **[isUnitOfSystem](#isunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[isoNormativeReference](#isonormativereference)** | <sub>0..\*</sub> | None |  |
| **[latexDefinition](#latexdefinition)** | <sub>0..\*</sub> | None |  |
| **[latexSymbol](#latexsymbol)** | <sub>0..\*</sub> | None |  |
| **[mathMLdefinition](#mathmldefinition)** | <sub>0..1</sub> | None |  |
| **[normativeReference](#normativereference)** | <sub>0..\*</sub> | None |  |
| **[omUnit](#omunit)** | <sub>0..\*</sub> | None |  |
| **[prefix](#prefix)** | <sub>0..\*</sub> | [Prefix](#prefix) |  |
| **[qkdvDenominator](#qkdvdenominator)** | <sub>0..1</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[qkdvNumerator](#qkdvnumerator)** | <sub>0..1</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[scalingOf](#scalingof)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[siUnitsExpression](#siunitsexpression)** | <sub>0..\*</sub> | None |  |
| **[symbol](#symbol)** | <sub>0..\*</sub> | None |  |
| **[ucumCode](#ucumcode)** | <sub>0..\*</sub> | [UCUMcs](#ucumcs) |  |
| **[udunitsCode](#udunitscode)** | <sub>0..\*</sub> | string |  |
| **[uneceCommonCode](#unececommoncode)** | <sub>0..\*</sub> | string |  |
| **[unitFor](#unitfor)** | <sub>0..\*</sub> | None |  |
| **[wikidataMatch](#wikidatamatch)** | <sub>0..\*</sub> | uri |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |

#### Parents

 * [AngleUnit](#angleunit)




### Statement




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
Statement: {}

```
</details>


This class has no attributes





### StringEncodingType




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
StringEncodingType: {}

```
</details>


#### Local class diagram

![class_stringencodingtype_local](images/class_stringencodingtype_local.svg)

This class has no attributes


#### Children

 * [DateTimeStringEncodingType](#datetimestringencodingtype)




### Symbol




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
Symbol:
  is_a: Concept
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription

```
</details>

![class_symbol_erd](images/class_symbol_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |

#### Parents

 * [Concept](#concept)




### SymmetricRelation




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
SymmetricRelation: {}

```
</details>


This class has no attributes





### SystemOfQuantityKinds



A system of quantity kinds is a set of one or more quantity kinds together with a set of zero or more algebraic equations that define relationships between quantity kinds in the set. In the physical sciences, the equations relating quantity kinds are typically physical laws and definitional relations, and constants of proportionality. Examples include Newton’s First Law of Motion, Coulomb’s Law, and the definition of velocity as the instantaneous change in position.  In almost all cases, the system identifies a subset of base quantity kinds. The base set is chosen so that all other quantity kinds of interest can be derived from the base quantity kinds and the algebraic equations. If the unit system is explicitly associated with a quantity kind system, then the unit system must define at least one unit for each quantity kind.  From a scientific point of view, the division of quantities into base quantities and derived quantities is a matter of convention.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
SystemOfQuantityKinds:
  is_a: Concept
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - SystemOfQuantityKinds_baseDimensionEnumeration
  - SystemOfQuantityKinds_hasBaseQuantityKind
  - SystemOfQuantityKinds_hasQuantityKind
  - SystemOfQuantityKinds_hasUnitSystem
  - SystemOfQuantityKinds_systemDerivedQuantityKind
  slot_usage:
    baseDimensionEnumeration:
      range: Enumeration
      multivalued: false
    hasBaseQuantityKind:
      range: QuantityKind
    hasQuantityKind:
      range: QuantityKind
      required: false
    hasUnitSystem:
      range: SystemOfUnits
    systemDerivedQuantityKind:
      range: QuantityKind

```
</details>

![class_systemofquantitykinds_erd](images/class_systemofquantitykinds_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |
| **[baseDimensionEnumeration](#basedimensionenumeration)** | <sub>0..1</sub> | [Enumeration](#enumeration) |  |
| **[hasBaseQuantityKind](#hasbasequantitykind)** | <sub>0..\*</sub> | [QuantityKind](#quantitykind) |  |
| **[hasQuantityKind](#hasquantitykind)** | <sub>0..\*</sub> | [QuantityKind](#quantitykind) |  |
| **[hasUnitSystem](#hasunitsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[systemDerivedQuantityKind](#systemderivedquantitykind)** | <sub>0..\*</sub> | [QuantityKind](#quantitykind) |  |

#### Parents

 * [Concept](#concept)

#### Referenced by:

 *  **[QuantityKind](#quantitykind)** : belongsToSystemOfQuantities  <sub>0..\*</sub> 




### SystemOfUnits



A system of units is a set of units which are chosen as the reference scales for some set of quantity kinds together with the definitions of each unit. Units may be defined by experimental observation or by proportion to another unit not included in the system. If the unit system is explicitly associated with a quantity kind system, then the unit system must define at least one unit for each quantity kind.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
SystemOfUnits:
  is_a: Verifiable
  mixins:
  - Concept
  slots:
  - Verifiable_wikidataMatch
  - Verifiable_dbpediaMatch
  - Verifiable_isoNormativeReference
  - Verifiable_normativeReference
  - SystemOfUnits_applicablePhysicalConstant
  - SystemOfUnits_hasAllowedUnit
  - SystemOfUnits_hasBaseUnit
  - SystemOfUnits_hasCoherentUnit
  - SystemOfUnits_hasDefinedUnit
  - SystemOfUnits_hasDerivedCoherentUnit
  - SystemOfUnits_hasDerivedUnit
  - SystemOfUnits_hasUnit
  - SystemOfUnits_prefix
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  slot_usage:
    applicablePhysicalConstant:
      range: PhysicalConstant
    hasAllowedUnit:
      range: Unit
    hasBaseUnit:
      range: Unit
    hasCoherentUnit:
      range: Unit
    hasDefinedUnit:
      range: Unit
    hasDerivedCoherentUnit:
      range: Unit
    hasDerivedUnit:
      range: Unit
    hasUnit:
      range: Unit
    prefix:
      range: Prefix

```
</details>

![class_systemofunits_erd](images/class_systemofunits_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[dbpediaMatch](#dbpediamatch)** | <sub>0..\*</sub> | uri |  |
| **[isoNormativeReference](#isonormativereference)** | <sub>0..\*</sub> | None |  |
| **[normativeReference](#normativereference)** | <sub>0..\*</sub> | None |  |
| **[wikidataMatch](#wikidatamatch)** | <sub>0..\*</sub> | uri |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[applicablePhysicalConstant](#applicablephysicalconstant)** | <sub>0..\*</sub> | [PhysicalConstant](#physicalconstant) |  |
| **[hasAllowedUnit](#hasallowedunit)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[hasBaseUnit](#hasbaseunit)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[hasCoherentUnit](#hascoherentunit)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[hasDefinedUnit](#hasdefinedunit)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[hasDerivedCoherentUnit](#hasderivedcoherentunit)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[hasDerivedUnit](#hasderivedunit)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[hasUnit](#hasunit)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[prefix](#prefix)** | <sub>0..\*</sub> | [Prefix](#prefix) |  |

#### Parents

 * [Verifiable](#verifiable)

#### Uses

 *  mixin: [Concept](#concept)

#### Referenced by:

 *  **[PhysicalConstant](#physicalconstant)** : applicableSystem  <sub>0..\*</sub> 
 *  **[SystemOfQuantityKinds](#systemofquantitykinds)** : hasUnitSystem  <sub>0..\*</sub> 
 *  **[Unit](#unit)** : applicableSystem  <sub>0..\*</sub> 
 *  **[Unit](#unit)** : definedUnitOfSystem  <sub>0..\*</sub> 
 *  **[Unit](#unit)** : derivedCoherentUnitOfSystem  <sub>0..\*</sub> 
 *  **[Unit](#unit)** : derivedUnitOfSystem  <sub>0..\*</sub> 
 *  **[Unit](#unit)** : isUnitOfSystem  <sub>0..\*</sub> 




### Thing

The root class for all QUDT concepts


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
Thing:
  description: !!python/object/new:linkml_runtime.utils.yamlutils.extended_str
    args:
    - The root class for all QUDT concepts
    state:
      _s: !!python/object/apply:yaml._yaml.__pyx_unpickle_Mark
        args:
        - !!python/name:yaml._yaml.Mark ''
        - 41581148
        - null
        state: !!python/tuple
        - null
        - 17
        - 620
        - 21
        - linkml_qudt.yaml
        - null
      _len: 36

```
</details>


#### Local class diagram

![class_thing_local](images/class_thing_local.svg)

This class has no attributes


#### Children

 * [Aspect](#aspect)
 * [Concept](#concept)




### TransformType




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
TransformType:
  is_a: EnumeratedValue
  slots:
  - Verifiable_wikidataMatch
  - Verifiable_dbpediaMatch
  - Verifiable_isoNormativeReference
  - Verifiable_normativeReference
  - EnumeratedValue_altSymbol
  - EnumeratedValue_description
  - EnumeratedValue_abbreviation
  - EnumeratedValue_symbol
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_deprecated
  - Concept_plainTextDescription

```
</details>

![class_transformtype_erd](images/class_transformtype_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[altSymbol](#altsymbol)** | <sub>0..\*</sub> | None |  |
| **[dbpediaMatch](#dbpediamatch)** | <sub>0..\*</sub> | uri |  |
| **[isoNormativeReference](#isonormativereference)** | <sub>0..\*</sub> | None |  |
| **[normativeReference](#normativereference)** | <sub>0..\*</sub> | None |  |
| **[symbol](#symbol)** | <sub>0..1</sub> | None |  |
| **[wikidataMatch](#wikidatamatch)** | <sub>0..\*</sub> | uri |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |

#### Parents

 * [EnumeratedValue](#enumeratedvalue)

#### Referenced by:

 *  **[ScaleType](#scaletype)** : permissibleTransformation  <sub>0..\*</sub> 
 *  **[Scale](#scale)** : permissibleTransformation  <sub>0..\*</sub> 




### UCUMcs



Lexical pattern for the case-sensitive version of UCUM code


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
UCUMcs:
  is_a: Resource

```
</details>

![class_ucumcs_erd](images/class_ucumcs_erd.svg)

This class has no attributes


#### Parents

 * [Resource](#resource)

#### Referenced by:

 *  **[Unit](#unit)** : ucumCode  <sub>0..\*</sub> 




### UCUMcs-term



Lexical pattern for the terminal symbols in the case-sensitive version of UCUM code


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
UCUMcs-term:
  is_a: Resource

```
</details>

![class_ucumcs-term_erd](images/class_ucumcs-term_erd.svg)

This class has no attributes


#### Parents

 * [Resource](#resource)

#### Referenced by:

 *  **[Prefix](#prefix)** : ucumCode  <sub>0..\*</sub> 




### Unit




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
Unit:
  is_a: Verifiable
  mixins:
  - Concept
  slots:
  - Verifiable_wikidataMatch
  - Verifiable_dbpediaMatch
  - Verifiable_isoNormativeReference
  - Verifiable_normativeReference
  - hasReciprocalUnit
  - isUnitOfSystem
  - omUnit
  - unitFor
  - Unit_applicableSystem
  - Unit_definedUnitOfSystem
  - Unit_derivedCoherentUnitOfSystem
  - Unit_derivedUnitOfSystem
  - Unit_exactMatch
  - Unit_hasDimensionVector
  - Unit_hasFactorUnit
  - Unit_hasQuantityKind
  - Unit_iec61360Code
  - Unit_prefix
  - Unit_qkdvDenominator
  - Unit_qkdvNumerator
  - Unit_scalingOf
  - Unit_ucumCode
  - Unit_udunitsCode
  - Unit_uneceCommonCode
  - Unit_altSymbol
  - Unit_latexDefinition
  - Unit_latexSymbol
  - Unit_siUnitsExpression
  - Unit_symbol
  - Unit_conversionMultiplier
  - Unit_conversionMultiplierSN
  - Unit_conversionOffset
  - Unit_conversionOffsetSN
  - Unit_factorUnitScalar
  - Unit_mathMLdefinition
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  slot_usage:
    applicableSystem:
      range: SystemOfUnits
    definedUnitOfSystem:
      range: SystemOfUnits
    derivedCoherentUnitOfSystem:
      range: SystemOfUnits
    derivedUnitOfSystem:
      range: SystemOfUnits
    exactMatch:
      range: Unit
    hasDimensionVector:
      range: QuantityKindDimensionVector
      multivalued: false
    hasFactorUnit:
      range: Class
    hasQuantityKind:
      range: QuantityKind
    iec61360Code:
      range: string
    prefix:
      range: Prefix
    qkdvDenominator:
      range: QuantityKindDimensionVector
      multivalued: false
    qkdvNumerator:
      range: QuantityKindDimensionVector
      multivalued: false
    scalingOf:
      range: Unit
    ucumCode:
      range: UCUMcs
    udunitsCode:
      range: string
    uneceCommonCode:
      range: string
    altSymbol:
      required: false
    latexDefinition:
      required: false
    latexSymbol:
      required: false
    siUnitsExpression:
      required: false
    symbol:
      required: false
    conversionMultiplier:
      multivalued: false
    conversionMultiplierSN:
      multivalued: false
    conversionOffset:
      multivalued: false
    conversionOffsetSN:
      multivalued: false
    factorUnitScalar:
      multivalued: false
    mathMLdefinition:
      multivalued: false

```
</details>

![class_unit_erd](images/class_unit_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[dbpediaMatch](#dbpediamatch)** | <sub>0..\*</sub> | uri |  |
| **[isoNormativeReference](#isonormativereference)** | <sub>0..\*</sub> | None |  |
| **[normativeReference](#normativereference)** | <sub>0..\*</sub> | None |  |
| **[wikidataMatch](#wikidatamatch)** | <sub>0..\*</sub> | uri |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[altSymbol](#altsymbol)** | <sub>0..\*</sub> | None |  |
| **[applicableSystem](#applicablesystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[conversionMultiplier](#conversionmultiplier)** | <sub>0..1</sub> | None |  |
| **[conversionMultiplierSN](#conversionmultipliersn)** | <sub>0..1</sub> | None |  |
| **[conversionOffset](#conversionoffset)** | <sub>0..1</sub> | None |  |
| **[conversionOffsetSN](#conversionoffsetsn)** | <sub>0..1</sub> | None |  |
| **[definedUnitOfSystem](#definedunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[derivedCoherentUnitOfSystem](#derivedcoherentunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[derivedUnitOfSystem](#derivedunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[exactMatch](#exactmatch)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[factorUnitScalar](#factorunitscalar)** | <sub>0..1</sub> | None |  |
| **[hasDimensionVector](#hasdimensionvector)** | <sub>0..1</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[hasFactorUnit](#hasfactorunit)** | <sub>0..\*</sub> | [Class](#class) |  |
| **[hasQuantityKind](#hasquantitykind)** | <sub>0..\*</sub> | [QuantityKind](#quantitykind) |  |
| **[hasReciprocalUnit](#hasreciprocalunit)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[iec61360Code](#iec61360code)** | <sub>0..\*</sub> | string |  |
| **[isUnitOfSystem](#isunitofsystem)** | <sub>0..\*</sub> | [SystemOfUnits](#systemofunits) |  |
| **[latexDefinition](#latexdefinition)** | <sub>0..\*</sub> | None |  |
| **[latexSymbol](#latexsymbol)** | <sub>0..\*</sub> | None |  |
| **[mathMLdefinition](#mathmldefinition)** | <sub>0..1</sub> | None |  |
| **[omUnit](#omunit)** | <sub>0..\*</sub> | None |  |
| **[prefix](#prefix)** | <sub>0..\*</sub> | [Prefix](#prefix) |  |
| **[qkdvDenominator](#qkdvdenominator)** | <sub>0..1</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[qkdvNumerator](#qkdvnumerator)** | <sub>0..1</sub> | [QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| **[scalingOf](#scalingof)** | <sub>0..\*</sub> | [Unit](#unit) |  |
| **[siUnitsExpression](#siunitsexpression)** | <sub>0..\*</sub> | None |  |
| **[symbol](#symbol)** | <sub>0..\*</sub> | None |  |
| **[ucumCode](#ucumcode)** | <sub>0..\*</sub> | [UCUMcs](#ucumcs) |  |
| **[udunitsCode](#udunitscode)** | <sub>0..\*</sub> | string |  |
| **[uneceCommonCode](#unececommoncode)** | <sub>0..\*</sub> | string |  |
| **[unitFor](#unitfor)** | <sub>0..\*</sub> | None |  |

#### Parents

 * [Verifiable](#verifiable)

#### Children

 * [ContextualUnit](#contextualunit)
 * [DerivedUnit](#derivedunit)
 * [DimensionlessUnit](#dimensionlessunit)

#### Uses

 *  mixin: [Concept](#concept)

#### Referenced by:

 *  **[ContextualUnit](#contextualunit)** : broader  <sub>0..1</sub> 
 *  **[PhysicalConstant](#physicalconstant)** : applicableUnit  <sub>0..\*</sub> 
 *  **[Quantifiable](#quantifiable)** : hasUnit  <sub>0..\*</sub> 
 *  **[QuantityKind](#quantitykind)** : applicableCGSUnit  <sub>0..\*</sub> 
 *  **[QuantityKind](#quantitykind)** : applicableISOUnit  <sub>0..\*</sub> 
 *  **[QuantityKind](#quantitykind)** : applicableImperialUnit  <sub>0..\*</sub> 
 *  **[QuantityKind](#quantitykind)** : applicableSIUnit  <sub>0..\*</sub> 
 *  **[QuantityKind](#quantitykind)** : applicableUSCustomaryUnit  <sub>0..\*</sub> 
 *  **[QuantityKind](#quantitykind)** : applicableUnit  <sub>0..\*</sub> 
 *  **[QuantityValue](#quantityvalue)** : hasUnit  <sub>0..\*</sub> 
 *  **[SystemOfUnits](#systemofunits)** : hasAllowedUnit  <sub>0..\*</sub> 
 *  **[SystemOfUnits](#systemofunits)** : hasBaseUnit  <sub>0..\*</sub> 
 *  **[SystemOfUnits](#systemofunits)** : hasCoherentUnit  <sub>0..\*</sub> 
 *  **[SystemOfUnits](#systemofunits)** : hasDefinedUnit  <sub>0..\*</sub> 
 *  **[SystemOfUnits](#systemofunits)** : hasDerivedCoherentUnit  <sub>0..\*</sub> 
 *  **[SystemOfUnits](#systemofunits)** : hasDerivedUnit  <sub>0..\*</sub> 
 *  **[SystemOfUnits](#systemofunits)** : hasUnit  <sub>0..\*</sub> 
 *  **[Unit](#unit)** : exactMatch  <sub>0..\*</sub> 
 *  **[Unit](#unit)** : scalingOf  <sub>0..\*</sub> 
 *  **[Unit](#unit)** : hasReciprocalUnit  <sub>0..\*</sub> 




### UserQuantityKind




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
UserQuantityKind:
  is_a: AbstractQuantityKind
  slots:
  - guidance
  - Concept_id
  - Concept_hasRule
  - Concept_isReplacedBy
  - Concept_description
  - Concept_abbreviation
  - Concept_deprecated
  - Concept_plainTextDescription
  - AbstractQuantityKind_broader
  - AbstractQuantityKind_altSymbol
  - AbstractQuantityKind_latexSymbol
  - AbstractQuantityKind_symbol
  - UserQuantityKind_hasQuantityKind
  slot_usage:
    hasQuantityKind:
      range: QuantityKind
      required: true
      multivalued: false

```
</details>

![class_userquantitykind_erd](images/class_userquantitykind_erd.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | None |  |
| **[description](#description)** | <sub>0..1</sub> | None |  |
| **[abbreviation](#abbreviation)** | <sub>0..1</sub> | None |  |
| **[altSymbol](#altsymbol)** | <sub>0..\*</sub> | None |  |
| **[deprecated](#deprecated)** | <sub>0..1</sub> | None |  |
| **[guidance](#guidance)** | <sub>0..\*</sub> | string |  |
| **[hasRule](#hasrule)** | <sub>0..\*</sub> | [Rule](#rule) |  |
| **[isReplacedBy](#isreplacedby)** | <sub>0..1</sub> | None |  |
| **[latexSymbol](#latexsymbol)** | <sub>0..\*</sub> | None |  |
| **[plainTextDescription](#plaintextdescription)** | <sub>0..1</sub> | None |  |
| **[symbol](#symbol)** | <sub>0..1</sub> | None |  |
| **[hasQuantityKind](#hasquantitykind)** | <sub>1..1</sub> | [QuantityKind](#quantitykind) |  |

#### Parents

 * [AbstractQuantityKind](#abstractquantitykind)




### Verifiable



An aspect class that holds properties that provide external knowledge and specifications of a given resource.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
Verifiable:
  is_a: Aspect
  slots:
  - Verifiable_wikidataMatch
  - Verifiable_dbpediaMatch
  - Verifiable_isoNormativeReference
  - Verifiable_normativeReference
  slot_usage:
    wikidataMatch:
      required: false
    dbpediaMatch:
      required: false
    isoNormativeReference:
      required: false
    normativeReference:
      required: false

```
</details>


#### Local class diagram

![class_verifiable_local](images/class_verifiable_local.svg)

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[dbpediaMatch](#dbpediamatch)** | <sub>0..\*</sub> | uri |  |
| **[isoNormativeReference](#isonormativereference)** | <sub>0..\*</sub> | None |  |
| **[normativeReference](#normativereference)** | <sub>0..\*</sub> | None |  |
| **[wikidataMatch](#wikidatamatch)** | <sub>0..\*</sub> | uri |  |

#### Parents

 * [Aspect](#aspect)

#### Children

 * [Comment](#comment)
 * [EnumeratedValue](#enumeratedvalue)
 * [Prefix](#prefix)
 * [QuantityKind](#quantitykind)
 * [Rule](#rule)
 * [SystemOfUnits](#systemofunits)
 * [Unit](#unit)




### GDay




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
gDay: {}

```
</details>


This class has no attributes





### GMonth




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
gMonth: {}

```
</details>


This class has no attributes





### GMonthDay




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
gMonthDay: {}

```
</details>


This class has no attributes





### GYear




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
gYear: {}

```
</details>


This class has no attributes





### GYearMonth




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
gYearMonth: {}

```
</details>


This class has no attributes





### ValueUnion




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
valueUnion:
  is_a: Resource

```
</details>


#### Local class diagram

![class_valueunion_local](images/class_valueunion_local.svg)

This class has no attributes


#### Parents

 * [Resource](#resource)




## Slots

| Name | Cardinality/Range | Used By |
| --- | --- | --- |
| <a id="id"></a>**id** | <sub>0..\*</sub><br/>string | [AbstractQuantityKind](#abstractquantitykind), [AngleUnit](#angleunit), [BaseDimensionMagnitude](#basedimensionmagnitude), [BinaryPrefix](#binaryprefix), [BitEncodingType](#bitencodingtype), [BooleanEncodingType](#booleanencodingtype), [ByteEncodingType](#byteencodingtype), [CardinalityType](#cardinalitytype), [CharEncodingType](#charencodingtype), [Citation](#citation), [Concept](#concept), [ConstantValue](#constantvalue), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DataItem](#dataitem), [Datatype](#datatype), [DecimalPrefix](#decimalprefix), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [Discipline](#discipline), [Encoding](#encoding), [EndianType](#endiantype), [EnumeratedQuantity](#enumeratedquantity), [EnumeratedValue](#enumeratedvalue), [Enumeration](#enumeration), [EnumerationScale](#enumerationscale), [Figure](#figure), [FloatingPointEncodingType](#floatingpointencodingtype), [IntegerEncodingType](#integerencodingtype), [IntervalScale](#intervalscale), [LogarithmicUnit](#logarithmicunit), [MathsFunctionType](#mathsfunctiontype), [NominalScale](#nominalscale), [NumericUnion](#numericunion), [OrderedType](#orderedtype), [OrdinalScale](#ordinalscale), [Organization](#organization), [PhysicalConstant](#physicalconstant), [PlaneAngleUnit](#planeangleunit), [Prefix](#prefix), [Quantity](#quantity), [QuantityKind](#quantitykind), [QuantityKindDimensionVector](#quantitykinddimensionvector), [QuantityKindDimensionVectorCGS](#quantitykinddimensionvectorcgs), [QuantityKindDimensionVectorCGS-EMU](#quantitykinddimensionvectorcgs-emu), [QuantityKindDimensionVectorCGS-ESU](#quantitykinddimensionvectorcgs-esu), [QuantityKindDimensionVectorCGS-GAUSS](#quantitykinddimensionvectorcgs-gauss), [QuantityKindDimensionVectorCGS-LH](#quantitykinddimensionvectorcgs-lh), [QuantityKindDimensionVectorISO](#quantitykinddimensionvectoriso), [QuantityKindDimensionVectorImperial](#quantitykinddimensionvectorimperial), [QuantityKindDimensionVectorSI](#quantitykinddimensionvectorsi), [QuantityType](#quantitytype), [QuantityValue](#quantityvalue), [RatioScale](#ratioscale), [Rule](#rule), [RuleType](#ruletype), [ScalarDatatype](#scalardatatype), [Scale](#scale), [ScaleType](#scaletype), [SolidAngleUnit](#solidangleunit), [Symbol](#symbol), [SystemOfQuantityKinds](#systemofquantitykinds), [SystemOfUnits](#systemofunits), [TransformType](#transformtype), [Unit](#unit), [UserQuantityKind](#userquantitykind) |
| <a id="description"></a>**description** | <sub>0..\*</sub><br/>string | [AbstractQuantityKind](#abstractquantitykind), [BaseDimensionMagnitude](#basedimensionmagnitude), [BitEncodingType](#bitencodingtype), [BooleanEncodingType](#booleanencodingtype), [ByteEncodingType](#byteencodingtype), [CardinalityType](#cardinalitytype), [CharEncodingType](#charencodingtype), [Citation](#citation), [Comment](#comment), [Concept](#concept), [DataItem](#dataitem), [Datatype](#datatype), [Discipline](#discipline), [Encoding](#encoding), [EndianType](#endiantype), [EnumeratedQuantity](#enumeratedquantity), [EnumeratedValue](#enumeratedvalue), [Enumeration](#enumeration), [EnumerationScale](#enumerationscale), [Figure](#figure), [FloatingPointEncodingType](#floatingpointencodingtype), [IntegerEncodingType](#integerencodingtype), [IntervalScale](#intervalscale), [MathsFunctionType](#mathsfunctiontype), [NISTSP811Comment](#nistsp811comment), [NominalScale](#nominalscale), [OrderedType](#orderedtype), [OrdinalScale](#ordinalscale), [Organization](#organization), [QuantityKindDimensionVector](#quantitykinddimensionvector), [QuantityKindDimensionVectorCGS](#quantitykinddimensionvectorcgs), [QuantityKindDimensionVectorCGS-EMU](#quantitykinddimensionvectorcgs-emu), [QuantityKindDimensionVectorCGS-ESU](#quantitykinddimensionvectorcgs-esu), [QuantityKindDimensionVectorCGS-GAUSS](#quantitykinddimensionvectorcgs-gauss), [QuantityKindDimensionVectorCGS-LH](#quantitykinddimensionvectorcgs-lh), [QuantityKindDimensionVectorISO](#quantitykinddimensionvectoriso), [QuantityKindDimensionVectorImperial](#quantitykinddimensionvectorimperial), [QuantityKindDimensionVectorSI](#quantitykinddimensionvectorsi), [QuantityType](#quantitytype), [RatioScale](#ratioscale), [RuleType](#ruletype), [ScalarDatatype](#scalardatatype), [Scale](#scale), [ScaleType](#scaletype), [Symbol](#symbol), [SystemOfQuantityKinds](#systemofquantitykinds), [TransformType](#transformtype), [UserQuantityKind](#userquantitykind) |
| <a id="abstractquantitykind_altsymbol"></a>**AbstractQuantityKind_altSymbol** | <sub>0..\*</sub><br/>string |  |
| <a id="abstractquantitykind_broader"></a>**AbstractQuantityKind_broader** | <sub>0..1</sub><br/>[QuantityKind](#quantitykind) |  |
| <a id="abstractquantitykind_latexsymbol"></a>**AbstractQuantityKind_latexSymbol** | <sub>0..\*</sub><br/>string |  |
| <a id="abstractquantitykind_symbol"></a>**AbstractQuantityKind_symbol** | <sub>0..\*</sub><br/>string |  |
| <a id="basedimensionmagnitude_hasbasequantitykind"></a>**BaseDimensionMagnitude_hasBaseQuantityKind** | <sub>1..\*</sub><br/>[QuantityKind](#quantitykind) |  |
| <a id="basedimensionmagnitude_vectormagnitude"></a>**BaseDimensionMagnitude_vectorMagnitude** | <sub>1..\*</sub><br/>float |  |
| <a id="cardinalitytype_literal"></a>**CardinalityType_literal** | <sub>0..\*</sub><br/>string |  |
| <a id="citation_description"></a>**Citation_description** | <sub>1..\*</sub><br/>string |  |
| <a id="citation_url"></a>**Citation_url** | <sub>0..\*</sub><br/>string |  |
| <a id="comment_description"></a>**Comment_description** | <sub>0..\*</sub><br/>string |  |
| <a id="comment_rationale"></a>**Comment_rationale** | <sub>0..\*</sub><br/>string |  |
| <a id="concept_abbreviation"></a>**Concept_abbreviation** | <sub>0..\*</sub><br/>string |  |
| <a id="concept_deprecated"></a>**Concept_deprecated** | <sub>0..\*</sub><br/>string |  |
| <a id="concept_description"></a>**Concept_description** | <sub>0..\*</sub><br/>string |  |
| <a id="concept_hasrule"></a>**Concept_hasRule** | <sub>0..\*</sub><br/>[Rule](#rule) |  |
| <a id="concept_id"></a>**Concept_id** | <sub>0..\*</sub><br/>string |  |
| <a id="concept_isreplacedby"></a>**Concept_isReplacedBy** | <sub>0..\*</sub><br/>string |  |
| <a id="concept_plaintextdescription"></a>**Concept_plainTextDescription** | <sub>0..\*</sub><br/>string |  |
| <a id="constantvalue_exactconstant"></a>**ConstantValue_exactConstant** | <sub>0..\*</sub><br/>string |  |
| <a id="contextualunit_broader"></a>**ContextualUnit_broader** | <sub>0..1</sub><br/>[Unit](#unit) |  |
| <a id="currencyunit_currencycode"></a>**CurrencyUnit_currencyCode** | <sub>0..\*</sub><br/>string |  |
| <a id="currencyunit_currencyexponent"></a>**CurrencyUnit_currencyExponent** | <sub>0..\*</sub><br/>string |  |
| <a id="dataencoding_bitorder"></a>**DataEncoding_bitOrder** | <sub>0..\*</sub><br/>[EndianType](#endiantype) |  |
| <a id="dataencoding_byteorder"></a>**DataEncoding_byteOrder** | <sub>0..\*</sub><br/>[EndianType](#endiantype) |  |
| <a id="dataencoding_encoding"></a>**DataEncoding_encoding** | <sub>0..\*</sub><br/>[Encoding](#encoding) |  |
| <a id="dataitem_value"></a>**DataItem_value** | <sub>0..\*</sub><br/>string |  |
| <a id="datatype_ansisqlname"></a>**Datatype_ansiSQLName** | <sub>0..\*</sub><br/>string |  |
| <a id="datatype_basis"></a>**Datatype_basis** | <sub>0..\*</sub><br/>[Datatype](#datatype) |  |
| <a id="datatype_bounded"></a>**Datatype_bounded** | <sub>0..\*</sub><br/>string |  |
| <a id="datatype_cname"></a>**Datatype_cName** | <sub>0..\*</sub><br/>string |  |
| <a id="datatype_cardinality"></a>**Datatype_cardinality** | <sub>0..\*</sub><br/>[CardinalityType](#cardinalitytype) |  |
| <a id="datatype_id"></a>**Datatype_id** | <sub>0..\*</sub><br/>string |  |
| <a id="datatype_javaname"></a>**Datatype_javaName** | <sub>0..\*</sub><br/>string |  |
| <a id="datatype_jsname"></a>**Datatype_jsName** | <sub>0..\*</sub><br/>string |  |
| <a id="datatype_matlabname"></a>**Datatype_matlabName** | <sub>0..\*</sub><br/>string |  |
| <a id="datatype_microsoftsqlservername"></a>**Datatype_microsoftSQLServerName** | <sub>0..\*</sub><br/>string |  |
| <a id="datatype_mysqlname"></a>**Datatype_mySQLName** | <sub>0..\*</sub><br/>string |  |
| <a id="datatype_odbcname"></a>**Datatype_odbcName** | <sub>0..\*</sub><br/>string |  |
| <a id="datatype_oledbname"></a>**Datatype_oleDBName** | <sub>0..\*</sub><br/>string |  |
| <a id="datatype_oraclesqlname"></a>**Datatype_oracleSQLName** | <sub>0..\*</sub><br/>string |  |
| <a id="datatype_orderedtype"></a>**Datatype_orderedType** | <sub>0..\*</sub><br/>[OrderedType](#orderedtype) |  |
| <a id="datatype_protocolbuffersname"></a>**Datatype_protocolBuffersName** | <sub>0..\*</sub><br/>string |  |
| <a id="datatype_pythonname"></a>**Datatype_pythonName** | <sub>0..\*</sub><br/>string |  |
| <a id="datatype_vbname"></a>**Datatype_vbName** | <sub>0..\*</sub><br/>string |  |
| <a id="datetimestringencodingtype_allowedpattern"></a>**DateTimeStringEncodingType_allowedPattern** | <sub>1..\*</sub><br/>string |  |
| <a id="encoding_bits"></a>**Encoding_bits** | <sub>0..\*</sub><br/>string |  |
| <a id="encoding_bytes"></a>**Encoding_bytes** | <sub>0..\*</sub><br/>string |  |
| <a id="enumeratedquantity_enumeratedvalue"></a>**EnumeratedQuantity_enumeratedValue** | <sub>0..\*</sub><br/>[EnumeratedValue](#enumeratedvalue) |  |
| <a id="enumeratedquantity_enumeration"></a>**EnumeratedQuantity_enumeration** | <sub>0..\*</sub><br/>[Enumeration](#enumeration) |  |
| <a id="enumeratedvalue_abbreviation"></a>**EnumeratedValue_abbreviation** | <sub>0..\*</sub><br/>string |  |
| <a id="enumeratedvalue_altsymbol"></a>**EnumeratedValue_altSymbol** | <sub>0..\*</sub><br/>string |  |
| <a id="enumeratedvalue_description"></a>**EnumeratedValue_description** | <sub>0..\*</sub><br/>string |  |
| <a id="enumeratedvalue_symbol"></a>**EnumeratedValue_symbol** | <sub>0..\*</sub><br/>string |  |
| <a id="enumeration_abbreviation"></a>**Enumeration_abbreviation** | <sub>0..\*</sub><br/>string |  |
| <a id="enumeration_default"></a>**Enumeration_default** | <sub>0..\*</sub><br/>[EnumeratedValue](#enumeratedvalue) |  |
| <a id="enumeration_element"></a>**Enumeration_element** | <sub>1..\*</sub><br/>[EnumeratedValue](#enumeratedvalue) |  |
| <a id="figure_figurecaption"></a>**Figure_figureCaption** | <sub>0..\*</sub><br/>string |  |
| <a id="figure_figurelabel"></a>**Figure_figureLabel** | <sub>0..\*</sub><br/>string |  |
| <a id="figure_height"></a>**Figure_height** | <sub>0..\*</sub><br/>string |  |
| <a id="figure_image"></a>**Figure_image** | <sub>0..\*</sub><br/>string |  |
| <a id="figure_imagelocation"></a>**Figure_imageLocation** | <sub>1..\*</sub><br/>string |  |
| <a id="figure_landscape"></a>**Figure_landscape** | <sub>0..\*</sub><br/>string |  |
| <a id="figure_width"></a>**Figure_width** | <sub>0..\*</sub><br/>string |  |
| <a id="orderedtype_literal"></a>**OrderedType_literal** | <sub>0..\*</sub><br/>string |  |
| <a id="ordinalscale_order"></a>**OrdinalScale_order** | <sub>1..\*</sub><br/>string |  |
| <a id="organization_url"></a>**Organization_url** | <sub>0..\*</sub><br/>string |  |
| <a id="physicalconstant_altsymbol"></a>**PhysicalConstant_altSymbol** | <sub>0..\*</sub><br/>string |  |
| <a id="physicalconstant_applicablesystem"></a>**PhysicalConstant_applicableSystem** | <sub>0..\*</sub><br/>[SystemOfUnits](#systemofunits) |  |
| <a id="physicalconstant_applicableunit"></a>**PhysicalConstant_applicableUnit** | <sub>0..\*</sub><br/>[Unit](#unit) |  |
| <a id="physicalconstant_dbpediamatch"></a>**PhysicalConstant_dbpediaMatch** | <sub>0..\*</sub><br/>uri |  |
| <a id="physicalconstant_exactconstant"></a>**PhysicalConstant_exactConstant** | <sub>0..\*</sub><br/>boolean |  |
| <a id="physicalconstant_exactmatch"></a>**PhysicalConstant_exactMatch** | <sub>0..\*</sub><br/>[PhysicalConstant](#physicalconstant) |  |
| <a id="physicalconstant_hasdimensionvector"></a>**PhysicalConstant_hasDimensionVector** | <sub>0..\*</sub><br/>[QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| <a id="physicalconstant_isonormativereference"></a>**PhysicalConstant_isoNormativeReference** | <sub>0..\*</sub><br/>string |  |
| <a id="physicalconstant_latexdefinition"></a>**PhysicalConstant_latexDefinition** | <sub>0..\*</sub><br/>string |  |
| <a id="physicalconstant_latexsymbol"></a>**PhysicalConstant_latexSymbol** | <sub>0..\*</sub><br/>string |  |
| <a id="physicalconstant_mathmldefinition"></a>**PhysicalConstant_mathMLdefinition** | <sub>0..\*</sub><br/>string |  |
| <a id="physicalconstant_normativereference"></a>**PhysicalConstant_normativeReference** | <sub>0..\*</sub><br/>string |  |
| <a id="physicalconstant_symbol"></a>**PhysicalConstant_symbol** | <sub>0..\*</sub><br/>string |  |
| <a id="physicalconstant_ucumcode"></a>**PhysicalConstant_ucumCode** | <sub>0..\*</sub><br/>string |  |
| <a id="prefix_altsymbol"></a>**Prefix_altSymbol** | <sub>0..\*</sub><br/>string |  |
| <a id="prefix_exactmatch"></a>**Prefix_exactMatch** | <sub>0..\*</sub><br/>[Prefix](#prefix) |  |
| <a id="prefix_latexsymbol"></a>**Prefix_latexSymbol** | <sub>0..\*</sub><br/>string |  |
| <a id="prefix_prefixmultiplier"></a>**Prefix_prefixMultiplier** | <sub>0..\*</sub><br/>string |  |
| <a id="prefix_symbol"></a>**Prefix_symbol** | <sub>0..\*</sub><br/>string |  |
| <a id="prefix_ucumcode"></a>**Prefix_ucumCode** | <sub>0..\*</sub><br/>[UCUMcs-term](#ucumcs-term) |  |
| <a id="quantifiable_dataencoding"></a>**Quantifiable_dataEncoding** | <sub>0..\*</sub><br/>[DataEncoding](#dataencoding) |  |
| <a id="quantifiable_datatype"></a>**Quantifiable_datatype** | <sub>0..\*</sub><br/>[Datatype](#datatype) |  |
| <a id="quantifiable_hasunit"></a>**Quantifiable_hasUnit** | <sub>0..\*</sub><br/>[Unit](#unit) |  |
| <a id="quantifiable_relativestandarduncertainty"></a>**Quantifiable_relativeStandardUncertainty** | <sub>0..\*</sub><br/>double |  |
| <a id="quantifiable_standarduncertainty"></a>**Quantifiable_standardUncertainty** | <sub>0..\*</sub><br/>decimal |  |
| <a id="quantifiable_standarduncertaintysn"></a>**Quantifiable_standardUncertaintySN** | <sub>0..\*</sub><br/>double |  |
| <a id="quantifiable_value"></a>**Quantifiable_value** | <sub>0..\*</sub><br/>string |  |
| <a id="quantifiable_valuesn"></a>**Quantifiable_valueSN** | <sub>0..\*</sub><br/>string |  |
| <a id="quantitykinddimensionvector_dimensionexponentforamountofsubstance"></a>**QuantityKindDimensionVector_dimensionExponentForAmountOfSubstance** | <sub>1..\*</sub><br/>string |  |
| <a id="quantitykinddimensionvector_dimensionexponentforelectriccurrent"></a>**QuantityKindDimensionVector_dimensionExponentForElectricCurrent** | <sub>1..\*</sub><br/>string |  |
| <a id="quantitykinddimensionvector_dimensionexponentforlength"></a>**QuantityKindDimensionVector_dimensionExponentForLength** | <sub>1..\*</sub><br/>string |  |
| <a id="quantitykinddimensionvector_dimensionexponentforluminousintensity"></a>**QuantityKindDimensionVector_dimensionExponentForLuminousIntensity** | <sub>1..\*</sub><br/>string |  |
| <a id="quantitykinddimensionvector_dimensionexponentformass"></a>**QuantityKindDimensionVector_dimensionExponentForMass** | <sub>1..\*</sub><br/>string |  |
| <a id="quantitykinddimensionvector_dimensionexponentforthermodynamictemperature"></a>**QuantityKindDimensionVector_dimensionExponentForThermodynamicTemperature** | <sub>1..\*</sub><br/>string |  |
| <a id="quantitykinddimensionvector_dimensionexponentfortime"></a>**QuantityKindDimensionVector_dimensionExponentForTime** | <sub>1..\*</sub><br/>string |  |
| <a id="quantitykinddimensionvector_dimensionlessexponent"></a>**QuantityKindDimensionVector_dimensionlessExponent** | <sub>1..\*</sub><br/>string |  |
| <a id="quantitykinddimensionvector_hasreferencequantitykind"></a>**QuantityKindDimensionVector_hasReferenceQuantityKind** | <sub>0..\*</sub><br/>[QuantityKind](#quantitykind) |  |
| <a id="quantitykinddimensionvector_latexdefinition"></a>**QuantityKindDimensionVector_latexDefinition** | <sub>0..\*</sub><br/>string |  |
| <a id="quantitykinddimensionvector_latexsymbol"></a>**QuantityKindDimensionVector_latexSymbol** | <sub>0..\*</sub><br/>string |  |
| <a id="quantitykind_applicablecgsunit"></a>**QuantityKind_applicableCGSUnit** | <sub>0..\*</sub><br/>[Unit](#unit) |  |
| <a id="quantitykind_applicableisounit"></a>**QuantityKind_applicableISOUnit** | <sub>0..\*</sub><br/>[Unit](#unit) |  |
| <a id="quantitykind_applicableimperialunit"></a>**QuantityKind_applicableImperialUnit** | <sub>0..\*</sub><br/>[Unit](#unit) |  |
| <a id="quantitykind_applicablesiunit"></a>**QuantityKind_applicableSIUnit** | <sub>0..\*</sub><br/>[Unit](#unit) |  |
| <a id="quantitykind_applicableuscustomaryunit"></a>**QuantityKind_applicableUSCustomaryUnit** | <sub>0..\*</sub><br/>[Unit](#unit) |  |
| <a id="quantitykind_applicableunit"></a>**QuantityKind_applicableUnit** | <sub>0..\*</sub><br/>[Unit](#unit) |  |
| <a id="quantitykind_dimensionvectorforsi"></a>**QuantityKind_dimensionVectorForSI** | <sub>0..\*</sub><br/>[QuantityKindDimensionVectorSI](#quantitykinddimensionvectorsi) |  |
| <a id="quantitykind_exactmatch"></a>**QuantityKind_exactMatch** | <sub>0..\*</sub><br/>[QuantityKind](#quantitykind) |  |
| <a id="quantitykind_hasdimensionvector"></a>**QuantityKind_hasDimensionVector** | <sub>0..\*</sub><br/>[QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| <a id="quantitykind_iec61360code"></a>**QuantityKind_iec61360Code** | <sub>0..\*</sub><br/>string |  |
| <a id="quantitykind_latexdefinition"></a>**QuantityKind_latexDefinition** | <sub>0..\*</sub><br/>string |  |
| <a id="quantitykind_mathmldefinition"></a>**QuantityKind_mathMLdefinition** | <sub>0..\*</sub><br/>string |  |
| <a id="quantitykind_qkdvdenominator"></a>**QuantityKind_qkdvDenominator** | <sub>0..\*</sub><br/>[QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| <a id="quantitykind_qkdvnumerator"></a>**QuantityKind_qkdvNumerator** | <sub>0..\*</sub><br/>[QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| <a id="quantitytype_value"></a>**QuantityType_value** | <sub>0..\*</sub><br/>[QuantityKind](#quantitykind) |  |
| <a id="quantityvalue_hasunit"></a>**QuantityValue_hasUnit** | <sub>0..\*</sub><br/>[Unit](#unit) |  |
| <a id="quantity_hasquantitykind"></a>**Quantity_hasQuantityKind** | <sub>0..\*</sub><br/>[QuantityKind](#quantitykind) |  |
| <a id="quantity_isdeltaquantity"></a>**Quantity_isDeltaQuantity** | <sub>0..\*</sub><br/>boolean |  |
| <a id="quantity_quantityvalue"></a>**Quantity_quantityValue** | <sub>0..\*</sub><br/>[QuantityValue](#quantityvalue) |  |
| <a id="rule_rationale"></a>**Rule_rationale** | <sub>0..\*</sub><br/>string |  |
| <a id="rule_ruletype"></a>**Rule_ruleType** | <sub>0..\*</sub><br/>[RuleType](#ruletype) |  |
| <a id="scalardatatype_bits"></a>**ScalarDatatype_bits** | <sub>0..\*</sub><br/>string |  |
| <a id="scalardatatype_bytes"></a>**ScalarDatatype_bytes** | <sub>0..\*</sub><br/>string |  |
| <a id="scalardatatype_length"></a>**ScalarDatatype_length** | <sub>0..\*</sub><br/>string |  |
| <a id="scalardatatype_maxexclusive"></a>**ScalarDatatype_maxExclusive** | <sub>0..\*</sub><br/>string |  |
| <a id="scalardatatype_maxinclusive"></a>**ScalarDatatype_maxInclusive** | <sub>0..\*</sub><br/>string |  |
| <a id="scalardatatype_minexclusive"></a>**ScalarDatatype_minExclusive** | <sub>0..\*</sub><br/>string |  |
| <a id="scalardatatype_mininclusive"></a>**ScalarDatatype_minInclusive** | <sub>0..\*</sub><br/>string |  |
| <a id="scalardatatype_rdfsdatatype"></a>**ScalarDatatype_rdfsDatatype** | <sub>0..\*</sub><br/>[Datatype](#datatype) |  |
| <a id="scaletype_datastructure"></a>**ScaleType_dataStructure** | <sub>0..\*</sub><br/>string |  |
| <a id="scaletype_permissiblemaths"></a>**ScaleType_permissibleMaths** | <sub>0..\*</sub><br/>[MathsFunctionType](#mathsfunctiontype) |  |
| <a id="scaletype_permissibletransformation"></a>**ScaleType_permissibleTransformation** | <sub>0..\*</sub><br/>[TransformType](#transformtype) |  |
| <a id="scale_datastructure"></a>**Scale_dataStructure** | <sub>0..\*</sub><br/>string |  |
| <a id="scale_permissiblemaths"></a>**Scale_permissibleMaths** | <sub>0..\*</sub><br/>[MathsFunctionType](#mathsfunctiontype) |  |
| <a id="scale_permissibletransformation"></a>**Scale_permissibleTransformation** | <sub>0..\*</sub><br/>[TransformType](#transformtype) |  |
| <a id="scale_scaletype"></a>**Scale_scaleType** | <sub>0..\*</sub><br/>[ScaleType](#scaletype) |  |
| <a id="systemofquantitykinds_basedimensionenumeration"></a>**SystemOfQuantityKinds_baseDimensionEnumeration** | <sub>0..\*</sub><br/>[Enumeration](#enumeration) |  |
| <a id="systemofquantitykinds_hasbasequantitykind"></a>**SystemOfQuantityKinds_hasBaseQuantityKind** | <sub>0..\*</sub><br/>[QuantityKind](#quantitykind) |  |
| <a id="systemofquantitykinds_hasquantitykind"></a>**SystemOfQuantityKinds_hasQuantityKind** | <sub>0..\*</sub><br/>[QuantityKind](#quantitykind) |  |
| <a id="systemofquantitykinds_hasunitsystem"></a>**SystemOfQuantityKinds_hasUnitSystem** | <sub>0..\*</sub><br/>[SystemOfUnits](#systemofunits) |  |
| <a id="systemofquantitykinds_systemderivedquantitykind"></a>**SystemOfQuantityKinds_systemDerivedQuantityKind** | <sub>0..\*</sub><br/>[QuantityKind](#quantitykind) |  |
| <a id="systemofunits_applicablephysicalconstant"></a>**SystemOfUnits_applicablePhysicalConstant** | <sub>0..\*</sub><br/>[PhysicalConstant](#physicalconstant) |  |
| <a id="systemofunits_hasallowedunit"></a>**SystemOfUnits_hasAllowedUnit** | <sub>0..\*</sub><br/>[Unit](#unit) |  |
| <a id="systemofunits_hasbaseunit"></a>**SystemOfUnits_hasBaseUnit** | <sub>0..\*</sub><br/>[Unit](#unit) |  |
| <a id="systemofunits_hascoherentunit"></a>**SystemOfUnits_hasCoherentUnit** | <sub>0..\*</sub><br/>[Unit](#unit) |  |
| <a id="systemofunits_hasdefinedunit"></a>**SystemOfUnits_hasDefinedUnit** | <sub>0..\*</sub><br/>[Unit](#unit) |  |
| <a id="systemofunits_hasderivedcoherentunit"></a>**SystemOfUnits_hasDerivedCoherentUnit** | <sub>0..\*</sub><br/>[Unit](#unit) |  |
| <a id="systemofunits_hasderivedunit"></a>**SystemOfUnits_hasDerivedUnit** | <sub>0..\*</sub><br/>[Unit](#unit) |  |
| <a id="systemofunits_hasunit"></a>**SystemOfUnits_hasUnit** | <sub>0..\*</sub><br/>[Unit](#unit) |  |
| <a id="systemofunits_prefix"></a>**SystemOfUnits_prefix** | <sub>0..\*</sub><br/>[Prefix](#prefix) |  |
| <a id="unit_altsymbol"></a>**Unit_altSymbol** | <sub>0..\*</sub><br/>string |  |
| <a id="unit_applicablesystem"></a>**Unit_applicableSystem** | <sub>0..\*</sub><br/>[SystemOfUnits](#systemofunits) |  |
| <a id="unit_conversionmultiplier"></a>**Unit_conversionMultiplier** | <sub>0..\*</sub><br/>string |  |
| <a id="unit_conversionmultipliersn"></a>**Unit_conversionMultiplierSN** | <sub>0..\*</sub><br/>string |  |
| <a id="unit_conversionoffset"></a>**Unit_conversionOffset** | <sub>0..\*</sub><br/>string |  |
| <a id="unit_conversionoffsetsn"></a>**Unit_conversionOffsetSN** | <sub>0..\*</sub><br/>string |  |
| <a id="unit_definedunitofsystem"></a>**Unit_definedUnitOfSystem** | <sub>0..\*</sub><br/>[SystemOfUnits](#systemofunits) |  |
| <a id="unit_derivedcoherentunitofsystem"></a>**Unit_derivedCoherentUnitOfSystem** | <sub>0..\*</sub><br/>[SystemOfUnits](#systemofunits) |  |
| <a id="unit_derivedunitofsystem"></a>**Unit_derivedUnitOfSystem** | <sub>0..\*</sub><br/>[SystemOfUnits](#systemofunits) |  |
| <a id="unit_exactmatch"></a>**Unit_exactMatch** | <sub>0..\*</sub><br/>[Unit](#unit) |  |
| <a id="unit_factorunitscalar"></a>**Unit_factorUnitScalar** | <sub>0..\*</sub><br/>string |  |
| <a id="unit_hasdimensionvector"></a>**Unit_hasDimensionVector** | <sub>0..\*</sub><br/>[QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| <a id="unit_hasfactorunit"></a>**Unit_hasFactorUnit** | <sub>0..\*</sub><br/>[Class](#class) |  |
| <a id="unit_hasquantitykind"></a>**Unit_hasQuantityKind** | <sub>0..\*</sub><br/>[QuantityKind](#quantitykind) |  |
| <a id="unit_iec61360code"></a>**Unit_iec61360Code** | <sub>0..\*</sub><br/>string |  |
| <a id="unit_latexdefinition"></a>**Unit_latexDefinition** | <sub>0..\*</sub><br/>string |  |
| <a id="unit_latexsymbol"></a>**Unit_latexSymbol** | <sub>0..\*</sub><br/>string |  |
| <a id="unit_mathmldefinition"></a>**Unit_mathMLdefinition** | <sub>0..\*</sub><br/>string |  |
| <a id="unit_prefix"></a>**Unit_prefix** | <sub>0..\*</sub><br/>[Prefix](#prefix) |  |
| <a id="unit_qkdvdenominator"></a>**Unit_qkdvDenominator** | <sub>0..\*</sub><br/>[QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| <a id="unit_qkdvnumerator"></a>**Unit_qkdvNumerator** | <sub>0..\*</sub><br/>[QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| <a id="unit_scalingof"></a>**Unit_scalingOf** | <sub>0..\*</sub><br/>[Unit](#unit) |  |
| <a id="unit_siunitsexpression"></a>**Unit_siUnitsExpression** | <sub>0..\*</sub><br/>string |  |
| <a id="unit_symbol"></a>**Unit_symbol** | <sub>0..\*</sub><br/>string |  |
| <a id="unit_ucumcode"></a>**Unit_ucumCode** | <sub>0..\*</sub><br/>[UCUMcs](#ucumcs) |  |
| <a id="unit_udunitscode"></a>**Unit_udunitsCode** | <sub>0..\*</sub><br/>string |  |
| <a id="unit_unececommoncode"></a>**Unit_uneceCommonCode** | <sub>0..\*</sub><br/>string |  |
| <a id="userquantitykind_hasquantitykind"></a>**UserQuantityKind_hasQuantityKind** | <sub>1..\*</sub><br/>[QuantityKind](#quantitykind) |  |
| <a id="verifiable_dbpediamatch"></a>**Verifiable_dbpediaMatch** | <sub>0..\*</sub><br/>uri |  |
| <a id="verifiable_isonormativereference"></a>**Verifiable_isoNormativeReference** | <sub>0..\*</sub><br/>string |  |
| <a id="verifiable_normativereference"></a>**Verifiable_normativeReference** | <sub>0..\*</sub><br/>string |  |
| <a id="verifiable_wikidatamatch"></a>**Verifiable_wikidataMatch** | <sub>0..\*</sub><br/>uri |  |
| <a id="abbreviation"></a>**abbreviation** | <sub>0..\*</sub><br/>string | [AbstractQuantityKind](#abstractquantitykind), [BaseDimensionMagnitude](#basedimensionmagnitude), [BitEncodingType](#bitencodingtype), [BooleanEncodingType](#booleanencodingtype), [ByteEncodingType](#byteencodingtype), [CardinalityType](#cardinalitytype), [CharEncodingType](#charencodingtype), [Citation](#citation), [Concept](#concept), [DataItem](#dataitem), [Datatype](#datatype), [Discipline](#discipline), [Encoding](#encoding), [EndianType](#endiantype), [EnumeratedQuantity](#enumeratedquantity), [EnumeratedValue](#enumeratedvalue), [Enumeration](#enumeration), [EnumerationScale](#enumerationscale), [Figure](#figure), [FloatingPointEncodingType](#floatingpointencodingtype), [IntegerEncodingType](#integerencodingtype), [IntervalScale](#intervalscale), [MathsFunctionType](#mathsfunctiontype), [NominalScale](#nominalscale), [OrderedType](#orderedtype), [OrdinalScale](#ordinalscale), [Organization](#organization), [QuantityKindDimensionVector](#quantitykinddimensionvector), [QuantityKindDimensionVectorCGS](#quantitykinddimensionvectorcgs), [QuantityKindDimensionVectorCGS-EMU](#quantitykinddimensionvectorcgs-emu), [QuantityKindDimensionVectorCGS-ESU](#quantitykinddimensionvectorcgs-esu), [QuantityKindDimensionVectorCGS-GAUSS](#quantitykinddimensionvectorcgs-gauss), [QuantityKindDimensionVectorCGS-LH](#quantitykinddimensionvectorcgs-lh), [QuantityKindDimensionVectorISO](#quantitykinddimensionvectoriso), [QuantityKindDimensionVectorImperial](#quantitykinddimensionvectorimperial), [QuantityKindDimensionVectorSI](#quantitykinddimensionvectorsi), [QuantityType](#quantitytype), [RatioScale](#ratioscale), [RuleType](#ruletype), [ScalarDatatype](#scalardatatype), [Scale](#scale), [ScaleType](#scaletype), [Symbol](#symbol), [SystemOfQuantityKinds](#systemofquantitykinds), [TransformType](#transformtype), [UserQuantityKind](#userquantitykind) |
| <a id="abstract"></a>**abstract** | <sub>0..\*</sub><br/>string |  |
| <a id="acronym"></a>**acronym** | <sub>0..\*</sub><br/>string |  |
| <a id="allowedpattern"></a>**allowedPattern** | <sub>0..\*</sub><br/>string | [DateTimeStringEncodingType](#datetimestringencodingtype) |
| <a id="altsymbol"></a>**altSymbol** | <sub>0..\*</sub><br/>string | [AbstractQuantityKind](#abstractquantitykind), [AngleUnit](#angleunit), [BinaryPrefix](#binaryprefix), [CardinalityType](#cardinalitytype), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DecimalPrefix](#decimalprefix), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [EndianType](#endiantype), [EnumeratedValue](#enumeratedvalue), [LogarithmicUnit](#logarithmicunit), [OrderedType](#orderedtype), [PhysicalConstant](#physicalconstant), [PlaneAngleUnit](#planeangleunit), [Prefix](#prefix), [QuantityType](#quantitytype), [RuleType](#ruletype), [ScaleType](#scaletype), [SolidAngleUnit](#solidangleunit), [TransformType](#transformtype), [Unit](#unit), [UserQuantityKind](#userquantitykind) |
| <a id="ansisqlname"></a>**ansiSQLName** | <sub>0..\*</sub><br/>string | [Datatype](#datatype), [ScalarDatatype](#scalardatatype) |
| <a id="applicablecgsunit"></a>**applicableCGSUnit** | <sub>0..\*</sub><br/>[Unit](#unit) | [QuantityKind](#quantitykind) |
| <a id="applicableisounit"></a>**applicableISOUnit** | <sub>0..\*</sub><br/>[Unit](#unit) | [QuantityKind](#quantitykind) |
| <a id="applicableimperialunit"></a>**applicableImperialUnit** | <sub>0..\*</sub><br/>[Unit](#unit) | [QuantityKind](#quantitykind) |
| <a id="applicablephysicalconstant"></a>**applicablePhysicalConstant** | <sub>0..\*</sub><br/>string | [SystemOfUnits](#systemofunits) |
| <a id="applicableplanckunit"></a>**applicablePlanckUnit** | <sub>0..\*</sub><br/>[Unit](#unit) |  |
| <a id="applicablesiunit"></a>**applicableSIUnit** | <sub>0..\*</sub><br/>[Unit](#unit) | [QuantityKind](#quantitykind) |
| <a id="applicablesystem"></a>**applicableSystem** | <sub>0..\*</sub><br/>string | [AngleUnit](#angleunit), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [LogarithmicUnit](#logarithmicunit), [PhysicalConstant](#physicalconstant), [PlaneAngleUnit](#planeangleunit), [SolidAngleUnit](#solidangleunit), [Unit](#unit) |
| <a id="applicableuscustomaryunit"></a>**applicableUSCustomaryUnit** | <sub>0..\*</sub><br/>[Unit](#unit) | [QuantityKind](#quantitykind) |
| <a id="applicableunit"></a>**applicableUnit** | <sub>0..\*</sub><br/>[Unit](#unit) | [PhysicalConstant](#physicalconstant), [QuantityKind](#quantitykind) |
| <a id="basedimensionenumeration"></a>**baseDimensionEnumeration** | <sub>0..\*</sub><br/>[Enumeration](#enumeration) | [SystemOfQuantityKinds](#systemofquantitykinds) |
| <a id="baseunitofsystem"></a>**baseUnitOfSystem** | <sub>0..\*</sub><br/>[SystemOfUnits](#systemofunits) |  |
| <a id="basis"></a>**basis** | <sub>0..\*</sub><br/>string | [Datatype](#datatype), [ScalarDatatype](#scalardatatype) |
| <a id="belongstosystemofquantities"></a>**belongsToSystemOfQuantities** | <sub>0..\*</sub><br/>[SystemOfQuantityKinds](#systemofquantitykinds) | [QuantityKind](#quantitykind) |
| <a id="bitorder"></a>**bitOrder** | <sub>0..\*</sub><br/>[EndianType](#endiantype) | [DataEncoding](#dataencoding) |
| <a id="bits"></a>**bits** | <sub>0..\*</sub><br/>string | [BitEncodingType](#bitencodingtype), [BooleanEncodingType](#booleanencodingtype), [ByteEncodingType](#byteencodingtype), [CharEncodingType](#charencodingtype), [Encoding](#encoding), [FloatingPointEncodingType](#floatingpointencodingtype), [IntegerEncodingType](#integerencodingtype), [ScalarDatatype](#scalardatatype) |
| <a id="bounded"></a>**bounded** | <sub>0..\*</sub><br/>string | [Datatype](#datatype), [ScalarDatatype](#scalardatatype) |
| <a id="broader"></a>**broader** | <sub>0..1</sub><br/>[QuantityKind](#quantitykind) |  |
| <a id="byteorder"></a>**byteOrder** | <sub>0..\*</sub><br/>[EndianType](#endiantype) | [DataEncoding](#dataencoding) |
| <a id="bytes"></a>**bytes** | <sub>0..\*</sub><br/>string | [BitEncodingType](#bitencodingtype), [BooleanEncodingType](#booleanencodingtype), [ByteEncodingType](#byteencodingtype), [CharEncodingType](#charencodingtype), [Encoding](#encoding), [FloatingPointEncodingType](#floatingpointencodingtype), [IntegerEncodingType](#integerencodingtype), [ScalarDatatype](#scalardatatype) |
| <a id="cname"></a>**cName** | <sub>0..\*</sub><br/>string | [Datatype](#datatype), [ScalarDatatype](#scalardatatype) |
| <a id="cardinality"></a>**cardinality** | <sub>0..\*</sub><br/>string | [Datatype](#datatype), [ScalarDatatype](#scalardatatype) |
| <a id="categorizedas"></a>**categorizedAs** | <sub>0..\*</sub><br/>string |  |
| <a id="coherentunitsystem"></a>**coherentUnitSystem** | <sub>0..\*</sub><br/>string |  |
| <a id="conversionmultiplier"></a>**conversionMultiplier** | <sub>0..\*</sub><br/>string | [AngleUnit](#angleunit), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [LogarithmicUnit](#logarithmicunit), [PlaneAngleUnit](#planeangleunit), [SolidAngleUnit](#solidangleunit), [Unit](#unit) |
| <a id="conversionmultipliersn"></a>**conversionMultiplierSN** | <sub>0..\*</sub><br/>string | [AngleUnit](#angleunit), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [LogarithmicUnit](#logarithmicunit), [PlaneAngleUnit](#planeangleunit), [SolidAngleUnit](#solidangleunit), [Unit](#unit) |
| <a id="conversionoffset"></a>**conversionOffset** | <sub>0..\*</sub><br/>string | [AngleUnit](#angleunit), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [LogarithmicUnit](#logarithmicunit), [PlaneAngleUnit](#planeangleunit), [SolidAngleUnit](#solidangleunit), [Unit](#unit) |
| <a id="conversionoffsetsn"></a>**conversionOffsetSN** | <sub>0..\*</sub><br/>string | [AngleUnit](#angleunit), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [LogarithmicUnit](#logarithmicunit), [PlaneAngleUnit](#planeangleunit), [SolidAngleUnit](#solidangleunit), [Unit](#unit) |
| <a id="created"></a>**created** | <sub>0..\*</sub><br/>date |  |
| <a id="creator"></a>**creator** | <sub>0..\*</sub><br/>string |  |
| <a id="currencycode"></a>**currencyCode** | <sub>0..\*</sub><br/>string | [CurrencyUnit](#currencyunit) |
| <a id="currencyexponent"></a>**currencyExponent** | <sub>0..\*</sub><br/>string | [CurrencyUnit](#currencyunit) |
| <a id="currencynumber"></a>**currencyNumber** | <sub>0..\*</sub><br/>string |  |
| <a id="dataencoding"></a>**dataEncoding** | <sub>0..\*</sub><br/>[DataEncoding](#dataencoding) | [ConstantValue](#constantvalue), [PhysicalConstant](#physicalconstant), [Quantifiable](#quantifiable), [Quantity](#quantity), [QuantityValue](#quantityvalue) |
| <a id="datastructure"></a>**dataStructure** | <sub>0..\*</sub><br/>string | [EnumerationScale](#enumerationscale), [IntervalScale](#intervalscale), [NominalScale](#nominalscale), [OrdinalScale](#ordinalscale), [RatioScale](#ratioscale), [Scale](#scale), [ScaleType](#scaletype) |
| <a id="datatype"></a>**datatype** | <sub>0..\*</sub><br/>string | [ConstantValue](#constantvalue), [PhysicalConstant](#physicalconstant), [Quantifiable](#quantifiable), [Quantity](#quantity), [QuantityValue](#quantityvalue) |
| <a id="dbpediamatch"></a>**dbpediaMatch** | <sub>0..\*</sub><br/>uri | [AngleUnit](#angleunit), [BinaryPrefix](#binaryprefix), [CardinalityType](#cardinalitytype), [Comment](#comment), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DecimalPrefix](#decimalprefix), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [EndianType](#endiantype), [EnumeratedValue](#enumeratedvalue), [LogarithmicUnit](#logarithmicunit), [NISTSP811Comment](#nistsp811comment), [OrderedType](#orderedtype), [PhysicalConstant](#physicalconstant), [PlaneAngleUnit](#planeangleunit), [Prefix](#prefix), [QuantityKind](#quantitykind), [QuantityType](#quantitytype), [Rule](#rule), [RuleType](#ruletype), [ScaleType](#scaletype), [SolidAngleUnit](#solidangleunit), [SystemOfUnits](#systemofunits), [TransformType](#transformtype), [Unit](#unit), [Verifiable](#verifiable) |
| <a id="default"></a>**default** | <sub>0..\*</sub><br/>string | [Enumeration](#enumeration) |
| <a id="definedunitofsystem"></a>**definedUnitOfSystem** | <sub>0..\*</sub><br/>[SystemOfUnits](#systemofunits) | [AngleUnit](#angleunit), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [LogarithmicUnit](#logarithmicunit), [PlaneAngleUnit](#planeangleunit), [SolidAngleUnit](#solidangleunit), [Unit](#unit) |
| <a id="denominatordimensionvector"></a>**denominatorDimensionVector** | <sub>0..\*</sub><br/>[QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| <a id="deprecated"></a>**deprecated** | <sub>0..\*</sub><br/>string | [AbstractQuantityKind](#abstractquantitykind), [BaseDimensionMagnitude](#basedimensionmagnitude), [BitEncodingType](#bitencodingtype), [BooleanEncodingType](#booleanencodingtype), [ByteEncodingType](#byteencodingtype), [CharEncodingType](#charencodingtype), [Citation](#citation), [Concept](#concept), [DataItem](#dataitem), [Datatype](#datatype), [Discipline](#discipline), [Encoding](#encoding), [EnumeratedQuantity](#enumeratedquantity), [Enumeration](#enumeration), [EnumerationScale](#enumerationscale), [Figure](#figure), [FloatingPointEncodingType](#floatingpointencodingtype), [IntegerEncodingType](#integerencodingtype), [IntervalScale](#intervalscale), [MathsFunctionType](#mathsfunctiontype), [NominalScale](#nominalscale), [OrdinalScale](#ordinalscale), [Organization](#organization), [QuantityKindDimensionVector](#quantitykinddimensionvector), [QuantityKindDimensionVectorCGS](#quantitykinddimensionvectorcgs), [QuantityKindDimensionVectorCGS-EMU](#quantitykinddimensionvectorcgs-emu), [QuantityKindDimensionVectorCGS-ESU](#quantitykinddimensionvectorcgs-esu), [QuantityKindDimensionVectorCGS-GAUSS](#quantitykinddimensionvectorcgs-gauss), [QuantityKindDimensionVectorCGS-LH](#quantitykinddimensionvectorcgs-lh), [QuantityKindDimensionVectorISO](#quantitykinddimensionvectoriso), [QuantityKindDimensionVectorImperial](#quantitykinddimensionvectorimperial), [QuantityKindDimensionVectorSI](#quantitykinddimensionvectorsi), [RatioScale](#ratioscale), [ScalarDatatype](#scalardatatype), [Scale](#scale), [Symbol](#symbol), [SystemOfQuantityKinds](#systemofquantitykinds), [UserQuantityKind](#userquantitykind) |
| <a id="derivedcoherentunitofsystem"></a>**derivedCoherentUnitOfSystem** | <sub>0..\*</sub><br/>[SystemOfUnits](#systemofunits) | [AngleUnit](#angleunit), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [LogarithmicUnit](#logarithmicunit), [PlaneAngleUnit](#planeangleunit), [SolidAngleUnit](#solidangleunit), [Unit](#unit) |
| <a id="derivednoncoherentunitofsystem"></a>**derivedNonCoherentUnitOfSystem** | <sub>0..\*</sub><br/>[SystemOfUnits](#systemofunits) |  |
| <a id="derivedunitofsystem"></a>**derivedUnitOfSystem** | <sub>0..\*</sub><br/>[SystemOfUnits](#systemofunits) | [AngleUnit](#angleunit), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [LogarithmicUnit](#logarithmicunit), [PlaneAngleUnit](#planeangleunit), [SolidAngleUnit](#solidangleunit), [Unit](#unit) |
| <a id="dimensionexponent"></a>**dimensionExponent** | <sub>0..\*</sub><br/>string |  |
| <a id="dimensionexponentforamountofsubstance"></a>**dimensionExponentForAmountOfSubstance** | <sub>0..\*</sub><br/>string | [QuantityKindDimensionVector](#quantitykinddimensionvector), [QuantityKindDimensionVectorCGS](#quantitykinddimensionvectorcgs), [QuantityKindDimensionVectorCGS-EMU](#quantitykinddimensionvectorcgs-emu), [QuantityKindDimensionVectorCGS-ESU](#quantitykinddimensionvectorcgs-esu), [QuantityKindDimensionVectorCGS-GAUSS](#quantitykinddimensionvectorcgs-gauss), [QuantityKindDimensionVectorCGS-LH](#quantitykinddimensionvectorcgs-lh), [QuantityKindDimensionVectorISO](#quantitykinddimensionvectoriso), [QuantityKindDimensionVectorImperial](#quantitykinddimensionvectorimperial), [QuantityKindDimensionVectorSI](#quantitykinddimensionvectorsi) |
| <a id="dimensionexponentforelectriccurrent"></a>**dimensionExponentForElectricCurrent** | <sub>0..\*</sub><br/>string | [QuantityKindDimensionVector](#quantitykinddimensionvector), [QuantityKindDimensionVectorCGS](#quantitykinddimensionvectorcgs), [QuantityKindDimensionVectorCGS-EMU](#quantitykinddimensionvectorcgs-emu), [QuantityKindDimensionVectorCGS-ESU](#quantitykinddimensionvectorcgs-esu), [QuantityKindDimensionVectorCGS-GAUSS](#quantitykinddimensionvectorcgs-gauss), [QuantityKindDimensionVectorCGS-LH](#quantitykinddimensionvectorcgs-lh), [QuantityKindDimensionVectorISO](#quantitykinddimensionvectoriso), [QuantityKindDimensionVectorImperial](#quantitykinddimensionvectorimperial), [QuantityKindDimensionVectorSI](#quantitykinddimensionvectorsi) |
| <a id="dimensionexponentforlength"></a>**dimensionExponentForLength** | <sub>0..\*</sub><br/>string | [QuantityKindDimensionVector](#quantitykinddimensionvector), [QuantityKindDimensionVectorCGS](#quantitykinddimensionvectorcgs), [QuantityKindDimensionVectorCGS-EMU](#quantitykinddimensionvectorcgs-emu), [QuantityKindDimensionVectorCGS-ESU](#quantitykinddimensionvectorcgs-esu), [QuantityKindDimensionVectorCGS-GAUSS](#quantitykinddimensionvectorcgs-gauss), [QuantityKindDimensionVectorCGS-LH](#quantitykinddimensionvectorcgs-lh), [QuantityKindDimensionVectorISO](#quantitykinddimensionvectoriso), [QuantityKindDimensionVectorImperial](#quantitykinddimensionvectorimperial), [QuantityKindDimensionVectorSI](#quantitykinddimensionvectorsi) |
| <a id="dimensionexponentforluminousintensity"></a>**dimensionExponentForLuminousIntensity** | <sub>0..\*</sub><br/>string | [QuantityKindDimensionVector](#quantitykinddimensionvector), [QuantityKindDimensionVectorCGS](#quantitykinddimensionvectorcgs), [QuantityKindDimensionVectorCGS-EMU](#quantitykinddimensionvectorcgs-emu), [QuantityKindDimensionVectorCGS-ESU](#quantitykinddimensionvectorcgs-esu), [QuantityKindDimensionVectorCGS-GAUSS](#quantitykinddimensionvectorcgs-gauss), [QuantityKindDimensionVectorCGS-LH](#quantitykinddimensionvectorcgs-lh), [QuantityKindDimensionVectorISO](#quantitykinddimensionvectoriso), [QuantityKindDimensionVectorImperial](#quantitykinddimensionvectorimperial), [QuantityKindDimensionVectorSI](#quantitykinddimensionvectorsi) |
| <a id="dimensionexponentformass"></a>**dimensionExponentForMass** | <sub>0..\*</sub><br/>string | [QuantityKindDimensionVector](#quantitykinddimensionvector), [QuantityKindDimensionVectorCGS](#quantitykinddimensionvectorcgs), [QuantityKindDimensionVectorCGS-EMU](#quantitykinddimensionvectorcgs-emu), [QuantityKindDimensionVectorCGS-ESU](#quantitykinddimensionvectorcgs-esu), [QuantityKindDimensionVectorCGS-GAUSS](#quantitykinddimensionvectorcgs-gauss), [QuantityKindDimensionVectorCGS-LH](#quantitykinddimensionvectorcgs-lh), [QuantityKindDimensionVectorISO](#quantitykinddimensionvectoriso), [QuantityKindDimensionVectorImperial](#quantitykinddimensionvectorimperial), [QuantityKindDimensionVectorSI](#quantitykinddimensionvectorsi) |
| <a id="dimensionexponentforthermodynamictemperature"></a>**dimensionExponentForThermodynamicTemperature** | <sub>0..\*</sub><br/>string | [QuantityKindDimensionVector](#quantitykinddimensionvector), [QuantityKindDimensionVectorCGS](#quantitykinddimensionvectorcgs), [QuantityKindDimensionVectorCGS-EMU](#quantitykinddimensionvectorcgs-emu), [QuantityKindDimensionVectorCGS-ESU](#quantitykinddimensionvectorcgs-esu), [QuantityKindDimensionVectorCGS-GAUSS](#quantitykinddimensionvectorcgs-gauss), [QuantityKindDimensionVectorCGS-LH](#quantitykinddimensionvectorcgs-lh), [QuantityKindDimensionVectorISO](#quantitykinddimensionvectoriso), [QuantityKindDimensionVectorImperial](#quantitykinddimensionvectorimperial), [QuantityKindDimensionVectorSI](#quantitykinddimensionvectorsi) |
| <a id="dimensionexponentfortime"></a>**dimensionExponentForTime** | <sub>0..\*</sub><br/>string | [QuantityKindDimensionVector](#quantitykinddimensionvector), [QuantityKindDimensionVectorCGS](#quantitykinddimensionvectorcgs), [QuantityKindDimensionVectorCGS-EMU](#quantitykinddimensionvectorcgs-emu), [QuantityKindDimensionVectorCGS-ESU](#quantitykinddimensionvectorcgs-esu), [QuantityKindDimensionVectorCGS-GAUSS](#quantitykinddimensionvectorcgs-gauss), [QuantityKindDimensionVectorCGS-LH](#quantitykinddimensionvectorcgs-lh), [QuantityKindDimensionVectorISO](#quantitykinddimensionvectoriso), [QuantityKindDimensionVectorImperial](#quantitykinddimensionvectorimperial), [QuantityKindDimensionVectorSI](#quantitykinddimensionvectorsi) |
| <a id="dimensioninverse"></a>**dimensionInverse** | <sub>0..\*</sub><br/>string |  |
| <a id="dimensionvectorforsi"></a>**dimensionVectorForSI** | <sub>0..\*</sub><br/>[QuantityKindDimensionVectorSI](#quantitykinddimensionvectorsi) | [QuantityKind](#quantitykind) |
| <a id="dimensionlessexponent"></a>**dimensionlessExponent** | <sub>0..\*</sub><br/>string | [QuantityKindDimensionVector](#quantitykinddimensionvector), [QuantityKindDimensionVectorCGS](#quantitykinddimensionvectorcgs), [QuantityKindDimensionVectorCGS-EMU](#quantitykinddimensionvectorcgs-emu), [QuantityKindDimensionVectorCGS-ESU](#quantitykinddimensionvectorcgs-esu), [QuantityKindDimensionVectorCGS-GAUSS](#quantitykinddimensionvectorcgs-gauss), [QuantityKindDimensionVectorCGS-LH](#quantitykinddimensionvectorcgs-lh), [QuantityKindDimensionVectorISO](#quantitykinddimensionvectoriso), [QuantityKindDimensionVectorImperial](#quantitykinddimensionvectorimperial), [QuantityKindDimensionVectorSI](#quantitykinddimensionvectorsi) |
| <a id="element"></a>**element** | <sub>0..\*</sub><br/>string | [Enumeration](#enumeration) |
| <a id="elementkind"></a>**elementKind** | <sub>0..\*</sub><br/>string |  |
| <a id="encoding"></a>**encoding** | <sub>0..\*</sub><br/>string | [DataEncoding](#dataencoding) |
| <a id="enumeratedvalue"></a>**enumeratedValue** | <sub>0..\*</sub><br/>[EnumeratedValue](#enumeratedvalue) | [EnumeratedQuantity](#enumeratedquantity) |
| <a id="enumeration"></a>**enumeration** | <sub>0..\*</sub><br/>[Enumeration](#enumeration) | [EnumeratedQuantity](#enumeratedquantity) |
| <a id="exactconstant"></a>**exactConstant** | <sub>0..\*</sub><br/>string | [ConstantValue](#constantvalue), [PhysicalConstant](#physicalconstant) |
| <a id="exactmatch"></a>**exactMatch** | <sub>0..\*</sub><br/>string | [AngleUnit](#angleunit), [BinaryPrefix](#binaryprefix), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DecimalPrefix](#decimalprefix), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [LogarithmicUnit](#logarithmicunit), [PhysicalConstant](#physicalconstant), [PlaneAngleUnit](#planeangleunit), [Prefix](#prefix), [QuantityKind](#quantitykind), [SolidAngleUnit](#solidangleunit), [Unit](#unit) |
| <a id="example"></a>**example** | <sub>0..\*</sub><br/>string |  |
| <a id="exponent"></a>**exponent** | <sub>0..\*</sub><br/>string |  |
| <a id="expression"></a>**expression** | <sub>0..\*</sub><br/>string |  |
| <a id="factorunitscalar"></a>**factorUnitScalar** | <sub>0..\*</sub><br/>string | [AngleUnit](#angleunit), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [LogarithmicUnit](#logarithmicunit), [PlaneAngleUnit](#planeangleunit), [SolidAngleUnit](#solidangleunit), [Unit](#unit) |
| <a id="fieldcode"></a>**fieldCode** | <sub>0..\*</sub><br/>string |  |
| <a id="figure"></a>**figure** | <sub>0..\*</sub><br/>[Figure](#figure) |  |
| <a id="figurecaption"></a>**figureCaption** | <sub>0..\*</sub><br/>string | [Figure](#figure) |
| <a id="figurelabel"></a>**figureLabel** | <sub>0..\*</sub><br/>string | [Figure](#figure) |
| <a id="graphname"></a>**graphName** | <sub>0..\*</sub><br/>string |  |
| <a id="graphtitle"></a>**graphTitle** | <sub>0..\*</sub><br/>string |  |
| <a id="guidance"></a>**guidance** | <sub>0..\*</sub><br/>string | [AbstractQuantityKind](#abstractquantitykind), [AngleUnit](#angleunit), [BaseDimensionMagnitude](#basedimensionmagnitude), [BinaryPrefix](#binaryprefix), [BitEncodingType](#bitencodingtype), [BooleanEncodingType](#booleanencodingtype), [ByteEncodingType](#byteencodingtype), [CardinalityType](#cardinalitytype), [CharEncodingType](#charencodingtype), [Citation](#citation), [Concept](#concept), [ConstantValue](#constantvalue), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DataItem](#dataitem), [Datatype](#datatype), [DecimalPrefix](#decimalprefix), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [Discipline](#discipline), [Encoding](#encoding), [EndianType](#endiantype), [EnumeratedQuantity](#enumeratedquantity), [EnumeratedValue](#enumeratedvalue), [Enumeration](#enumeration), [EnumerationScale](#enumerationscale), [Figure](#figure), [FloatingPointEncodingType](#floatingpointencodingtype), [IntegerEncodingType](#integerencodingtype), [IntervalScale](#intervalscale), [LogarithmicUnit](#logarithmicunit), [MathsFunctionType](#mathsfunctiontype), [NominalScale](#nominalscale), [NumericUnion](#numericunion), [OrderedType](#orderedtype), [OrdinalScale](#ordinalscale), [Organization](#organization), [PhysicalConstant](#physicalconstant), [PlaneAngleUnit](#planeangleunit), [Prefix](#prefix), [Quantity](#quantity), [QuantityKind](#quantitykind), [QuantityKindDimensionVector](#quantitykinddimensionvector), [QuantityKindDimensionVectorCGS](#quantitykinddimensionvectorcgs), [QuantityKindDimensionVectorCGS-EMU](#quantitykinddimensionvectorcgs-emu), [QuantityKindDimensionVectorCGS-ESU](#quantitykinddimensionvectorcgs-esu), [QuantityKindDimensionVectorCGS-GAUSS](#quantitykinddimensionvectorcgs-gauss), [QuantityKindDimensionVectorCGS-LH](#quantitykinddimensionvectorcgs-lh), [QuantityKindDimensionVectorISO](#quantitykinddimensionvectoriso), [QuantityKindDimensionVectorImperial](#quantitykinddimensionvectorimperial), [QuantityKindDimensionVectorSI](#quantitykinddimensionvectorsi), [QuantityType](#quantitytype), [QuantityValue](#quantityvalue), [RatioScale](#ratioscale), [Rule](#rule), [RuleType](#ruletype), [ScalarDatatype](#scalardatatype), [Scale](#scale), [ScaleType](#scaletype), [SolidAngleUnit](#solidangleunit), [Symbol](#symbol), [SystemOfQuantityKinds](#systemofquantitykinds), [SystemOfUnits](#systemofunits), [TransformType](#transformtype), [Unit](#unit), [UserQuantityKind](#userquantitykind) |
| <a id="hasallowedunit"></a>**hasAllowedUnit** | <sub>0..\*</sub><br/>[Unit](#unit) | [SystemOfUnits](#systemofunits) |
| <a id="hasbasequantitykind"></a>**hasBaseQuantityKind** | <sub>0..\*</sub><br/>[QuantityKind](#quantitykind) | [BaseDimensionMagnitude](#basedimensionmagnitude), [SystemOfQuantityKinds](#systemofquantitykinds) |
| <a id="hasbaseunit"></a>**hasBaseUnit** | <sub>0..\*</sub><br/>[Unit](#unit) | [SystemOfUnits](#systemofunits) |
| <a id="hascitation"></a>**hasCitation** | <sub>0..\*</sub><br/>string |  |
| <a id="hascoherentunit"></a>**hasCoherentUnit** | <sub>0..\*</sub><br/>[Unit](#unit) | [SystemOfUnits](#systemofunits) |
| <a id="hasdefinedunit"></a>**hasDefinedUnit** | <sub>0..\*</sub><br/>[Unit](#unit) | [SystemOfUnits](#systemofunits) |
| <a id="hasdenominatorpart"></a>**hasDenominatorPart** | <sub>0..\*</sub><br/>string |  |
| <a id="hasderivedcoherentunit"></a>**hasDerivedCoherentUnit** | <sub>0..\*</sub><br/>[Unit](#unit) | [SystemOfUnits](#systemofunits) |
| <a id="hasderivednoncoherentunit"></a>**hasDerivedNonCoherentUnit** | <sub>0..\*</sub><br/>string |  |
| <a id="hasderivedunit"></a>**hasDerivedUnit** | <sub>0..\*</sub><br/>string | [SystemOfUnits](#systemofunits) |
| <a id="hasdimension"></a>**hasDimension** | <sub>0..\*</sub><br/>string |  |
| <a id="hasdimensionexpression"></a>**hasDimensionExpression** | <sub>0..\*</sub><br/>string |  |
| <a id="hasdimensionvector"></a>**hasDimensionVector** | <sub>0..\*</sub><br/>[QuantityKindDimensionVector](#quantitykinddimensionvector) | [AngleUnit](#angleunit), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [LogarithmicUnit](#logarithmicunit), [PhysicalConstant](#physicalconstant), [PlaneAngleUnit](#planeangleunit), [QuantityKind](#quantitykind), [SolidAngleUnit](#solidangleunit), [Unit](#unit) |
| <a id="hasfactorunit"></a>**hasFactorUnit** | <sub>0..\*</sub><br/>string | [AngleUnit](#angleunit), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [LogarithmicUnit](#logarithmicunit), [PlaneAngleUnit](#planeangleunit), [SolidAngleUnit](#solidangleunit), [Unit](#unit) |
| <a id="hasnumeratorpart"></a>**hasNumeratorPart** | <sub>0..\*</sub><br/>string |  |
| <a id="hasprefixunit"></a>**hasPrefixUnit** | <sub>0..\*</sub><br/>[Unit](#unit) |  |
| <a id="hasquantity"></a>**hasQuantity** | <sub>0..\*</sub><br/>[Quantity](#quantity) |  |
| <a id="hasquantitykind"></a>**hasQuantityKind** | <sub>0..\*</sub><br/>[QuantityKind](#quantitykind) | [AngleUnit](#angleunit), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [LogarithmicUnit](#logarithmicunit), [PhysicalConstant](#physicalconstant), [PlaneAngleUnit](#planeangleunit), [Quantity](#quantity), [SolidAngleUnit](#solidangleunit), [SystemOfQuantityKinds](#systemofquantitykinds), [Unit](#unit), [UserQuantityKind](#userquantitykind) |
| <a id="hasreciprocalunit"></a>**hasReciprocalUnit** | <sub>0..\*</sub><br/>[Unit](#unit) | [AngleUnit](#angleunit), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [LogarithmicUnit](#logarithmicunit), [PlaneAngleUnit](#planeangleunit), [SolidAngleUnit](#solidangleunit), [Unit](#unit) |
| <a id="hasreferencequantitykind"></a>**hasReferenceQuantityKind** | <sub>0..\*</sub><br/>string | [QuantityKindDimensionVector](#quantitykinddimensionvector), [QuantityKindDimensionVectorCGS](#quantitykinddimensionvectorcgs), [QuantityKindDimensionVectorCGS-EMU](#quantitykinddimensionvectorcgs-emu), [QuantityKindDimensionVectorCGS-ESU](#quantitykinddimensionvectorcgs-esu), [QuantityKindDimensionVectorCGS-GAUSS](#quantitykinddimensionvectorcgs-gauss), [QuantityKindDimensionVectorCGS-LH](#quantitykinddimensionvectorcgs-lh), [QuantityKindDimensionVectorISO](#quantitykinddimensionvectoriso), [QuantityKindDimensionVectorImperial](#quantitykinddimensionvectorimperial), [QuantityKindDimensionVectorSI](#quantitykinddimensionvectorsi) |
| <a id="hasrule"></a>**hasRule** | <sub>0..\*</sub><br/>string | [AbstractQuantityKind](#abstractquantitykind), [BaseDimensionMagnitude](#basedimensionmagnitude), [BitEncodingType](#bitencodingtype), [BooleanEncodingType](#booleanencodingtype), [ByteEncodingType](#byteencodingtype), [CharEncodingType](#charencodingtype), [Citation](#citation), [Concept](#concept), [DataItem](#dataitem), [Datatype](#datatype), [Discipline](#discipline), [Encoding](#encoding), [EnumeratedQuantity](#enumeratedquantity), [Enumeration](#enumeration), [EnumerationScale](#enumerationscale), [Figure](#figure), [FloatingPointEncodingType](#floatingpointencodingtype), [IntegerEncodingType](#integerencodingtype), [IntervalScale](#intervalscale), [MathsFunctionType](#mathsfunctiontype), [NominalScale](#nominalscale), [OrdinalScale](#ordinalscale), [Organization](#organization), [QuantityKindDimensionVector](#quantitykinddimensionvector), [QuantityKindDimensionVectorCGS](#quantitykinddimensionvectorcgs), [QuantityKindDimensionVectorCGS-EMU](#quantitykinddimensionvectorcgs-emu), [QuantityKindDimensionVectorCGS-ESU](#quantitykinddimensionvectorcgs-esu), [QuantityKindDimensionVectorCGS-GAUSS](#quantitykinddimensionvectorcgs-gauss), [QuantityKindDimensionVectorCGS-LH](#quantitykinddimensionvectorcgs-lh), [QuantityKindDimensionVectorISO](#quantitykinddimensionvectoriso), [QuantityKindDimensionVectorImperial](#quantitykinddimensionvectorimperial), [QuantityKindDimensionVectorSI](#quantitykinddimensionvectorsi), [RatioScale](#ratioscale), [ScalarDatatype](#scalardatatype), [Scale](#scale), [Symbol](#symbol), [SystemOfQuantityKinds](#systemofquantitykinds), [UserQuantityKind](#userquantitykind) |
| <a id="hasunit"></a>**hasUnit** | <sub>0..\*</sub><br/>[Unit](#unit) | [ConstantValue](#constantvalue), [PhysicalConstant](#physicalconstant), [Quantifiable](#quantifiable), [Quantity](#quantity), [QuantityValue](#quantityvalue), [SystemOfUnits](#systemofunits) |
| <a id="hasunitsystem"></a>**hasUnitSystem** | <sub>0..\*</sub><br/>string | [SystemOfQuantityKinds](#systemofquantitykinds) |
| <a id="hasvocabulary"></a>**hasVocabulary** | <sub>0..\*</sub><br/>[Ontology](#ontology) |  |
| <a id="height"></a>**height** | <sub>0..\*</sub><br/>string | [Figure](#figure) |
| <a id="iec61360code"></a>**iec61360Code** | <sub>0..\*</sub><br/>string | [AngleUnit](#angleunit), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [LogarithmicUnit](#logarithmicunit), [PlaneAngleUnit](#planeangleunit), [QuantityKind](#quantitykind), [SolidAngleUnit](#solidangleunit), [Unit](#unit) |
| <a id="image"></a>**image** | <sub>0..\*</sub><br/>string | [Figure](#figure) |
| <a id="imagelocation"></a>**imageLocation** | <sub>0..\*</sub><br/>string | [Figure](#figure) |
| <a id="informativereference"></a>**informativeReference** | <sub>0..\*</sub><br/>uri |  |
| <a id="isdeltaquantity"></a>**isDeltaQuantity** | <sub>0..\*</sub><br/>string | [PhysicalConstant](#physicalconstant), [Quantity](#quantity) |
| <a id="isdimensioninsystem"></a>**isDimensionInSystem** | <sub>0..\*</sub><br/>string |  |
| <a id="ismetadatafor"></a>**isMetadataFor** | <sub>0..\*</sub><br/>string |  |
| <a id="ismetricunit"></a>**isMetricUnit** | <sub>0..\*</sub><br/>string |  |
| <a id="isreplacedby"></a>**isReplacedBy** | <sub>0..\*</sub><br/>string | [AbstractQuantityKind](#abstractquantitykind), [BaseDimensionMagnitude](#basedimensionmagnitude), [BitEncodingType](#bitencodingtype), [BooleanEncodingType](#booleanencodingtype), [ByteEncodingType](#byteencodingtype), [CharEncodingType](#charencodingtype), [Citation](#citation), [Concept](#concept), [DataItem](#dataitem), [Datatype](#datatype), [Discipline](#discipline), [Encoding](#encoding), [EnumeratedQuantity](#enumeratedquantity), [Enumeration](#enumeration), [EnumerationScale](#enumerationscale), [Figure](#figure), [FloatingPointEncodingType](#floatingpointencodingtype), [IntegerEncodingType](#integerencodingtype), [IntervalScale](#intervalscale), [MathsFunctionType](#mathsfunctiontype), [NominalScale](#nominalscale), [OrdinalScale](#ordinalscale), [Organization](#organization), [QuantityKindDimensionVector](#quantitykinddimensionvector), [QuantityKindDimensionVectorCGS](#quantitykinddimensionvectorcgs), [QuantityKindDimensionVectorCGS-EMU](#quantitykinddimensionvectorcgs-emu), [QuantityKindDimensionVectorCGS-ESU](#quantitykinddimensionvectorcgs-esu), [QuantityKindDimensionVectorCGS-GAUSS](#quantitykinddimensionvectorcgs-gauss), [QuantityKindDimensionVectorCGS-LH](#quantitykinddimensionvectorcgs-lh), [QuantityKindDimensionVectorISO](#quantitykinddimensionvectoriso), [QuantityKindDimensionVectorImperial](#quantitykinddimensionvectorimperial), [QuantityKindDimensionVectorSI](#quantitykinddimensionvectorsi), [RatioScale](#ratioscale), [ScalarDatatype](#scalardatatype), [Scale](#scale), [Symbol](#symbol), [SystemOfQuantityKinds](#systemofquantitykinds), [UserQuantityKind](#userquantitykind) |
| <a id="isunitofsystem"></a>**isUnitOfSystem** | <sub>0..\*</sub><br/>[SystemOfUnits](#systemofunits) | [AngleUnit](#angleunit), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [LogarithmicUnit](#logarithmicunit), [PlaneAngleUnit](#planeangleunit), [SolidAngleUnit](#solidangleunit), [Unit](#unit) |
| <a id="isonormativereference"></a>**isoNormativeReference** | <sub>0..\*</sub><br/>string | [AngleUnit](#angleunit), [BinaryPrefix](#binaryprefix), [CardinalityType](#cardinalitytype), [Comment](#comment), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DecimalPrefix](#decimalprefix), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [EndianType](#endiantype), [EnumeratedValue](#enumeratedvalue), [LogarithmicUnit](#logarithmicunit), [NISTSP811Comment](#nistsp811comment), [OrderedType](#orderedtype), [PhysicalConstant](#physicalconstant), [PlaneAngleUnit](#planeangleunit), [Prefix](#prefix), [QuantityKind](#quantitykind), [QuantityType](#quantitytype), [Rule](#rule), [RuleType](#ruletype), [ScaleType](#scaletype), [SolidAngleUnit](#solidangleunit), [SystemOfUnits](#systemofunits), [TransformType](#transformtype), [Unit](#unit), [Verifiable](#verifiable) |
| <a id="javaname"></a>**javaName** | <sub>0..\*</sub><br/>string | [Datatype](#datatype), [ScalarDatatype](#scalardatatype) |
| <a id="jsname"></a>**jsName** | <sub>0..\*</sub><br/>string | [Datatype](#datatype), [ScalarDatatype](#scalardatatype) |
| <a id="landscape"></a>**landscape** | <sub>0..\*</sub><br/>string | [Figure](#figure) |
| <a id="latexdefinition"></a>**latexDefinition** | <sub>0..\*</sub><br/>string | [AngleUnit](#angleunit), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [LogarithmicUnit](#logarithmicunit), [PhysicalConstant](#physicalconstant), [PlaneAngleUnit](#planeangleunit), [QuantityKind](#quantitykind), [QuantityKindDimensionVector](#quantitykinddimensionvector), [QuantityKindDimensionVectorCGS](#quantitykinddimensionvectorcgs), [QuantityKindDimensionVectorCGS-EMU](#quantitykinddimensionvectorcgs-emu), [QuantityKindDimensionVectorCGS-ESU](#quantitykinddimensionvectorcgs-esu), [QuantityKindDimensionVectorCGS-GAUSS](#quantitykinddimensionvectorcgs-gauss), [QuantityKindDimensionVectorCGS-LH](#quantitykinddimensionvectorcgs-lh), [QuantityKindDimensionVectorISO](#quantitykinddimensionvectoriso), [QuantityKindDimensionVectorImperial](#quantitykinddimensionvectorimperial), [QuantityKindDimensionVectorSI](#quantitykinddimensionvectorsi), [SolidAngleUnit](#solidangleunit), [Unit](#unit) |
| <a id="latexsymbol"></a>**latexSymbol** | <sub>0..\*</sub><br/>string | [AbstractQuantityKind](#abstractquantitykind), [AngleUnit](#angleunit), [BinaryPrefix](#binaryprefix), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DecimalPrefix](#decimalprefix), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [LogarithmicUnit](#logarithmicunit), [PhysicalConstant](#physicalconstant), [PlaneAngleUnit](#planeangleunit), [Prefix](#prefix), [QuantityKindDimensionVector](#quantitykinddimensionvector), [QuantityKindDimensionVectorCGS](#quantitykinddimensionvectorcgs), [QuantityKindDimensionVectorCGS-EMU](#quantitykinddimensionvectorcgs-emu), [QuantityKindDimensionVectorCGS-ESU](#quantitykinddimensionvectorcgs-esu), [QuantityKindDimensionVectorCGS-GAUSS](#quantitykinddimensionvectorcgs-gauss), [QuantityKindDimensionVectorCGS-LH](#quantitykinddimensionvectorcgs-lh), [QuantityKindDimensionVectorISO](#quantitykinddimensionvectoriso), [QuantityKindDimensionVectorImperial](#quantitykinddimensionvectorimperial), [QuantityKindDimensionVectorSI](#quantitykinddimensionvectorsi), [SolidAngleUnit](#solidangleunit), [Unit](#unit), [UserQuantityKind](#userquantitykind) |
| <a id="length"></a>**length** | <sub>0..\*</sub><br/>string | [ScalarDatatype](#scalardatatype) |
| <a id="literal"></a>**literal** | <sub>0..\*</sub><br/>string | [CardinalityType](#cardinalitytype), [OrderedType](#orderedtype) |
| <a id="lowerbound"></a>**lowerBound** | <sub>0..\*</sub><br/>string |  |
| <a id="mathdefinition"></a>**mathDefinition** | <sub>0..\*</sub><br/>string |  |
| <a id="mathmldefinition"></a>**mathMLdefinition** | <sub>0..\*</sub><br/>string | [AngleUnit](#angleunit), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [LogarithmicUnit](#logarithmicunit), [PhysicalConstant](#physicalconstant), [PlaneAngleUnit](#planeangleunit), [QuantityKind](#quantitykind), [SolidAngleUnit](#solidangleunit), [Unit](#unit) |
| <a id="matlabname"></a>**matlabName** | <sub>0..\*</sub><br/>string | [Datatype](#datatype), [ScalarDatatype](#scalardatatype) |
| <a id="maxcardinality"></a>**maxCardinality** | <sub>0..\*</sub><br/>string |  |
| <a id="maxexclusive"></a>**maxExclusive** | <sub>0..\*</sub><br/>string | [ScalarDatatype](#scalardatatype) |
| <a id="maxinclusive"></a>**maxInclusive** | <sub>0..\*</sub><br/>string | [ScalarDatatype](#scalardatatype) |
| <a id="microsoftsqlservername"></a>**microsoftSQLServerName** | <sub>0..\*</sub><br/>string | [Datatype](#datatype), [ScalarDatatype](#scalardatatype) |
| <a id="mincardinality"></a>**minCardinality** | <sub>0..\*</sub><br/>string |  |
| <a id="minexclusive"></a>**minExclusive** | <sub>0..\*</sub><br/>string | [ScalarDatatype](#scalardatatype) |
| <a id="mininclusive"></a>**minInclusive** | <sub>0..\*</sub><br/>string | [ScalarDatatype](#scalardatatype) |
| <a id="modified"></a>**modified** | <sub>0..\*</sub><br/>date |  |
| <a id="mysqlname"></a>**mySQLName** | <sub>0..\*</sub><br/>string | [Datatype](#datatype), [ScalarDatatype](#scalardatatype) |
| <a id="negativedeltalimit"></a>**negativeDeltaLimit** | <sub>0..\*</sub><br/>string |  |
| <a id="normativereference"></a>**normativeReference** | <sub>0..\*</sub><br/>string | [AngleUnit](#angleunit), [BinaryPrefix](#binaryprefix), [CardinalityType](#cardinalitytype), [Comment](#comment), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DecimalPrefix](#decimalprefix), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [EndianType](#endiantype), [EnumeratedValue](#enumeratedvalue), [LogarithmicUnit](#logarithmicunit), [NISTSP811Comment](#nistsp811comment), [OrderedType](#orderedtype), [PhysicalConstant](#physicalconstant), [PlaneAngleUnit](#planeangleunit), [Prefix](#prefix), [QuantityKind](#quantitykind), [QuantityType](#quantitytype), [Rule](#rule), [RuleType](#ruletype), [ScaleType](#scaletype), [SolidAngleUnit](#solidangleunit), [SystemOfUnits](#systemofunits), [TransformType](#transformtype), [Unit](#unit), [Verifiable](#verifiable) |
| <a id="numeratordimensionvector"></a>**numeratorDimensionVector** | <sub>0..\*</sub><br/>[QuantityKindDimensionVector](#quantitykinddimensionvector) |  |
| <a id="numericvalue"></a>**numericValue** | <sub>0..\*</sub><br/>[NumericUnion](#numericunion) |  |
| <a id="odbcname"></a>**odbcName** | <sub>0..\*</sub><br/>string | [Datatype](#datatype), [ScalarDatatype](#scalardatatype) |
| <a id="oledbname"></a>**oleDBName** | <sub>0..\*</sub><br/>string | [Datatype](#datatype), [ScalarDatatype](#scalardatatype) |
| <a id="omunit"></a>**omUnit** | <sub>0..\*</sub><br/>string | [AngleUnit](#angleunit), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [LogarithmicUnit](#logarithmicunit), [PlaneAngleUnit](#planeangleunit), [SolidAngleUnit](#solidangleunit), [Unit](#unit) |
| <a id="onlinereference"></a>**onlineReference** | <sub>0..\*</sub><br/>string |  |
| <a id="oraclesqlname"></a>**oracleSQLName** | <sub>0..\*</sub><br/>string | [Datatype](#datatype), [ScalarDatatype](#scalardatatype) |
| <a id="order"></a>**order** | <sub>0..\*</sub><br/>string | [OrdinalScale](#ordinalscale) |
| <a id="orderedtype"></a>**orderedType** | <sub>0..\*</sub><br/>string | [Datatype](#datatype), [ScalarDatatype](#scalardatatype) |
| <a id="outofscope"></a>**outOfScope** | <sub>0..\*</sub><br/>string |  |
| <a id="pattern"></a>**pattern** | <sub>0..\*</sub><br/>string |  |
| <a id="permissiblemaths"></a>**permissibleMaths** | <sub>0..\*</sub><br/>string | [EnumerationScale](#enumerationscale), [IntervalScale](#intervalscale), [NominalScale](#nominalscale), [OrdinalScale](#ordinalscale), [RatioScale](#ratioscale), [Scale](#scale), [ScaleType](#scaletype) |
| <a id="permissibletransformation"></a>**permissibleTransformation** | <sub>0..\*</sub><br/>string | [EnumerationScale](#enumerationscale), [IntervalScale](#intervalscale), [NominalScale](#nominalscale), [OrdinalScale](#ordinalscale), [RatioScale](#ratioscale), [Scale](#scale), [ScaleType](#scaletype) |
| <a id="plaintextdescription"></a>**plainTextDescription** | <sub>0..\*</sub><br/>string | [AbstractQuantityKind](#abstractquantitykind), [BaseDimensionMagnitude](#basedimensionmagnitude), [BitEncodingType](#bitencodingtype), [BooleanEncodingType](#booleanencodingtype), [ByteEncodingType](#byteencodingtype), [CharEncodingType](#charencodingtype), [Citation](#citation), [Concept](#concept), [DataItem](#dataitem), [Datatype](#datatype), [Discipline](#discipline), [Encoding](#encoding), [EnumeratedQuantity](#enumeratedquantity), [Enumeration](#enumeration), [EnumerationScale](#enumerationscale), [Figure](#figure), [FloatingPointEncodingType](#floatingpointencodingtype), [IntegerEncodingType](#integerencodingtype), [IntervalScale](#intervalscale), [MathsFunctionType](#mathsfunctiontype), [NominalScale](#nominalscale), [OrdinalScale](#ordinalscale), [Organization](#organization), [QuantityKindDimensionVector](#quantitykinddimensionvector), [QuantityKindDimensionVectorCGS](#quantitykinddimensionvectorcgs), [QuantityKindDimensionVectorCGS-EMU](#quantitykinddimensionvectorcgs-emu), [QuantityKindDimensionVectorCGS-ESU](#quantitykinddimensionvectorcgs-esu), [QuantityKindDimensionVectorCGS-GAUSS](#quantitykinddimensionvectorcgs-gauss), [QuantityKindDimensionVectorCGS-LH](#quantitykinddimensionvectorcgs-lh), [QuantityKindDimensionVectorISO](#quantitykinddimensionvectoriso), [QuantityKindDimensionVectorImperial](#quantitykinddimensionvectorimperial), [QuantityKindDimensionVectorSI](#quantitykinddimensionvectorsi), [RatioScale](#ratioscale), [ScalarDatatype](#scalardatatype), [Scale](#scale), [Symbol](#symbol), [SystemOfQuantityKinds](#systemofquantitykinds), [UserQuantityKind](#userquantitykind) |
| <a id="positivedeltalimit"></a>**positiveDeltaLimit** | <sub>0..\*</sub><br/>string |  |
| <a id="prefix"></a>**prefix** | <sub>0..\*</sub><br/>[Prefix](#prefix) | [AngleUnit](#angleunit), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [LogarithmicUnit](#logarithmicunit), [PlaneAngleUnit](#planeangleunit), [SolidAngleUnit](#solidangleunit), [SystemOfUnits](#systemofunits), [Unit](#unit) |
| <a id="prefixmultiplier"></a>**prefixMultiplier** | <sub>0..\*</sub><br/>string | [BinaryPrefix](#binaryprefix), [DecimalPrefix](#decimalprefix), [Prefix](#prefix) |
| <a id="prefixmultipliersn"></a>**prefixMultiplierSN** | <sub>0..\*</sub><br/>string |  |
| <a id="protocolbuffersname"></a>**protocolBuffersName** | <sub>0..\*</sub><br/>string | [Datatype](#datatype), [ScalarDatatype](#scalardatatype) |
| <a id="pythonname"></a>**pythonName** | <sub>0..\*</sub><br/>string | [Datatype](#datatype), [ScalarDatatype](#scalardatatype) |
| <a id="qkdvdenominator"></a>**qkdvDenominator** | <sub>0..\*</sub><br/>[QuantityKindDimensionVector](#quantitykinddimensionvector) | [AngleUnit](#angleunit), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [LogarithmicUnit](#logarithmicunit), [PlaneAngleUnit](#planeangleunit), [QuantityKind](#quantitykind), [SolidAngleUnit](#solidangleunit), [Unit](#unit) |
| <a id="qkdvnumerator"></a>**qkdvNumerator** | <sub>0..\*</sub><br/>[QuantityKindDimensionVector](#quantitykinddimensionvector) | [AngleUnit](#angleunit), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [LogarithmicUnit](#logarithmicunit), [PlaneAngleUnit](#planeangleunit), [QuantityKind](#quantitykind), [SolidAngleUnit](#solidangleunit), [Unit](#unit) |
| <a id="quantity"></a>**quantity** | <sub>0..\*</sub><br/>string |  |
| <a id="quantityvalue"></a>**quantityValue** | <sub>0..\*</sub><br/>[QuantityValue](#quantityvalue) | [PhysicalConstant](#physicalconstant), [Quantity](#quantity) |
| <a id="rationale"></a>**rationale** | <sub>0..\*</sub><br/>string | [Comment](#comment), [NISTSP811Comment](#nistsp811comment), [Rule](#rule) |
| <a id="rdfsdatatype"></a>**rdfsDatatype** | <sub>0..\*</sub><br/>string | [ScalarDatatype](#scalardatatype) |
| <a id="reference"></a>**reference** | <sub>0..\*</sub><br/>string |  |
| <a id="referenceunit"></a>**referenceUnit** | <sub>0..\*</sub><br/>string |  |
| <a id="relativestandarduncertainty"></a>**relativeStandardUncertainty** | <sub>0..\*</sub><br/>string | [ConstantValue](#constantvalue), [PhysicalConstant](#physicalconstant), [Quantifiable](#quantifiable), [Quantity](#quantity), [QuantityValue](#quantityvalue) |
| <a id="relevantquantitykind"></a>**relevantQuantityKind** | <sub>0..\*</sub><br/>[QuantityKind](#quantitykind) |  |
| <a id="relevantunit"></a>**relevantUnit** | <sub>0..\*</sub><br/>[Unit](#unit) |  |
| <a id="rights"></a>**rights** | <sub>0..\*</sub><br/>string |  |
| <a id="ruletype"></a>**ruleType** | <sub>0..\*</sub><br/>string | [Rule](#rule) |
| <a id="scaletype"></a>**scaleType** | <sub>0..\*</sub><br/>string | [EnumerationScale](#enumerationscale), [IntervalScale](#intervalscale), [NominalScale](#nominalscale), [OrdinalScale](#ordinalscale), [RatioScale](#ratioscale), [Scale](#scale) |
| <a id="scalingof"></a>**scalingOf** | <sub>0..\*</sub><br/>string | [AngleUnit](#angleunit), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [LogarithmicUnit](#logarithmicunit), [PlaneAngleUnit](#planeangleunit), [SolidAngleUnit](#solidangleunit), [Unit](#unit) |
| <a id="siexactmatch"></a>**siExactMatch** | <sub>0..\*</sub><br/>string |  |
| <a id="siunitsexpression"></a>**siUnitsExpression** | <sub>0..\*</sub><br/>string | [AngleUnit](#angleunit), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [LogarithmicUnit](#logarithmicunit), [PlaneAngleUnit](#planeangleunit), [SolidAngleUnit](#solidangleunit), [Unit](#unit) |
| <a id="source"></a>**source** | <sub>0..\*</sub><br/>uri |  |
| <a id="standarduncertainty"></a>**standardUncertainty** | <sub>0..\*</sub><br/>string | [ConstantValue](#constantvalue), [PhysicalConstant](#physicalconstant), [Quantifiable](#quantifiable), [Quantity](#quantity), [QuantityValue](#quantityvalue) |
| <a id="standarduncertaintysn"></a>**standardUncertaintySN** | <sub>0..\*</sub><br/>string | [ConstantValue](#constantvalue), [PhysicalConstant](#physicalconstant), [Quantifiable](#quantifiable), [Quantity](#quantity), [QuantityValue](#quantityvalue) |
| <a id="subject"></a>**subject** | <sub>0..\*</sub><br/>string |  |
| <a id="supersededby"></a>**supersededBy** | <sub>0..\*</sub><br/>string |  |
| <a id="symbol"></a>**symbol** | <sub>0..\*</sub><br/>string | [AbstractQuantityKind](#abstractquantitykind), [AngleUnit](#angleunit), [BinaryPrefix](#binaryprefix), [CardinalityType](#cardinalitytype), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DecimalPrefix](#decimalprefix), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [EndianType](#endiantype), [EnumeratedValue](#enumeratedvalue), [LogarithmicUnit](#logarithmicunit), [OrderedType](#orderedtype), [PhysicalConstant](#physicalconstant), [PlaneAngleUnit](#planeangleunit), [Prefix](#prefix), [QuantityType](#quantitytype), [RuleType](#ruletype), [ScaleType](#scaletype), [SolidAngleUnit](#solidangleunit), [TransformType](#transformtype), [Unit](#unit), [UserQuantityKind](#userquantitykind) |
| <a id="systemdefinition"></a>**systemDefinition** | <sub>0..\*</sub><br/>string |  |
| <a id="systemderivedquantitykind"></a>**systemDerivedQuantityKind** | <sub>0..\*</sub><br/>[QuantityKind](#quantitykind) | [SystemOfQuantityKinds](#systemofquantitykinds) |
| <a id="systemdimension"></a>**systemDimension** | <sub>0..\*</sub><br/>string |  |
| <a id="title"></a>**title** | <sub>0..\*</sub><br/>string |  |
| <a id="ucumcode"></a>**ucumCode** | <sub>0..\*</sub><br/>string | [AngleUnit](#angleunit), [BinaryPrefix](#binaryprefix), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DecimalPrefix](#decimalprefix), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [LogarithmicUnit](#logarithmicunit), [PhysicalConstant](#physicalconstant), [PlaneAngleUnit](#planeangleunit), [Prefix](#prefix), [SolidAngleUnit](#solidangleunit), [Unit](#unit) |
| <a id="udunitscode"></a>**udunitsCode** | <sub>0..\*</sub><br/>string | [AngleUnit](#angleunit), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [LogarithmicUnit](#logarithmicunit), [PlaneAngleUnit](#planeangleunit), [SolidAngleUnit](#solidangleunit), [Unit](#unit) |
| <a id="unececommoncode"></a>**uneceCommonCode** | <sub>0..\*</sub><br/>string | [AngleUnit](#angleunit), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [LogarithmicUnit](#logarithmicunit), [PlaneAngleUnit](#planeangleunit), [SolidAngleUnit](#solidangleunit), [Unit](#unit) |
| <a id="unitfor"></a>**unitFor** | <sub>0..\*</sub><br/>string | [AngleUnit](#angleunit), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [LogarithmicUnit](#logarithmicunit), [PlaneAngleUnit](#planeangleunit), [SolidAngleUnit](#solidangleunit), [Unit](#unit) |
| <a id="upperbound"></a>**upperBound** | <sub>0..\*</sub><br/>string |  |
| <a id="url"></a>**url** | <sub>0..\*</sub><br/>string | [Citation](#citation), [Organization](#organization) |
| <a id="value"></a>**value** | <sub>0..\*</sub><br/>string | [ConstantValue](#constantvalue), [DataItem](#dataitem), [PhysicalConstant](#physicalconstant), [Quantifiable](#quantifiable), [Quantity](#quantity), [QuantityType](#quantitytype), [QuantityValue](#quantityvalue) |
| <a id="valuequantity"></a>**valueQuantity** | <sub>0..\*</sub><br/>string |  |
| <a id="valuesn"></a>**valueSN** | <sub>0..\*</sub><br/>string | [ConstantValue](#constantvalue), [PhysicalConstant](#physicalconstant), [Quantifiable](#quantifiable), [Quantity](#quantity), [QuantityValue](#quantityvalue) |
| <a id="vbname"></a>**vbName** | <sub>0..\*</sub><br/>string | [Datatype](#datatype), [ScalarDatatype](#scalardatatype) |
| <a id="vectormagnitude"></a>**vectorMagnitude** | <sub>0..\*</sub><br/>string | [BaseDimensionMagnitude](#basedimensionmagnitude) |
| <a id="wasderivedfrom"></a>**wasDerivedFrom** | <sub>0..\*</sub><br/>[Concept](#concept) |  |
| <a id="website"></a>**website** | <sub>0..\*</sub><br/>string |  |
| <a id="width"></a>**width** | <sub>0..\*</sub><br/>string | [Figure](#figure) |
| <a id="wikidatamatch"></a>**wikidataMatch** | <sub>0..\*</sub><br/>uri | [AngleUnit](#angleunit), [BinaryPrefix](#binaryprefix), [CardinalityType](#cardinalitytype), [Comment](#comment), [ContextualUnit](#contextualunit), [CountingUnit](#countingunit), [CurrencyUnit](#currencyunit), [DecimalPrefix](#decimalprefix), [DerivedUnit](#derivedunit), [DimensionlessUnit](#dimensionlessunit), [EndianType](#endiantype), [EnumeratedValue](#enumeratedvalue), [LogarithmicUnit](#logarithmicunit), [NISTSP811Comment](#nistsp811comment), [OrderedType](#orderedtype), [PlaneAngleUnit](#planeangleunit), [Prefix](#prefix), [QuantityKind](#quantitykind), [QuantityType](#quantitytype), [Rule](#rule), [RuleType](#ruletype), [ScaleType](#scaletype), [SolidAngleUnit](#solidangleunit), [SystemOfUnits](#systemofunits), [TransformType](#transformtype), [Unit](#unit), [Verifiable](#verifiable) |

