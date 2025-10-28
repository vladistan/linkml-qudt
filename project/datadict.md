
# QUDT


**metamodel version:** 1.7.0

**version:** None


qudt


## Class Diagram

```mermaid
classDiagram
AbstractQuantityKind <|-- UserQuantityKind
AngleUnit <|-- PlaneAngleUnit
AngleUnit <|-- SolidAngleUnit
Aspect <|-- DataEncoding
Aspect <|-- Quantifiable
Class <|-- AspectClass
Comment <|-- NIST_SP811_Comment
Concept <|-- AbstractQuantityKind
Concept <|-- BaseDimensionMagnitude
Concept <|-- Citation
Concept <|-- DataItem
Concept <|-- Datatype
Concept <|-- Discipline
Concept <|-- Encoding
Concept <|-- EnumeratedQuantity
Concept <|-- Enumeration
Concept <|-- Figure
Concept <|-- MathsFunctionType
Concept <|-- Organization
Concept <|-- QuantityKindDimensionVector
Concept <|-- Scale
Concept <|-- Symbol
Concept <|-- SystemOfQuantityKinds
Datatype <|-- ScalarDatatype
DimensionlessUnit <|-- AngleUnit
DimensionlessUnit <|-- CountingUnit
DimensionlessUnit <|-- CurrencyUnit
DimensionlessUnit <|-- LogarithmicUnit
Encoding <|-- BitEncodingType
Encoding <|-- BooleanEncodingType
Encoding <|-- ByteEncodingType
Encoding <|-- CharEncodingType
Encoding <|-- FloatingPointEncodingType
Encoding <|-- IntegerEncodingType
EnumeratedValue <|-- CardinalityType
EnumeratedValue <|-- EndianType
EnumeratedValue <|-- OrderedType
EnumeratedValue <|-- QuantityType
EnumeratedValue <|-- RuleType
EnumeratedValue <|-- ScaleType
EnumeratedValue <|-- TransformType
Error3 <|-- Verifiable
Prefix <|-- BinaryPrefix
Prefix <|-- DecimalPrefix
Quantifiable <|-- Quantity
Quantifiable <|-- QuantityValue
Quantity <|-- PhysicalConstant
QuantityKindDimensionVector <|-- QuantityKindDimensionVector_CGS
QuantityKindDimensionVector <|-- QuantityKindDimensionVector_ISO
QuantityKindDimensionVector <|-- QuantityKindDimensionVector_Imperial
QuantityKindDimensionVector <|-- QuantityKindDimensionVector_SI
QuantityKindDimensionVector_CGS <|-- QuantityKindDimensionVector_CGS_EMU
QuantityKindDimensionVector_CGS <|-- QuantityKindDimensionVector_CGS_ESU
QuantityKindDimensionVector_CGS <|-- QuantityKindDimensionVector_CGS_GAUSS
QuantityKindDimensionVector_CGS <|-- QuantityKindDimensionVector_CGS_LH
QuantityValue <|-- ConstantValue
Resource <|-- UCUMcs
Resource <|-- UCUMcs_term
Resource <|-- valueUnion
Scale <|-- EnumerationScale
Scale <|-- IntervalScale
Scale <|-- NominalScale
Scale <|-- OrdinalScale
Scale <|-- RatioScale
StringEncodingType <|-- DateTimeStringEncodingType
Thing <|-- Aspect
Thing <|-- Concept
Unit <|-- ContextualUnit
Unit <|-- DerivedUnit
Unit <|-- DimensionlessUnit
Verifiable <|-- Comment
Verifiable <|-- EnumeratedValue
Verifiable <|-- Prefix
Verifiable <|-- QuantityKind
Verifiable <|-- Rule
Verifiable <|-- SystemOfUnits
Verifiable <|-- Unit

```

## ERD Diagram

```mermaid
erDiagram
AbstractQuantityKind {
    stringList guidance  
    string id  
    stringList altSymbol  
    string abbreviation  
    string description  
    stringList latexSymbol  
    string isReplacedBy  
    string symbol  
    string plainTextDescription  
    string deprecated  
}
AngleUnit {
    stringList omUnit  
    stringList unitFor  
    stringList guidance  
    string id  
    string mathMLdefinition  
    stringList latexSymbol  
    stringList symbol  
    string conversionOffsetSN  
    string conversionMultiplier  
    stringList altSymbol  
    stringList siUnitsExpression  
    stringList normativeReference  
    stringList uneceCommonCode  
    stringList latexDefinition  
    stringList udunitsCode  
    stringList iec61360Code  
    string conversionOffset  
    string factorUnitScalar  
    string conversionMultiplierSN  
    stringList isoNormativeReference  
}
BaseDimensionMagnitude {
    stringList guidance  
    string id  
    float vectorMagnitude  
    string abbreviation  
    string description  
    string isReplacedBy  
    string plainTextDescription  
    string deprecated  
}
BinaryPrefix {
    stringList guidance  
    string id  
    stringList altSymbol  
    string prefixMultiplier  
    stringList latexSymbol  
    stringList isoNormativeReference  
    stringList symbol  
    stringList normativeReference  
}
BitEncodingType {
    stringList guidance  
    string id  
    string bytes  
    string abbreviation  
    string description  
    string isReplacedBy  
    string plainTextDescription  
    string deprecated  
    string bits  
}
BooleanEncodingType {
    stringList guidance  
    string id  
    string bytes  
    string abbreviation  
    string description  
    string isReplacedBy  
    string plainTextDescription  
    string deprecated  
    string bits  
}
ByteEncodingType {
    stringList guidance  
    string id  
    string bytes  
    string abbreviation  
    string description  
    string isReplacedBy  
    string plainTextDescription  
    string deprecated  
    string bits  
}
CardinalityType {
    stringList guidance  
    string id  
    stringList altSymbol  
    string abbreviation  
    string literal  
    string description  
    string symbol  
    stringList normativeReference  
    stringList isoNormativeReference  
}
CharEncodingType {
    stringList guidance  
    string id  
    string bytes  
    string abbreviation  
    string description  
    string isReplacedBy  
    string plainTextDescription  
    string deprecated  
    string bits  
}
Citation {
    stringList guidance  
    string id  
    string abbreviation  
    string description  
    string url  
    string isReplacedBy  
    string plainTextDescription  
    string deprecated  
}
Concept {
    stringList guidance  
    string id  
    string abbreviation  
    string description  
    string isReplacedBy  
    string plainTextDescription  
    string deprecated  
}
ConstantValue {
    stringList guidance  
    string id  
    string value  
    double relativeStandardUncertainty  
    doubleList standardUncertaintySN  
    decimal standardUncertainty  
    stringList exactConstant  
    string valueSN  
}
ContextualUnit {
    stringList omUnit  
    stringList unitFor  
    stringList guidance  
    string id  
    string mathMLdefinition  
    stringList latexSymbol  
    stringList symbol  
    string conversionOffsetSN  
    string conversionMultiplier  
    stringList altSymbol  
    stringList siUnitsExpression  
    stringList normativeReference  
    stringList uneceCommonCode  
    stringList latexDefinition  
    stringList udunitsCode  
    stringList iec61360Code  
    string conversionOffset  
    string factorUnitScalar  
    string conversionMultiplierSN  
    stringList isoNormativeReference  
}
CountingUnit {
    stringList omUnit  
    stringList unitFor  
    stringList guidance  
    string id  
    string mathMLdefinition  
    stringList latexSymbol  
    stringList symbol  
    string conversionOffsetSN  
    string conversionMultiplier  
    stringList altSymbol  
    stringList siUnitsExpression  
    stringList normativeReference  
    stringList uneceCommonCode  
    stringList latexDefinition  
    stringList udunitsCode  
    stringList iec61360Code  
    string conversionOffset  
    string factorUnitScalar  
    string conversionMultiplierSN  
    stringList isoNormativeReference  
}
CurrencyUnit {
    stringList omUnit  
    stringList unitFor  
    stringList guidance  
    string id  
    string mathMLdefinition  
    stringList latexSymbol  
    string currencyCode  
    stringList symbol  
    string conversionOffsetSN  
    string conversionMultiplier  
    stringList altSymbol  
    stringList siUnitsExpression  
    stringList normativeReference  
    stringList uneceCommonCode  
    stringList latexDefinition  
    stringList udunitsCode  
    stringList iec61360Code  
    string currencyExponent  
    string conversionOffset  
    string factorUnitScalar  
    string conversionMultiplierSN  
    stringList isoNormativeReference  
}
DataEncoding {

}
DataItem {
    stringList guidance  
    string id  
    string value  
    string abbreviation  
    string description  
    string isReplacedBy  
    string plainTextDescription  
    string deprecated  
}
Datatype {
    stringList guidance  
    string id  
    string javaName  
    string protocolBuffersName  
    string odbcName  
    string pythonName  
    string oleDBName  
    string cName  
    string ansiSQLName  
    string mySQLName  
    string plainTextDescription  
    string jsName  
    string vbName  
    string abbreviation  
    string isReplacedBy  
    string bounded  
    string microsoftSQLServerName  
    string description  
    string oracleSQLName  
    string deprecated  
    string matlabName  
}
DecimalPrefix {
    stringList guidance  
    string id  
    stringList altSymbol  
    string prefixMultiplier  
    stringList latexSymbol  
    stringList isoNormativeReference  
    stringList symbol  
    stringList normativeReference  
}
DerivedUnit {
    stringList omUnit  
    stringList unitFor  
    stringList guidance  
    string id  
    string mathMLdefinition  
    stringList latexSymbol  
    stringList symbol  
    string conversionOffsetSN  
    string conversionMultiplier  
    stringList altSymbol  
    stringList siUnitsExpression  
    stringList normativeReference  
    stringList uneceCommonCode  
    stringList latexDefinition  
    stringList udunitsCode  
    stringList iec61360Code  
    string conversionOffset  
    string factorUnitScalar  
    string conversionMultiplierSN  
    stringList isoNormativeReference  
}
DimensionlessUnit {
    stringList omUnit  
    stringList unitFor  
    stringList guidance  
    string id  
    string mathMLdefinition  
    stringList latexSymbol  
    stringList symbol  
    string conversionOffsetSN  
    string conversionMultiplier  
    stringList altSymbol  
    stringList siUnitsExpression  
    stringList normativeReference  
    stringList uneceCommonCode  
    stringList latexDefinition  
    stringList udunitsCode  
    stringList iec61360Code  
    string conversionOffset  
    string factorUnitScalar  
    string conversionMultiplierSN  
    stringList isoNormativeReference  
}
Discipline {
    stringList guidance  
    string id  
    string abbreviation  
    string description  
    string isReplacedBy  
    string plainTextDescription  
    string deprecated  
}
Encoding {
    stringList guidance  
    string id  
    string bytes  
    string abbreviation  
    string description  
    string isReplacedBy  
    string plainTextDescription  
    string deprecated  
    string bits  
}
EndianType {
    stringList guidance  
    string id  
    stringList altSymbol  
    string abbreviation  
    string description  
    string symbol  
    stringList normativeReference  
    stringList isoNormativeReference  
}
EnumeratedQuantity {
    stringList guidance  
    string id  
    string description  
    string abbreviation  
    string isReplacedBy  
    string plainTextDescription  
    string deprecated  
}
EnumeratedValue {
    stringList guidance  
    string id  
    stringList altSymbol  
    string abbreviation  
    string description  
    string symbol  
    stringList normativeReference  
    stringList isoNormativeReference  
}
Enumeration {
    stringList guidance  
    string id  
    string abbreviation  
    string description  
    string isReplacedBy  
    string plainTextDescription  
    string deprecated  
}
EnumerationScale {
    stringList guidance  
    string id  
    string abbreviation  
    string description  
    string dataStructure  
    string isReplacedBy  
    string plainTextDescription  
    string deprecated  
}
Figure {
    stringList guidance  
    string id  
    string abbreviation  
    string image  
    string description  
    string width  
    string imageLocation  
    string figureCaption  
    string height  
    string isReplacedBy  
    string figureLabel  
    string plainTextDescription  
    string deprecated  
    string landscape  
}
FloatingPointEncodingType {
    stringList guidance  
    string id  
    string bytes  
    string abbreviation  
    string description  
    string isReplacedBy  
    string plainTextDescription  
    string deprecated  
    string bits  
}
IntegerEncodingType {
    stringList guidance  
    string id  
    string bytes  
    string abbreviation  
    string description  
    string isReplacedBy  
    string plainTextDescription  
    string deprecated  
    string bits  
}
IntervalScale {
    stringList guidance  
    string id  
    string abbreviation  
    string description  
    string dataStructure  
    string isReplacedBy  
    string plainTextDescription  
    string deprecated  
}
LogarithmicUnit {
    stringList omUnit  
    stringList unitFor  
    stringList guidance  
    string id  
    string mathMLdefinition  
    stringList latexSymbol  
    stringList symbol  
    string conversionOffsetSN  
    string conversionMultiplier  
    stringList altSymbol  
    stringList siUnitsExpression  
    stringList normativeReference  
    stringList uneceCommonCode  
    stringList latexDefinition  
    stringList udunitsCode  
    stringList iec61360Code  
    string conversionOffset  
    string factorUnitScalar  
    string conversionMultiplierSN  
    stringList isoNormativeReference  
}
MathsFunctionType {
    stringList guidance  
    string id  
    string abbreviation  
    string description  
    string isReplacedBy  
    string plainTextDescription  
    string deprecated  
}
NominalScale {
    stringList guidance  
    string id  
    string abbreviation  
    string description  
    string dataStructure  
    string isReplacedBy  
    string plainTextDescription  
    string deprecated  
}
NumericUnion {
    stringList guidance  
    string id  
}
OrderedType {
    stringList guidance  
    string id  
    stringList altSymbol  
    string abbreviation  
    string literal  
    string description  
    string symbol  
    stringList normativeReference  
    stringList isoNormativeReference  
}
OrdinalScale {
    stringList guidance  
    string id  
    string abbreviation  
    string description  
    string order  
    string dataStructure  
    string isReplacedBy  
    string plainTextDescription  
    string deprecated  
}
Organization {
    stringList guidance  
    string id  
    string abbreviation  
    string description  
    stringList url  
    string isReplacedBy  
    string plainTextDescription  
    string deprecated  
}
PhysicalConstant {
    stringList guidance  
    string id  
    string mathMLdefinition  
    stringList latexSymbol  
    doubleList standardUncertaintySN  
    stringList symbol  
    double relativeStandardUncertainty  
    stringList altSymbol  
    string value  
    stringList normativeReference  
    decimal standardUncertainty  
    string latexDefinition  
    stringList ucumCode  
    string valueSN  
    booleanList isDeltaQuantity  
    stringList isoNormativeReference  
    booleanList exactConstant  
}
PlaneAngleUnit {
    stringList omUnit  
    stringList unitFor  
    stringList guidance  
    string id  
    string mathMLdefinition  
    stringList latexSymbol  
    stringList symbol  
    string conversionOffsetSN  
    string conversionMultiplier  
    stringList altSymbol  
    stringList siUnitsExpression  
    stringList normativeReference  
    stringList uneceCommonCode  
    stringList latexDefinition  
    stringList udunitsCode  
    stringList iec61360Code  
    string conversionOffset  
    string factorUnitScalar  
    string conversionMultiplierSN  
    stringList isoNormativeReference  
}
Prefix {
    stringList guidance  
    string id  
    stringList altSymbol  
    string prefixMultiplier  
    stringList latexSymbol  
    stringList isoNormativeReference  
    stringList symbol  
    stringList normativeReference  
}
Quantifiable {
    string value  
    doubleList standardUncertaintySN  
    decimal standardUncertainty  
    double relativeStandardUncertainty  
    string valueSN  
}
Quantity {
    stringList guidance  
    string id  
    string value  
    doubleList standardUncertaintySN  
    booleanList isDeltaQuantity  
    decimal standardUncertainty  
    double relativeStandardUncertainty  
    string valueSN  
}
QuantityKind {
    stringList guidance  
    string id  
    string mathMLdefinition  
    stringList iec61360Code  
    string latexDefinition  
    stringList isoNormativeReference  
    stringList normativeReference  
}
QuantityKindDimensionVector {
    stringList guidance  
    string id  
    string dimensionExponentForMass  
    string dimensionlessExponent  
    string dimensionExponentForAmountOfSubstance  
    string description  
    stringList latexSymbol  
    string dimensionExponentForThermodynamicTemperature  
    string abbreviation  
    string dimensionExponentForLuminousIntensity  
    string isReplacedBy  
    string dimensionExponentForLength  
    string plainTextDescription  
    string deprecated  
    string latexDefinition  
    string dimensionExponentForTime  
    string dimensionExponentForElectricCurrent  
}
QuantityKindDimensionVectorCGS {
    stringList guidance  
    string id  
    string dimensionExponentForMass  
    string dimensionlessExponent  
    string dimensionExponentForAmountOfSubstance  
    string description  
    stringList latexSymbol  
    string dimensionExponentForThermodynamicTemperature  
    string abbreviation  
    string dimensionExponentForLuminousIntensity  
    string isReplacedBy  
    string dimensionExponentForLength  
    string plainTextDescription  
    string deprecated  
    string latexDefinition  
    string dimensionExponentForTime  
    string dimensionExponentForElectricCurrent  
}
QuantityKindDimensionVectorCGS-EMU {
    stringList guidance  
    string id  
    string dimensionExponentForMass  
    string dimensionlessExponent  
    string dimensionExponentForAmountOfSubstance  
    string description  
    stringList latexSymbol  
    string dimensionExponentForThermodynamicTemperature  
    string abbreviation  
    string dimensionExponentForLuminousIntensity  
    string isReplacedBy  
    string dimensionExponentForLength  
    string plainTextDescription  
    string deprecated  
    string latexDefinition  
    string dimensionExponentForTime  
    string dimensionExponentForElectricCurrent  
}
QuantityKindDimensionVectorCGS-ESU {
    stringList guidance  
    string id  
    string dimensionExponentForMass  
    string dimensionlessExponent  
    string dimensionExponentForAmountOfSubstance  
    string description  
    stringList latexSymbol  
    string dimensionExponentForThermodynamicTemperature  
    string abbreviation  
    string dimensionExponentForLuminousIntensity  
    string isReplacedBy  
    string dimensionExponentForLength  
    string plainTextDescription  
    string deprecated  
    string latexDefinition  
    string dimensionExponentForTime  
    string dimensionExponentForElectricCurrent  
}
QuantityKindDimensionVectorCGS-GAUSS {
    stringList guidance  
    string id  
    string dimensionExponentForMass  
    string dimensionlessExponent  
    string dimensionExponentForAmountOfSubstance  
    string description  
    stringList latexSymbol  
    string dimensionExponentForThermodynamicTemperature  
    string abbreviation  
    string dimensionExponentForLuminousIntensity  
    string isReplacedBy  
    string dimensionExponentForLength  
    string plainTextDescription  
    string deprecated  
    string latexDefinition  
    string dimensionExponentForTime  
    string dimensionExponentForElectricCurrent  
}
QuantityKindDimensionVectorCGS-LH {
    stringList guidance  
    string id  
    string dimensionExponentForMass  
    string dimensionlessExponent  
    string dimensionExponentForAmountOfSubstance  
    string description  
    stringList latexSymbol  
    string dimensionExponentForThermodynamicTemperature  
    string abbreviation  
    string dimensionExponentForLuminousIntensity  
    string isReplacedBy  
    string dimensionExponentForLength  
    string plainTextDescription  
    string deprecated  
    string latexDefinition  
    string dimensionExponentForTime  
    string dimensionExponentForElectricCurrent  
}
QuantityKindDimensionVectorISO {
    stringList guidance  
    string id  
    string dimensionExponentForMass  
    string dimensionlessExponent  
    string dimensionExponentForAmountOfSubstance  
    string description  
    stringList latexSymbol  
    string dimensionExponentForThermodynamicTemperature  
    string abbreviation  
    string dimensionExponentForLuminousIntensity  
    string isReplacedBy  
    string dimensionExponentForLength  
    string plainTextDescription  
    string deprecated  
    string latexDefinition  
    string dimensionExponentForTime  
    string dimensionExponentForElectricCurrent  
}
QuantityKindDimensionVectorImperial {
    stringList guidance  
    string id  
    string dimensionExponentForMass  
    string dimensionlessExponent  
    string dimensionExponentForAmountOfSubstance  
    string description  
    stringList latexSymbol  
    string dimensionExponentForThermodynamicTemperature  
    string abbreviation  
    string dimensionExponentForLuminousIntensity  
    string isReplacedBy  
    string dimensionExponentForLength  
    string plainTextDescription  
    string deprecated  
    string latexDefinition  
    string dimensionExponentForTime  
    string dimensionExponentForElectricCurrent  
}
QuantityKindDimensionVectorSI {
    stringList guidance  
    string id  
    string dimensionExponentForMass  
    string dimensionlessExponent  
    string dimensionExponentForAmountOfSubstance  
    string description  
    stringList latexSymbol  
    string dimensionExponentForThermodynamicTemperature  
    string abbreviation  
    string dimensionExponentForLuminousIntensity  
    string isReplacedBy  
    string dimensionExponentForLength  
    string plainTextDescription  
    string deprecated  
    string latexDefinition  
    string dimensionExponentForTime  
    string dimensionExponentForElectricCurrent  
}
QuantityType {
    stringList guidance  
    string id  
    stringList altSymbol  
    string abbreviation  
    string description  
    string symbol  
    stringList normativeReference  
    stringList isoNormativeReference  
}
QuantityValue {
    stringList guidance  
    string id  
    string value  
    doubleList standardUncertaintySN  
    decimal standardUncertainty  
    double relativeStandardUncertainty  
    string valueSN  
}
RatioScale {
    stringList guidance  
    string id  
    string abbreviation  
    string description  
    string dataStructure  
    string isReplacedBy  
    string plainTextDescription  
    string deprecated  
}
Rule {
    stringList guidance  
    string id  
    stringList normativeReference  
    stringList rationale  
    stringList isoNormativeReference  
}
RuleType {
    stringList guidance  
    string id  
    stringList altSymbol  
    string abbreviation  
    string description  
    string symbol  
    stringList normativeReference  
    stringList isoNormativeReference  
}
ScalarDatatype {
    stringList guidance  
    string id  
    string javaName  
    string protocolBuffersName  
    string odbcName  
    string pythonName  
    string oleDBName  
    string maxInclusive  
    string cName  
    string minInclusive  
    string ansiSQLName  
    string bits  
    string mySQLName  
    string length  
    string minExclusive  
    string plainTextDescription  
    string jsName  
    string bytes  
    string vbName  
    string abbreviation  
    string isReplacedBy  
    string bounded  
    string microsoftSQLServerName  
    string description  
    string oracleSQLName  
    string maxExclusive  
    string deprecated  
    string matlabName  
}
Scale {
    stringList guidance  
    string id  
    string abbreviation  
    string description  
    string dataStructure  
    string isReplacedBy  
    string plainTextDescription  
    string deprecated  
}
ScaleType {
    stringList guidance  
    string id  
    stringList altSymbol  
    string abbreviation  
    string description  
    string dataStructure  
    string symbol  
    stringList normativeReference  
    stringList isoNormativeReference  
}
SolidAngleUnit {
    stringList omUnit  
    stringList unitFor  
    stringList guidance  
    string id  
    string mathMLdefinition  
    stringList latexSymbol  
    stringList symbol  
    string conversionOffsetSN  
    string conversionMultiplier  
    stringList altSymbol  
    stringList siUnitsExpression  
    stringList normativeReference  
    stringList uneceCommonCode  
    stringList latexDefinition  
    stringList udunitsCode  
    stringList iec61360Code  
    string conversionOffset  
    string factorUnitScalar  
    string conversionMultiplierSN  
    stringList isoNormativeReference  
}
Symbol {
    stringList guidance  
    string id  
    string abbreviation  
    string description  
    string isReplacedBy  
    string plainTextDescription  
    string deprecated  
}
SystemOfQuantityKinds {
    stringList guidance  
    string id  
    string abbreviation  
    string description  
    string isReplacedBy  
    string plainTextDescription  
    string deprecated  
}
SystemOfUnits {
    stringList guidance  
    string id  
    stringList normativeReference  
    stringList isoNormativeReference  
}
TransformType {
    stringList guidance  
    string id  
    stringList altSymbol  
    string abbreviation  
    string description  
    string symbol  
    stringList normativeReference  
    stringList isoNormativeReference  
}
UCUMcs {

}
UCUMcs-term {

}
Unit {
    stringList omUnit  
    stringList unitFor  
    stringList guidance  
    string id  
    string mathMLdefinition  
    stringList latexSymbol  
    stringList symbol  
    string conversionOffsetSN  
    string conversionMultiplier  
    stringList altSymbol  
    stringList siUnitsExpression  
    stringList normativeReference  
    stringList uneceCommonCode  
    stringList latexDefinition  
    stringList udunitsCode  
    stringList iec61360Code  
    string conversionOffset  
    string factorUnitScalar  
    string conversionMultiplierSN  
    stringList isoNormativeReference  
}
UserQuantityKind {
    stringList guidance  
    string id  
    stringList altSymbol  
    string abbreviation  
    string description  
    stringList latexSymbol  
    string isReplacedBy  
    string symbol  
    string plainTextDescription  
    string deprecated  
}
__Class {

}

AbstractQuantityKind ||--}o Rule : "hasRule"
AngleUnit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
AngleUnit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
AngleUnit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
AngleUnit ||--}o Prefix : "prefix"
AngleUnit ||--}o QuantityKind : "hasQuantityKind"
AngleUnit ||--}o SystemOfUnits : "applicableSystem"
AngleUnit ||--}o SystemOfUnits : "definedUnitOfSystem"
AngleUnit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
AngleUnit ||--}o SystemOfUnits : "derivedUnitOfSystem"
AngleUnit ||--}o SystemOfUnits : "isUnitOfSystem"
AngleUnit ||--}o UCUMcs : "ucumCode"
AngleUnit ||--}o Unit : "exactMatch"
AngleUnit ||--}o Unit : "hasReciprocalUnit"
AngleUnit ||--}o Unit : "scalingOf"
AngleUnit ||--}o __Class : "hasFactorUnit"
BaseDimensionMagnitude ||--|| QuantityKind : "hasBaseQuantityKind"
BaseDimensionMagnitude ||--}o Rule : "hasRule"
BinaryPrefix ||--}o Prefix : "exactMatch"
BinaryPrefix ||--}o UCUMcs-term : "ucumCode"
BitEncodingType ||--}o Rule : "hasRule"
BooleanEncodingType ||--}o Rule : "hasRule"
ByteEncodingType ||--}o Rule : "hasRule"
CharEncodingType ||--}o Rule : "hasRule"
Citation ||--}o Rule : "hasRule"
Concept ||--}o Rule : "hasRule"
ConstantValue ||--|o DataEncoding : "dataEncoding"
ConstantValue ||--|o Datatype : "datatype"
ConstantValue ||--|o Unit : "hasUnit"
ContextualUnit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
ContextualUnit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
ContextualUnit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
ContextualUnit ||--}o Prefix : "prefix"
ContextualUnit ||--}o QuantityKind : "hasQuantityKind"
ContextualUnit ||--}o SystemOfUnits : "applicableSystem"
ContextualUnit ||--}o SystemOfUnits : "definedUnitOfSystem"
ContextualUnit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
ContextualUnit ||--}o SystemOfUnits : "derivedUnitOfSystem"
ContextualUnit ||--}o SystemOfUnits : "isUnitOfSystem"
ContextualUnit ||--}o UCUMcs : "ucumCode"
ContextualUnit ||--}o Unit : "exactMatch"
ContextualUnit ||--}o Unit : "hasReciprocalUnit"
ContextualUnit ||--}o Unit : "scalingOf"
ContextualUnit ||--}o __Class : "hasFactorUnit"
CountingUnit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
CountingUnit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
CountingUnit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
CountingUnit ||--}o Prefix : "prefix"
CountingUnit ||--}o QuantityKind : "hasQuantityKind"
CountingUnit ||--}o SystemOfUnits : "applicableSystem"
CountingUnit ||--}o SystemOfUnits : "definedUnitOfSystem"
CountingUnit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
CountingUnit ||--}o SystemOfUnits : "derivedUnitOfSystem"
CountingUnit ||--}o SystemOfUnits : "isUnitOfSystem"
CountingUnit ||--}o UCUMcs : "ucumCode"
CountingUnit ||--}o Unit : "exactMatch"
CountingUnit ||--}o Unit : "hasReciprocalUnit"
CountingUnit ||--}o Unit : "scalingOf"
CountingUnit ||--}o __Class : "hasFactorUnit"
CurrencyUnit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
CurrencyUnit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
CurrencyUnit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
CurrencyUnit ||--}o Prefix : "prefix"
CurrencyUnit ||--}o QuantityKind : "hasQuantityKind"
CurrencyUnit ||--}o SystemOfUnits : "applicableSystem"
CurrencyUnit ||--}o SystemOfUnits : "definedUnitOfSystem"
CurrencyUnit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
CurrencyUnit ||--}o SystemOfUnits : "derivedUnitOfSystem"
CurrencyUnit ||--}o SystemOfUnits : "isUnitOfSystem"
CurrencyUnit ||--}o UCUMcs : "ucumCode"
CurrencyUnit ||--}o Unit : "exactMatch"
CurrencyUnit ||--}o Unit : "hasReciprocalUnit"
CurrencyUnit ||--}o Unit : "scalingOf"
CurrencyUnit ||--}o __Class : "hasFactorUnit"
DataEncoding ||--|o Encoding : "encoding"
DataEncoding ||--|o EndianType : "bitOrder"
DataEncoding ||--|o EndianType : "byteOrder"
DataItem ||--}o Rule : "hasRule"
Datatype ||--|o CardinalityType : "cardinality"
Datatype ||--|o Datatype : "basis"
Datatype ||--|o OrderedType : "orderedType"
Datatype ||--}o Rule : "hasRule"
DecimalPrefix ||--}o Prefix : "exactMatch"
DecimalPrefix ||--}o UCUMcs-term : "ucumCode"
DerivedUnit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
DerivedUnit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
DerivedUnit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
DerivedUnit ||--}o Prefix : "prefix"
DerivedUnit ||--}o QuantityKind : "hasQuantityKind"
DerivedUnit ||--}o SystemOfUnits : "applicableSystem"
DerivedUnit ||--}o SystemOfUnits : "definedUnitOfSystem"
DerivedUnit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
DerivedUnit ||--}o SystemOfUnits : "derivedUnitOfSystem"
DerivedUnit ||--}o SystemOfUnits : "isUnitOfSystem"
DerivedUnit ||--}o UCUMcs : "ucumCode"
DerivedUnit ||--}o Unit : "exactMatch"
DerivedUnit ||--}o Unit : "hasReciprocalUnit"
DerivedUnit ||--}o Unit : "scalingOf"
DerivedUnit ||--}o __Class : "hasFactorUnit"
DimensionlessUnit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
DimensionlessUnit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
DimensionlessUnit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
DimensionlessUnit ||--}o Prefix : "prefix"
DimensionlessUnit ||--}o QuantityKind : "hasQuantityKind"
DimensionlessUnit ||--}o SystemOfUnits : "applicableSystem"
DimensionlessUnit ||--}o SystemOfUnits : "definedUnitOfSystem"
DimensionlessUnit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
DimensionlessUnit ||--}o SystemOfUnits : "derivedUnitOfSystem"
DimensionlessUnit ||--}o SystemOfUnits : "isUnitOfSystem"
DimensionlessUnit ||--}o UCUMcs : "ucumCode"
DimensionlessUnit ||--}o Unit : "exactMatch"
DimensionlessUnit ||--}o Unit : "hasReciprocalUnit"
DimensionlessUnit ||--}o Unit : "scalingOf"
DimensionlessUnit ||--}o __Class : "hasFactorUnit"
Discipline ||--}o Rule : "hasRule"
Encoding ||--}o Rule : "hasRule"
EnumeratedQuantity ||--}o EnumeratedValue : "enumeratedValue"
EnumeratedQuantity ||--}o Enumeration : "enumeration"
EnumeratedQuantity ||--}o Rule : "hasRule"
Enumeration ||--|o EnumeratedValue : "default"
Enumeration ||--}o Rule : "hasRule"
Enumeration ||--}| EnumeratedValue : "element"
EnumerationScale ||--|o ScaleType : "scaleType"
EnumerationScale ||--}o MathsFunctionType : "permissibleMaths"
EnumerationScale ||--}o Rule : "hasRule"
EnumerationScale ||--}o TransformType : "permissibleTransformation"
Figure ||--}o Rule : "hasRule"
FloatingPointEncodingType ||--}o Rule : "hasRule"
IntegerEncodingType ||--}o Rule : "hasRule"
IntervalScale ||--|o ScaleType : "scaleType"
IntervalScale ||--}o MathsFunctionType : "permissibleMaths"
IntervalScale ||--}o Rule : "hasRule"
IntervalScale ||--}o TransformType : "permissibleTransformation"
LogarithmicUnit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
LogarithmicUnit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
LogarithmicUnit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
LogarithmicUnit ||--}o Prefix : "prefix"
LogarithmicUnit ||--}o QuantityKind : "hasQuantityKind"
LogarithmicUnit ||--}o SystemOfUnits : "applicableSystem"
LogarithmicUnit ||--}o SystemOfUnits : "definedUnitOfSystem"
LogarithmicUnit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
LogarithmicUnit ||--}o SystemOfUnits : "derivedUnitOfSystem"
LogarithmicUnit ||--}o SystemOfUnits : "isUnitOfSystem"
LogarithmicUnit ||--}o UCUMcs : "ucumCode"
LogarithmicUnit ||--}o Unit : "exactMatch"
LogarithmicUnit ||--}o Unit : "hasReciprocalUnit"
LogarithmicUnit ||--}o Unit : "scalingOf"
LogarithmicUnit ||--}o __Class : "hasFactorUnit"
MathsFunctionType ||--}o Rule : "hasRule"
NominalScale ||--|o ScaleType : "scaleType"
NominalScale ||--}o MathsFunctionType : "permissibleMaths"
NominalScale ||--}o Rule : "hasRule"
NominalScale ||--}o TransformType : "permissibleTransformation"
OrdinalScale ||--|o ScaleType : "scaleType"
OrdinalScale ||--}o MathsFunctionType : "permissibleMaths"
OrdinalScale ||--}o Rule : "hasRule"
OrdinalScale ||--}o TransformType : "permissibleTransformation"
Organization ||--}o Rule : "hasRule"
PhysicalConstant ||--|o DataEncoding : "dataEncoding"
PhysicalConstant ||--|o Datatype : "datatype"
PhysicalConstant ||--|o Unit : "hasUnit"
PhysicalConstant ||--}o PhysicalConstant : "exactMatch"
PhysicalConstant ||--}o QuantityKind : "hasQuantityKind"
PhysicalConstant ||--}o QuantityKindDimensionVector : "hasDimensionVector"
PhysicalConstant ||--}o QuantityValue : "quantityValue"
PhysicalConstant ||--}o SystemOfUnits : "applicableSystem"
PhysicalConstant ||--}o Unit : "applicableUnit"
PlaneAngleUnit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
PlaneAngleUnit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
PlaneAngleUnit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
PlaneAngleUnit ||--}o Prefix : "prefix"
PlaneAngleUnit ||--}o QuantityKind : "hasQuantityKind"
PlaneAngleUnit ||--}o SystemOfUnits : "applicableSystem"
PlaneAngleUnit ||--}o SystemOfUnits : "definedUnitOfSystem"
PlaneAngleUnit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
PlaneAngleUnit ||--}o SystemOfUnits : "derivedUnitOfSystem"
PlaneAngleUnit ||--}o SystemOfUnits : "isUnitOfSystem"
PlaneAngleUnit ||--}o UCUMcs : "ucumCode"
PlaneAngleUnit ||--}o Unit : "exactMatch"
PlaneAngleUnit ||--}o Unit : "hasReciprocalUnit"
PlaneAngleUnit ||--}o Unit : "scalingOf"
PlaneAngleUnit ||--}o __Class : "hasFactorUnit"
Prefix ||--}o Prefix : "exactMatch"
Prefix ||--}o UCUMcs-term : "ucumCode"
Quantifiable ||--|o DataEncoding : "dataEncoding"
Quantifiable ||--|o Datatype : "datatype"
Quantifiable ||--|o Unit : "hasUnit"
Quantity ||--|o DataEncoding : "dataEncoding"
Quantity ||--|o Datatype : "datatype"
Quantity ||--|o Unit : "hasUnit"
Quantity ||--}o QuantityKind : "hasQuantityKind"
Quantity ||--}o QuantityValue : "quantityValue"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvDenominator"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvNumerator"
QuantityKind ||--|o QuantityKindDimensionVectorSI : "dimensionVectorForSI"
QuantityKind ||--}o QuantityKind : "exactMatch"
QuantityKind ||--}o QuantityKindDimensionVector : "hasDimensionVector"
QuantityKind ||--}o SystemOfQuantityKinds : "belongsToSystemOfQuantities"
QuantityKind ||--}o Unit : "applicableCGSUnit"
QuantityKind ||--}o Unit : "applicableISOUnit"
QuantityKind ||--}o Unit : "applicableImperialUnit"
QuantityKind ||--}o Unit : "applicableSIUnit"
QuantityKind ||--}o Unit : "applicableUSCustomaryUnit"
QuantityKind ||--}o Unit : "applicableUnit"
QuantityKindDimensionVector ||--}o QuantityKind : "hasReferenceQuantityKind"
QuantityKindDimensionVector ||--}o Rule : "hasRule"
QuantityKindDimensionVectorCGS ||--}o QuantityKind : "hasReferenceQuantityKind"
QuantityKindDimensionVectorCGS ||--}o Rule : "hasRule"
QuantityKindDimensionVectorCGS-EMU ||--}o QuantityKind : "hasReferenceQuantityKind"
QuantityKindDimensionVectorCGS-EMU ||--}o Rule : "hasRule"
QuantityKindDimensionVectorCGS-ESU ||--}o QuantityKind : "hasReferenceQuantityKind"
QuantityKindDimensionVectorCGS-ESU ||--}o Rule : "hasRule"
QuantityKindDimensionVectorCGS-GAUSS ||--}o QuantityKind : "hasReferenceQuantityKind"
QuantityKindDimensionVectorCGS-GAUSS ||--}o Rule : "hasRule"
QuantityKindDimensionVectorCGS-LH ||--}o QuantityKind : "hasReferenceQuantityKind"
QuantityKindDimensionVectorCGS-LH ||--}o Rule : "hasRule"
QuantityKindDimensionVectorISO ||--}o QuantityKind : "hasReferenceQuantityKind"
QuantityKindDimensionVectorISO ||--}o Rule : "hasRule"
QuantityKindDimensionVectorImperial ||--}o QuantityKind : "hasReferenceQuantityKind"
QuantityKindDimensionVectorImperial ||--}o Rule : "hasRule"
QuantityKindDimensionVectorSI ||--}o QuantityKind : "hasReferenceQuantityKind"
QuantityKindDimensionVectorSI ||--}o Rule : "hasRule"
QuantityType ||--}o QuantityKind : "value"
QuantityValue ||--|o DataEncoding : "dataEncoding"
QuantityValue ||--|o Datatype : "datatype"
QuantityValue ||--|o Unit : "hasUnit"
RatioScale ||--|o ScaleType : "scaleType"
RatioScale ||--}o MathsFunctionType : "permissibleMaths"
RatioScale ||--}o Rule : "hasRule"
RatioScale ||--}o TransformType : "permissibleTransformation"
Rule ||--}o RuleType : "ruleType"
ScalarDatatype ||--|o CardinalityType : "cardinality"
ScalarDatatype ||--|o Datatype : "basis"
ScalarDatatype ||--|o Datatype : "rdfsDatatype"
ScalarDatatype ||--|o OrderedType : "orderedType"
ScalarDatatype ||--}o Rule : "hasRule"
Scale ||--|o ScaleType : "scaleType"
Scale ||--}o MathsFunctionType : "permissibleMaths"
Scale ||--}o Rule : "hasRule"
Scale ||--}o TransformType : "permissibleTransformation"
ScaleType ||--}o MathsFunctionType : "permissibleMaths"
ScaleType ||--}o TransformType : "permissibleTransformation"
SolidAngleUnit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
SolidAngleUnit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
SolidAngleUnit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
SolidAngleUnit ||--}o Prefix : "prefix"
SolidAngleUnit ||--}o QuantityKind : "hasQuantityKind"
SolidAngleUnit ||--}o SystemOfUnits : "applicableSystem"
SolidAngleUnit ||--}o SystemOfUnits : "definedUnitOfSystem"
SolidAngleUnit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
SolidAngleUnit ||--}o SystemOfUnits : "derivedUnitOfSystem"
SolidAngleUnit ||--}o SystemOfUnits : "isUnitOfSystem"
SolidAngleUnit ||--}o UCUMcs : "ucumCode"
SolidAngleUnit ||--}o Unit : "exactMatch"
SolidAngleUnit ||--}o Unit : "hasReciprocalUnit"
SolidAngleUnit ||--}o Unit : "scalingOf"
SolidAngleUnit ||--}o __Class : "hasFactorUnit"
Symbol ||--}o Rule : "hasRule"
SystemOfQuantityKinds ||--|o Enumeration : "baseDimensionEnumeration"
SystemOfQuantityKinds ||--}o QuantityKind : "hasBaseQuantityKind"
SystemOfQuantityKinds ||--}o QuantityKind : "hasQuantityKind"
SystemOfQuantityKinds ||--}o QuantityKind : "systemDerivedQuantityKind"
SystemOfQuantityKinds ||--}o Rule : "hasRule"
SystemOfQuantityKinds ||--}o SystemOfUnits : "hasUnitSystem"
SystemOfUnits ||--}o PhysicalConstant : "applicablePhysicalConstant"
SystemOfUnits ||--}o Prefix : "prefix"
SystemOfUnits ||--}o Unit : "hasAllowedUnit"
SystemOfUnits ||--}o Unit : "hasBaseUnit"
SystemOfUnits ||--}o Unit : "hasCoherentUnit"
SystemOfUnits ||--}o Unit : "hasDefinedUnit"
SystemOfUnits ||--}o Unit : "hasDerivedCoherentUnit"
SystemOfUnits ||--}o Unit : "hasDerivedUnit"
SystemOfUnits ||--}o Unit : "hasUnit"
Unit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
Unit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
Unit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
Unit ||--}o Prefix : "prefix"
Unit ||--}o QuantityKind : "hasQuantityKind"
Unit ||--}o SystemOfUnits : "applicableSystem"
Unit ||--}o SystemOfUnits : "definedUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedUnitOfSystem"
Unit ||--}o SystemOfUnits : "isUnitOfSystem"
Unit ||--}o UCUMcs : "ucumCode"
Unit ||--}o Unit : "exactMatch"
Unit ||--}o Unit : "hasReciprocalUnit"
Unit ||--}o Unit : "scalingOf"
Unit ||--}o __Class : "hasFactorUnit"
UserQuantityKind ||--|| QuantityKind : "hasQuantityKind"
UserQuantityKind ||--}o Rule : "hasRule"

```


## Base Classes


These classes have no direct relationships but serve as base classes for other classes:

| Class | Description |
| --- | --- |
| [Aspect](#Aspect) |  |
| [Error3](#Error3) |  |
| [Resource](#Resource) |  |
| [Thing](#Thing) | The root class for all QUDT concepts |
| [Verifiable](#Verifiable) |  |

## Standalone Classes


These classes are completely isolated with no relationships and are not used as base classes:

| Class | Description |
| --- | --- |
| [AspectClass](#AspectClass) |  |
| [CatalogEntry](#CatalogEntry) |  |
| [Comment](#Comment) |  |
| [DateTimeStringEncodingType](#DateTimeStringEncodingType) |  |
| [Error1](#Error1) |  |
| [Error2](#Error2) |  |
| [LatexString](#LatexString) |  |
| [List](#List) |  |
| [NISTSP811Comment](#NISTSP811Comment) |  |
| [Ontology](#Ontology) |  |
| [SignednessType](#SignednessType) |  |
| [Statement](#Statement) |  |
| [StringEncodingType](#StringEncodingType) |  |
| [SymmetricRelation](#SymmetricRelation) |  |
| [GDay](#GDay) |  |
| [GMonth](#GMonth) |  |
| [GMonthDay](#GMonthDay) |  |
| [GYear](#GYear) |  |
| [GYearMonth](#GYearMonth) |  |
| [ValueUnion](#ValueUnion) |  |

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

```mermaid
erDiagram
AbstractQuantityKind {

}
QuantityKind {

}
Rule {

}

AbstractQuantityKind ||--}o Rule : "hasRule"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvDenominator"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvNumerator"
QuantityKind ||--|o QuantityKindDimensionVectorSI : "dimensionVectorForSI"
QuantityKind ||--}o QuantityKind : "exactMatch"
QuantityKind ||--}o QuantityKindDimensionVector : "hasDimensionVector"
QuantityKind ||--}o SystemOfQuantityKinds : "belongsToSystemOfQuantities"
QuantityKind ||--}o Unit : "applicableCGSUnit"
QuantityKind ||--}o Unit : "applicableISOUnit"
QuantityKind ||--}o Unit : "applicableImperialUnit"
QuantityKind ||--}o Unit : "applicableSIUnit"
QuantityKind ||--}o Unit : "applicableUSCustomaryUnit"
QuantityKind ||--}o Unit : "applicableUnit"
Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [Concept](#Concept)

#### Children

 * [UserQuantityKind](#UserQuantityKind)

#### Used as mixin by

 * [QuantityKind](#QuantityKind)




### AngleUnit




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
AngleUnit:
  is_a: DimensionlessUnit
  slots:
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

```mermaid
erDiagram
AngleUnit {

}
Prefix {

}
QuantityKind {

}
QuantityKindDimensionVector {

}
Rule {

}
SystemOfUnits {

}
UCUMcs {

}
Unit {

}
__Class {

}

AngleUnit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
AngleUnit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
AngleUnit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
AngleUnit ||--}o Prefix : "prefix"
AngleUnit ||--}o QuantityKind : "hasQuantityKind"
AngleUnit ||--}o SystemOfUnits : "applicableSystem"
AngleUnit ||--}o SystemOfUnits : "definedUnitOfSystem"
AngleUnit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
AngleUnit ||--}o SystemOfUnits : "derivedUnitOfSystem"
AngleUnit ||--}o SystemOfUnits : "isUnitOfSystem"
AngleUnit ||--}o UCUMcs : "ucumCode"
AngleUnit ||--}o Unit : "exactMatch"
AngleUnit ||--}o Unit : "hasReciprocalUnit"
AngleUnit ||--}o Unit : "scalingOf"
AngleUnit ||--}o __Class : "hasFactorUnit"
Prefix ||--}o Prefix : "exactMatch"
Prefix ||--}o UCUMcs-term : "ucumCode"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvDenominator"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvNumerator"
QuantityKind ||--|o QuantityKindDimensionVectorSI : "dimensionVectorForSI"
QuantityKind ||--}o QuantityKind : "exactMatch"
QuantityKind ||--}o QuantityKindDimensionVector : "hasDimensionVector"
QuantityKind ||--}o SystemOfQuantityKinds : "belongsToSystemOfQuantities"
QuantityKind ||--}o Unit : "applicableCGSUnit"
QuantityKind ||--}o Unit : "applicableISOUnit"
QuantityKind ||--}o Unit : "applicableImperialUnit"
QuantityKind ||--}o Unit : "applicableSIUnit"
QuantityKind ||--}o Unit : "applicableUSCustomaryUnit"
QuantityKind ||--}o Unit : "applicableUnit"
QuantityKindDimensionVector ||--}o QuantityKind : "hasReferenceQuantityKind"
QuantityKindDimensionVector ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"
SystemOfUnits ||--}o PhysicalConstant : "applicablePhysicalConstant"
SystemOfUnits ||--}o Prefix : "prefix"
SystemOfUnits ||--}o Unit : "hasAllowedUnit"
SystemOfUnits ||--}o Unit : "hasBaseUnit"
SystemOfUnits ||--}o Unit : "hasCoherentUnit"
SystemOfUnits ||--}o Unit : "hasDefinedUnit"
SystemOfUnits ||--}o Unit : "hasDerivedCoherentUnit"
SystemOfUnits ||--}o Unit : "hasDerivedUnit"
SystemOfUnits ||--}o Unit : "hasUnit"
Unit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
Unit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
Unit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
Unit ||--}o Prefix : "prefix"
Unit ||--}o QuantityKind : "hasQuantityKind"
Unit ||--}o SystemOfUnits : "applicableSystem"
Unit ||--}o SystemOfUnits : "definedUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedUnitOfSystem"
Unit ||--}o SystemOfUnits : "isUnitOfSystem"
Unit ||--}o UCUMcs : "ucumCode"
Unit ||--}o Unit : "exactMatch"
Unit ||--}o Unit : "hasReciprocalUnit"
Unit ||--}o Unit : "scalingOf"
Unit ||--}o __Class : "hasFactorUnit"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| hasReciprocalUnit | <sub>0..\*</sub> | [Unit](#Unit) |  |
| isUnitOfSystem | <sub>0..\*</sub> | [SystemOfUnits](#SystemOfUnits) |  |
| omUnit | <sub>0..\*</sub> | None |  |
| unitFor | <sub>0..\*</sub> | None |  |
| *id* | <sub>0..1</sub> | None |  |
| *guidance* | <sub>0..\*</sub> | string |  |

#### Parents

 * [DimensionlessUnit](#DimensionlessUnit)

#### Children

 * [PlaneAngleUnit](#PlaneAngleUnit)
 * [SolidAngleUnit](#SolidAngleUnit)




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

```mermaid
classDiagram
Aspect <|-- DataEncoding
Aspect <|-- Quantifiable
Thing <|-- Aspect

```

This class has no attributes


#### Parents

 * [Thing](#Thing) - The root class for all QUDT concepts

#### Children

 * [DataEncoding](#DataEncoding)
 * [Quantifiable](#Quantifiable)

#### Used as mixin by

 * [Verifiable](#Verifiable)




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

```mermaid
classDiagram
Class <|-- AspectClass

```

This class has no attributes


#### Parents

 * [Class](#Class)




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

```mermaid
erDiagram
BaseDimensionMagnitude {

}
QuantityKind {

}
Rule {

}

BaseDimensionMagnitude ||--|| QuantityKind : "hasBaseQuantityKind"
BaseDimensionMagnitude ||--}o Rule : "hasRule"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvDenominator"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvNumerator"
QuantityKind ||--|o QuantityKindDimensionVectorSI : "dimensionVectorForSI"
QuantityKind ||--}o QuantityKind : "exactMatch"
QuantityKind ||--}o QuantityKindDimensionVector : "hasDimensionVector"
QuantityKind ||--}o SystemOfQuantityKinds : "belongsToSystemOfQuantities"
QuantityKind ||--}o Unit : "applicableCGSUnit"
QuantityKind ||--}o Unit : "applicableISOUnit"
QuantityKind ||--}o Unit : "applicableImperialUnit"
QuantityKind ||--}o Unit : "applicableSIUnit"
QuantityKind ||--}o Unit : "applicableUSCustomaryUnit"
QuantityKind ||--}o Unit : "applicableUnit"
Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [Concept](#Concept)




### BinaryPrefix



A <em>Binary Prefix</em> is a prefix for multiples of units in data processing, data transmission, and digital information, notably the bit and the byte, to indicate multiplication by a power of 2.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
BinaryPrefix:
  is_a: Prefix
  slots:
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

```mermaid
erDiagram
BinaryPrefix {

}
Prefix {

}
Rule {

}
UCUMcs-term {

}

BinaryPrefix ||--}o Prefix : "exactMatch"
BinaryPrefix ||--}o UCUMcs-term : "ucumCode"
Prefix ||--}o Prefix : "exactMatch"
Prefix ||--}o UCUMcs-term : "ucumCode"
Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| *id* | <sub>0..1</sub> | None |  |
| *guidance* | <sub>0..\*</sub> | string |  |

#### Parents

 * [Prefix](#Prefix)




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

```mermaid
erDiagram
BitEncodingType {

}
Rule {

}

BitEncodingType ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [Encoding](#Encoding)




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

```mermaid
erDiagram
BooleanEncodingType {

}
Rule {

}

BooleanEncodingType ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [Encoding](#Encoding)




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

```mermaid
erDiagram
ByteEncodingType {

}
Rule {

}

ByteEncodingType ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [Encoding](#Encoding)




### CardinalityType




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
CardinalityType:
  is_a: EnumeratedValue
  slots:
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

```mermaid
erDiagram
CardinalityType {

}
Datatype {

}
Rule {

}

Datatype ||--|o CardinalityType : "cardinality"
Datatype ||--|o Datatype : "basis"
Datatype ||--|o OrderedType : "orderedType"
Datatype ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| *id* | <sub>0..1</sub> | None |  |
| *guidance* | <sub>0..\*</sub> | string |  |

#### Parents

 * [EnumeratedValue](#EnumeratedValue)

#### Referenced by:

 *  **[Datatype](#Datatype)** : *[Datatype_cardinality](#Datatype_cardinality)*  <sub>0..\*</sub> 




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

```mermaid
erDiagram
CharEncodingType {

}
Rule {

}

CharEncodingType ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [Encoding](#Encoding)




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

```mermaid
erDiagram
Citation {

}
Rule {

}

Citation ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [Concept](#Concept)




### Class




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
Class: {}

```
</details>

```mermaid
erDiagram
Unit {

}
__Class {

}

Unit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
Unit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
Unit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
Unit ||--}o Prefix : "prefix"
Unit ||--}o QuantityKind : "hasQuantityKind"
Unit ||--}o SystemOfUnits : "applicableSystem"
Unit ||--}o SystemOfUnits : "definedUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedUnitOfSystem"
Unit ||--}o SystemOfUnits : "isUnitOfSystem"
Unit ||--}o UCUMcs : "ucumCode"
Unit ||--}o Unit : "exactMatch"
Unit ||--}o Unit : "hasReciprocalUnit"
Unit ||--}o Unit : "scalingOf"
Unit ||--}o __Class : "hasFactorUnit"

```


This class has no attributes


#### Children

 * [AspectClass](#AspectClass)

#### Referenced by:

 *  **[Unit](#Unit)** : *[Unit_hasFactorUnit](#Unit_hasFactorUnit)*  <sub>0..\*</sub> 




### Comment




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
Comment:
  is_a: Verifiable
  mixins:
  - Thing
  slots:
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

```mermaid
classDiagram
Comment <|-- NIST_SP811_Comment
Error3 <|-- Verifiable
Verifiable <|-- Comment
Comment ..> Thing

```

This class has no attributes


#### Parents

 * [Verifiable](#Verifiable)

#### Children

 * [NISTSP811Comment](#NISTSP811Comment)

#### Uses

 *  mixin: [Thing](#Thing) - The root class for all QUDT concepts




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

```mermaid
erDiagram
Concept {

}
Rule {

}

Concept ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **id** | <sub>0..1</sub> | None |  |
| **guidance** | <sub>0..\*</sub> | string |  |

#### Parents

 * [Thing](#Thing) - The root class for all QUDT concepts

#### Children

 * [AbstractQuantityKind](#AbstractQuantityKind)
 * [BaseDimensionMagnitude](#BaseDimensionMagnitude)
 * [Citation](#Citation)
 * [DataItem](#DataItem)
 * [Datatype](#Datatype)
 * [Discipline](#Discipline)
 * [Encoding](#Encoding)
 * [EnumeratedQuantity](#EnumeratedQuantity)
 * [Enumeration](#Enumeration)
 * [Figure](#Figure)
 * [MathsFunctionType](#MathsFunctionType)
 * [Organization](#Organization)
 * [QuantityKindDimensionVector](#QuantityKindDimensionVector)
 * [Scale](#Scale)
 * [Symbol](#Symbol)
 * [SystemOfQuantityKinds](#SystemOfQuantityKinds)

#### Used as mixin by

 * [EnumeratedValue](#EnumeratedValue)
 * [NumericUnion](#NumericUnion)
 * [Prefix](#Prefix)
 * [Quantity](#Quantity)
 * [QuantityValue](#QuantityValue)
 * [Rule](#Rule)
 * [SystemOfUnits](#SystemOfUnits)
 * [Unit](#Unit)

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

```mermaid
erDiagram
ConstantValue {

}
DataEncoding {

}
Datatype {

}
Rule {

}
Unit {

}

ConstantValue ||--|o DataEncoding : "dataEncoding"
ConstantValue ||--|o Datatype : "datatype"
ConstantValue ||--|o Unit : "hasUnit"
DataEncoding ||--|o Encoding : "encoding"
DataEncoding ||--|o EndianType : "bitOrder"
DataEncoding ||--|o EndianType : "byteOrder"
Datatype ||--|o CardinalityType : "cardinality"
Datatype ||--|o Datatype : "basis"
Datatype ||--|o OrderedType : "orderedType"
Datatype ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"
Unit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
Unit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
Unit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
Unit ||--}o Prefix : "prefix"
Unit ||--}o QuantityKind : "hasQuantityKind"
Unit ||--}o SystemOfUnits : "applicableSystem"
Unit ||--}o SystemOfUnits : "definedUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedUnitOfSystem"
Unit ||--}o SystemOfUnits : "isUnitOfSystem"
Unit ||--}o UCUMcs : "ucumCode"
Unit ||--}o Unit : "exactMatch"
Unit ||--}o Unit : "hasReciprocalUnit"
Unit ||--}o Unit : "scalingOf"
Unit ||--}o __Class : "hasFactorUnit"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| *id* | <sub>0..1</sub> | None |  |
| *guidance* | <sub>0..\*</sub> | string |  |

#### Parents

 * [QuantityValue](#QuantityValue)




### ContextualUnit




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
ContextualUnit:
  is_a: Unit
  slots:
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

```mermaid
erDiagram
ContextualUnit {

}
Prefix {

}
QuantityKind {

}
QuantityKindDimensionVector {

}
Rule {

}
SystemOfUnits {

}
UCUMcs {

}
Unit {

}
__Class {

}

ContextualUnit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
ContextualUnit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
ContextualUnit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
ContextualUnit ||--}o Prefix : "prefix"
ContextualUnit ||--}o QuantityKind : "hasQuantityKind"
ContextualUnit ||--}o SystemOfUnits : "applicableSystem"
ContextualUnit ||--}o SystemOfUnits : "definedUnitOfSystem"
ContextualUnit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
ContextualUnit ||--}o SystemOfUnits : "derivedUnitOfSystem"
ContextualUnit ||--}o SystemOfUnits : "isUnitOfSystem"
ContextualUnit ||--}o UCUMcs : "ucumCode"
ContextualUnit ||--}o Unit : "exactMatch"
ContextualUnit ||--}o Unit : "hasReciprocalUnit"
ContextualUnit ||--}o Unit : "scalingOf"
ContextualUnit ||--}o __Class : "hasFactorUnit"
Prefix ||--}o Prefix : "exactMatch"
Prefix ||--}o UCUMcs-term : "ucumCode"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvDenominator"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvNumerator"
QuantityKind ||--|o QuantityKindDimensionVectorSI : "dimensionVectorForSI"
QuantityKind ||--}o QuantityKind : "exactMatch"
QuantityKind ||--}o QuantityKindDimensionVector : "hasDimensionVector"
QuantityKind ||--}o SystemOfQuantityKinds : "belongsToSystemOfQuantities"
QuantityKind ||--}o Unit : "applicableCGSUnit"
QuantityKind ||--}o Unit : "applicableISOUnit"
QuantityKind ||--}o Unit : "applicableImperialUnit"
QuantityKind ||--}o Unit : "applicableSIUnit"
QuantityKind ||--}o Unit : "applicableUSCustomaryUnit"
QuantityKind ||--}o Unit : "applicableUnit"
QuantityKindDimensionVector ||--}o QuantityKind : "hasReferenceQuantityKind"
QuantityKindDimensionVector ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"
SystemOfUnits ||--}o PhysicalConstant : "applicablePhysicalConstant"
SystemOfUnits ||--}o Prefix : "prefix"
SystemOfUnits ||--}o Unit : "hasAllowedUnit"
SystemOfUnits ||--}o Unit : "hasBaseUnit"
SystemOfUnits ||--}o Unit : "hasCoherentUnit"
SystemOfUnits ||--}o Unit : "hasDefinedUnit"
SystemOfUnits ||--}o Unit : "hasDerivedCoherentUnit"
SystemOfUnits ||--}o Unit : "hasDerivedUnit"
SystemOfUnits ||--}o Unit : "hasUnit"
Unit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
Unit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
Unit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
Unit ||--}o Prefix : "prefix"
Unit ||--}o QuantityKind : "hasQuantityKind"
Unit ||--}o SystemOfUnits : "applicableSystem"
Unit ||--}o SystemOfUnits : "definedUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedUnitOfSystem"
Unit ||--}o SystemOfUnits : "isUnitOfSystem"
Unit ||--}o UCUMcs : "ucumCode"
Unit ||--}o Unit : "exactMatch"
Unit ||--}o Unit : "hasReciprocalUnit"
Unit ||--}o Unit : "scalingOf"
Unit ||--}o __Class : "hasFactorUnit"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| hasReciprocalUnit | <sub>0..\*</sub> | [Unit](#Unit) |  |
| isUnitOfSystem | <sub>0..\*</sub> | [SystemOfUnits](#SystemOfUnits) |  |
| omUnit | <sub>0..\*</sub> | None |  |
| unitFor | <sub>0..\*</sub> | None |  |
| *id* | <sub>0..1</sub> | None |  |
| *guidance* | <sub>0..\*</sub> | string |  |

#### Parents

 * [Unit](#Unit)




### CountingUnit



Used for all units that express counts. Examples are Atomic Number, Number, Number per Year, Percent and Sample per Second.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
CountingUnit:
  is_a: DimensionlessUnit
  slots:
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

```mermaid
erDiagram
CountingUnit {

}
Prefix {

}
QuantityKind {

}
QuantityKindDimensionVector {

}
Rule {

}
SystemOfUnits {

}
UCUMcs {

}
Unit {

}
__Class {

}

CountingUnit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
CountingUnit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
CountingUnit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
CountingUnit ||--}o Prefix : "prefix"
CountingUnit ||--}o QuantityKind : "hasQuantityKind"
CountingUnit ||--}o SystemOfUnits : "applicableSystem"
CountingUnit ||--}o SystemOfUnits : "definedUnitOfSystem"
CountingUnit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
CountingUnit ||--}o SystemOfUnits : "derivedUnitOfSystem"
CountingUnit ||--}o SystemOfUnits : "isUnitOfSystem"
CountingUnit ||--}o UCUMcs : "ucumCode"
CountingUnit ||--}o Unit : "exactMatch"
CountingUnit ||--}o Unit : "hasReciprocalUnit"
CountingUnit ||--}o Unit : "scalingOf"
CountingUnit ||--}o __Class : "hasFactorUnit"
Prefix ||--}o Prefix : "exactMatch"
Prefix ||--}o UCUMcs-term : "ucumCode"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvDenominator"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvNumerator"
QuantityKind ||--|o QuantityKindDimensionVectorSI : "dimensionVectorForSI"
QuantityKind ||--}o QuantityKind : "exactMatch"
QuantityKind ||--}o QuantityKindDimensionVector : "hasDimensionVector"
QuantityKind ||--}o SystemOfQuantityKinds : "belongsToSystemOfQuantities"
QuantityKind ||--}o Unit : "applicableCGSUnit"
QuantityKind ||--}o Unit : "applicableISOUnit"
QuantityKind ||--}o Unit : "applicableImperialUnit"
QuantityKind ||--}o Unit : "applicableSIUnit"
QuantityKind ||--}o Unit : "applicableUSCustomaryUnit"
QuantityKind ||--}o Unit : "applicableUnit"
QuantityKindDimensionVector ||--}o QuantityKind : "hasReferenceQuantityKind"
QuantityKindDimensionVector ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"
SystemOfUnits ||--}o PhysicalConstant : "applicablePhysicalConstant"
SystemOfUnits ||--}o Prefix : "prefix"
SystemOfUnits ||--}o Unit : "hasAllowedUnit"
SystemOfUnits ||--}o Unit : "hasBaseUnit"
SystemOfUnits ||--}o Unit : "hasCoherentUnit"
SystemOfUnits ||--}o Unit : "hasDefinedUnit"
SystemOfUnits ||--}o Unit : "hasDerivedCoherentUnit"
SystemOfUnits ||--}o Unit : "hasDerivedUnit"
SystemOfUnits ||--}o Unit : "hasUnit"
Unit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
Unit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
Unit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
Unit ||--}o Prefix : "prefix"
Unit ||--}o QuantityKind : "hasQuantityKind"
Unit ||--}o SystemOfUnits : "applicableSystem"
Unit ||--}o SystemOfUnits : "definedUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedUnitOfSystem"
Unit ||--}o SystemOfUnits : "isUnitOfSystem"
Unit ||--}o UCUMcs : "ucumCode"
Unit ||--}o Unit : "exactMatch"
Unit ||--}o Unit : "hasReciprocalUnit"
Unit ||--}o Unit : "scalingOf"
Unit ||--}o __Class : "hasFactorUnit"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| hasReciprocalUnit | <sub>0..\*</sub> | [Unit](#Unit) |  |
| isUnitOfSystem | <sub>0..\*</sub> | [SystemOfUnits](#SystemOfUnits) |  |
| omUnit | <sub>0..\*</sub> | None |  |
| unitFor | <sub>0..\*</sub> | None |  |
| *id* | <sub>0..1</sub> | None |  |
| *guidance* | <sub>0..\*</sub> | string |  |

#### Parents

 * [DimensionlessUnit](#DimensionlessUnit)




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

```mermaid
erDiagram
CurrencyUnit {

}
Prefix {

}
QuantityKind {

}
QuantityKindDimensionVector {

}
Rule {

}
SystemOfUnits {

}
UCUMcs {

}
Unit {

}
__Class {

}

CurrencyUnit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
CurrencyUnit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
CurrencyUnit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
CurrencyUnit ||--}o Prefix : "prefix"
CurrencyUnit ||--}o QuantityKind : "hasQuantityKind"
CurrencyUnit ||--}o SystemOfUnits : "applicableSystem"
CurrencyUnit ||--}o SystemOfUnits : "definedUnitOfSystem"
CurrencyUnit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
CurrencyUnit ||--}o SystemOfUnits : "derivedUnitOfSystem"
CurrencyUnit ||--}o SystemOfUnits : "isUnitOfSystem"
CurrencyUnit ||--}o UCUMcs : "ucumCode"
CurrencyUnit ||--}o Unit : "exactMatch"
CurrencyUnit ||--}o Unit : "hasReciprocalUnit"
CurrencyUnit ||--}o Unit : "scalingOf"
CurrencyUnit ||--}o __Class : "hasFactorUnit"
Prefix ||--}o Prefix : "exactMatch"
Prefix ||--}o UCUMcs-term : "ucumCode"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvDenominator"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvNumerator"
QuantityKind ||--|o QuantityKindDimensionVectorSI : "dimensionVectorForSI"
QuantityKind ||--}o QuantityKind : "exactMatch"
QuantityKind ||--}o QuantityKindDimensionVector : "hasDimensionVector"
QuantityKind ||--}o SystemOfQuantityKinds : "belongsToSystemOfQuantities"
QuantityKind ||--}o Unit : "applicableCGSUnit"
QuantityKind ||--}o Unit : "applicableISOUnit"
QuantityKind ||--}o Unit : "applicableImperialUnit"
QuantityKind ||--}o Unit : "applicableSIUnit"
QuantityKind ||--}o Unit : "applicableUSCustomaryUnit"
QuantityKind ||--}o Unit : "applicableUnit"
QuantityKindDimensionVector ||--}o QuantityKind : "hasReferenceQuantityKind"
QuantityKindDimensionVector ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"
SystemOfUnits ||--}o PhysicalConstant : "applicablePhysicalConstant"
SystemOfUnits ||--}o Prefix : "prefix"
SystemOfUnits ||--}o Unit : "hasAllowedUnit"
SystemOfUnits ||--}o Unit : "hasBaseUnit"
SystemOfUnits ||--}o Unit : "hasCoherentUnit"
SystemOfUnits ||--}o Unit : "hasDefinedUnit"
SystemOfUnits ||--}o Unit : "hasDerivedCoherentUnit"
SystemOfUnits ||--}o Unit : "hasDerivedUnit"
SystemOfUnits ||--}o Unit : "hasUnit"
Unit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
Unit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
Unit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
Unit ||--}o Prefix : "prefix"
Unit ||--}o QuantityKind : "hasQuantityKind"
Unit ||--}o SystemOfUnits : "applicableSystem"
Unit ||--}o SystemOfUnits : "definedUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedUnitOfSystem"
Unit ||--}o SystemOfUnits : "isUnitOfSystem"
Unit ||--}o UCUMcs : "ucumCode"
Unit ||--}o Unit : "exactMatch"
Unit ||--}o Unit : "hasReciprocalUnit"
Unit ||--}o Unit : "scalingOf"
Unit ||--}o __Class : "hasFactorUnit"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| hasReciprocalUnit | <sub>0..\*</sub> | [Unit](#Unit) |  |
| isUnitOfSystem | <sub>0..\*</sub> | [SystemOfUnits](#SystemOfUnits) |  |
| omUnit | <sub>0..\*</sub> | None |  |
| unitFor | <sub>0..\*</sub> | None |  |
| *id* | <sub>0..1</sub> | None |  |
| *guidance* | <sub>0..\*</sub> | string |  |

#### Parents

 * [DimensionlessUnit](#DimensionlessUnit)




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

```mermaid
erDiagram
DataEncoding {

}
Encoding {

}
EndianType {

}
Quantifiable {

}

DataEncoding ||--|o Encoding : "encoding"
DataEncoding ||--|o EndianType : "bitOrder"
DataEncoding ||--|o EndianType : "byteOrder"
Encoding ||--}o Rule : "hasRule"
Quantifiable ||--|o DataEncoding : "dataEncoding"
Quantifiable ||--|o Datatype : "datatype"
Quantifiable ||--|o Unit : "hasUnit"

```


This class has no attributes


#### Parents

 * [Aspect](#Aspect)

#### Referenced by:

 *  **[Quantifiable](#Quantifiable)** : *[Quantifiable_dataEncoding](#Quantifiable_dataEncoding)*  <sub>0..\*</sub> 




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

```mermaid
erDiagram
DataItem {

}
Rule {

}

DataItem ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [Concept](#Concept)




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

```mermaid
erDiagram
CardinalityType {

}
Datatype {

}
OrderedType {

}
Quantifiable {

}
Rule {

}
ScalarDatatype {

}

Datatype ||--|o CardinalityType : "cardinality"
Datatype ||--|o Datatype : "basis"
Datatype ||--|o OrderedType : "orderedType"
Datatype ||--}o Rule : "hasRule"
Quantifiable ||--|o DataEncoding : "dataEncoding"
Quantifiable ||--|o Datatype : "datatype"
Quantifiable ||--|o Unit : "hasUnit"
Rule ||--}o RuleType : "ruleType"
ScalarDatatype ||--|o CardinalityType : "cardinality"
ScalarDatatype ||--|o Datatype : "basis"
ScalarDatatype ||--|o Datatype : "rdfsDatatype"
ScalarDatatype ||--|o OrderedType : "orderedType"
ScalarDatatype ||--}o Rule : "hasRule"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [Concept](#Concept)

#### Children

 * [ScalarDatatype](#ScalarDatatype)

#### Referenced by:

 *  **[Datatype](#Datatype)** : *[Datatype_basis](#Datatype_basis)*  <sub>0..\*</sub> 
 *  **[Quantifiable](#Quantifiable)** : *[Quantifiable_datatype](#Quantifiable_datatype)*  <sub>0..\*</sub> 
 *  **[ScalarDatatype](#ScalarDatatype)** : *[ScalarDatatype_rdfsDatatype](#ScalarDatatype_rdfsDatatype)*  <sub>0..\*</sub> 




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

```mermaid
classDiagram
StringEncodingType <|-- DateTimeStringEncodingType

```

This class has no attributes


#### Parents

 * [StringEncodingType](#StringEncodingType)




### DecimalPrefix



A <em>Decimal Prefix</em> is a prefix for multiples of units that are powers of 10.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
DecimalPrefix:
  is_a: Prefix
  slots:
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

```mermaid
erDiagram
DecimalPrefix {

}
Prefix {

}
Rule {

}
UCUMcs-term {

}

DecimalPrefix ||--}o Prefix : "exactMatch"
DecimalPrefix ||--}o UCUMcs-term : "ucumCode"
Prefix ||--}o Prefix : "exactMatch"
Prefix ||--}o UCUMcs-term : "ucumCode"
Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| *id* | <sub>0..1</sub> | None |  |
| *guidance* | <sub>0..\*</sub> | string |  |

#### Parents

 * [Prefix](#Prefix)




### DerivedUnit



A DerivedUnit is a type specification for units that are derived from other units.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
DerivedUnit:
  is_a: Unit
  slots:
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

```mermaid
erDiagram
DerivedUnit {

}
Prefix {

}
QuantityKind {

}
QuantityKindDimensionVector {

}
Rule {

}
SystemOfUnits {

}
UCUMcs {

}
Unit {

}
__Class {

}

DerivedUnit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
DerivedUnit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
DerivedUnit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
DerivedUnit ||--}o Prefix : "prefix"
DerivedUnit ||--}o QuantityKind : "hasQuantityKind"
DerivedUnit ||--}o SystemOfUnits : "applicableSystem"
DerivedUnit ||--}o SystemOfUnits : "definedUnitOfSystem"
DerivedUnit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
DerivedUnit ||--}o SystemOfUnits : "derivedUnitOfSystem"
DerivedUnit ||--}o SystemOfUnits : "isUnitOfSystem"
DerivedUnit ||--}o UCUMcs : "ucumCode"
DerivedUnit ||--}o Unit : "exactMatch"
DerivedUnit ||--}o Unit : "hasReciprocalUnit"
DerivedUnit ||--}o Unit : "scalingOf"
DerivedUnit ||--}o __Class : "hasFactorUnit"
Prefix ||--}o Prefix : "exactMatch"
Prefix ||--}o UCUMcs-term : "ucumCode"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvDenominator"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvNumerator"
QuantityKind ||--|o QuantityKindDimensionVectorSI : "dimensionVectorForSI"
QuantityKind ||--}o QuantityKind : "exactMatch"
QuantityKind ||--}o QuantityKindDimensionVector : "hasDimensionVector"
QuantityKind ||--}o SystemOfQuantityKinds : "belongsToSystemOfQuantities"
QuantityKind ||--}o Unit : "applicableCGSUnit"
QuantityKind ||--}o Unit : "applicableISOUnit"
QuantityKind ||--}o Unit : "applicableImperialUnit"
QuantityKind ||--}o Unit : "applicableSIUnit"
QuantityKind ||--}o Unit : "applicableUSCustomaryUnit"
QuantityKind ||--}o Unit : "applicableUnit"
QuantityKindDimensionVector ||--}o QuantityKind : "hasReferenceQuantityKind"
QuantityKindDimensionVector ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"
SystemOfUnits ||--}o PhysicalConstant : "applicablePhysicalConstant"
SystemOfUnits ||--}o Prefix : "prefix"
SystemOfUnits ||--}o Unit : "hasAllowedUnit"
SystemOfUnits ||--}o Unit : "hasBaseUnit"
SystemOfUnits ||--}o Unit : "hasCoherentUnit"
SystemOfUnits ||--}o Unit : "hasDefinedUnit"
SystemOfUnits ||--}o Unit : "hasDerivedCoherentUnit"
SystemOfUnits ||--}o Unit : "hasDerivedUnit"
SystemOfUnits ||--}o Unit : "hasUnit"
Unit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
Unit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
Unit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
Unit ||--}o Prefix : "prefix"
Unit ||--}o QuantityKind : "hasQuantityKind"
Unit ||--}o SystemOfUnits : "applicableSystem"
Unit ||--}o SystemOfUnits : "definedUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedUnitOfSystem"
Unit ||--}o SystemOfUnits : "isUnitOfSystem"
Unit ||--}o UCUMcs : "ucumCode"
Unit ||--}o Unit : "exactMatch"
Unit ||--}o Unit : "hasReciprocalUnit"
Unit ||--}o Unit : "scalingOf"
Unit ||--}o __Class : "hasFactorUnit"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| hasReciprocalUnit | <sub>0..\*</sub> | [Unit](#Unit) |  |
| isUnitOfSystem | <sub>0..\*</sub> | [SystemOfUnits](#SystemOfUnits) |  |
| omUnit | <sub>0..\*</sub> | None |  |
| unitFor | <sub>0..\*</sub> | None |  |
| *id* | <sub>0..1</sub> | None |  |
| *guidance* | <sub>0..\*</sub> | string |  |

#### Parents

 * [Unit](#Unit)




### DimensionlessUnit



A Dimensionless Unit is a quantity for which all the exponents of the factors corresponding to the base quantities in its quantity dimension are zero.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
DimensionlessUnit:
  is_a: Unit
  slots:
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

```mermaid
erDiagram
DimensionlessUnit {

}
Prefix {

}
QuantityKind {

}
QuantityKindDimensionVector {

}
Rule {

}
SystemOfUnits {

}
UCUMcs {

}
Unit {

}
__Class {

}

DimensionlessUnit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
DimensionlessUnit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
DimensionlessUnit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
DimensionlessUnit ||--}o Prefix : "prefix"
DimensionlessUnit ||--}o QuantityKind : "hasQuantityKind"
DimensionlessUnit ||--}o SystemOfUnits : "applicableSystem"
DimensionlessUnit ||--}o SystemOfUnits : "definedUnitOfSystem"
DimensionlessUnit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
DimensionlessUnit ||--}o SystemOfUnits : "derivedUnitOfSystem"
DimensionlessUnit ||--}o SystemOfUnits : "isUnitOfSystem"
DimensionlessUnit ||--}o UCUMcs : "ucumCode"
DimensionlessUnit ||--}o Unit : "exactMatch"
DimensionlessUnit ||--}o Unit : "hasReciprocalUnit"
DimensionlessUnit ||--}o Unit : "scalingOf"
DimensionlessUnit ||--}o __Class : "hasFactorUnit"
Prefix ||--}o Prefix : "exactMatch"
Prefix ||--}o UCUMcs-term : "ucumCode"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvDenominator"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvNumerator"
QuantityKind ||--|o QuantityKindDimensionVectorSI : "dimensionVectorForSI"
QuantityKind ||--}o QuantityKind : "exactMatch"
QuantityKind ||--}o QuantityKindDimensionVector : "hasDimensionVector"
QuantityKind ||--}o SystemOfQuantityKinds : "belongsToSystemOfQuantities"
QuantityKind ||--}o Unit : "applicableCGSUnit"
QuantityKind ||--}o Unit : "applicableISOUnit"
QuantityKind ||--}o Unit : "applicableImperialUnit"
QuantityKind ||--}o Unit : "applicableSIUnit"
QuantityKind ||--}o Unit : "applicableUSCustomaryUnit"
QuantityKind ||--}o Unit : "applicableUnit"
QuantityKindDimensionVector ||--}o QuantityKind : "hasReferenceQuantityKind"
QuantityKindDimensionVector ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"
SystemOfUnits ||--}o PhysicalConstant : "applicablePhysicalConstant"
SystemOfUnits ||--}o Prefix : "prefix"
SystemOfUnits ||--}o Unit : "hasAllowedUnit"
SystemOfUnits ||--}o Unit : "hasBaseUnit"
SystemOfUnits ||--}o Unit : "hasCoherentUnit"
SystemOfUnits ||--}o Unit : "hasDefinedUnit"
SystemOfUnits ||--}o Unit : "hasDerivedCoherentUnit"
SystemOfUnits ||--}o Unit : "hasDerivedUnit"
SystemOfUnits ||--}o Unit : "hasUnit"
Unit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
Unit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
Unit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
Unit ||--}o Prefix : "prefix"
Unit ||--}o QuantityKind : "hasQuantityKind"
Unit ||--}o SystemOfUnits : "applicableSystem"
Unit ||--}o SystemOfUnits : "definedUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedUnitOfSystem"
Unit ||--}o SystemOfUnits : "isUnitOfSystem"
Unit ||--}o UCUMcs : "ucumCode"
Unit ||--}o Unit : "exactMatch"
Unit ||--}o Unit : "hasReciprocalUnit"
Unit ||--}o Unit : "scalingOf"
Unit ||--}o __Class : "hasFactorUnit"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| hasReciprocalUnit | <sub>0..\*</sub> | [Unit](#Unit) |  |
| isUnitOfSystem | <sub>0..\*</sub> | [SystemOfUnits](#SystemOfUnits) |  |
| omUnit | <sub>0..\*</sub> | None |  |
| unitFor | <sub>0..\*</sub> | None |  |
| *id* | <sub>0..1</sub> | None |  |
| *guidance* | <sub>0..\*</sub> | string |  |

#### Parents

 * [Unit](#Unit)

#### Children

 * [AngleUnit](#AngleUnit)
 * [CountingUnit](#CountingUnit)
 * [CurrencyUnit](#CurrencyUnit)
 * [LogarithmicUnit](#LogarithmicUnit)




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

```mermaid
erDiagram
Discipline {

}
Rule {

}

Discipline ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [Concept](#Concept)




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

```mermaid
erDiagram
DataEncoding {

}
Encoding {

}
Rule {

}

DataEncoding ||--|o Encoding : "encoding"
DataEncoding ||--|o EndianType : "bitOrder"
DataEncoding ||--|o EndianType : "byteOrder"
Encoding ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [Concept](#Concept)

#### Children

 * [BitEncodingType](#BitEncodingType)
 * [BooleanEncodingType](#BooleanEncodingType)
 * [ByteEncodingType](#ByteEncodingType)
 * [CharEncodingType](#CharEncodingType)
 * [FloatingPointEncodingType](#FloatingPointEncodingType)
 * [IntegerEncodingType](#IntegerEncodingType)

#### Referenced by:

 *  **[DataEncoding](#DataEncoding)** : *[DataEncoding_encoding](#DataEncoding_encoding)*  <sub>0..\*</sub> 




### EndianType




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
EndianType:
  is_a: EnumeratedValue
  slots:
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

```mermaid
erDiagram
DataEncoding {

}
EndianType {

}
Rule {

}

DataEncoding ||--|o Encoding : "encoding"
DataEncoding ||--|o EndianType : "bitOrder"
DataEncoding ||--|o EndianType : "byteOrder"
Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| *id* | <sub>0..1</sub> | None |  |
| *guidance* | <sub>0..\*</sub> | string |  |

#### Parents

 * [EnumeratedValue](#EnumeratedValue)

#### Referenced by:

 *  **[DataEncoding](#DataEncoding)** : *[DataEncoding_bitOrder](#DataEncoding_bitOrder)*  <sub>0..\*</sub> 
 *  **[DataEncoding](#DataEncoding)** : *[DataEncoding_byteOrder](#DataEncoding_byteOrder)*  <sub>0..\*</sub> 




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

```mermaid
erDiagram
EnumeratedQuantity {

}
EnumeratedValue {

}
Enumeration {

}
Rule {

}

EnumeratedQuantity ||--}o EnumeratedValue : "enumeratedValue"
EnumeratedQuantity ||--}o Enumeration : "enumeration"
EnumeratedQuantity ||--}o Rule : "hasRule"
Enumeration ||--|o EnumeratedValue : "default"
Enumeration ||--}o Rule : "hasRule"
Enumeration ||--}| EnumeratedValue : "element"
Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [Concept](#Concept)




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

```mermaid
erDiagram
EnumeratedQuantity {

}
EnumeratedValue {

}
Enumeration {

}
Rule {

}

EnumeratedQuantity ||--}o EnumeratedValue : "enumeratedValue"
EnumeratedQuantity ||--}o Enumeration : "enumeration"
EnumeratedQuantity ||--}o Rule : "hasRule"
Enumeration ||--|o EnumeratedValue : "default"
Enumeration ||--}o Rule : "hasRule"
Enumeration ||--}| EnumeratedValue : "element"
Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| *id* | <sub>0..1</sub> | None |  |
| *guidance* | <sub>0..\*</sub> | string |  |

#### Parents

 * [Verifiable](#Verifiable)

#### Children

 * [CardinalityType](#CardinalityType)
 * [EndianType](#EndianType)
 * [OrderedType](#OrderedType)
 * [QuantityType](#QuantityType)
 * [RuleType](#RuleType)
 * [ScaleType](#ScaleType)
 * [TransformType](#TransformType)

#### Uses

 *  mixin: [Concept](#Concept)

#### Referenced by:

 *  **[EnumeratedQuantity](#EnumeratedQuantity)** : *[EnumeratedQuantity_enumeratedValue](#EnumeratedQuantity_enumeratedValue)*  <sub>0..\*</sub> 
 *  **[Enumeration](#Enumeration)** : *[Enumeration_default](#Enumeration_default)*  <sub>0..\*</sub> 
 *  **[Enumeration](#Enumeration)** : *[Enumeration_element](#Enumeration_element)*  <sub>1..\*</sub> 




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

```mermaid
erDiagram
EnumeratedQuantity {

}
EnumeratedValue {

}
Enumeration {

}
Rule {

}
SystemOfQuantityKinds {

}

EnumeratedQuantity ||--}o EnumeratedValue : "enumeratedValue"
EnumeratedQuantity ||--}o Enumeration : "enumeration"
EnumeratedQuantity ||--}o Rule : "hasRule"
Enumeration ||--|o EnumeratedValue : "default"
Enumeration ||--}o Rule : "hasRule"
Enumeration ||--}| EnumeratedValue : "element"
Rule ||--}o RuleType : "ruleType"
SystemOfQuantityKinds ||--|o Enumeration : "baseDimensionEnumeration"
SystemOfQuantityKinds ||--}o QuantityKind : "hasBaseQuantityKind"
SystemOfQuantityKinds ||--}o QuantityKind : "hasQuantityKind"
SystemOfQuantityKinds ||--}o QuantityKind : "systemDerivedQuantityKind"
SystemOfQuantityKinds ||--}o Rule : "hasRule"
SystemOfQuantityKinds ||--}o SystemOfUnits : "hasUnitSystem"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [Concept](#Concept)

#### Used as mixin by

 * [EnumerationScale](#EnumerationScale)

#### Referenced by:

 *  **[EnumeratedQuantity](#EnumeratedQuantity)** : *[EnumeratedQuantity_enumeration](#EnumeratedQuantity_enumeration)*  <sub>0..\*</sub> 
 *  **[SystemOfQuantityKinds](#SystemOfQuantityKinds)** : *[SystemOfQuantityKinds_baseDimensionEnumeration](#SystemOfQuantityKinds_baseDimensionEnumeration)*  <sub>0..\*</sub> 




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

```mermaid
erDiagram
EnumeratedValue {

}
EnumerationScale {

}
MathsFunctionType {

}
Rule {

}
ScaleType {

}
TransformType {

}

EnumerationScale ||--|o ScaleType : "scaleType"
EnumerationScale ||--}o MathsFunctionType : "permissibleMaths"
EnumerationScale ||--}o Rule : "hasRule"
EnumerationScale ||--}o TransformType : "permissibleTransformation"
MathsFunctionType ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"
ScaleType ||--}o MathsFunctionType : "permissibleMaths"
ScaleType ||--}o TransformType : "permissibleTransformation"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [Scale](#Scale)

#### Uses

 *  mixin: [Enumeration](#Enumeration)




### Error1




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
Error1: {}

```
</details>


This class has no attributes


#### Used as mixin by

 * [PhysicalConstant](#PhysicalConstant)




### Error2




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
Error2: {}

```
</details>


This class has no attributes


#### Used as mixin by

 * [Verifiable](#Verifiable)




### Error3




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
Error3: {}

```
</details>


#### Local class diagram

```mermaid
classDiagram
Error3 <|-- Verifiable

```

This class has no attributes


#### Children

 * [Verifiable](#Verifiable)




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

```mermaid
erDiagram
Figure {

}
Rule {

}

Figure ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [Concept](#Concept)

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

```mermaid
erDiagram
FloatingPointEncodingType {

}
Rule {

}

FloatingPointEncodingType ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [Encoding](#Encoding)




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

```mermaid
erDiagram
IntegerEncodingType {

}
Rule {

}

IntegerEncodingType ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [Encoding](#Encoding)




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

```mermaid
erDiagram
IntervalScale {

}
MathsFunctionType {

}
Rule {

}
ScaleType {

}
TransformType {

}

IntervalScale ||--|o ScaleType : "scaleType"
IntervalScale ||--}o MathsFunctionType : "permissibleMaths"
IntervalScale ||--}o Rule : "hasRule"
IntervalScale ||--}o TransformType : "permissibleTransformation"
MathsFunctionType ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"
ScaleType ||--}o MathsFunctionType : "permissibleMaths"
ScaleType ||--}o TransformType : "permissibleTransformation"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [Scale](#Scale)




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

```mermaid
erDiagram
LogarithmicUnit {

}
Prefix {

}
QuantityKind {

}
QuantityKindDimensionVector {

}
Rule {

}
SystemOfUnits {

}
UCUMcs {

}
Unit {

}
__Class {

}

LogarithmicUnit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
LogarithmicUnit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
LogarithmicUnit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
LogarithmicUnit ||--}o Prefix : "prefix"
LogarithmicUnit ||--}o QuantityKind : "hasQuantityKind"
LogarithmicUnit ||--}o SystemOfUnits : "applicableSystem"
LogarithmicUnit ||--}o SystemOfUnits : "definedUnitOfSystem"
LogarithmicUnit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
LogarithmicUnit ||--}o SystemOfUnits : "derivedUnitOfSystem"
LogarithmicUnit ||--}o SystemOfUnits : "isUnitOfSystem"
LogarithmicUnit ||--}o UCUMcs : "ucumCode"
LogarithmicUnit ||--}o Unit : "exactMatch"
LogarithmicUnit ||--}o Unit : "hasReciprocalUnit"
LogarithmicUnit ||--}o Unit : "scalingOf"
LogarithmicUnit ||--}o __Class : "hasFactorUnit"
Prefix ||--}o Prefix : "exactMatch"
Prefix ||--}o UCUMcs-term : "ucumCode"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvDenominator"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvNumerator"
QuantityKind ||--|o QuantityKindDimensionVectorSI : "dimensionVectorForSI"
QuantityKind ||--}o QuantityKind : "exactMatch"
QuantityKind ||--}o QuantityKindDimensionVector : "hasDimensionVector"
QuantityKind ||--}o SystemOfQuantityKinds : "belongsToSystemOfQuantities"
QuantityKind ||--}o Unit : "applicableCGSUnit"
QuantityKind ||--}o Unit : "applicableISOUnit"
QuantityKind ||--}o Unit : "applicableImperialUnit"
QuantityKind ||--}o Unit : "applicableSIUnit"
QuantityKind ||--}o Unit : "applicableUSCustomaryUnit"
QuantityKind ||--}o Unit : "applicableUnit"
QuantityKindDimensionVector ||--}o QuantityKind : "hasReferenceQuantityKind"
QuantityKindDimensionVector ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"
SystemOfUnits ||--}o PhysicalConstant : "applicablePhysicalConstant"
SystemOfUnits ||--}o Prefix : "prefix"
SystemOfUnits ||--}o Unit : "hasAllowedUnit"
SystemOfUnits ||--}o Unit : "hasBaseUnit"
SystemOfUnits ||--}o Unit : "hasCoherentUnit"
SystemOfUnits ||--}o Unit : "hasDefinedUnit"
SystemOfUnits ||--}o Unit : "hasDerivedCoherentUnit"
SystemOfUnits ||--}o Unit : "hasDerivedUnit"
SystemOfUnits ||--}o Unit : "hasUnit"
Unit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
Unit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
Unit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
Unit ||--}o Prefix : "prefix"
Unit ||--}o QuantityKind : "hasQuantityKind"
Unit ||--}o SystemOfUnits : "applicableSystem"
Unit ||--}o SystemOfUnits : "definedUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedUnitOfSystem"
Unit ||--}o SystemOfUnits : "isUnitOfSystem"
Unit ||--}o UCUMcs : "ucumCode"
Unit ||--}o Unit : "exactMatch"
Unit ||--}o Unit : "hasReciprocalUnit"
Unit ||--}o Unit : "scalingOf"
Unit ||--}o __Class : "hasFactorUnit"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| hasReciprocalUnit | <sub>0..\*</sub> | [Unit](#Unit) |  |
| isUnitOfSystem | <sub>0..\*</sub> | [SystemOfUnits](#SystemOfUnits) |  |
| omUnit | <sub>0..\*</sub> | None |  |
| unitFor | <sub>0..\*</sub> | None |  |
| *id* | <sub>0..1</sub> | None |  |
| *guidance* | <sub>0..\*</sub> | string |  |

#### Parents

 * [DimensionlessUnit](#DimensionlessUnit)




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

```mermaid
erDiagram
MathsFunctionType {

}
Rule {

}
Scale {

}
ScaleType {

}

MathsFunctionType ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"
Scale ||--|o ScaleType : "scaleType"
Scale ||--}o MathsFunctionType : "permissibleMaths"
Scale ||--}o Rule : "hasRule"
Scale ||--}o TransformType : "permissibleTransformation"
ScaleType ||--}o MathsFunctionType : "permissibleMaths"
ScaleType ||--}o TransformType : "permissibleTransformation"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [Concept](#Concept)

#### Referenced by:

 *  **[ScaleType](#ScaleType)** : *[ScaleType_permissibleMaths](#ScaleType_permissibleMaths)*  <sub>0..\*</sub> 
 *  **[Scale](#Scale)** : *[Scale_permissibleMaths](#Scale_permissibleMaths)*  <sub>0..\*</sub> 




### NIST_SP811_Comment




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
NIST_SP811_Comment:
  is_a: Comment
  slots:
  - Verifiable_isoNormativeReference
  - Verifiable_normativeReference
  - Comment_rationale
  - Comment_description

```
</details>


#### Local class diagram

```mermaid
classDiagram
Comment <|-- NIST_SP811_Comment
Error3 <|-- Verifiable
Verifiable <|-- Comment

```

This class has no attributes


#### Parents

 * [Comment](#Comment)




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

```mermaid
erDiagram
MathsFunctionType {

}
NominalScale {

}
Rule {

}
ScaleType {

}
TransformType {

}

MathsFunctionType ||--}o Rule : "hasRule"
NominalScale ||--|o ScaleType : "scaleType"
NominalScale ||--}o MathsFunctionType : "permissibleMaths"
NominalScale ||--}o Rule : "hasRule"
NominalScale ||--}o TransformType : "permissibleTransformation"
Rule ||--}o RuleType : "ruleType"
ScaleType ||--}o MathsFunctionType : "permissibleMaths"
ScaleType ||--}o TransformType : "permissibleTransformation"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [Scale](#Scale)




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

```mermaid
erDiagram
NumericUnion {

}
Rule {

}

Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| *id* | <sub>0..1</sub> | None |  |
| *guidance* | <sub>0..\*</sub> | string |  |

#### Uses

 *  mixin: [Concept](#Concept)

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

```mermaid
erDiagram
Datatype {

}
OrderedType {

}
Rule {

}

Datatype ||--|o CardinalityType : "cardinality"
Datatype ||--|o Datatype : "basis"
Datatype ||--|o OrderedType : "orderedType"
Datatype ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| *id* | <sub>0..1</sub> | None |  |
| *guidance* | <sub>0..\*</sub> | string |  |

#### Parents

 * [EnumeratedValue](#EnumeratedValue)

#### Referenced by:

 *  **[Datatype](#Datatype)** : *[Datatype_orderedType](#Datatype_orderedType)*  <sub>0..\*</sub> 




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

```mermaid
erDiagram
MathsFunctionType {

}
OrdinalScale {

}
Rule {

}
ScaleType {

}
TransformType {

}

MathsFunctionType ||--}o Rule : "hasRule"
OrdinalScale ||--|o ScaleType : "scaleType"
OrdinalScale ||--}o MathsFunctionType : "permissibleMaths"
OrdinalScale ||--}o Rule : "hasRule"
OrdinalScale ||--}o TransformType : "permissibleTransformation"
Rule ||--}o RuleType : "ruleType"
ScaleType ||--}o MathsFunctionType : "permissibleMaths"
ScaleType ||--}o TransformType : "permissibleTransformation"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [Scale](#Scale)




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

```mermaid
erDiagram
Organization {

}
Rule {

}

Organization ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [Concept](#Concept)




### PhysicalConstant



A physical constant is a physical quantity that is generally believed to be both universal in nature and constant in time. It can be contrasted with a mathematical constant, which is a fixed numerical value but does not directly involve any physical measurement. There are many physical constants in science, some of the most widely recognized being the speed of light in vacuum c, Newton's gravitational constant G, Planck's constant h, the electric permittivity of free space ε0, and the elementary charge e. Physical constants can take many dimensional forms, or may be dimensionless depending on the system of quantities and units used.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
PhysicalConstant:
  is_a: Quantity
  mixins:
  - Error1
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

```mermaid
erDiagram
DataEncoding {

}
Datatype {

}
PhysicalConstant {

}
QuantityKind {

}
QuantityKindDimensionVector {

}
QuantityValue {

}
Rule {

}
SystemOfUnits {

}
Unit {

}

DataEncoding ||--|o Encoding : "encoding"
DataEncoding ||--|o EndianType : "bitOrder"
DataEncoding ||--|o EndianType : "byteOrder"
Datatype ||--|o CardinalityType : "cardinality"
Datatype ||--|o Datatype : "basis"
Datatype ||--|o OrderedType : "orderedType"
Datatype ||--}o Rule : "hasRule"
PhysicalConstant ||--|o DataEncoding : "dataEncoding"
PhysicalConstant ||--|o Datatype : "datatype"
PhysicalConstant ||--|o Unit : "hasUnit"
PhysicalConstant ||--}o PhysicalConstant : "exactMatch"
PhysicalConstant ||--}o QuantityKind : "hasQuantityKind"
PhysicalConstant ||--}o QuantityKindDimensionVector : "hasDimensionVector"
PhysicalConstant ||--}o QuantityValue : "quantityValue"
PhysicalConstant ||--}o SystemOfUnits : "applicableSystem"
PhysicalConstant ||--}o Unit : "applicableUnit"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvDenominator"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvNumerator"
QuantityKind ||--|o QuantityKindDimensionVectorSI : "dimensionVectorForSI"
QuantityKind ||--}o QuantityKind : "exactMatch"
QuantityKind ||--}o QuantityKindDimensionVector : "hasDimensionVector"
QuantityKind ||--}o SystemOfQuantityKinds : "belongsToSystemOfQuantities"
QuantityKind ||--}o Unit : "applicableCGSUnit"
QuantityKind ||--}o Unit : "applicableISOUnit"
QuantityKind ||--}o Unit : "applicableImperialUnit"
QuantityKind ||--}o Unit : "applicableSIUnit"
QuantityKind ||--}o Unit : "applicableUSCustomaryUnit"
QuantityKind ||--}o Unit : "applicableUnit"
QuantityKindDimensionVector ||--}o QuantityKind : "hasReferenceQuantityKind"
QuantityKindDimensionVector ||--}o Rule : "hasRule"
QuantityValue ||--|o DataEncoding : "dataEncoding"
QuantityValue ||--|o Datatype : "datatype"
QuantityValue ||--|o Unit : "hasUnit"
Rule ||--}o RuleType : "ruleType"
SystemOfUnits ||--}o PhysicalConstant : "applicablePhysicalConstant"
SystemOfUnits ||--}o Prefix : "prefix"
SystemOfUnits ||--}o Unit : "hasAllowedUnit"
SystemOfUnits ||--}o Unit : "hasBaseUnit"
SystemOfUnits ||--}o Unit : "hasCoherentUnit"
SystemOfUnits ||--}o Unit : "hasDefinedUnit"
SystemOfUnits ||--}o Unit : "hasDerivedCoherentUnit"
SystemOfUnits ||--}o Unit : "hasDerivedUnit"
SystemOfUnits ||--}o Unit : "hasUnit"
Unit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
Unit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
Unit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
Unit ||--}o Prefix : "prefix"
Unit ||--}o QuantityKind : "hasQuantityKind"
Unit ||--}o SystemOfUnits : "applicableSystem"
Unit ||--}o SystemOfUnits : "definedUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedUnitOfSystem"
Unit ||--}o SystemOfUnits : "isUnitOfSystem"
Unit ||--}o UCUMcs : "ucumCode"
Unit ||--}o Unit : "exactMatch"
Unit ||--}o Unit : "hasReciprocalUnit"
Unit ||--}o Unit : "scalingOf"
Unit ||--}o __Class : "hasFactorUnit"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| *id* | <sub>0..1</sub> | None |  |
| *guidance* | <sub>0..\*</sub> | string |  |

#### Parents

 * [Quantity](#Quantity)

#### Uses

 *  mixin: [Error1](#Error1)

#### Referenced by:

 *  **[PhysicalConstant](#PhysicalConstant)** : *[PhysicalConstant_exactMatch](#PhysicalConstant_exactMatch)*  <sub>0..\*</sub> 
 *  **[SystemOfUnits](#SystemOfUnits)** : *[SystemOfUnits_applicablePhysicalConstant](#SystemOfUnits_applicablePhysicalConstant)*  <sub>0..\*</sub> 




### PlaneAngleUnit




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
PlaneAngleUnit:
  is_a: AngleUnit
  slots:
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

```mermaid
erDiagram
PlaneAngleUnit {

}
Prefix {

}
QuantityKind {

}
QuantityKindDimensionVector {

}
Rule {

}
SystemOfUnits {

}
UCUMcs {

}
Unit {

}
__Class {

}

PlaneAngleUnit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
PlaneAngleUnit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
PlaneAngleUnit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
PlaneAngleUnit ||--}o Prefix : "prefix"
PlaneAngleUnit ||--}o QuantityKind : "hasQuantityKind"
PlaneAngleUnit ||--}o SystemOfUnits : "applicableSystem"
PlaneAngleUnit ||--}o SystemOfUnits : "definedUnitOfSystem"
PlaneAngleUnit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
PlaneAngleUnit ||--}o SystemOfUnits : "derivedUnitOfSystem"
PlaneAngleUnit ||--}o SystemOfUnits : "isUnitOfSystem"
PlaneAngleUnit ||--}o UCUMcs : "ucumCode"
PlaneAngleUnit ||--}o Unit : "exactMatch"
PlaneAngleUnit ||--}o Unit : "hasReciprocalUnit"
PlaneAngleUnit ||--}o Unit : "scalingOf"
PlaneAngleUnit ||--}o __Class : "hasFactorUnit"
Prefix ||--}o Prefix : "exactMatch"
Prefix ||--}o UCUMcs-term : "ucumCode"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvDenominator"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvNumerator"
QuantityKind ||--|o QuantityKindDimensionVectorSI : "dimensionVectorForSI"
QuantityKind ||--}o QuantityKind : "exactMatch"
QuantityKind ||--}o QuantityKindDimensionVector : "hasDimensionVector"
QuantityKind ||--}o SystemOfQuantityKinds : "belongsToSystemOfQuantities"
QuantityKind ||--}o Unit : "applicableCGSUnit"
QuantityKind ||--}o Unit : "applicableISOUnit"
QuantityKind ||--}o Unit : "applicableImperialUnit"
QuantityKind ||--}o Unit : "applicableSIUnit"
QuantityKind ||--}o Unit : "applicableUSCustomaryUnit"
QuantityKind ||--}o Unit : "applicableUnit"
QuantityKindDimensionVector ||--}o QuantityKind : "hasReferenceQuantityKind"
QuantityKindDimensionVector ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"
SystemOfUnits ||--}o PhysicalConstant : "applicablePhysicalConstant"
SystemOfUnits ||--}o Prefix : "prefix"
SystemOfUnits ||--}o Unit : "hasAllowedUnit"
SystemOfUnits ||--}o Unit : "hasBaseUnit"
SystemOfUnits ||--}o Unit : "hasCoherentUnit"
SystemOfUnits ||--}o Unit : "hasDefinedUnit"
SystemOfUnits ||--}o Unit : "hasDerivedCoherentUnit"
SystemOfUnits ||--}o Unit : "hasDerivedUnit"
SystemOfUnits ||--}o Unit : "hasUnit"
Unit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
Unit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
Unit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
Unit ||--}o Prefix : "prefix"
Unit ||--}o QuantityKind : "hasQuantityKind"
Unit ||--}o SystemOfUnits : "applicableSystem"
Unit ||--}o SystemOfUnits : "definedUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedUnitOfSystem"
Unit ||--}o SystemOfUnits : "isUnitOfSystem"
Unit ||--}o UCUMcs : "ucumCode"
Unit ||--}o Unit : "exactMatch"
Unit ||--}o Unit : "hasReciprocalUnit"
Unit ||--}o Unit : "scalingOf"
Unit ||--}o __Class : "hasFactorUnit"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| hasReciprocalUnit | <sub>0..\*</sub> | [Unit](#Unit) |  |
| isUnitOfSystem | <sub>0..\*</sub> | [SystemOfUnits](#SystemOfUnits) |  |
| omUnit | <sub>0..\*</sub> | None |  |
| unitFor | <sub>0..\*</sub> | None |  |
| *id* | <sub>0..1</sub> | None |  |
| *guidance* | <sub>0..\*</sub> | string |  |

#### Parents

 * [AngleUnit](#AngleUnit)




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

```mermaid
erDiagram
Prefix {

}
Rule {

}
SystemOfUnits {

}
UCUMcs-term {

}
Unit {

}

Prefix ||--}o Prefix : "exactMatch"
Prefix ||--}o UCUMcs-term : "ucumCode"
Rule ||--}o RuleType : "ruleType"
SystemOfUnits ||--}o PhysicalConstant : "applicablePhysicalConstant"
SystemOfUnits ||--}o Prefix : "prefix"
SystemOfUnits ||--}o Unit : "hasAllowedUnit"
SystemOfUnits ||--}o Unit : "hasBaseUnit"
SystemOfUnits ||--}o Unit : "hasCoherentUnit"
SystemOfUnits ||--}o Unit : "hasDefinedUnit"
SystemOfUnits ||--}o Unit : "hasDerivedCoherentUnit"
SystemOfUnits ||--}o Unit : "hasDerivedUnit"
SystemOfUnits ||--}o Unit : "hasUnit"
Unit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
Unit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
Unit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
Unit ||--}o Prefix : "prefix"
Unit ||--}o QuantityKind : "hasQuantityKind"
Unit ||--}o SystemOfUnits : "applicableSystem"
Unit ||--}o SystemOfUnits : "definedUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedUnitOfSystem"
Unit ||--}o SystemOfUnits : "isUnitOfSystem"
Unit ||--}o UCUMcs : "ucumCode"
Unit ||--}o Unit : "exactMatch"
Unit ||--}o Unit : "hasReciprocalUnit"
Unit ||--}o Unit : "scalingOf"
Unit ||--}o __Class : "hasFactorUnit"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| *id* | <sub>0..1</sub> | None |  |
| *guidance* | <sub>0..\*</sub> | string |  |

#### Parents

 * [Verifiable](#Verifiable)

#### Children

 * [BinaryPrefix](#BinaryPrefix)
 * [DecimalPrefix](#DecimalPrefix)

#### Uses

 *  mixin: [Concept](#Concept)

#### Referenced by:

 *  **[Prefix](#Prefix)** : *[Prefix_exactMatch](#Prefix_exactMatch)*  <sub>0..\*</sub> 
 *  **[SystemOfUnits](#SystemOfUnits)** : *[SystemOfUnits_prefix](#SystemOfUnits_prefix)*  <sub>0..\*</sub> 
 *  **[Unit](#Unit)** : *[Unit_prefix](#Unit_prefix)*  <sub>0..\*</sub> 




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

```mermaid
erDiagram
DataEncoding {

}
Datatype {

}
Quantifiable {

}
Unit {

}

DataEncoding ||--|o Encoding : "encoding"
DataEncoding ||--|o EndianType : "bitOrder"
DataEncoding ||--|o EndianType : "byteOrder"
Datatype ||--|o CardinalityType : "cardinality"
Datatype ||--|o Datatype : "basis"
Datatype ||--|o OrderedType : "orderedType"
Datatype ||--}o Rule : "hasRule"
Quantifiable ||--|o DataEncoding : "dataEncoding"
Quantifiable ||--|o Datatype : "datatype"
Quantifiable ||--|o Unit : "hasUnit"
Unit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
Unit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
Unit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
Unit ||--}o Prefix : "prefix"
Unit ||--}o QuantityKind : "hasQuantityKind"
Unit ||--}o SystemOfUnits : "applicableSystem"
Unit ||--}o SystemOfUnits : "definedUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedUnitOfSystem"
Unit ||--}o SystemOfUnits : "isUnitOfSystem"
Unit ||--}o UCUMcs : "ucumCode"
Unit ||--}o Unit : "exactMatch"
Unit ||--}o Unit : "hasReciprocalUnit"
Unit ||--}o Unit : "scalingOf"
Unit ||--}o __Class : "hasFactorUnit"

```


This class has no attributes


#### Parents

 * [Aspect](#Aspect)

#### Children

 * [Quantity](#Quantity)
 * [QuantityValue](#QuantityValue)




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

```mermaid
erDiagram
DataEncoding {

}
Datatype {

}
Quantity {

}
QuantityKind {

}
QuantityValue {

}
Rule {

}
Unit {

}

DataEncoding ||--|o Encoding : "encoding"
DataEncoding ||--|o EndianType : "bitOrder"
DataEncoding ||--|o EndianType : "byteOrder"
Datatype ||--|o CardinalityType : "cardinality"
Datatype ||--|o Datatype : "basis"
Datatype ||--|o OrderedType : "orderedType"
Datatype ||--}o Rule : "hasRule"
Quantity ||--|o DataEncoding : "dataEncoding"
Quantity ||--|o Datatype : "datatype"
Quantity ||--|o Unit : "hasUnit"
Quantity ||--}o QuantityKind : "hasQuantityKind"
Quantity ||--}o QuantityValue : "quantityValue"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvDenominator"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvNumerator"
QuantityKind ||--|o QuantityKindDimensionVectorSI : "dimensionVectorForSI"
QuantityKind ||--}o QuantityKind : "exactMatch"
QuantityKind ||--}o QuantityKindDimensionVector : "hasDimensionVector"
QuantityKind ||--}o SystemOfQuantityKinds : "belongsToSystemOfQuantities"
QuantityKind ||--}o Unit : "applicableCGSUnit"
QuantityKind ||--}o Unit : "applicableISOUnit"
QuantityKind ||--}o Unit : "applicableImperialUnit"
QuantityKind ||--}o Unit : "applicableSIUnit"
QuantityKind ||--}o Unit : "applicableUSCustomaryUnit"
QuantityKind ||--}o Unit : "applicableUnit"
QuantityValue ||--|o DataEncoding : "dataEncoding"
QuantityValue ||--|o Datatype : "datatype"
QuantityValue ||--|o Unit : "hasUnit"
Rule ||--}o RuleType : "ruleType"
Unit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
Unit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
Unit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
Unit ||--}o Prefix : "prefix"
Unit ||--}o QuantityKind : "hasQuantityKind"
Unit ||--}o SystemOfUnits : "applicableSystem"
Unit ||--}o SystemOfUnits : "definedUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedUnitOfSystem"
Unit ||--}o SystemOfUnits : "isUnitOfSystem"
Unit ||--}o UCUMcs : "ucumCode"
Unit ||--}o Unit : "exactMatch"
Unit ||--}o Unit : "hasReciprocalUnit"
Unit ||--}o Unit : "scalingOf"
Unit ||--}o __Class : "hasFactorUnit"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| *id* | <sub>0..1</sub> | None |  |
| *guidance* | <sub>0..\*</sub> | string |  |

#### Parents

 * [Quantifiable](#Quantifiable)

#### Children

 * [PhysicalConstant](#PhysicalConstant)

#### Uses

 *  mixin: [Concept](#Concept)

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

```mermaid
erDiagram
AbstractQuantityKind {

}
BaseDimensionMagnitude {

}
Quantity {

}
QuantityKind {

}
QuantityKindDimensionVector {

}
QuantityKindDimensionVectorSI {

}
QuantityType {

}
Rule {

}
SystemOfQuantityKinds {

}
Unit {

}
UserQuantityKind {

}

AbstractQuantityKind ||--}o Rule : "hasRule"
BaseDimensionMagnitude ||--|| QuantityKind : "hasBaseQuantityKind"
BaseDimensionMagnitude ||--}o Rule : "hasRule"
Quantity ||--|o DataEncoding : "dataEncoding"
Quantity ||--|o Datatype : "datatype"
Quantity ||--|o Unit : "hasUnit"
Quantity ||--}o QuantityKind : "hasQuantityKind"
Quantity ||--}o QuantityValue : "quantityValue"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvDenominator"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvNumerator"
QuantityKind ||--|o QuantityKindDimensionVectorSI : "dimensionVectorForSI"
QuantityKind ||--}o QuantityKind : "exactMatch"
QuantityKind ||--}o QuantityKindDimensionVector : "hasDimensionVector"
QuantityKind ||--}o SystemOfQuantityKinds : "belongsToSystemOfQuantities"
QuantityKind ||--}o Unit : "applicableCGSUnit"
QuantityKind ||--}o Unit : "applicableISOUnit"
QuantityKind ||--}o Unit : "applicableImperialUnit"
QuantityKind ||--}o Unit : "applicableSIUnit"
QuantityKind ||--}o Unit : "applicableUSCustomaryUnit"
QuantityKind ||--}o Unit : "applicableUnit"
QuantityKindDimensionVector ||--}o QuantityKind : "hasReferenceQuantityKind"
QuantityKindDimensionVector ||--}o Rule : "hasRule"
QuantityKindDimensionVectorSI ||--}o QuantityKind : "hasReferenceQuantityKind"
QuantityKindDimensionVectorSI ||--}o Rule : "hasRule"
QuantityType ||--}o QuantityKind : "value"
Rule ||--}o RuleType : "ruleType"
SystemOfQuantityKinds ||--|o Enumeration : "baseDimensionEnumeration"
SystemOfQuantityKinds ||--}o QuantityKind : "hasBaseQuantityKind"
SystemOfQuantityKinds ||--}o QuantityKind : "hasQuantityKind"
SystemOfQuantityKinds ||--}o QuantityKind : "systemDerivedQuantityKind"
SystemOfQuantityKinds ||--}o Rule : "hasRule"
SystemOfQuantityKinds ||--}o SystemOfUnits : "hasUnitSystem"
Unit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
Unit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
Unit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
Unit ||--}o Prefix : "prefix"
Unit ||--}o QuantityKind : "hasQuantityKind"
Unit ||--}o SystemOfUnits : "applicableSystem"
Unit ||--}o SystemOfUnits : "definedUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedUnitOfSystem"
Unit ||--}o SystemOfUnits : "isUnitOfSystem"
Unit ||--}o UCUMcs : "ucumCode"
Unit ||--}o Unit : "exactMatch"
Unit ||--}o Unit : "hasReciprocalUnit"
Unit ||--}o Unit : "scalingOf"
Unit ||--}o __Class : "hasFactorUnit"
UserQuantityKind ||--|| QuantityKind : "hasQuantityKind"
UserQuantityKind ||--}o Rule : "hasRule"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **belongsToSystemOfQuantities** | <sub>0..\*</sub> | [SystemOfQuantityKinds](#SystemOfQuantityKinds) |  |
| *id* | <sub>0..1</sub> | None |  |
| *guidance* | <sub>0..\*</sub> | string |  |

#### Parents

 * [Verifiable](#Verifiable)

#### Uses

 *  mixin: [AbstractQuantityKind](#AbstractQuantityKind)

#### Referenced by:

 *  **[AbstractQuantityKind](#AbstractQuantityKind)** : *[AbstractQuantityKind_broader](#AbstractQuantityKind_broader)*  <sub>0..1</sub> 
 *  **[BaseDimensionMagnitude](#BaseDimensionMagnitude)** : *[BaseDimensionMagnitude_hasBaseQuantityKind](#BaseDimensionMagnitude_hasBaseQuantityKind)*  <sub>1..\*</sub> 
 *  **[QuantityKindDimensionVector](#QuantityKindDimensionVector)** : *[QuantityKindDimensionVector_hasReferenceQuantityKind](#QuantityKindDimensionVector_hasReferenceQuantityKind)*  <sub>0..\*</sub> 
 *  **[QuantityKind](#QuantityKind)** : *[QuantityKind_exactMatch](#QuantityKind_exactMatch)*  <sub>0..\*</sub> 
 *  **[QuantityType](#QuantityType)** : *[QuantityType_value](#QuantityType_value)*  <sub>0..\*</sub> 
 *  **[Quantity](#Quantity)** : *[Quantity_hasQuantityKind](#Quantity_hasQuantityKind)*  <sub>0..\*</sub> 
 *  **[SystemOfQuantityKinds](#SystemOfQuantityKinds)** : *[SystemOfQuantityKinds_hasBaseQuantityKind](#SystemOfQuantityKinds_hasBaseQuantityKind)*  <sub>0..\*</sub> 
 *  **[SystemOfQuantityKinds](#SystemOfQuantityKinds)** : *[SystemOfQuantityKinds_hasQuantityKind](#SystemOfQuantityKinds_hasQuantityKind)*  <sub>0..\*</sub> 
 *  **[SystemOfQuantityKinds](#SystemOfQuantityKinds)** : *[SystemOfQuantityKinds_systemDerivedQuantityKind](#SystemOfQuantityKinds_systemDerivedQuantityKind)*  <sub>0..\*</sub> 
 *  **[Unit](#Unit)** : *[Unit_hasQuantityKind](#Unit_hasQuantityKind)*  <sub>0..\*</sub> 
 *  **[UserQuantityKind](#UserQuantityKind)** : *[UserQuantityKind_hasQuantityKind](#UserQuantityKind_hasQuantityKind)*  <sub>1..\*</sub> 




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

```mermaid
erDiagram
PhysicalConstant {

}
QuantityKind {

}
QuantityKindDimensionVector {

}
Rule {

}
Unit {

}

PhysicalConstant ||--|o DataEncoding : "dataEncoding"
PhysicalConstant ||--|o Datatype : "datatype"
PhysicalConstant ||--|o Unit : "hasUnit"
PhysicalConstant ||--}o PhysicalConstant : "exactMatch"
PhysicalConstant ||--}o QuantityKind : "hasQuantityKind"
PhysicalConstant ||--}o QuantityKindDimensionVector : "hasDimensionVector"
PhysicalConstant ||--}o QuantityValue : "quantityValue"
PhysicalConstant ||--}o SystemOfUnits : "applicableSystem"
PhysicalConstant ||--}o Unit : "applicableUnit"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvDenominator"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvNumerator"
QuantityKind ||--|o QuantityKindDimensionVectorSI : "dimensionVectorForSI"
QuantityKind ||--}o QuantityKind : "exactMatch"
QuantityKind ||--}o QuantityKindDimensionVector : "hasDimensionVector"
QuantityKind ||--}o SystemOfQuantityKinds : "belongsToSystemOfQuantities"
QuantityKind ||--}o Unit : "applicableCGSUnit"
QuantityKind ||--}o Unit : "applicableISOUnit"
QuantityKind ||--}o Unit : "applicableImperialUnit"
QuantityKind ||--}o Unit : "applicableSIUnit"
QuantityKind ||--}o Unit : "applicableUSCustomaryUnit"
QuantityKind ||--}o Unit : "applicableUnit"
QuantityKindDimensionVector ||--}o QuantityKind : "hasReferenceQuantityKind"
QuantityKindDimensionVector ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"
Unit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
Unit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
Unit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
Unit ||--}o Prefix : "prefix"
Unit ||--}o QuantityKind : "hasQuantityKind"
Unit ||--}o SystemOfUnits : "applicableSystem"
Unit ||--}o SystemOfUnits : "definedUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedUnitOfSystem"
Unit ||--}o SystemOfUnits : "isUnitOfSystem"
Unit ||--}o UCUMcs : "ucumCode"
Unit ||--}o Unit : "exactMatch"
Unit ||--}o Unit : "hasReciprocalUnit"
Unit ||--}o Unit : "scalingOf"
Unit ||--}o __Class : "hasFactorUnit"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [Concept](#Concept)

#### Children

 * [QuantityKindDimensionVectorCGS](#QuantityKindDimensionVectorCGS)
 * [QuantityKindDimensionVectorISO](#QuantityKindDimensionVectorISO)
 * [QuantityKindDimensionVectorImperial](#QuantityKindDimensionVectorImperial)
 * [QuantityKindDimensionVectorSI](#QuantityKindDimensionVectorSI)

#### Referenced by:

 *  **[PhysicalConstant](#PhysicalConstant)** : *[PhysicalConstant_hasDimensionVector](#PhysicalConstant_hasDimensionVector)*  <sub>0..\*</sub> 
 *  **[QuantityKind](#QuantityKind)** : *[QuantityKind_hasDimensionVector](#QuantityKind_hasDimensionVector)*  <sub>0..\*</sub> 
 *  **[QuantityKind](#QuantityKind)** : *[QuantityKind_qkdvDenominator](#QuantityKind_qkdvDenominator)*  <sub>0..\*</sub> 
 *  **[QuantityKind](#QuantityKind)** : *[QuantityKind_qkdvNumerator](#QuantityKind_qkdvNumerator)*  <sub>0..\*</sub> 
 *  **[Unit](#Unit)** : *[Unit_hasDimensionVector](#Unit_hasDimensionVector)*  <sub>0..\*</sub> 
 *  **[Unit](#Unit)** : *[Unit_qkdvDenominator](#Unit_qkdvDenominator)*  <sub>0..\*</sub> 
 *  **[Unit](#Unit)** : *[Unit_qkdvNumerator](#Unit_qkdvNumerator)*  <sub>0..\*</sub> 




### QuantityKindDimensionVector_CGS



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

```mermaid
erDiagram
QuantityKind {

}
QuantityKindDimensionVectorCGS {

}
Rule {

}

QuantityKind ||--|o QuantityKindDimensionVector : "qkdvDenominator"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvNumerator"
QuantityKind ||--|o QuantityKindDimensionVectorSI : "dimensionVectorForSI"
QuantityKind ||--}o QuantityKind : "exactMatch"
QuantityKind ||--}o QuantityKindDimensionVector : "hasDimensionVector"
QuantityKind ||--}o SystemOfQuantityKinds : "belongsToSystemOfQuantities"
QuantityKind ||--}o Unit : "applicableCGSUnit"
QuantityKind ||--}o Unit : "applicableISOUnit"
QuantityKind ||--}o Unit : "applicableImperialUnit"
QuantityKind ||--}o Unit : "applicableSIUnit"
QuantityKind ||--}o Unit : "applicableUSCustomaryUnit"
QuantityKind ||--}o Unit : "applicableUnit"
QuantityKindDimensionVectorCGS ||--}o QuantityKind : "hasReferenceQuantityKind"
QuantityKindDimensionVectorCGS ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [QuantityKindDimensionVector](#QuantityKindDimensionVector)

#### Children

 * [QuantityKindDimensionVectorCGS-EMU](#QuantityKindDimensionVectorCGS-EMU)
 * [QuantityKindDimensionVectorCGS-ESU](#QuantityKindDimensionVectorCGS-ESU)
 * [QuantityKindDimensionVectorCGS-GAUSS](#QuantityKindDimensionVectorCGS-GAUSS)
 * [QuantityKindDimensionVectorCGS-LH](#QuantityKindDimensionVectorCGS-LH)




### QuantityKindDimensionVector_CGS-EMU



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

```mermaid
erDiagram
QuantityKind {

}
QuantityKindDimensionVectorCGS-EMU {

}
Rule {

}

QuantityKind ||--|o QuantityKindDimensionVector : "qkdvDenominator"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvNumerator"
QuantityKind ||--|o QuantityKindDimensionVectorSI : "dimensionVectorForSI"
QuantityKind ||--}o QuantityKind : "exactMatch"
QuantityKind ||--}o QuantityKindDimensionVector : "hasDimensionVector"
QuantityKind ||--}o SystemOfQuantityKinds : "belongsToSystemOfQuantities"
QuantityKind ||--}o Unit : "applicableCGSUnit"
QuantityKind ||--}o Unit : "applicableISOUnit"
QuantityKind ||--}o Unit : "applicableImperialUnit"
QuantityKind ||--}o Unit : "applicableSIUnit"
QuantityKind ||--}o Unit : "applicableUSCustomaryUnit"
QuantityKind ||--}o Unit : "applicableUnit"
QuantityKindDimensionVectorCGS-EMU ||--}o QuantityKind : "hasReferenceQuantityKind"
QuantityKindDimensionVectorCGS-EMU ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [QuantityKindDimensionVectorCGS](#QuantityKindDimensionVectorCGS)




### QuantityKindDimensionVector_CGS-ESU



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

```mermaid
erDiagram
QuantityKind {

}
QuantityKindDimensionVectorCGS-ESU {

}
Rule {

}

QuantityKind ||--|o QuantityKindDimensionVector : "qkdvDenominator"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvNumerator"
QuantityKind ||--|o QuantityKindDimensionVectorSI : "dimensionVectorForSI"
QuantityKind ||--}o QuantityKind : "exactMatch"
QuantityKind ||--}o QuantityKindDimensionVector : "hasDimensionVector"
QuantityKind ||--}o SystemOfQuantityKinds : "belongsToSystemOfQuantities"
QuantityKind ||--}o Unit : "applicableCGSUnit"
QuantityKind ||--}o Unit : "applicableISOUnit"
QuantityKind ||--}o Unit : "applicableImperialUnit"
QuantityKind ||--}o Unit : "applicableSIUnit"
QuantityKind ||--}o Unit : "applicableUSCustomaryUnit"
QuantityKind ||--}o Unit : "applicableUnit"
QuantityKindDimensionVectorCGS-ESU ||--}o QuantityKind : "hasReferenceQuantityKind"
QuantityKindDimensionVectorCGS-ESU ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [QuantityKindDimensionVectorCGS](#QuantityKindDimensionVectorCGS)




### QuantityKindDimensionVector_CGS-GAUSS



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

```mermaid
erDiagram
QuantityKind {

}
QuantityKindDimensionVectorCGS-GAUSS {

}
Rule {

}

QuantityKind ||--|o QuantityKindDimensionVector : "qkdvDenominator"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvNumerator"
QuantityKind ||--|o QuantityKindDimensionVectorSI : "dimensionVectorForSI"
QuantityKind ||--}o QuantityKind : "exactMatch"
QuantityKind ||--}o QuantityKindDimensionVector : "hasDimensionVector"
QuantityKind ||--}o SystemOfQuantityKinds : "belongsToSystemOfQuantities"
QuantityKind ||--}o Unit : "applicableCGSUnit"
QuantityKind ||--}o Unit : "applicableISOUnit"
QuantityKind ||--}o Unit : "applicableImperialUnit"
QuantityKind ||--}o Unit : "applicableSIUnit"
QuantityKind ||--}o Unit : "applicableUSCustomaryUnit"
QuantityKind ||--}o Unit : "applicableUnit"
QuantityKindDimensionVectorCGS-GAUSS ||--}o QuantityKind : "hasReferenceQuantityKind"
QuantityKindDimensionVectorCGS-GAUSS ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [QuantityKindDimensionVectorCGS](#QuantityKindDimensionVectorCGS)




### QuantityKindDimensionVector_CGS-LH



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

```mermaid
erDiagram
QuantityKind {

}
QuantityKindDimensionVectorCGS-LH {

}
Rule {

}

QuantityKind ||--|o QuantityKindDimensionVector : "qkdvDenominator"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvNumerator"
QuantityKind ||--|o QuantityKindDimensionVectorSI : "dimensionVectorForSI"
QuantityKind ||--}o QuantityKind : "exactMatch"
QuantityKind ||--}o QuantityKindDimensionVector : "hasDimensionVector"
QuantityKind ||--}o SystemOfQuantityKinds : "belongsToSystemOfQuantities"
QuantityKind ||--}o Unit : "applicableCGSUnit"
QuantityKind ||--}o Unit : "applicableISOUnit"
QuantityKind ||--}o Unit : "applicableImperialUnit"
QuantityKind ||--}o Unit : "applicableSIUnit"
QuantityKind ||--}o Unit : "applicableUSCustomaryUnit"
QuantityKind ||--}o Unit : "applicableUnit"
QuantityKindDimensionVectorCGS-LH ||--}o QuantityKind : "hasReferenceQuantityKind"
QuantityKindDimensionVectorCGS-LH ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [QuantityKindDimensionVectorCGS](#QuantityKindDimensionVectorCGS)




### QuantityKindDimensionVector_ISO




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

```mermaid
erDiagram
QuantityKind {

}
QuantityKindDimensionVectorISO {

}
Rule {

}

QuantityKind ||--|o QuantityKindDimensionVector : "qkdvDenominator"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvNumerator"
QuantityKind ||--|o QuantityKindDimensionVectorSI : "dimensionVectorForSI"
QuantityKind ||--}o QuantityKind : "exactMatch"
QuantityKind ||--}o QuantityKindDimensionVector : "hasDimensionVector"
QuantityKind ||--}o SystemOfQuantityKinds : "belongsToSystemOfQuantities"
QuantityKind ||--}o Unit : "applicableCGSUnit"
QuantityKind ||--}o Unit : "applicableISOUnit"
QuantityKind ||--}o Unit : "applicableImperialUnit"
QuantityKind ||--}o Unit : "applicableSIUnit"
QuantityKind ||--}o Unit : "applicableUSCustomaryUnit"
QuantityKind ||--}o Unit : "applicableUnit"
QuantityKindDimensionVectorISO ||--}o QuantityKind : "hasReferenceQuantityKind"
QuantityKindDimensionVectorISO ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [QuantityKindDimensionVector](#QuantityKindDimensionVector)




### QuantityKindDimensionVector_Imperial




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

```mermaid
erDiagram
QuantityKind {

}
QuantityKindDimensionVectorImperial {

}
Rule {

}

QuantityKind ||--|o QuantityKindDimensionVector : "qkdvDenominator"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvNumerator"
QuantityKind ||--|o QuantityKindDimensionVectorSI : "dimensionVectorForSI"
QuantityKind ||--}o QuantityKind : "exactMatch"
QuantityKind ||--}o QuantityKindDimensionVector : "hasDimensionVector"
QuantityKind ||--}o SystemOfQuantityKinds : "belongsToSystemOfQuantities"
QuantityKind ||--}o Unit : "applicableCGSUnit"
QuantityKind ||--}o Unit : "applicableISOUnit"
QuantityKind ||--}o Unit : "applicableImperialUnit"
QuantityKind ||--}o Unit : "applicableSIUnit"
QuantityKind ||--}o Unit : "applicableUSCustomaryUnit"
QuantityKind ||--}o Unit : "applicableUnit"
QuantityKindDimensionVectorImperial ||--}o QuantityKind : "hasReferenceQuantityKind"
QuantityKindDimensionVectorImperial ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [QuantityKindDimensionVector](#QuantityKindDimensionVector)




### QuantityKindDimensionVector_SI




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

```mermaid
erDiagram
QuantityKind {

}
QuantityKindDimensionVectorSI {

}
Rule {

}

QuantityKind ||--|o QuantityKindDimensionVector : "qkdvDenominator"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvNumerator"
QuantityKind ||--|o QuantityKindDimensionVectorSI : "dimensionVectorForSI"
QuantityKind ||--}o QuantityKind : "exactMatch"
QuantityKind ||--}o QuantityKindDimensionVector : "hasDimensionVector"
QuantityKind ||--}o SystemOfQuantityKinds : "belongsToSystemOfQuantities"
QuantityKind ||--}o Unit : "applicableCGSUnit"
QuantityKind ||--}o Unit : "applicableISOUnit"
QuantityKind ||--}o Unit : "applicableImperialUnit"
QuantityKind ||--}o Unit : "applicableSIUnit"
QuantityKind ||--}o Unit : "applicableUSCustomaryUnit"
QuantityKind ||--}o Unit : "applicableUnit"
QuantityKindDimensionVectorSI ||--}o QuantityKind : "hasReferenceQuantityKind"
QuantityKindDimensionVectorSI ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [QuantityKindDimensionVector](#QuantityKindDimensionVector)

#### Referenced by:

 *  **[QuantityKind](#QuantityKind)** : *[QuantityKind_dimensionVectorForSI](#QuantityKind_dimensionVectorForSI)*  <sub>0..\*</sub> 




### QuantityType




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
QuantityType:
  is_a: EnumeratedValue
  slots:
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

```mermaid
erDiagram
QuantityKind {

}
QuantityType {

}
Rule {

}

QuantityKind ||--|o QuantityKindDimensionVector : "qkdvDenominator"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvNumerator"
QuantityKind ||--|o QuantityKindDimensionVectorSI : "dimensionVectorForSI"
QuantityKind ||--}o QuantityKind : "exactMatch"
QuantityKind ||--}o QuantityKindDimensionVector : "hasDimensionVector"
QuantityKind ||--}o SystemOfQuantityKinds : "belongsToSystemOfQuantities"
QuantityKind ||--}o Unit : "applicableCGSUnit"
QuantityKind ||--}o Unit : "applicableISOUnit"
QuantityKind ||--}o Unit : "applicableImperialUnit"
QuantityKind ||--}o Unit : "applicableSIUnit"
QuantityKind ||--}o Unit : "applicableUSCustomaryUnit"
QuantityKind ||--}o Unit : "applicableUnit"
QuantityType ||--}o QuantityKind : "value"
Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| *id* | <sub>0..1</sub> | None |  |
| *guidance* | <sub>0..\*</sub> | string |  |

#### Parents

 * [EnumeratedValue](#EnumeratedValue)




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

```mermaid
erDiagram
DataEncoding {

}
Datatype {

}
Quantity {

}
QuantityValue {

}
Rule {

}
Unit {

}

DataEncoding ||--|o Encoding : "encoding"
DataEncoding ||--|o EndianType : "bitOrder"
DataEncoding ||--|o EndianType : "byteOrder"
Datatype ||--|o CardinalityType : "cardinality"
Datatype ||--|o Datatype : "basis"
Datatype ||--|o OrderedType : "orderedType"
Datatype ||--}o Rule : "hasRule"
Quantity ||--|o DataEncoding : "dataEncoding"
Quantity ||--|o Datatype : "datatype"
Quantity ||--|o Unit : "hasUnit"
Quantity ||--}o QuantityKind : "hasQuantityKind"
Quantity ||--}o QuantityValue : "quantityValue"
QuantityValue ||--|o DataEncoding : "dataEncoding"
QuantityValue ||--|o Datatype : "datatype"
QuantityValue ||--|o Unit : "hasUnit"
Rule ||--}o RuleType : "ruleType"
Unit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
Unit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
Unit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
Unit ||--}o Prefix : "prefix"
Unit ||--}o QuantityKind : "hasQuantityKind"
Unit ||--}o SystemOfUnits : "applicableSystem"
Unit ||--}o SystemOfUnits : "definedUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedUnitOfSystem"
Unit ||--}o SystemOfUnits : "isUnitOfSystem"
Unit ||--}o UCUMcs : "ucumCode"
Unit ||--}o Unit : "exactMatch"
Unit ||--}o Unit : "hasReciprocalUnit"
Unit ||--}o Unit : "scalingOf"
Unit ||--}o __Class : "hasFactorUnit"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| *id* | <sub>0..1</sub> | None |  |
| *guidance* | <sub>0..\*</sub> | string |  |

#### Parents

 * [Quantifiable](#Quantifiable)

#### Children

 * [ConstantValue](#ConstantValue)

#### Uses

 *  mixin: [Concept](#Concept)

#### Referenced by:

 *  **[Quantity](#Quantity)** : *[Quantity_quantityValue](#Quantity_quantityValue)*  <sub>0..\*</sub> 




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

```mermaid
erDiagram
MathsFunctionType {

}
RatioScale {

}
Rule {

}
ScaleType {

}
TransformType {

}

MathsFunctionType ||--}o Rule : "hasRule"
RatioScale ||--|o ScaleType : "scaleType"
RatioScale ||--}o MathsFunctionType : "permissibleMaths"
RatioScale ||--}o Rule : "hasRule"
RatioScale ||--}o TransformType : "permissibleTransformation"
Rule ||--}o RuleType : "ruleType"
ScaleType ||--}o MathsFunctionType : "permissibleMaths"
ScaleType ||--}o TransformType : "permissibleTransformation"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [Scale](#Scale)




### Resource




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
Resource: {}

```
</details>


#### Local class diagram

```mermaid
classDiagram
Resource <|-- UCUMcs
Resource <|-- UCUMcs_term
Resource <|-- valueUnion

```

This class has no attributes


#### Children

 * [UCUMcs](#UCUMcs)
 * [UCUMcs-term](#UCUMcs-term)
 * [ValueUnion](#ValueUnion)




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

```mermaid
erDiagram
Concept {

}
Rule {

}
RuleType {

}

Concept ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| *id* | <sub>0..1</sub> | None |  |
| *guidance* | <sub>0..\*</sub> | string |  |

#### Parents

 * [Verifiable](#Verifiable)

#### Uses

 *  mixin: [Concept](#Concept)

#### Referenced by:

 *  **[Concept](#Concept)** : *[Concept_hasRule](#Concept_hasRule)*  <sub>0..\*</sub> 




### RuleType




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
RuleType:
  is_a: EnumeratedValue
  slots:
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

```mermaid
erDiagram
Rule {

}
RuleType {

}

Rule ||--}o RuleType : "ruleType"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| *id* | <sub>0..1</sub> | None |  |
| *guidance* | <sub>0..\*</sub> | string |  |

#### Parents

 * [EnumeratedValue](#EnumeratedValue)

#### Referenced by:

 *  **[Rule](#Rule)** : *[Rule_ruleType](#Rule_ruleType)*  <sub>0..\*</sub> 




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

```mermaid
erDiagram
CardinalityType {

}
Datatype {

}
OrderedType {

}
Rule {

}
ScalarDatatype {

}

Datatype ||--|o CardinalityType : "cardinality"
Datatype ||--|o Datatype : "basis"
Datatype ||--|o OrderedType : "orderedType"
Datatype ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"
ScalarDatatype ||--|o CardinalityType : "cardinality"
ScalarDatatype ||--|o Datatype : "basis"
ScalarDatatype ||--|o Datatype : "rdfsDatatype"
ScalarDatatype ||--|o OrderedType : "orderedType"
ScalarDatatype ||--}o Rule : "hasRule"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [Datatype](#Datatype)




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

```mermaid
erDiagram
MathsFunctionType {

}
Rule {

}
Scale {

}
ScaleType {

}
TransformType {

}

MathsFunctionType ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"
Scale ||--|o ScaleType : "scaleType"
Scale ||--}o MathsFunctionType : "permissibleMaths"
Scale ||--}o Rule : "hasRule"
Scale ||--}o TransformType : "permissibleTransformation"
ScaleType ||--}o MathsFunctionType : "permissibleMaths"
ScaleType ||--}o TransformType : "permissibleTransformation"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [Concept](#Concept)

#### Children

 * [EnumerationScale](#EnumerationScale)
 * [IntervalScale](#IntervalScale)
 * [NominalScale](#NominalScale)
 * [OrdinalScale](#OrdinalScale)
 * [RatioScale](#RatioScale)




### ScaleType




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
ScaleType:
  is_a: EnumeratedValue
  slots:
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

```mermaid
erDiagram
MathsFunctionType {

}
Rule {

}
Scale {

}
ScaleType {

}
TransformType {

}

MathsFunctionType ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"
Scale ||--|o ScaleType : "scaleType"
Scale ||--}o MathsFunctionType : "permissibleMaths"
Scale ||--}o Rule : "hasRule"
Scale ||--}o TransformType : "permissibleTransformation"
ScaleType ||--}o MathsFunctionType : "permissibleMaths"
ScaleType ||--}o TransformType : "permissibleTransformation"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| *id* | <sub>0..1</sub> | None |  |
| *guidance* | <sub>0..\*</sub> | string |  |

#### Parents

 * [EnumeratedValue](#EnumeratedValue)

#### Referenced by:

 *  **[Scale](#Scale)** : *[Scale_scaleType](#Scale_scaleType)*  <sub>0..\*</sub> 




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

```mermaid
erDiagram
Prefix {

}
QuantityKind {

}
QuantityKindDimensionVector {

}
Rule {

}
SolidAngleUnit {

}
SystemOfUnits {

}
UCUMcs {

}
Unit {

}
__Class {

}

Prefix ||--}o Prefix : "exactMatch"
Prefix ||--}o UCUMcs-term : "ucumCode"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvDenominator"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvNumerator"
QuantityKind ||--|o QuantityKindDimensionVectorSI : "dimensionVectorForSI"
QuantityKind ||--}o QuantityKind : "exactMatch"
QuantityKind ||--}o QuantityKindDimensionVector : "hasDimensionVector"
QuantityKind ||--}o SystemOfQuantityKinds : "belongsToSystemOfQuantities"
QuantityKind ||--}o Unit : "applicableCGSUnit"
QuantityKind ||--}o Unit : "applicableISOUnit"
QuantityKind ||--}o Unit : "applicableImperialUnit"
QuantityKind ||--}o Unit : "applicableSIUnit"
QuantityKind ||--}o Unit : "applicableUSCustomaryUnit"
QuantityKind ||--}o Unit : "applicableUnit"
QuantityKindDimensionVector ||--}o QuantityKind : "hasReferenceQuantityKind"
QuantityKindDimensionVector ||--}o Rule : "hasRule"
Rule ||--}o RuleType : "ruleType"
SolidAngleUnit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
SolidAngleUnit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
SolidAngleUnit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
SolidAngleUnit ||--}o Prefix : "prefix"
SolidAngleUnit ||--}o QuantityKind : "hasQuantityKind"
SolidAngleUnit ||--}o SystemOfUnits : "applicableSystem"
SolidAngleUnit ||--}o SystemOfUnits : "definedUnitOfSystem"
SolidAngleUnit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
SolidAngleUnit ||--}o SystemOfUnits : "derivedUnitOfSystem"
SolidAngleUnit ||--}o SystemOfUnits : "isUnitOfSystem"
SolidAngleUnit ||--}o UCUMcs : "ucumCode"
SolidAngleUnit ||--}o Unit : "exactMatch"
SolidAngleUnit ||--}o Unit : "hasReciprocalUnit"
SolidAngleUnit ||--}o Unit : "scalingOf"
SolidAngleUnit ||--}o __Class : "hasFactorUnit"
SystemOfUnits ||--}o PhysicalConstant : "applicablePhysicalConstant"
SystemOfUnits ||--}o Prefix : "prefix"
SystemOfUnits ||--}o Unit : "hasAllowedUnit"
SystemOfUnits ||--}o Unit : "hasBaseUnit"
SystemOfUnits ||--}o Unit : "hasCoherentUnit"
SystemOfUnits ||--}o Unit : "hasDefinedUnit"
SystemOfUnits ||--}o Unit : "hasDerivedCoherentUnit"
SystemOfUnits ||--}o Unit : "hasDerivedUnit"
SystemOfUnits ||--}o Unit : "hasUnit"
Unit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
Unit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
Unit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
Unit ||--}o Prefix : "prefix"
Unit ||--}o QuantityKind : "hasQuantityKind"
Unit ||--}o SystemOfUnits : "applicableSystem"
Unit ||--}o SystemOfUnits : "definedUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedUnitOfSystem"
Unit ||--}o SystemOfUnits : "isUnitOfSystem"
Unit ||--}o UCUMcs : "ucumCode"
Unit ||--}o Unit : "exactMatch"
Unit ||--}o Unit : "hasReciprocalUnit"
Unit ||--}o Unit : "scalingOf"
Unit ||--}o __Class : "hasFactorUnit"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| hasReciprocalUnit | <sub>0..\*</sub> | [Unit](#Unit) |  |
| isUnitOfSystem | <sub>0..\*</sub> | [SystemOfUnits](#SystemOfUnits) |  |
| omUnit | <sub>0..\*</sub> | None |  |
| unitFor | <sub>0..\*</sub> | None |  |
| *id* | <sub>0..1</sub> | None |  |
| *guidance* | <sub>0..\*</sub> | string |  |

#### Parents

 * [AngleUnit](#AngleUnit)




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

```mermaid
classDiagram
StringEncodingType <|-- DateTimeStringEncodingType

```

This class has no attributes


#### Children

 * [DateTimeStringEncodingType](#DateTimeStringEncodingType)




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

```mermaid
erDiagram
Rule {

}
Symbol {

}

Rule ||--}o RuleType : "ruleType"
Symbol ||--}o Rule : "hasRule"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [Concept](#Concept)




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

```mermaid
erDiagram
Enumeration {

}
QuantityKind {

}
Rule {

}
SystemOfQuantityKinds {

}
SystemOfUnits {

}

Enumeration ||--|o EnumeratedValue : "default"
Enumeration ||--}o Rule : "hasRule"
Enumeration ||--}| EnumeratedValue : "element"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvDenominator"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvNumerator"
QuantityKind ||--|o QuantityKindDimensionVectorSI : "dimensionVectorForSI"
QuantityKind ||--}o QuantityKind : "exactMatch"
QuantityKind ||--}o QuantityKindDimensionVector : "hasDimensionVector"
QuantityKind ||--}o SystemOfQuantityKinds : "belongsToSystemOfQuantities"
QuantityKind ||--}o Unit : "applicableCGSUnit"
QuantityKind ||--}o Unit : "applicableISOUnit"
QuantityKind ||--}o Unit : "applicableImperialUnit"
QuantityKind ||--}o Unit : "applicableSIUnit"
QuantityKind ||--}o Unit : "applicableUSCustomaryUnit"
QuantityKind ||--}o Unit : "applicableUnit"
Rule ||--}o RuleType : "ruleType"
SystemOfQuantityKinds ||--|o Enumeration : "baseDimensionEnumeration"
SystemOfQuantityKinds ||--}o QuantityKind : "hasBaseQuantityKind"
SystemOfQuantityKinds ||--}o QuantityKind : "hasQuantityKind"
SystemOfQuantityKinds ||--}o QuantityKind : "systemDerivedQuantityKind"
SystemOfQuantityKinds ||--}o Rule : "hasRule"
SystemOfQuantityKinds ||--}o SystemOfUnits : "hasUnitSystem"
SystemOfUnits ||--}o PhysicalConstant : "applicablePhysicalConstant"
SystemOfUnits ||--}o Prefix : "prefix"
SystemOfUnits ||--}o Unit : "hasAllowedUnit"
SystemOfUnits ||--}o Unit : "hasBaseUnit"
SystemOfUnits ||--}o Unit : "hasCoherentUnit"
SystemOfUnits ||--}o Unit : "hasDefinedUnit"
SystemOfUnits ||--}o Unit : "hasDerivedCoherentUnit"
SystemOfUnits ||--}o Unit : "hasDerivedUnit"
SystemOfUnits ||--}o Unit : "hasUnit"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [Concept](#Concept)

#### Referenced by:

 *  **[QuantityKind](#QuantityKind)** : *[belongsToSystemOfQuantities](#belongsToSystemOfQuantities)*  <sub>0..\*</sub> 




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

```mermaid
erDiagram
PhysicalConstant {

}
Prefix {

}
Rule {

}
SystemOfQuantityKinds {

}
SystemOfUnits {

}
Unit {

}

PhysicalConstant ||--|o DataEncoding : "dataEncoding"
PhysicalConstant ||--|o Datatype : "datatype"
PhysicalConstant ||--|o Unit : "hasUnit"
PhysicalConstant ||--}o PhysicalConstant : "exactMatch"
PhysicalConstant ||--}o QuantityKind : "hasQuantityKind"
PhysicalConstant ||--}o QuantityKindDimensionVector : "hasDimensionVector"
PhysicalConstant ||--}o QuantityValue : "quantityValue"
PhysicalConstant ||--}o SystemOfUnits : "applicableSystem"
PhysicalConstant ||--}o Unit : "applicableUnit"
Prefix ||--}o Prefix : "exactMatch"
Prefix ||--}o UCUMcs-term : "ucumCode"
Rule ||--}o RuleType : "ruleType"
SystemOfQuantityKinds ||--|o Enumeration : "baseDimensionEnumeration"
SystemOfQuantityKinds ||--}o QuantityKind : "hasBaseQuantityKind"
SystemOfQuantityKinds ||--}o QuantityKind : "hasQuantityKind"
SystemOfQuantityKinds ||--}o QuantityKind : "systemDerivedQuantityKind"
SystemOfQuantityKinds ||--}o Rule : "hasRule"
SystemOfQuantityKinds ||--}o SystemOfUnits : "hasUnitSystem"
SystemOfUnits ||--}o PhysicalConstant : "applicablePhysicalConstant"
SystemOfUnits ||--}o Prefix : "prefix"
SystemOfUnits ||--}o Unit : "hasAllowedUnit"
SystemOfUnits ||--}o Unit : "hasBaseUnit"
SystemOfUnits ||--}o Unit : "hasCoherentUnit"
SystemOfUnits ||--}o Unit : "hasDefinedUnit"
SystemOfUnits ||--}o Unit : "hasDerivedCoherentUnit"
SystemOfUnits ||--}o Unit : "hasDerivedUnit"
SystemOfUnits ||--}o Unit : "hasUnit"
Unit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
Unit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
Unit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
Unit ||--}o Prefix : "prefix"
Unit ||--}o QuantityKind : "hasQuantityKind"
Unit ||--}o SystemOfUnits : "applicableSystem"
Unit ||--}o SystemOfUnits : "definedUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedUnitOfSystem"
Unit ||--}o SystemOfUnits : "isUnitOfSystem"
Unit ||--}o UCUMcs : "ucumCode"
Unit ||--}o Unit : "exactMatch"
Unit ||--}o Unit : "hasReciprocalUnit"
Unit ||--}o Unit : "scalingOf"
Unit ||--}o __Class : "hasFactorUnit"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| *id* | <sub>0..1</sub> | None |  |
| *guidance* | <sub>0..\*</sub> | string |  |

#### Parents

 * [Verifiable](#Verifiable)

#### Uses

 *  mixin: [Concept](#Concept)

#### Referenced by:

 *  **[PhysicalConstant](#PhysicalConstant)** : *[PhysicalConstant_applicableSystem](#PhysicalConstant_applicableSystem)*  <sub>0..\*</sub> 
 *  **[SystemOfQuantityKinds](#SystemOfQuantityKinds)** : *[SystemOfQuantityKinds_hasUnitSystem](#SystemOfQuantityKinds_hasUnitSystem)*  <sub>0..\*</sub> 
 *  **[Unit](#Unit)** : *[Unit_applicableSystem](#Unit_applicableSystem)*  <sub>0..\*</sub> 
 *  **[Unit](#Unit)** : *[Unit_definedUnitOfSystem](#Unit_definedUnitOfSystem)*  <sub>0..\*</sub> 
 *  **[Unit](#Unit)** : *[Unit_derivedCoherentUnitOfSystem](#Unit_derivedCoherentUnitOfSystem)*  <sub>0..\*</sub> 
 *  **[Unit](#Unit)** : *[Unit_derivedUnitOfSystem](#Unit_derivedUnitOfSystem)*  <sub>0..\*</sub> 
 *  **[Unit](#Unit)** : *[isUnitOfSystem](#isUnitOfSystem)*  <sub>0..\*</sub> 




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

```mermaid
classDiagram
Thing <|-- Aspect
Thing <|-- Concept

```

This class has no attributes


#### Children

 * [Aspect](#Aspect)
 * [Concept](#Concept)

#### Used as mixin by

 * [Comment](#Comment)




### TransformType




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
TransformType:
  is_a: EnumeratedValue
  slots:
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

```mermaid
erDiagram
Rule {

}
Scale {

}
ScaleType {

}
TransformType {

}

Rule ||--}o RuleType : "ruleType"
Scale ||--|o ScaleType : "scaleType"
Scale ||--}o MathsFunctionType : "permissibleMaths"
Scale ||--}o Rule : "hasRule"
Scale ||--}o TransformType : "permissibleTransformation"
ScaleType ||--}o MathsFunctionType : "permissibleMaths"
ScaleType ||--}o TransformType : "permissibleTransformation"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| *id* | <sub>0..1</sub> | None |  |
| *guidance* | <sub>0..\*</sub> | string |  |

#### Parents

 * [EnumeratedValue](#EnumeratedValue)

#### Referenced by:

 *  **[ScaleType](#ScaleType)** : *[ScaleType_permissibleTransformation](#ScaleType_permissibleTransformation)*  <sub>0..\*</sub> 
 *  **[Scale](#Scale)** : *[Scale_permissibleTransformation](#Scale_permissibleTransformation)*  <sub>0..\*</sub> 




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

```mermaid
erDiagram
UCUMcs {

}
Unit {

}

Unit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
Unit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
Unit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
Unit ||--}o Prefix : "prefix"
Unit ||--}o QuantityKind : "hasQuantityKind"
Unit ||--}o SystemOfUnits : "applicableSystem"
Unit ||--}o SystemOfUnits : "definedUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedUnitOfSystem"
Unit ||--}o SystemOfUnits : "isUnitOfSystem"
Unit ||--}o UCUMcs : "ucumCode"
Unit ||--}o Unit : "exactMatch"
Unit ||--}o Unit : "hasReciprocalUnit"
Unit ||--}o Unit : "scalingOf"
Unit ||--}o __Class : "hasFactorUnit"

```


This class has no attributes


#### Parents

 * [Resource](#Resource)

#### Referenced by:

 *  **[Unit](#Unit)** : *[Unit_ucumCode](#Unit_ucumCode)*  <sub>0..\*</sub> 




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

```mermaid
erDiagram
Prefix {

}
UCUMcs-term {

}

Prefix ||--}o Prefix : "exactMatch"
Prefix ||--}o UCUMcs-term : "ucumCode"

```


This class has no attributes


#### Parents

 * [Resource](#Resource)

#### Referenced by:

 *  **[Prefix](#Prefix)** : *[Prefix_ucumCode](#Prefix_ucumCode)*  <sub>0..\*</sub> 




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

```mermaid
erDiagram
ContextualUnit {

}
PhysicalConstant {

}
Prefix {

}
Quantifiable {

}
QuantityKind {

}
QuantityKindDimensionVector {

}
QuantityValue {

}
Rule {

}
SystemOfUnits {

}
UCUMcs {

}
Unit {

}
__Class {

}

ContextualUnit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
ContextualUnit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
ContextualUnit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
ContextualUnit ||--}o Prefix : "prefix"
ContextualUnit ||--}o QuantityKind : "hasQuantityKind"
ContextualUnit ||--}o SystemOfUnits : "applicableSystem"
ContextualUnit ||--}o SystemOfUnits : "definedUnitOfSystem"
ContextualUnit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
ContextualUnit ||--}o SystemOfUnits : "derivedUnitOfSystem"
ContextualUnit ||--}o SystemOfUnits : "isUnitOfSystem"
ContextualUnit ||--}o UCUMcs : "ucumCode"
ContextualUnit ||--}o Unit : "exactMatch"
ContextualUnit ||--}o Unit : "hasReciprocalUnit"
ContextualUnit ||--}o Unit : "scalingOf"
ContextualUnit ||--}o __Class : "hasFactorUnit"
PhysicalConstant ||--|o DataEncoding : "dataEncoding"
PhysicalConstant ||--|o Datatype : "datatype"
PhysicalConstant ||--|o Unit : "hasUnit"
PhysicalConstant ||--}o PhysicalConstant : "exactMatch"
PhysicalConstant ||--}o QuantityKind : "hasQuantityKind"
PhysicalConstant ||--}o QuantityKindDimensionVector : "hasDimensionVector"
PhysicalConstant ||--}o QuantityValue : "quantityValue"
PhysicalConstant ||--}o SystemOfUnits : "applicableSystem"
PhysicalConstant ||--}o Unit : "applicableUnit"
Prefix ||--}o Prefix : "exactMatch"
Prefix ||--}o UCUMcs-term : "ucumCode"
Quantifiable ||--|o DataEncoding : "dataEncoding"
Quantifiable ||--|o Datatype : "datatype"
Quantifiable ||--|o Unit : "hasUnit"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvDenominator"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvNumerator"
QuantityKind ||--|o QuantityKindDimensionVectorSI : "dimensionVectorForSI"
QuantityKind ||--}o QuantityKind : "exactMatch"
QuantityKind ||--}o QuantityKindDimensionVector : "hasDimensionVector"
QuantityKind ||--}o SystemOfQuantityKinds : "belongsToSystemOfQuantities"
QuantityKind ||--}o Unit : "applicableCGSUnit"
QuantityKind ||--}o Unit : "applicableISOUnit"
QuantityKind ||--}o Unit : "applicableImperialUnit"
QuantityKind ||--}o Unit : "applicableSIUnit"
QuantityKind ||--}o Unit : "applicableUSCustomaryUnit"
QuantityKind ||--}o Unit : "applicableUnit"
QuantityKindDimensionVector ||--}o QuantityKind : "hasReferenceQuantityKind"
QuantityKindDimensionVector ||--}o Rule : "hasRule"
QuantityValue ||--|o DataEncoding : "dataEncoding"
QuantityValue ||--|o Datatype : "datatype"
QuantityValue ||--|o Unit : "hasUnit"
Rule ||--}o RuleType : "ruleType"
SystemOfUnits ||--}o PhysicalConstant : "applicablePhysicalConstant"
SystemOfUnits ||--}o Prefix : "prefix"
SystemOfUnits ||--}o Unit : "hasAllowedUnit"
SystemOfUnits ||--}o Unit : "hasBaseUnit"
SystemOfUnits ||--}o Unit : "hasCoherentUnit"
SystemOfUnits ||--}o Unit : "hasDefinedUnit"
SystemOfUnits ||--}o Unit : "hasDerivedCoherentUnit"
SystemOfUnits ||--}o Unit : "hasDerivedUnit"
SystemOfUnits ||--}o Unit : "hasUnit"
Unit ||--|o QuantityKindDimensionVector : "hasDimensionVector"
Unit ||--|o QuantityKindDimensionVector : "qkdvDenominator"
Unit ||--|o QuantityKindDimensionVector : "qkdvNumerator"
Unit ||--}o Prefix : "prefix"
Unit ||--}o QuantityKind : "hasQuantityKind"
Unit ||--}o SystemOfUnits : "applicableSystem"
Unit ||--}o SystemOfUnits : "definedUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedCoherentUnitOfSystem"
Unit ||--}o SystemOfUnits : "derivedUnitOfSystem"
Unit ||--}o SystemOfUnits : "isUnitOfSystem"
Unit ||--}o UCUMcs : "ucumCode"
Unit ||--}o Unit : "exactMatch"
Unit ||--}o Unit : "hasReciprocalUnit"
Unit ||--}o Unit : "scalingOf"
Unit ||--}o __Class : "hasFactorUnit"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| *id* | <sub>0..1</sub> | None |  |
| *guidance* | <sub>0..\*</sub> | string |  |
| **hasReciprocalUnit** | <sub>0..\*</sub> | [Unit](#Unit) |  |
| **isUnitOfSystem** | <sub>0..\*</sub> | [SystemOfUnits](#SystemOfUnits) |  |
| **omUnit** | <sub>0..\*</sub> | None |  |
| **unitFor** | <sub>0..\*</sub> | None |  |

#### Parents

 * [Verifiable](#Verifiable)

#### Children

 * [ContextualUnit](#ContextualUnit)
 * [DerivedUnit](#DerivedUnit)
 * [DimensionlessUnit](#DimensionlessUnit)

#### Uses

 *  mixin: [Concept](#Concept)

#### Referenced by:

 *  **[ContextualUnit](#ContextualUnit)** : *[ContextualUnit_broader](#ContextualUnit_broader)*  <sub>0..1</sub> 
 *  **[PhysicalConstant](#PhysicalConstant)** : *[PhysicalConstant_applicableUnit](#PhysicalConstant_applicableUnit)*  <sub>0..\*</sub> 
 *  **[Quantifiable](#Quantifiable)** : *[Quantifiable_hasUnit](#Quantifiable_hasUnit)*  <sub>0..\*</sub> 
 *  **[QuantityKind](#QuantityKind)** : *[QuantityKind_applicableCGSUnit](#QuantityKind_applicableCGSUnit)*  <sub>0..\*</sub> 
 *  **[QuantityKind](#QuantityKind)** : *[QuantityKind_applicableISOUnit](#QuantityKind_applicableISOUnit)*  <sub>0..\*</sub> 
 *  **[QuantityKind](#QuantityKind)** : *[QuantityKind_applicableImperialUnit](#QuantityKind_applicableImperialUnit)*  <sub>0..\*</sub> 
 *  **[QuantityKind](#QuantityKind)** : *[QuantityKind_applicableSIUnit](#QuantityKind_applicableSIUnit)*  <sub>0..\*</sub> 
 *  **[QuantityKind](#QuantityKind)** : *[QuantityKind_applicableUSCustomaryUnit](#QuantityKind_applicableUSCustomaryUnit)*  <sub>0..\*</sub> 
 *  **[QuantityKind](#QuantityKind)** : *[QuantityKind_applicableUnit](#QuantityKind_applicableUnit)*  <sub>0..\*</sub> 
 *  **[QuantityValue](#QuantityValue)** : *[QuantityValue_hasUnit](#QuantityValue_hasUnit)*  <sub>0..\*</sub> 
 *  **[SystemOfUnits](#SystemOfUnits)** : *[SystemOfUnits_hasAllowedUnit](#SystemOfUnits_hasAllowedUnit)*  <sub>0..\*</sub> 
 *  **[SystemOfUnits](#SystemOfUnits)** : *[SystemOfUnits_hasBaseUnit](#SystemOfUnits_hasBaseUnit)*  <sub>0..\*</sub> 
 *  **[SystemOfUnits](#SystemOfUnits)** : *[SystemOfUnits_hasCoherentUnit](#SystemOfUnits_hasCoherentUnit)*  <sub>0..\*</sub> 
 *  **[SystemOfUnits](#SystemOfUnits)** : *[SystemOfUnits_hasDefinedUnit](#SystemOfUnits_hasDefinedUnit)*  <sub>0..\*</sub> 
 *  **[SystemOfUnits](#SystemOfUnits)** : *[SystemOfUnits_hasDerivedCoherentUnit](#SystemOfUnits_hasDerivedCoherentUnit)*  <sub>0..\*</sub> 
 *  **[SystemOfUnits](#SystemOfUnits)** : *[SystemOfUnits_hasDerivedUnit](#SystemOfUnits_hasDerivedUnit)*  <sub>0..\*</sub> 
 *  **[SystemOfUnits](#SystemOfUnits)** : *[SystemOfUnits_hasUnit](#SystemOfUnits_hasUnit)*  <sub>0..\*</sub> 
 *  **[Unit](#Unit)** : *[Unit_exactMatch](#Unit_exactMatch)*  <sub>0..\*</sub> 
 *  **[Unit](#Unit)** : *[Unit_scalingOf](#Unit_scalingOf)*  <sub>0..\*</sub> 
 *  **[Unit](#Unit)** : *[hasReciprocalUnit](#hasReciprocalUnit)*  <sub>0..\*</sub> 




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

```mermaid
erDiagram
QuantityKind {

}
Rule {

}
UserQuantityKind {

}

QuantityKind ||--|o QuantityKindDimensionVector : "qkdvDenominator"
QuantityKind ||--|o QuantityKindDimensionVector : "qkdvNumerator"
QuantityKind ||--|o QuantityKindDimensionVectorSI : "dimensionVectorForSI"
QuantityKind ||--}o QuantityKind : "exactMatch"
QuantityKind ||--}o QuantityKindDimensionVector : "hasDimensionVector"
QuantityKind ||--}o SystemOfQuantityKinds : "belongsToSystemOfQuantities"
QuantityKind ||--}o Unit : "applicableCGSUnit"
QuantityKind ||--}o Unit : "applicableISOUnit"
QuantityKind ||--}o Unit : "applicableImperialUnit"
QuantityKind ||--}o Unit : "applicableSIUnit"
QuantityKind ||--}o Unit : "applicableUSCustomaryUnit"
QuantityKind ||--}o Unit : "applicableUnit"
Rule ||--}o RuleType : "ruleType"
UserQuantityKind ||--|| QuantityKind : "hasQuantityKind"
UserQuantityKind ||--}o Rule : "hasRule"

```


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| id | <sub>0..1</sub> | None |  |
| guidance | <sub>0..\*</sub> | string |  |

#### Parents

 * [AbstractQuantityKind](#AbstractQuantityKind)




### Verifiable



An aspect class that holds properties that provide external knowledge and specifications of a given resource.


#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
Verifiable:
  is_a: Error3
  mixins:
  - Error2
  - Aspect
  slots:
  - Verifiable_isoNormativeReference
  - Verifiable_normativeReference
  slot_usage:
    isoNormativeReference:
      required: false
    normativeReference:
      required: false

```
</details>


#### Local class diagram

```mermaid
classDiagram
Error3 <|-- Verifiable
Verifiable <|-- Comment
Verifiable <|-- EnumeratedValue
Verifiable <|-- Prefix
Verifiable <|-- QuantityKind
Verifiable <|-- Rule
Verifiable <|-- SystemOfUnits
Verifiable <|-- Unit
Verifiable ..> Aspect
Verifiable ..> Error2

```

This class has no attributes


#### Parents

 * [Error3](#Error3)

#### Children

 * [Comment](#Comment)
 * [EnumeratedValue](#EnumeratedValue)
 * [Prefix](#Prefix)
 * [QuantityKind](#QuantityKind)
 * [Rule](#Rule)
 * [SystemOfUnits](#SystemOfUnits)
 * [Unit](#Unit)

#### Uses

 *  mixin: [Aspect](#Aspect)
 *  mixin: [Error2](#Error2)




### gDay




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
gDay: {}

```
</details>


This class has no attributes





### gMonth




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
gMonth: {}

```
</details>


This class has no attributes





### gMonthDay




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
gMonthDay: {}

```
</details>


This class has no attributes





### gYear




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
gYear: {}

```
</details>


This class has no attributes





### gYearMonth




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
gYearMonth: {}

```
</details>


This class has no attributes





### valueUnion




#### YAML Definition

<details>
<summary>Click to expand</summary>

```yaml
valueUnion:
  is_a: Resource

```
</details>


#### Local class diagram

```mermaid
classDiagram
Resource <|-- valueUnion

```

This class has no attributes


#### Parents

 * [Resource](#Resource)

