

/**
 * The root class for all QUDT concepts
 */
export interface Thing {
}



export interface Error1 {
}



export interface Error2 {
}



export interface Error3 {
}



export interface AbstractQuantityKind extends Concept {
}



export interface AngleUnit extends DimensionlessUnit {
}



export interface Aspect extends Thing {
}



export interface AspectClass extends Class {
}



export interface BaseDimensionMagnitude extends Concept {
}



export interface BinaryPrefix extends Prefix {
}



export interface BitEncodingType extends Encoding {
}



export interface BooleanEncodingType extends Encoding {
}



export interface ByteEncodingType extends Encoding {
}



export interface CardinalityType extends EnumeratedValue {
}



export interface CharEncodingType extends Encoding {
}



export interface Citation extends Concept {
}



export interface Comment extends Verifiable, Thing {
}



export interface Concept extends Thing {
    guidance?: string[],
    id?: string,
}



export interface ConstantValue extends QuantityValue {
}



export interface ContextualUnit extends Unit {
}



export interface CountingUnit extends DimensionlessUnit {
}



export interface CurrencyUnit extends DimensionlessUnit {
}



export interface DataEncoding extends Aspect {
}



export interface DataItem extends Concept {
}



export interface Datatype extends Concept {
}



export interface DateTimeStringEncodingType extends StringEncodingType {
}



export interface DecimalPrefix extends Prefix {
}



export interface DerivedUnit extends Unit {
}



export interface DimensionlessUnit extends Unit {
}



export interface Discipline extends Concept {
}



export interface Encoding extends Concept {
}



export interface EndianType extends EnumeratedValue {
}



export interface EnumeratedQuantity extends Concept {
}



export interface EnumeratedValue extends Verifiable, Concept {
}



export interface Enumeration extends Concept {
}



export interface EnumerationScale extends Scale, Enumeration {
}



export interface Figure extends Concept {
}



export interface FloatingPointEncodingType extends Encoding {
}



export interface IntegerEncodingType extends Encoding {
}



export interface IntervalScale extends Scale {
}



export interface LogarithmicUnit extends DimensionlessUnit {
}



export interface MathsFunctionType extends Concept {
}



export interface NISTSP811Comment extends Comment {
}



export interface NominalScale extends Scale {
}



export interface NumericUnion extends Concept {
}



export interface OrderedType extends EnumeratedValue {
}



export interface OrdinalScale extends Scale {
}



export interface Organization extends Concept {
}



export interface PhysicalConstant extends Quantity, Error1 {
}



export interface PlaneAngleUnit extends AngleUnit {
}



export interface Prefix extends Verifiable, Concept {
}



export interface Quantifiable extends Aspect {
}



export interface Quantity extends Quantifiable, Concept {
}



export interface QuantityKind extends Verifiable, AbstractQuantityKind {
    belongsToSystemOfQuantities?: SystemOfQuantityKinds[],
}



export interface QuantityKindDimensionVector extends Concept {
}



export interface QuantityKindDimensionVectorCGS extends QuantityKindDimensionVector {
}



export interface QuantityKindDimensionVectorCGS-EMU extends QuantityKindDimensionVectorCGS {
}



export interface QuantityKindDimensionVectorCGS-ESU extends QuantityKindDimensionVectorCGS {
}



export interface QuantityKindDimensionVectorCGS-GAUSS extends QuantityKindDimensionVectorCGS {
}



export interface QuantityKindDimensionVectorCGS-LH extends QuantityKindDimensionVectorCGS {
}



export interface QuantityKindDimensionVectorISO extends QuantityKindDimensionVector {
}



export interface QuantityKindDimensionVectorImperial extends QuantityKindDimensionVector {
}



export interface QuantityKindDimensionVectorSI extends QuantityKindDimensionVector {
}



export interface QuantityType extends EnumeratedValue {
}



export interface QuantityValue extends Quantifiable, Concept {
}



export interface RatioScale extends Scale {
}



export interface Rule extends Verifiable, Concept {
}



export interface RuleType extends EnumeratedValue {
}



export interface ScalarDatatype extends Datatype {
}



export interface Scale extends Concept {
}



export interface ScaleType extends EnumeratedValue {
}



export interface SignednessType {
}



export interface SolidAngleUnit extends AngleUnit {
}



export interface Statement {
}



export interface StringEncodingType {
}



export interface Symbol extends Concept {
}



export interface SymmetricRelation {
}



export interface SystemOfQuantityKinds extends Concept {
}



export interface SystemOfUnits extends Verifiable, Concept {
}



export interface TransformType extends EnumeratedValue {
}



export interface Unit extends Verifiable, Concept {
    hasReciprocalUnit?: Unit[],
    isUnitOfSystem?: SystemOfUnits[],
    omUnit?: string,
    unitFor?: string,
}



export interface UserQuantityKind extends AbstractQuantityKind {
}



export interface Verifiable extends Error3, Error2, Aspect {
}



export interface CatalogEntry {
}



export interface List {
}



export interface Class {
}



export interface Resource {
}



export interface GDay {
}



export interface GMonth {
}



export interface GMonthDay {
}



export interface GYear {
}



export interface GYearMonth {
}



export interface Ontology {
}



export interface LatexString {
}



export interface UCUMcs extends Resource {
}



export interface UCUMcs-term extends Resource {
}



export interface ValueUnion extends Resource {
}



