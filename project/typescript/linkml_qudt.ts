

/**
 * The root class for all QUDT concepts
 */
export interface Thing {
}


/**
 * Quantity Kind (abstract)
 */
export interface AbstractQuantityKind extends Concept {
}


/**
 * All units relating to specification of angles.
 */
export interface AngleUnit extends DimensionlessUnit {
}



export interface Aspect extends Thing {
}


/**
 * Aspect Class
 */
export interface AspectClass extends Class {
}


/**
 * <p class="lm-para">A <em>Dimension</em> expresses a magnitude for a base quantiy kind such as mass, length and time.</p>
<p class="lm-para">DEPRECATED - each exponent is expressed as a property. Keep until a validaiton of this has been done.</p>
 */
export interface BaseDimensionMagnitude extends Concept {
}


/**
 * A <em>Binary Prefix</em> is a prefix for multiples of units in data processing, data transmission, and digital information, notably the bit and the byte, to indicate multiplication by a power of 2.
 */
export interface BinaryPrefix extends Prefix {
}


/**
 * A bit encoding is a correspondence between the two possible values of a bit, 0 or 1, and some interpretation. For example, in a boolean encoding, a bit denotes a truth value, where 0 corresponds to False and 1 corresponds to True.
 */
export interface BitEncodingType extends Encoding {
}


/**
 * Boolean encoding type
 */
export interface BooleanEncodingType extends Encoding {
}


/**
 * This class contains the various ways that information may be encoded into bytes.
 */
export interface ByteEncodingType extends Encoding {
}


/**
 *
  In mathematics, the cardinality of a set is a measure of the number of elements of the set.
  For example, the set $A = {2, 4, 6}$ contains 3 elements, and therefore $A$ has a cardinality of 3.
  There are two approaches to cardinality: one which compares sets directly using bijections and injections,
   and another which uses cardinal numbers.

 */
export interface CardinalityType extends EnumeratedValue {
}


/**
 * The class of all character encoding schemes, each of which defines a rule or algorithm for encoding character data as a sequence of bits or bytes.
 */
export interface CharEncodingType extends Encoding {
}


/**
 * Provides a simple way of making citations.
 */
export interface Citation extends Concept {
}


/**
 * Comment
 */
export interface Comment extends Verifiable {
}


/**
 * The root class for all QUDT concepts.
 */
export interface Concept extends Thing {
    /** guidance */
    guidance?: string[],
    /** The "qudt:id" is an identifier string that uniquely identifies a QUDT concept.  The identifier is constructed using a prefix. For example, units are coded using the pattern: "UCCCENNNN", where "CCC" is a numeric code or a category and "NNNN" is a digit string for a member element of that category. For scaled units there may be an addition field that has the format "QNN" where "NN" is a digit string representing an exponent power, and "Q" is a qualifier that indicates with the code "P" that the power is a positive decimal exponent, or the code "N" for a negative decimal exponent, or the code "B" for binary positive exponents. */
    id?: string,
}


/**
 * Used to specify the values of a constant.
 */
export interface ConstantValue extends QuantityValue {
}


/**
 * Contextual Unit
 */
export interface ContextualUnit extends Unit {
}


/**
 * Used for all units that express counts. Examples are Atomic Number, Number, Number per Year, Percent and Sample per Second.
 */
export interface CountingUnit extends DimensionlessUnit {
}


/**
 * Currency Units have their own subclass of unit because: (a) they have additional properties such as 'country' and (b) their URIs do not conform to the same rules as other units.
 */
export interface CurrencyUnit extends DimensionlessUnit {
}


/**
 * <p><em>Data Encoding</em> expresses the properties that specify how data is represented at the bit and byte level. These properties are applicable to describing raw data.</p>
 */
export interface DataEncoding extends Aspect {
}


/**
 *
  <p>A <em>Data Item</em> holds a value that maybe a scalar or structured datatype.
  <em>Quantity Value</em> specifies which case applies.
  </p>
 */
export interface DataItem extends Concept {
}


/**
 *
   <p>A <em>Datatype</em> is a definition of the type of the "value" of a data item (for example, "all integers between 0 and 10"),
   and the allowable operations on those values; the meaning of the data; and the way values of that type can be stored.
  Some types are primitive - built-in to the language, with no visible internal structure.
  For example "Boolean"; others are composite - constructed from one or more other types (of either kind).
  For example lists, arrays, structures, unions.
  Some languages provide strong typing, others allow implicit type conversion and/or explicit type conversion.
  </p>
 */
export interface Datatype extends Concept {
}


/**
 * Date Time encodings are logical encodings for expressing date/time quantities as strings by applying unambiguous formatting and parsing rules.
 */
export interface DateTimeStringEncodingType extends StringEncodingType {
}


/**
 * A <em>Decimal Prefix</em> is a prefix for multiples of units that are powers of 10.
 */
export interface DecimalPrefix extends Prefix {
}


/**
 * A DerivedUnit is a type specification for units that are derived from other units.
 */
export interface DerivedUnit extends Unit {
}


/**
 * A Dimensionless Unit is a quantity for which all the exponents of the factors corresponding to the base quantities in its quantity dimension are zero.
 */
export interface DimensionlessUnit extends Unit {
}


/**
 * Discipline
 */
export interface Discipline extends Concept {
}


/**
 * An encoding is a rule or algorithm that is used to convert data from a native, or unspecified form into a specific form that satisfies the encoding rules. Examples of encodings include character encodings, such as UTF-8.
 */
export interface Encoding extends Concept {
}


/**
 * Endian Type
 */
export interface EndianType extends EnumeratedValue {
}



export interface EnumeratedQuantity extends Concept {
}


/**
 * <p>This class is for all enumerated and/or coded values.  For example, it contains the dimension objects that are the basis elements in some abstract vector space associated with a quantity kind system. Another use is for the base dimensions for quantity systems. Each quantity kind system that defines a base set has a corresponding ordered enumeration whose elements are the dimension objects for the base quantity kinds. The order of the dimensions in the enumeration determines the canonical order of the basis elements in the corresponding abstract vector space.</p>

<p>An enumeration is a set of literals from which a single value is selected. Each literal can have a tag as an integer within a standard encoding appropriate to the range of integer values. Consistency of enumeration types will allow them, and the enumerated values, to be referred to unambiguously either through symbolic name or encoding. Enumerated values are also controlled vocabularies and as such need to be standardized. Without this consistency enumeration literals can be stated differently and result in  data conflicts and misinterpretations.</p>

<p>The tags are a set of positive whole numbers, not necessarily contiguous and having no numerical significance, each corresponding to the associated literal identifier. An order attribute can also be given on the enumeration elements. An enumeration can itself be a member of an enumeration. This allows enumerations to be enumerated in a selection. Enumerations are also subclasses of Scalar Datatype. This allows them to be used as the reference of a datatype specification.</p>
 */
export interface EnumeratedValue extends Verifiable, Concept {
}


/**
 * <p>An enumeration is a set of literals from which a single value is selected. Each literal can have a tag as an integer within a standard encoding appropriate to the range of integer values. Consistency of enumeration types will allow them, and the enumerated values, to be referred to unambiguously either through symbolic name or encoding. Enumerated values are also controlled vocabularies and as such need to be standardized. Without this consistency enumeration literals can be stated differently and result in  data conflicts and misinterpretations.</p>

<p>The tags are a set of positive whole numbers, not necessarily contiguous and having no numerical significance, each corresponding to the associated literal identifier. An order attribute can also be given on the enumeration elements. An enumeration can itself be a member of an enumeration. This allows enumerations to be enumerated in a selection. Enumerations are also subclasses of <em>Scalar Datatype</em>. This allows them to be used as the reference of a datatype specification.</p>
 */
export interface Enumeration extends Concept {
}


/**
 * Enumeration scale
 */
export interface EnumerationScale extends Scale, Enumeration {
}


/**
 * Figure
 */
export interface Figure extends Concept {
}


/**
 * A "Encoding" with the following instance(s): "Double Precision Encoding", "Single Precision Real Encoding".
 */
export interface FloatingPointEncodingType extends Encoding {
}


/**
 * The encoding scheme for integer types
 */
export interface IntegerEncodingType extends Encoding {
}


/**
 * <p>The interval type allows for the degree of difference between items, but not the ratio between them. Examples include temperature with the Celsius scale, which has two defined points (the freezing and boiling point of water at specific conditions) and then separated into 100 intervals, date when measured from an arbitrary epoch (such as AD), percentage such as a percentage return on a stock,[16] location in Cartesian coordinates, and direction measured in degrees from true or magnetic north. Ratios are not meaningful since 20 °C cannot be said to be "twice as hot" as 10 °C, nor can multiplication/division be carried out between any two dates directly. However, ratios of differences can be expressed; for example, one difference can be twice another. Interval type variables are sometimes also called "scaled variables", but the formal mathematical term is an affine space (in this case an affine line).</p>
<p>Characteristics: median, percentile &amp; Monotonic increasing (order (&lt;) &amp; totally ordered set</p>
 */
export interface IntervalScale extends Scale {
}


/**
 * Logarithmic units are abstract mathematical units that can be used to express any quantities (physical or mathematical) that are defined on a logarithmic scale, that is, as being proportional to the value of a logarithm function. Examples of logarithmic units include common units of information and entropy, such as the bit, and the byte, as well as units of relative signal strength magnitude such as the decibel.
 */
export interface LogarithmicUnit extends DimensionlessUnit {
}


/**
 * Maths Function Type
 */
export interface MathsFunctionType extends Concept {
}


/**
 * NIST SP~811 Comment
 */
export interface NISTSP811Comment extends Comment {
}


/**
 * A nominal scale differentiates between items or subjects based only on their names or (meta-)categories and other qualitative classifications they belong to; thus dichotomous data involves the construction of classifications as well as the classification of items. Discovery of an exception to a classification can be viewed as progress. Numbers may be used to represent the variables but the numbers do not have numerical value or relationship: For example, a Globally unique identifier. Examples of these classifications include gender, nationality, ethnicity, language, genre, style, biological species, and form. In a university one could also use hall of affiliation as an example.
 */
export interface NominalScale extends Scale {
}


/**
 * Numeric union
 */
export interface NumericUnion extends Concept {
}


/**
 * Describes how a data or information structure is ordered.
 */
export interface OrderedType extends EnumeratedValue {
}


/**
 * The ordinal type allows for rank order (1st, 2nd, 3rd, etc.) by which data can be sorted, but still does not allow for relative degree of difference between them. Examples include, on one hand, dichotomous data with dichotomous (or dichotomized) values such as 'sick' vs. 'healthy' when measuring health, 'guilty' vs. 'innocent' when making judgments in courts, 'wrong/false' vs. 'right/true' when measuring truth value, and, on the other hand, non-dichotomous data consisting of a spectrum of values, such as 'completely agree', 'mostly agree', 'mostly disagree', 'completely disagree' when measuring opinion.
 */
export interface OrdinalScale extends Scale {
}


/**
 * Organization
 */
export interface Organization extends Concept {
}


/**
 * A physical constant is a physical quantity that is generally believed to be both universal in nature and constant in time. It can be contrasted with a mathematical constant, which is a fixed numerical value but does not directly involve any physical measurement. There are many physical constants in science, some of the most widely recognized being the speed of light in vacuum c, Newton's gravitational constant G, Planck's constant h, the electric permittivity of free space ε0, and the elementary charge e. Physical constants can take many dimensional forms, or may be dimensionless depending on the system of quantities and units used.
 */
export interface PhysicalConstant extends Quantity {
}


/**
 * Plane Angle Unit
 */
export interface PlaneAngleUnit extends AngleUnit {
}


/**
 * Prefix
 */
export interface Prefix extends Verifiable, Concept {
}


/**
 * <p><em>Quantifiable</em> ascribes to some thing the capability of being measured, observed, or counted.</p>
 */
export interface Quantifiable extends Aspect {
}


/**
 * <p class="lm-para">A <b>quantity</b> is the measurement of an observable property of a particular object, event, or physical system.
  A quantity is always associated with the context of measurement (i.e. the thing measured, the measured value, the accuracy of measurement, etc.) whereas the
  underlying <b>quantity kind</b> is independent of any particular measurement. Thus, length is a quantity kind while the height of a rocket is a specific
  quantity of length; its magnitude that may be expressed in meters, feet, inches, etc. Examples of physical quantities include physical constants, such as
  the speed of light in a vacuum, Planck's constant, the electric permittivity of free space, and the fine structure constant. </p>
<p class="lm-para">In other words, quantities are quantifiable aspects of the world, such as the duration of a movie, the distance between two points,
velocity of a car, the pressure of the atmosphere, and a person's weight; and units are used to describe their numerical measure.</p>
<p class="lm-para">Many <b>quantity kinds</b> are related to each other by various physical laws, and as a result, the associated units of some quantity
kinds can be expressed as products (or ratios) of powers of other quantity kinds (e.g., momentum is mass times velocity and velocity is defined as distance
divided by time). In this way, some quantities can be calculated from other measured quantities using their associations to the quantity kinds in these
expressions. These quantity kind relationships are also discussed in dimensional analysis. Those that cannot be so expressed can be regarded
as "fundamental" in this sense.</p>
<p class="lm-para">A quantity is distinguished from a "quantity kind" in that the former carries a value and the latter is a type specifier.</p>
 */
export interface Quantity extends Quantifiable, Concept {
}


/**
 * A <b>Quantity Kind</b> is any observable property that can be measured and quantified numerically. Familiar examples include physical properties such as length, mass, time, force, energy, power, electric charge, etc. Less familiar examples include currency, interest rate, price to earning ratio, and information capacity.
 */
export interface QuantityKind extends Verifiable, AbstractQuantityKind {
    /** belongs to system of quantities */
    belongsToSystemOfQuantities?: SystemOfQuantityKinds[],
}


/**
 * <p class="lm-para">A  <em>Quantity Kind Dimension Vector</em> describes the dimensionality of a quantity kind in the context of a system of units. In the SI system of units, the dimensions of a quantity kind are expressed as a product of the basic physical dimensions mass ($M$), length ($L$), time ($T$) current ($I$), amount of substance ($N$), luminous intensity ($J$) and absolute temperature ($\theta$) as $dim \, Q = L^{\alpha} \, M^{\beta} \, T^{\gamma} \, I ^{\delta} \, \theta ^{\epsilon} \, N^{\eta} \, J ^{\nu}$.</p>

<p class="lm-para">The rational powers of the dimensional exponents, $\alpha, \, \beta, \, \gamma, \, \delta, \, \epsilon, \ , \eta, \, \nu$, are positive, negative, or zero.</p>

<p class="lm-para">For example, the dimension of the physical quantity kind $\it{speed}$ is $\ boxed{length/time}$, $L/T$ or $LT^{-1}$, and the dimension of the physical quantity kind force is $\boxed{mass \times acceleration}$ or $\boxed{mass \times (length/time)/time}$, $ML/T^2$ or $MLT^{-2}$ respectively.</p>
 */
export interface QuantityKindDimensionVector extends Concept {
}


/**
 * A <em>CGS Dimension Vector</em> is used to specify the dimensions for a C.G.S. quantity kind.
 */
export interface QuantityKindDimensionVectorCGS extends QuantityKindDimensionVector {
}


/**
 * A <em>CGS EMU Dimension Vector</em> is used to specify the dimensions for EMU C.G.S. quantity kind.
 */
export interface QuantityKindDimensionVectorCGS-EMU extends QuantityKindDimensionVectorCGS {
}


/**
 * A <em>CGS ESU Dimension Vector</em> is used to specify the dimensions for ESU C.G.S. quantity kind.
 */
export interface QuantityKindDimensionVectorCGS-ESU extends QuantityKindDimensionVectorCGS {
}


/**
 * A <em>CGS GAUSS Dimension Vector</em> is used to specify the dimensions for Gaussioan C.G.S. quantity kind.
 */
export interface QuantityKindDimensionVectorCGS-GAUSS extends QuantityKindDimensionVectorCGS {
}


/**
 * A <em>CGS LH Dimension Vector</em> is used to specify the dimensions for Lorentz-Heaviside C.G.S. quantity kind.
 */
export interface QuantityKindDimensionVectorCGS-LH extends QuantityKindDimensionVectorCGS {
}


/**
 * ISO Dimension vector
 */
export interface QuantityKindDimensionVectorISO extends QuantityKindDimensionVector {
}


/**
 * Imperial dimension vector
 */
export interface QuantityKindDimensionVectorImperial extends QuantityKindDimensionVector {
}


/**
 * Quantity Kind Dimension vector (SI)
 */
export interface QuantityKindDimensionVectorSI extends QuantityKindDimensionVector {
}


/**
 *
  A $\textit{Quantity Type}$ is an enumeration of quantity kinds.
  It specializes $\boxed{dtype:EnumeratedValue}$ by constrinaing $\boxed{dtype:value}$ to instances of $\boxed{qudt:QuantityKind}$.

 */
export interface QuantityType extends EnumeratedValue {
}


/**
 * A <i>Quantity Value</i> expresses the magnitude and kind of a quantity and is given by the product of a numerical value <code>n</code> and a unit of measure <code>U</code>. The number multiplying the unit is referred to as the numerical value of the quantity expressed in that unit. Refer to <a href="http://physics.nist.gov/Pubs/SP811/sec07.html">NIST SP 811 section 7</a> for more on quantity values.
 */
export interface QuantityValue extends Quantifiable, Concept {
}


/**
 * The ratio type takes its name from the fact that measurement is the estimation of the ratio between a magnitude of a continuous quantity and a unit magnitude of the same kind (Michell, 1997, 1999). A ratio scale possesses a meaningful (unique and non-arbitrary) zero value. Most measurement in the physical sciences and engineering is done on ratio scales. Examples include mass, length, duration, plane angle, energy and electric charge. In contrast to interval scales, ratios are now meaningful because having a non-arbitrary zero point makes it meaningful to say, for example, that one object has "twice the length" of another (= is "twice as long"). Very informally, many ratio scales can be described as specifying "how much" of something (i.e. an amount or magnitude) or "how many" (a count). The Kelvin temperature scale is a ratio scale because it has a unique, non-arbitrary zero point called absolute zero.
 */
export interface RatioScale extends Scale {
}


/**
 * Rule
 */
export interface Rule extends Verifiable, Concept {
}


/**
 * Rule Type
 */
export interface RuleType extends EnumeratedValue {
}


/**
 * Scalar data types are those that have a single value. The permissible values are defined over a domain that may be integers, float, character or boolean. Often a scalar data type is referred to as a primitive data type.
 */
export interface ScalarDatatype extends Datatype {
}


/**
 * Scales (also called "scales of measurement" or "levels of measurement")  are expressions that typically refer to the theory of scale types.
 */
export interface Scale extends Concept {
}


/**
 * Scale type
 */
export interface ScaleType extends EnumeratedValue {
}



export interface SignednessType {
}


/**
 * The solid angle subtended by a surface S is defined as the surface area of a unit sphere covered by the surface S's projection onto the sphere. A solid angle is related to the surface of a sphere in the same way an ordinary angle is related to the circumference of a circle. Since the total surface area of the unit sphere is 4*pi, the measure of solid angle will always be between 0 and 4*pi.
 */
export interface SolidAngleUnit extends AngleUnit {
}



export interface Statement {
}



export interface StringEncodingType {
}


/**
 * Symbol
 */
export interface Symbol extends Concept {
}



export interface SymmetricRelation {
}


/**
 * A system of quantity kinds is a set of one or more quantity kinds together with a set of zero or more algebraic equations that define relationships between quantity kinds in the set. In the physical sciences, the equations relating quantity kinds are typically physical laws and definitional relations, and constants of proportionality. Examples include Newton’s First Law of Motion, Coulomb’s Law, and the definition of velocity as the instantaneous change in position.  In almost all cases, the system identifies a subset of base quantity kinds. The base set is chosen so that all other quantity kinds of interest can be derived from the base quantity kinds and the algebraic equations. If the unit system is explicitly associated with a quantity kind system, then the unit system must define at least one unit for each quantity kind.  From a scientific point of view, the division of quantities into base quantities and derived quantities is a matter of convention.
 */
export interface SystemOfQuantityKinds extends Concept {
}


/**
 * A system of units is a set of units which are chosen as the reference scales for some set of quantity kinds together with the definitions of each unit. Units may be defined by experimental observation or by proportion to another unit not included in the system. If the unit system is explicitly associated with a quantity kind system, then the unit system must define at least one unit for each quantity kind.
 */
export interface SystemOfUnits extends Verifiable, Concept {
}


/**
 * Transform type
 */
export interface TransformType extends EnumeratedValue {
}


/**
 *
  A unit of measure, or unit, is a particular quantity value that has been chosen as a scale for measuring other quantities the same kind (more generally of equivalent dimension).
  For example, the meter is a quantity of length that has been rigorously defined and standardized by the BIPM (International Board of Weights and Measures).
  Any measurement of the length can be expressed as a number multiplied by the unit meter.
  More formally, the value of a physical quantity Q with respect to a unit (U) is expressed as the scalar multiple of a real number (n) and U, as  $Q = nU$.

 */
export interface Unit extends Verifiable, Concept {
    /** has reciprocal unit */
    hasReciprocalUnit?: Unit[],
    /** This property relates a unit of measure with a system of units that either a) defines the unit or b) allows the unit to be used within the system. */
    isUnitOfSystem?: SystemOfUnits[],
    /** om unit */
    omUnit?: string,
    /** unit for */
    unitFor?: string,
}


/**
 * User Quantity Kind
 */
export interface UserQuantityKind extends AbstractQuantityKind {
}



export interface Verifiable extends Aspect {
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


/**
 * A type of string in which some characters may be wrapped with '$' and '$ characters for LaTeX rendering.
 */
export interface LatexString {
}


/**
 * Lexical pattern for the case-sensitive version of UCUM code
 */
export interface UCUMcs extends Resource {
}


/**
 * Lexical pattern for the terminal symbols in the case-sensitive version of UCUM code
 */
export interface UCUMcs-term extends Resource {
}


/**
 * A datatype that is the union of numeric xsd data types. "numericUnion" is equivalent to the xsd specification that uses an xsd:union of memberTypes="xsd:decimal xsd:double xsd:float xsd:integer".
 */
export interface ValueUnion extends Resource {
}
