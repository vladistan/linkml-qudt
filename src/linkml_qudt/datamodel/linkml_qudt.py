# Auto generated from linkml_qudt.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-10-25T14:32:24
# Schema: qudt
#
# id: http://qudt.org/3.1.6/schema/qudt
# description: qudt
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Date, Decimal, Double, Float, String, Uri
from linkml_runtime.utils.metamodelcore import Bool, Decimal, URI, XSDDate

metamodel_version = "1.7.0"
version = None

# Namespaces
DC = CurieNamespace('dc', 'http://example.org/UNKNOWN/dc/')
DCTERMS = CurieNamespace('dcterms', 'http://example.org/UNKNOWN/dcterms/')
DTYPE = CurieNamespace('dtype', 'http://example.org/UNKNOWN/dtype/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PROV = CurieNamespace('prov', 'http://example.org/UNKNOWN/prov/')
QUDT = CurieNamespace('qudt', 'https://w3id.org/None/')
RDF = CurieNamespace('rdf', 'http://example.org/UNKNOWN/rdf/')
RDFS = CurieNamespace('rdfs', 'http://example.org/UNKNOWN/rdfs/')
VAEM = CurieNamespace('vaem', 'http://example.org/UNKNOWN/vaem/')
VOAG = CurieNamespace('voag', 'http://example.org/UNKNOWN/voag/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = QUDT


# Types

# Class references



class Thing(YAMLRoot):
    """
    The root class for all QUDT concepts
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL["Thing"]
    class_class_curie: ClassVar[str] = "owl:Thing"
    class_name: ClassVar[str] = "Thing"
    class_model_uri: ClassVar[URIRef] = QUDT.Thing


class Error1(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://org.semanticweb.owlapi/error#Error1")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Error1"
    class_model_uri: ClassVar[URIRef] = QUDT.Error1


class Error2(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://org.semanticweb.owlapi/error#Error2")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Error2"
    class_model_uri: ClassVar[URIRef] = QUDT.Error2


class Error3(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://org.semanticweb.owlapi/error#Error3")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Error3"
    class_model_uri: ClassVar[URIRef] = QUDT.Error3


class Aspect(Thing):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Aspect"]
    class_class_curie: ClassVar[str] = "qudt:Aspect"
    class_name: ClassVar[str] = "Aspect"
    class_model_uri: ClassVar[URIRef] = QUDT.Aspect


@dataclass(repr=False)
class Concept(Thing):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Concept"]
    class_class_curie: ClassVar[str] = "qudt:Concept"
    class_name: ClassVar[str] = "Concept"
    class_model_uri: ClassVar[URIRef] = QUDT.Concept

    guidance: Optional[Union[str, list[str]]] = empty_list()
    id: Optional[Union[str, list[str]]] = empty_list()
    hasRule: Optional[Union[Union[dict, "Rule"], list[Union[dict, "Rule"]]]] = empty_list()
    isReplacedBy: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[Union[str, list[str]]] = empty_list()
    abbreviation: Optional[Union[str, list[str]]] = empty_list()
    deprecated: Optional[Union[str, list[str]]] = empty_list()
    plainTextDescription: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.guidance, list):
            self.guidance = [self.guidance] if self.guidance is not None else []
        self.guidance = [v if isinstance(v, str) else str(v) for v in self.guidance]

        if not isinstance(self.id, list):
            self.id = [self.id] if self.id is not None else []
        self.id = [v if isinstance(v, str) else str(v) for v in self.id]

        if not isinstance(self.hasRule, list):
            self.hasRule = [self.hasRule] if self.hasRule is not None else []
        self.hasRule = [v if isinstance(v, Rule) else Rule(**as_dict(v)) for v in self.hasRule]

        if not isinstance(self.isReplacedBy, list):
            self.isReplacedBy = [self.isReplacedBy] if self.isReplacedBy is not None else []
        self.isReplacedBy = [v if isinstance(v, str) else str(v) for v in self.isReplacedBy]

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.abbreviation, list):
            self.abbreviation = [self.abbreviation] if self.abbreviation is not None else []
        self.abbreviation = [v if isinstance(v, str) else str(v) for v in self.abbreviation]

        if not isinstance(self.deprecated, list):
            self.deprecated = [self.deprecated] if self.deprecated is not None else []
        self.deprecated = [v if isinstance(v, str) else str(v) for v in self.deprecated]

        if not isinstance(self.plainTextDescription, list):
            self.plainTextDescription = [self.plainTextDescription] if self.plainTextDescription is not None else []
        self.plainTextDescription = [v if isinstance(v, str) else str(v) for v in self.plainTextDescription]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AbstractQuantityKind(Concept):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["AbstractQuantityKind"]
    class_class_curie: ClassVar[str] = "qudt:AbstractQuantityKind"
    class_name: ClassVar[str] = "AbstractQuantityKind"
    class_model_uri: ClassVar[URIRef] = QUDT.AbstractQuantityKind

    broader: Optional[Union[dict, "QuantityKind"]] = None
    altSymbol: Optional[Union[str, list[str]]] = empty_list()
    latexSymbol: Optional[Union[str, list[str]]] = empty_list()
    symbol: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.broader is not None and not isinstance(self.broader, QuantityKind):
            self.broader = QuantityKind(**as_dict(self.broader))

        if not isinstance(self.altSymbol, list):
            self.altSymbol = [self.altSymbol] if self.altSymbol is not None else []
        self.altSymbol = [v if isinstance(v, str) else str(v) for v in self.altSymbol]

        if not isinstance(self.latexSymbol, list):
            self.latexSymbol = [self.latexSymbol] if self.latexSymbol is not None else []
        self.latexSymbol = [v if isinstance(v, str) else str(v) for v in self.latexSymbol]

        if not isinstance(self.symbol, list):
            self.symbol = [self.symbol] if self.symbol is not None else []
        self.symbol = [v if isinstance(v, str) else str(v) for v in self.symbol]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BaseDimensionMagnitude(Concept):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["BaseDimensionMagnitude"]
    class_class_curie: ClassVar[str] = "qudt:BaseDimensionMagnitude"
    class_name: ClassVar[str] = "BaseDimensionMagnitude"
    class_model_uri: ClassVar[URIRef] = QUDT.BaseDimensionMagnitude

    hasBaseQuantityKind: Union[Union[dict, "QuantityKind"], list[Union[dict, "QuantityKind"]]] = None
    vectorMagnitude: Union[float, list[float]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.hasBaseQuantityKind):
            self.MissingRequiredField("hasBaseQuantityKind")
        if not isinstance(self.hasBaseQuantityKind, list):
            self.hasBaseQuantityKind = [self.hasBaseQuantityKind] if self.hasBaseQuantityKind is not None else []
        self.hasBaseQuantityKind = [v if isinstance(v, QuantityKind) else QuantityKind(**as_dict(v)) for v in self.hasBaseQuantityKind]

        if self._is_empty(self.vectorMagnitude):
            self.MissingRequiredField("vectorMagnitude")
        if not isinstance(self.vectorMagnitude, list):
            self.vectorMagnitude = [self.vectorMagnitude] if self.vectorMagnitude is not None else []
        self.vectorMagnitude = [v if isinstance(v, float) else float(v) for v in self.vectorMagnitude]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Citation(Concept):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Citation"]
    class_class_curie: ClassVar[str] = "qudt:Citation"
    class_name: ClassVar[str] = "Citation"
    class_model_uri: ClassVar[URIRef] = QUDT.Citation

    description: Union[str, list[str]] = None
    url: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.url, list):
            self.url = [self.url] if self.url is not None else []
        self.url = [v if isinstance(v, str) else str(v) for v in self.url]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataEncoding(Aspect):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["DataEncoding"]
    class_class_curie: ClassVar[str] = "qudt:DataEncoding"
    class_name: ClassVar[str] = "DataEncoding"
    class_model_uri: ClassVar[URIRef] = QUDT.DataEncoding

    bitOrder: Optional[Union[Union[dict, "EndianType"], list[Union[dict, "EndianType"]]]] = empty_list()
    encoding: Optional[Union[Union[dict, "Encoding"], list[Union[dict, "Encoding"]]]] = empty_list()
    byteOrder: Optional[Union[Union[dict, "EndianType"], list[Union[dict, "EndianType"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.bitOrder, list):
            self.bitOrder = [self.bitOrder] if self.bitOrder is not None else []
        self.bitOrder = [v if isinstance(v, EndianType) else EndianType(**as_dict(v)) for v in self.bitOrder]

        if not isinstance(self.encoding, list):
            self.encoding = [self.encoding] if self.encoding is not None else []
        self.encoding = [v if isinstance(v, Encoding) else Encoding(**as_dict(v)) for v in self.encoding]

        if not isinstance(self.byteOrder, list):
            self.byteOrder = [self.byteOrder] if self.byteOrder is not None else []
        self.byteOrder = [v if isinstance(v, EndianType) else EndianType(**as_dict(v)) for v in self.byteOrder]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataItem(Concept):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["DataItem"]
    class_class_curie: ClassVar[str] = "qudt:DataItem"
    class_name: ClassVar[str] = "DataItem"
    class_model_uri: ClassVar[URIRef] = QUDT.DataItem

    value: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.value, list):
            self.value = [self.value] if self.value is not None else []
        self.value = [v if isinstance(v, str) else str(v) for v in self.value]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Datatype(Concept):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RDFS["Datatype"]
    class_class_curie: ClassVar[str] = "rdfs:Datatype"
    class_name: ClassVar[str] = "Datatype"
    class_model_uri: ClassVar[URIRef] = QUDT.Datatype

    basis: Optional[Union[Union[dict, "Datatype"], list[Union[dict, "Datatype"]]]] = empty_list()
    cardinality: Optional[Union[Union[dict, "CardinalityType"], list[Union[dict, "CardinalityType"]]]] = empty_list()
    orderedType: Optional[Union[Union[dict, "OrderedType"], list[Union[dict, "OrderedType"]]]] = empty_list()
    ansiSQLName: Optional[Union[str, list[str]]] = empty_list()
    cName: Optional[Union[str, list[str]]] = empty_list()
    oracleSQLName: Optional[Union[str, list[str]]] = empty_list()
    protocolBuffersName: Optional[Union[str, list[str]]] = empty_list()
    pythonName: Optional[Union[str, list[str]]] = empty_list()
    vbName: Optional[Union[str, list[str]]] = empty_list()
    bounded: Optional[Union[str, list[str]]] = empty_list()
    id: Optional[Union[str, list[str]]] = empty_list()
    javaName: Optional[Union[str, list[str]]] = empty_list()
    jsName: Optional[Union[str, list[str]]] = empty_list()
    matlabName: Optional[Union[str, list[str]]] = empty_list()
    microsoftSQLServerName: Optional[Union[str, list[str]]] = empty_list()
    mySQLName: Optional[Union[str, list[str]]] = empty_list()
    odbcName: Optional[Union[str, list[str]]] = empty_list()
    oleDBName: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.basis, list):
            self.basis = [self.basis] if self.basis is not None else []
        self.basis = [v if isinstance(v, Datatype) else Datatype(**as_dict(v)) for v in self.basis]

        if not isinstance(self.cardinality, list):
            self.cardinality = [self.cardinality] if self.cardinality is not None else []
        self.cardinality = [v if isinstance(v, CardinalityType) else CardinalityType(**as_dict(v)) for v in self.cardinality]

        if not isinstance(self.orderedType, list):
            self.orderedType = [self.orderedType] if self.orderedType is not None else []
        self.orderedType = [v if isinstance(v, OrderedType) else OrderedType(**as_dict(v)) for v in self.orderedType]

        if not isinstance(self.ansiSQLName, list):
            self.ansiSQLName = [self.ansiSQLName] if self.ansiSQLName is not None else []
        self.ansiSQLName = [v if isinstance(v, str) else str(v) for v in self.ansiSQLName]

        if not isinstance(self.cName, list):
            self.cName = [self.cName] if self.cName is not None else []
        self.cName = [v if isinstance(v, str) else str(v) for v in self.cName]

        if not isinstance(self.oracleSQLName, list):
            self.oracleSQLName = [self.oracleSQLName] if self.oracleSQLName is not None else []
        self.oracleSQLName = [v if isinstance(v, str) else str(v) for v in self.oracleSQLName]

        if not isinstance(self.protocolBuffersName, list):
            self.protocolBuffersName = [self.protocolBuffersName] if self.protocolBuffersName is not None else []
        self.protocolBuffersName = [v if isinstance(v, str) else str(v) for v in self.protocolBuffersName]

        if not isinstance(self.pythonName, list):
            self.pythonName = [self.pythonName] if self.pythonName is not None else []
        self.pythonName = [v if isinstance(v, str) else str(v) for v in self.pythonName]

        if not isinstance(self.vbName, list):
            self.vbName = [self.vbName] if self.vbName is not None else []
        self.vbName = [v if isinstance(v, str) else str(v) for v in self.vbName]

        if not isinstance(self.bounded, list):
            self.bounded = [self.bounded] if self.bounded is not None else []
        self.bounded = [v if isinstance(v, str) else str(v) for v in self.bounded]

        if not isinstance(self.id, list):
            self.id = [self.id] if self.id is not None else []
        self.id = [v if isinstance(v, str) else str(v) for v in self.id]

        if not isinstance(self.javaName, list):
            self.javaName = [self.javaName] if self.javaName is not None else []
        self.javaName = [v if isinstance(v, str) else str(v) for v in self.javaName]

        if not isinstance(self.jsName, list):
            self.jsName = [self.jsName] if self.jsName is not None else []
        self.jsName = [v if isinstance(v, str) else str(v) for v in self.jsName]

        if not isinstance(self.matlabName, list):
            self.matlabName = [self.matlabName] if self.matlabName is not None else []
        self.matlabName = [v if isinstance(v, str) else str(v) for v in self.matlabName]

        if not isinstance(self.microsoftSQLServerName, list):
            self.microsoftSQLServerName = [self.microsoftSQLServerName] if self.microsoftSQLServerName is not None else []
        self.microsoftSQLServerName = [v if isinstance(v, str) else str(v) for v in self.microsoftSQLServerName]

        if not isinstance(self.mySQLName, list):
            self.mySQLName = [self.mySQLName] if self.mySQLName is not None else []
        self.mySQLName = [v if isinstance(v, str) else str(v) for v in self.mySQLName]

        if not isinstance(self.odbcName, list):
            self.odbcName = [self.odbcName] if self.odbcName is not None else []
        self.odbcName = [v if isinstance(v, str) else str(v) for v in self.odbcName]

        if not isinstance(self.oleDBName, list):
            self.oleDBName = [self.oleDBName] if self.oleDBName is not None else []
        self.oleDBName = [v if isinstance(v, str) else str(v) for v in self.oleDBName]

        super().__post_init__(**kwargs)


class Discipline(Concept):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Discipline"]
    class_class_curie: ClassVar[str] = "qudt:Discipline"
    class_name: ClassVar[str] = "Discipline"
    class_model_uri: ClassVar[URIRef] = QUDT.Discipline


@dataclass(repr=False)
class Encoding(Concept):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Encoding"]
    class_class_curie: ClassVar[str] = "qudt:Encoding"
    class_name: ClassVar[str] = "Encoding"
    class_model_uri: ClassVar[URIRef] = QUDT.Encoding

    bits: Optional[Union[str, list[str]]] = empty_list()
    bytes: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.bits, list):
            self.bits = [self.bits] if self.bits is not None else []
        self.bits = [v if isinstance(v, str) else str(v) for v in self.bits]

        if not isinstance(self.bytes, list):
            self.bytes = [self.bytes] if self.bytes is not None else []
        self.bytes = [v if isinstance(v, str) else str(v) for v in self.bytes]

        super().__post_init__(**kwargs)


class BitEncodingType(Encoding):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["BitEncodingType"]
    class_class_curie: ClassVar[str] = "qudt:BitEncodingType"
    class_name: ClassVar[str] = "BitEncodingType"
    class_model_uri: ClassVar[URIRef] = QUDT.BitEncodingType


class BooleanEncodingType(Encoding):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["BooleanEncodingType"]
    class_class_curie: ClassVar[str] = "qudt:BooleanEncodingType"
    class_name: ClassVar[str] = "BooleanEncodingType"
    class_model_uri: ClassVar[URIRef] = QUDT.BooleanEncodingType


class ByteEncodingType(Encoding):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["ByteEncodingType"]
    class_class_curie: ClassVar[str] = "qudt:ByteEncodingType"
    class_name: ClassVar[str] = "ByteEncodingType"
    class_model_uri: ClassVar[URIRef] = QUDT.ByteEncodingType


class CharEncodingType(Encoding):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["CharEncodingType"]
    class_class_curie: ClassVar[str] = "qudt:CharEncodingType"
    class_name: ClassVar[str] = "CharEncodingType"
    class_model_uri: ClassVar[URIRef] = QUDT.CharEncodingType


@dataclass(repr=False)
class EnumeratedQuantity(Concept):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["EnumeratedQuantity"]
    class_class_curie: ClassVar[str] = "qudt:EnumeratedQuantity"
    class_name: ClassVar[str] = "EnumeratedQuantity"
    class_model_uri: ClassVar[URIRef] = QUDT.EnumeratedQuantity

    enumeratedValue: Optional[Union[Union[dict, "EnumeratedValue"], list[Union[dict, "EnumeratedValue"]]]] = empty_list()
    enumeration: Optional[Union[Union[dict, "Enumeration"], list[Union[dict, "Enumeration"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.enumeratedValue, list):
            self.enumeratedValue = [self.enumeratedValue] if self.enumeratedValue is not None else []
        self.enumeratedValue = [v if isinstance(v, EnumeratedValue) else EnumeratedValue(**as_dict(v)) for v in self.enumeratedValue]

        if not isinstance(self.enumeration, list):
            self.enumeration = [self.enumeration] if self.enumeration is not None else []
        self.enumeration = [v if isinstance(v, Enumeration) else Enumeration(**as_dict(v)) for v in self.enumeration]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Enumeration(Concept):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Enumeration"]
    class_class_curie: ClassVar[str] = "qudt:Enumeration"
    class_name: ClassVar[str] = "Enumeration"
    class_model_uri: ClassVar[URIRef] = QUDT.Enumeration

    element: Union[Union[dict, "EnumeratedValue"], list[Union[dict, "EnumeratedValue"]]] = None
    default: Optional[Union[Union[dict, "EnumeratedValue"], list[Union[dict, "EnumeratedValue"]]]] = empty_list()
    abbreviation: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.element):
            self.MissingRequiredField("element")
        if not isinstance(self.element, list):
            self.element = [self.element] if self.element is not None else []
        self.element = [v if isinstance(v, EnumeratedValue) else EnumeratedValue(**as_dict(v)) for v in self.element]

        if not isinstance(self.default, list):
            self.default = [self.default] if self.default is not None else []
        self.default = [v if isinstance(v, EnumeratedValue) else EnumeratedValue(**as_dict(v)) for v in self.default]

        if not isinstance(self.abbreviation, list):
            self.abbreviation = [self.abbreviation] if self.abbreviation is not None else []
        self.abbreviation = [v if isinstance(v, str) else str(v) for v in self.abbreviation]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Figure(Concept):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Figure"]
    class_class_curie: ClassVar[str] = "qudt:Figure"
    class_name: ClassVar[str] = "Figure"
    class_model_uri: ClassVar[URIRef] = QUDT.Figure

    imageLocation: Union[str, list[str]] = None
    figureCaption: Optional[Union[str, list[str]]] = empty_list()
    figureLabel: Optional[Union[str, list[str]]] = empty_list()
    height: Optional[Union[str, list[str]]] = empty_list()
    image: Optional[Union[str, list[str]]] = empty_list()
    landscape: Optional[Union[str, list[str]]] = empty_list()
    width: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.imageLocation):
            self.MissingRequiredField("imageLocation")
        if not isinstance(self.imageLocation, list):
            self.imageLocation = [self.imageLocation] if self.imageLocation is not None else []
        self.imageLocation = [v if isinstance(v, str) else str(v) for v in self.imageLocation]

        if not isinstance(self.figureCaption, list):
            self.figureCaption = [self.figureCaption] if self.figureCaption is not None else []
        self.figureCaption = [v if isinstance(v, str) else str(v) for v in self.figureCaption]

        if not isinstance(self.figureLabel, list):
            self.figureLabel = [self.figureLabel] if self.figureLabel is not None else []
        self.figureLabel = [v if isinstance(v, str) else str(v) for v in self.figureLabel]

        if not isinstance(self.height, list):
            self.height = [self.height] if self.height is not None else []
        self.height = [v if isinstance(v, str) else str(v) for v in self.height]

        if not isinstance(self.image, list):
            self.image = [self.image] if self.image is not None else []
        self.image = [v if isinstance(v, str) else str(v) for v in self.image]

        if not isinstance(self.landscape, list):
            self.landscape = [self.landscape] if self.landscape is not None else []
        self.landscape = [v if isinstance(v, str) else str(v) for v in self.landscape]

        if not isinstance(self.width, list):
            self.width = [self.width] if self.width is not None else []
        self.width = [v if isinstance(v, str) else str(v) for v in self.width]

        super().__post_init__(**kwargs)


class FloatingPointEncodingType(Encoding):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["FloatingPointEncodingType"]
    class_class_curie: ClassVar[str] = "qudt:FloatingPointEncodingType"
    class_name: ClassVar[str] = "FloatingPointEncodingType"
    class_model_uri: ClassVar[URIRef] = QUDT.FloatingPointEncodingType


class IntegerEncodingType(Encoding):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["IntegerEncodingType"]
    class_class_curie: ClassVar[str] = "qudt:IntegerEncodingType"
    class_name: ClassVar[str] = "IntegerEncodingType"
    class_model_uri: ClassVar[URIRef] = QUDT.IntegerEncodingType


class MathsFunctionType(Concept):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["MathsFunctionType"]
    class_class_curie: ClassVar[str] = "qudt:MathsFunctionType"
    class_name: ClassVar[str] = "MathsFunctionType"
    class_model_uri: ClassVar[URIRef] = QUDT.MathsFunctionType


@dataclass(repr=False)
class NumericUnion(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["NumericUnion"]
    class_class_curie: ClassVar[str] = "qudt:NumericUnion"
    class_name: ClassVar[str] = "NumericUnion"
    class_model_uri: ClassVar[URIRef] = QUDT.NumericUnion

    guidance: Optional[Union[str, list[str]]] = empty_list()
    id: Optional[Union[str, list[str]]] = empty_list()
    hasRule: Optional[Union[Union[dict, "Rule"], list[Union[dict, "Rule"]]]] = empty_list()
    isReplacedBy: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[Union[str, list[str]]] = empty_list()
    abbreviation: Optional[Union[str, list[str]]] = empty_list()
    deprecated: Optional[Union[str, list[str]]] = empty_list()
    plainTextDescription: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.guidance, list):
            self.guidance = [self.guidance] if self.guidance is not None else []
        self.guidance = [v if isinstance(v, str) else str(v) for v in self.guidance]

        if not isinstance(self.id, list):
            self.id = [self.id] if self.id is not None else []
        self.id = [v if isinstance(v, str) else str(v) for v in self.id]

        if not isinstance(self.hasRule, list):
            self.hasRule = [self.hasRule] if self.hasRule is not None else []
        self.hasRule = [v if isinstance(v, Rule) else Rule(**as_dict(v)) for v in self.hasRule]

        if not isinstance(self.isReplacedBy, list):
            self.isReplacedBy = [self.isReplacedBy] if self.isReplacedBy is not None else []
        self.isReplacedBy = [v if isinstance(v, str) else str(v) for v in self.isReplacedBy]

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.abbreviation, list):
            self.abbreviation = [self.abbreviation] if self.abbreviation is not None else []
        self.abbreviation = [v if isinstance(v, str) else str(v) for v in self.abbreviation]

        if not isinstance(self.deprecated, list):
            self.deprecated = [self.deprecated] if self.deprecated is not None else []
        self.deprecated = [v if isinstance(v, str) else str(v) for v in self.deprecated]

        if not isinstance(self.plainTextDescription, list):
            self.plainTextDescription = [self.plainTextDescription] if self.plainTextDescription is not None else []
        self.plainTextDescription = [v if isinstance(v, str) else str(v) for v in self.plainTextDescription]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Organization(Concept):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Organization"]
    class_class_curie: ClassVar[str] = "qudt:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = QUDT.Organization

    url: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.url, list):
            self.url = [self.url] if self.url is not None else []
        self.url = [v if isinstance(v, str) else str(v) for v in self.url]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Quantifiable(Aspect):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantifiable"]
    class_class_curie: ClassVar[str] = "qudt:Quantifiable"
    class_name: ClassVar[str] = "Quantifiable"
    class_model_uri: ClassVar[URIRef] = QUDT.Quantifiable

    dataEncoding: Optional[Union[Union[dict, DataEncoding], list[Union[dict, DataEncoding]]]] = empty_list()
    datatype: Optional[Union[Union[dict, Datatype], list[Union[dict, Datatype]]]] = empty_list()
    hasUnit: Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]] = empty_list()
    relativeStandardUncertainty: Optional[Union[float, list[float]]] = empty_list()
    standardUncertainty: Optional[Union[Decimal, list[Decimal]]] = empty_list()
    standardUncertaintySN: Optional[Union[float, list[float]]] = empty_list()
    value: Optional[Union[str, list[str]]] = empty_list()
    valueSN: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.dataEncoding, list):
            self.dataEncoding = [self.dataEncoding] if self.dataEncoding is not None else []
        self.dataEncoding = [v if isinstance(v, DataEncoding) else DataEncoding(**as_dict(v)) for v in self.dataEncoding]

        if not isinstance(self.datatype, list):
            self.datatype = [self.datatype] if self.datatype is not None else []
        self.datatype = [v if isinstance(v, Datatype) else Datatype(**as_dict(v)) for v in self.datatype]

        if not isinstance(self.hasUnit, list):
            self.hasUnit = [self.hasUnit] if self.hasUnit is not None else []
        self.hasUnit = [v if isinstance(v, Unit) else Unit(**as_dict(v)) for v in self.hasUnit]

        if not isinstance(self.relativeStandardUncertainty, list):
            self.relativeStandardUncertainty = [self.relativeStandardUncertainty] if self.relativeStandardUncertainty is not None else []
        self.relativeStandardUncertainty = [v if isinstance(v, float) else float(v) for v in self.relativeStandardUncertainty]

        if not isinstance(self.standardUncertainty, list):
            self.standardUncertainty = [self.standardUncertainty] if self.standardUncertainty is not None else []
        self.standardUncertainty = [v if isinstance(v, Decimal) else Decimal(v) for v in self.standardUncertainty]

        if not isinstance(self.standardUncertaintySN, list):
            self.standardUncertaintySN = [self.standardUncertaintySN] if self.standardUncertaintySN is not None else []
        self.standardUncertaintySN = [v if isinstance(v, float) else float(v) for v in self.standardUncertaintySN]

        if not isinstance(self.value, list):
            self.value = [self.value] if self.value is not None else []
        self.value = [v if isinstance(v, str) else str(v) for v in self.value]

        if not isinstance(self.valueSN, list):
            self.valueSN = [self.valueSN] if self.valueSN is not None else []
        self.valueSN = [v if isinstance(v, str) else str(v) for v in self.valueSN]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Quantity(Quantifiable):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "Quantity"
    class_model_uri: ClassVar[URIRef] = QUDT.Quantity

    hasQuantityKind: Optional[Union[Union[dict, "QuantityKind"], list[Union[dict, "QuantityKind"]]]] = empty_list()
    quantityValue: Optional[Union[Union[dict, "QuantityValue"], list[Union[dict, "QuantityValue"]]]] = empty_list()
    isDeltaQuantity: Optional[Union[Union[bool, Bool], list[Union[bool, Bool]]]] = empty_list()
    guidance: Optional[Union[str, list[str]]] = empty_list()
    id: Optional[Union[str, list[str]]] = empty_list()
    hasRule: Optional[Union[Union[dict, "Rule"], list[Union[dict, "Rule"]]]] = empty_list()
    isReplacedBy: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[Union[str, list[str]]] = empty_list()
    abbreviation: Optional[Union[str, list[str]]] = empty_list()
    deprecated: Optional[Union[str, list[str]]] = empty_list()
    plainTextDescription: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.hasQuantityKind, list):
            self.hasQuantityKind = [self.hasQuantityKind] if self.hasQuantityKind is not None else []
        self.hasQuantityKind = [v if isinstance(v, QuantityKind) else QuantityKind(**as_dict(v)) for v in self.hasQuantityKind]

        if not isinstance(self.quantityValue, list):
            self.quantityValue = [self.quantityValue] if self.quantityValue is not None else []
        self.quantityValue = [v if isinstance(v, QuantityValue) else QuantityValue(**as_dict(v)) for v in self.quantityValue]

        if not isinstance(self.isDeltaQuantity, list):
            self.isDeltaQuantity = [self.isDeltaQuantity] if self.isDeltaQuantity is not None else []
        self.isDeltaQuantity = [v if isinstance(v, Bool) else Bool(v) for v in self.isDeltaQuantity]

        if not isinstance(self.guidance, list):
            self.guidance = [self.guidance] if self.guidance is not None else []
        self.guidance = [v if isinstance(v, str) else str(v) for v in self.guidance]

        if not isinstance(self.id, list):
            self.id = [self.id] if self.id is not None else []
        self.id = [v if isinstance(v, str) else str(v) for v in self.id]

        if not isinstance(self.hasRule, list):
            self.hasRule = [self.hasRule] if self.hasRule is not None else []
        self.hasRule = [v if isinstance(v, Rule) else Rule(**as_dict(v)) for v in self.hasRule]

        if not isinstance(self.isReplacedBy, list):
            self.isReplacedBy = [self.isReplacedBy] if self.isReplacedBy is not None else []
        self.isReplacedBy = [v if isinstance(v, str) else str(v) for v in self.isReplacedBy]

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.abbreviation, list):
            self.abbreviation = [self.abbreviation] if self.abbreviation is not None else []
        self.abbreviation = [v if isinstance(v, str) else str(v) for v in self.abbreviation]

        if not isinstance(self.deprecated, list):
            self.deprecated = [self.deprecated] if self.deprecated is not None else []
        self.deprecated = [v if isinstance(v, str) else str(v) for v in self.deprecated]

        if not isinstance(self.plainTextDescription, list):
            self.plainTextDescription = [self.plainTextDescription] if self.plainTextDescription is not None else []
        self.plainTextDescription = [v if isinstance(v, str) else str(v) for v in self.plainTextDescription]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhysicalConstant(Quantity):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["PhysicalConstant"]
    class_class_curie: ClassVar[str] = "qudt:PhysicalConstant"
    class_name: ClassVar[str] = "PhysicalConstant"
    class_model_uri: ClassVar[URIRef] = QUDT.PhysicalConstant

    applicableSystem: Optional[Union[Union[dict, "SystemOfUnits"], list[Union[dict, "SystemOfUnits"]]]] = empty_list()
    applicableUnit: Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]] = empty_list()
    exactMatch: Optional[Union[Union[dict, "PhysicalConstant"], list[Union[dict, "PhysicalConstant"]]]] = empty_list()
    hasDimensionVector: Optional[Union[Union[dict, "QuantityKindDimensionVector"], list[Union[dict, "QuantityKindDimensionVector"]]]] = empty_list()
    ucumCode: Optional[Union[str, list[str]]] = empty_list()
    exactConstant: Optional[Union[Union[bool, Bool], list[Union[bool, Bool]]]] = empty_list()
    altSymbol: Optional[Union[str, list[str]]] = empty_list()
    isoNormativeReference: Optional[Union[str, list[str]]] = empty_list()
    latexSymbol: Optional[Union[str, list[str]]] = empty_list()
    normativeReference: Optional[Union[str, list[str]]] = empty_list()
    symbol: Optional[Union[str, list[str]]] = empty_list()
    latexDefinition: Optional[Union[str, list[str]]] = empty_list()
    mathMLdefinition: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.applicableSystem, list):
            self.applicableSystem = [self.applicableSystem] if self.applicableSystem is not None else []
        self.applicableSystem = [v if isinstance(v, SystemOfUnits) else SystemOfUnits(**as_dict(v)) for v in self.applicableSystem]

        if not isinstance(self.applicableUnit, list):
            self.applicableUnit = [self.applicableUnit] if self.applicableUnit is not None else []
        self.applicableUnit = [v if isinstance(v, Unit) else Unit(**as_dict(v)) for v in self.applicableUnit]

        if not isinstance(self.exactMatch, list):
            self.exactMatch = [self.exactMatch] if self.exactMatch is not None else []
        self.exactMatch = [v if isinstance(v, PhysicalConstant) else PhysicalConstant(**as_dict(v)) for v in self.exactMatch]

        if not isinstance(self.hasDimensionVector, list):
            self.hasDimensionVector = [self.hasDimensionVector] if self.hasDimensionVector is not None else []
        self.hasDimensionVector = [v if isinstance(v, QuantityKindDimensionVector) else QuantityKindDimensionVector(**as_dict(v)) for v in self.hasDimensionVector]

        if not isinstance(self.ucumCode, list):
            self.ucumCode = [self.ucumCode] if self.ucumCode is not None else []
        self.ucumCode = [v if isinstance(v, str) else str(v) for v in self.ucumCode]

        if not isinstance(self.exactConstant, list):
            self.exactConstant = [self.exactConstant] if self.exactConstant is not None else []
        self.exactConstant = [v if isinstance(v, Bool) else Bool(v) for v in self.exactConstant]

        if not isinstance(self.altSymbol, list):
            self.altSymbol = [self.altSymbol] if self.altSymbol is not None else []
        self.altSymbol = [v if isinstance(v, str) else str(v) for v in self.altSymbol]

        if not isinstance(self.isoNormativeReference, list):
            self.isoNormativeReference = [self.isoNormativeReference] if self.isoNormativeReference is not None else []
        self.isoNormativeReference = [v if isinstance(v, str) else str(v) for v in self.isoNormativeReference]

        if not isinstance(self.latexSymbol, list):
            self.latexSymbol = [self.latexSymbol] if self.latexSymbol is not None else []
        self.latexSymbol = [v if isinstance(v, str) else str(v) for v in self.latexSymbol]

        if not isinstance(self.normativeReference, list):
            self.normativeReference = [self.normativeReference] if self.normativeReference is not None else []
        self.normativeReference = [v if isinstance(v, str) else str(v) for v in self.normativeReference]

        if not isinstance(self.symbol, list):
            self.symbol = [self.symbol] if self.symbol is not None else []
        self.symbol = [v if isinstance(v, str) else str(v) for v in self.symbol]

        if not isinstance(self.latexDefinition, list):
            self.latexDefinition = [self.latexDefinition] if self.latexDefinition is not None else []
        self.latexDefinition = [v if isinstance(v, str) else str(v) for v in self.latexDefinition]

        if not isinstance(self.mathMLdefinition, list):
            self.mathMLdefinition = [self.mathMLdefinition] if self.mathMLdefinition is not None else []
        self.mathMLdefinition = [v if isinstance(v, str) else str(v) for v in self.mathMLdefinition]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantityKindDimensionVector(Concept):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["QuantityKindDimensionVector"]
    class_class_curie: ClassVar[str] = "qudt:QuantityKindDimensionVector"
    class_name: ClassVar[str] = "QuantityKindDimensionVector"
    class_model_uri: ClassVar[URIRef] = QUDT.QuantityKindDimensionVector

    dimensionExponentForAmountOfSubstance: Union[str, list[str]] = None
    dimensionExponentForElectricCurrent: Union[str, list[str]] = None
    dimensionExponentForLength: Union[str, list[str]] = None
    dimensionExponentForLuminousIntensity: Union[str, list[str]] = None
    dimensionExponentForMass: Union[str, list[str]] = None
    dimensionExponentForThermodynamicTemperature: Union[str, list[str]] = None
    dimensionExponentForTime: Union[str, list[str]] = None
    dimensionlessExponent: Union[str, list[str]] = None
    hasReferenceQuantityKind: Optional[Union[Union[dict, "QuantityKind"], list[Union[dict, "QuantityKind"]]]] = empty_list()
    latexSymbol: Optional[Union[str, list[str]]] = empty_list()
    latexDefinition: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.dimensionExponentForAmountOfSubstance):
            self.MissingRequiredField("dimensionExponentForAmountOfSubstance")
        if not isinstance(self.dimensionExponentForAmountOfSubstance, list):
            self.dimensionExponentForAmountOfSubstance = [self.dimensionExponentForAmountOfSubstance] if self.dimensionExponentForAmountOfSubstance is not None else []
        self.dimensionExponentForAmountOfSubstance = [v if isinstance(v, str) else str(v) for v in self.dimensionExponentForAmountOfSubstance]

        if self._is_empty(self.dimensionExponentForElectricCurrent):
            self.MissingRequiredField("dimensionExponentForElectricCurrent")
        if not isinstance(self.dimensionExponentForElectricCurrent, list):
            self.dimensionExponentForElectricCurrent = [self.dimensionExponentForElectricCurrent] if self.dimensionExponentForElectricCurrent is not None else []
        self.dimensionExponentForElectricCurrent = [v if isinstance(v, str) else str(v) for v in self.dimensionExponentForElectricCurrent]

        if self._is_empty(self.dimensionExponentForLength):
            self.MissingRequiredField("dimensionExponentForLength")
        if not isinstance(self.dimensionExponentForLength, list):
            self.dimensionExponentForLength = [self.dimensionExponentForLength] if self.dimensionExponentForLength is not None else []
        self.dimensionExponentForLength = [v if isinstance(v, str) else str(v) for v in self.dimensionExponentForLength]

        if self._is_empty(self.dimensionExponentForLuminousIntensity):
            self.MissingRequiredField("dimensionExponentForLuminousIntensity")
        if not isinstance(self.dimensionExponentForLuminousIntensity, list):
            self.dimensionExponentForLuminousIntensity = [self.dimensionExponentForLuminousIntensity] if self.dimensionExponentForLuminousIntensity is not None else []
        self.dimensionExponentForLuminousIntensity = [v if isinstance(v, str) else str(v) for v in self.dimensionExponentForLuminousIntensity]

        if self._is_empty(self.dimensionExponentForMass):
            self.MissingRequiredField("dimensionExponentForMass")
        if not isinstance(self.dimensionExponentForMass, list):
            self.dimensionExponentForMass = [self.dimensionExponentForMass] if self.dimensionExponentForMass is not None else []
        self.dimensionExponentForMass = [v if isinstance(v, str) else str(v) for v in self.dimensionExponentForMass]

        if self._is_empty(self.dimensionExponentForThermodynamicTemperature):
            self.MissingRequiredField("dimensionExponentForThermodynamicTemperature")
        if not isinstance(self.dimensionExponentForThermodynamicTemperature, list):
            self.dimensionExponentForThermodynamicTemperature = [self.dimensionExponentForThermodynamicTemperature] if self.dimensionExponentForThermodynamicTemperature is not None else []
        self.dimensionExponentForThermodynamicTemperature = [v if isinstance(v, str) else str(v) for v in self.dimensionExponentForThermodynamicTemperature]

        if self._is_empty(self.dimensionExponentForTime):
            self.MissingRequiredField("dimensionExponentForTime")
        if not isinstance(self.dimensionExponentForTime, list):
            self.dimensionExponentForTime = [self.dimensionExponentForTime] if self.dimensionExponentForTime is not None else []
        self.dimensionExponentForTime = [v if isinstance(v, str) else str(v) for v in self.dimensionExponentForTime]

        if self._is_empty(self.dimensionlessExponent):
            self.MissingRequiredField("dimensionlessExponent")
        if not isinstance(self.dimensionlessExponent, list):
            self.dimensionlessExponent = [self.dimensionlessExponent] if self.dimensionlessExponent is not None else []
        self.dimensionlessExponent = [v if isinstance(v, str) else str(v) for v in self.dimensionlessExponent]

        if not isinstance(self.hasReferenceQuantityKind, list):
            self.hasReferenceQuantityKind = [self.hasReferenceQuantityKind] if self.hasReferenceQuantityKind is not None else []
        self.hasReferenceQuantityKind = [v if isinstance(v, QuantityKind) else QuantityKind(**as_dict(v)) for v in self.hasReferenceQuantityKind]

        if not isinstance(self.latexSymbol, list):
            self.latexSymbol = [self.latexSymbol] if self.latexSymbol is not None else []
        self.latexSymbol = [v if isinstance(v, str) else str(v) for v in self.latexSymbol]

        if not isinstance(self.latexDefinition, list):
            self.latexDefinition = [self.latexDefinition] if self.latexDefinition is not None else []
        self.latexDefinition = [v if isinstance(v, str) else str(v) for v in self.latexDefinition]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantityKindDimensionVectorCGS(QuantityKindDimensionVector):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["QuantityKindDimensionVector_CGS"]
    class_class_curie: ClassVar[str] = "qudt:QuantityKindDimensionVector_CGS"
    class_name: ClassVar[str] = "QuantityKindDimensionVector_CGS"
    class_model_uri: ClassVar[URIRef] = QUDT.QuantityKindDimensionVectorCGS

    dimensionExponentForAmountOfSubstance: Union[str, list[str]] = None
    dimensionExponentForElectricCurrent: Union[str, list[str]] = None
    dimensionExponentForLength: Union[str, list[str]] = None
    dimensionExponentForLuminousIntensity: Union[str, list[str]] = None
    dimensionExponentForMass: Union[str, list[str]] = None
    dimensionExponentForThermodynamicTemperature: Union[str, list[str]] = None
    dimensionExponentForTime: Union[str, list[str]] = None
    dimensionlessExponent: Union[str, list[str]] = None

@dataclass(repr=False)
class QuantityKindDimensionVectorCGS-EMU(QuantityKindDimensionVectorCGS):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["QuantityKindDimensionVector_CGS-EMU"]
    class_class_curie: ClassVar[str] = "qudt:QuantityKindDimensionVector_CGS-EMU"
    class_name: ClassVar[str] = "QuantityKindDimensionVector_CGS-EMU"
    class_model_uri: ClassVar[URIRef] = QUDT.QuantityKindDimensionVectorCGS-EMU

    dimensionExponentForAmountOfSubstance: Union[str, list[str]] = None
    dimensionExponentForElectricCurrent: Union[str, list[str]] = None
    dimensionExponentForLength: Union[str, list[str]] = None
    dimensionExponentForLuminousIntensity: Union[str, list[str]] = None
    dimensionExponentForMass: Union[str, list[str]] = None
    dimensionExponentForThermodynamicTemperature: Union[str, list[str]] = None
    dimensionExponentForTime: Union[str, list[str]] = None
    dimensionlessExponent: Union[str, list[str]] = None

@dataclass(repr=False)
class QuantityKindDimensionVectorCGS-ESU(QuantityKindDimensionVectorCGS):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["QuantityKindDimensionVector_CGS-ESU"]
    class_class_curie: ClassVar[str] = "qudt:QuantityKindDimensionVector_CGS-ESU"
    class_name: ClassVar[str] = "QuantityKindDimensionVector_CGS-ESU"
    class_model_uri: ClassVar[URIRef] = QUDT.QuantityKindDimensionVectorCGS-ESU

    dimensionExponentForAmountOfSubstance: Union[str, list[str]] = None
    dimensionExponentForElectricCurrent: Union[str, list[str]] = None
    dimensionExponentForLength: Union[str, list[str]] = None
    dimensionExponentForLuminousIntensity: Union[str, list[str]] = None
    dimensionExponentForMass: Union[str, list[str]] = None
    dimensionExponentForThermodynamicTemperature: Union[str, list[str]] = None
    dimensionExponentForTime: Union[str, list[str]] = None
    dimensionlessExponent: Union[str, list[str]] = None

@dataclass(repr=False)
class QuantityKindDimensionVectorCGS-GAUSS(QuantityKindDimensionVectorCGS):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["QuantityKindDimensionVector_CGS-GAUSS"]
    class_class_curie: ClassVar[str] = "qudt:QuantityKindDimensionVector_CGS-GAUSS"
    class_name: ClassVar[str] = "QuantityKindDimensionVector_CGS-GAUSS"
    class_model_uri: ClassVar[URIRef] = QUDT.QuantityKindDimensionVectorCGS-GAUSS

    dimensionExponentForAmountOfSubstance: Union[str, list[str]] = None
    dimensionExponentForElectricCurrent: Union[str, list[str]] = None
    dimensionExponentForLength: Union[str, list[str]] = None
    dimensionExponentForLuminousIntensity: Union[str, list[str]] = None
    dimensionExponentForMass: Union[str, list[str]] = None
    dimensionExponentForThermodynamicTemperature: Union[str, list[str]] = None
    dimensionExponentForTime: Union[str, list[str]] = None
    dimensionlessExponent: Union[str, list[str]] = None

@dataclass(repr=False)
class QuantityKindDimensionVectorCGS-LH(QuantityKindDimensionVectorCGS):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["QuantityKindDimensionVector_CGS-LH"]
    class_class_curie: ClassVar[str] = "qudt:QuantityKindDimensionVector_CGS-LH"
    class_name: ClassVar[str] = "QuantityKindDimensionVector_CGS-LH"
    class_model_uri: ClassVar[URIRef] = QUDT.QuantityKindDimensionVectorCGS-LH

    dimensionExponentForAmountOfSubstance: Union[str, list[str]] = None
    dimensionExponentForElectricCurrent: Union[str, list[str]] = None
    dimensionExponentForLength: Union[str, list[str]] = None
    dimensionExponentForLuminousIntensity: Union[str, list[str]] = None
    dimensionExponentForMass: Union[str, list[str]] = None
    dimensionExponentForThermodynamicTemperature: Union[str, list[str]] = None
    dimensionExponentForTime: Union[str, list[str]] = None
    dimensionlessExponent: Union[str, list[str]] = None

@dataclass(repr=False)
class QuantityKindDimensionVectorISO(QuantityKindDimensionVector):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["QuantityKindDimensionVector_ISO"]
    class_class_curie: ClassVar[str] = "qudt:QuantityKindDimensionVector_ISO"
    class_name: ClassVar[str] = "QuantityKindDimensionVector_ISO"
    class_model_uri: ClassVar[URIRef] = QUDT.QuantityKindDimensionVectorISO

    dimensionExponentForAmountOfSubstance: Union[str, list[str]] = None
    dimensionExponentForElectricCurrent: Union[str, list[str]] = None
    dimensionExponentForLength: Union[str, list[str]] = None
    dimensionExponentForLuminousIntensity: Union[str, list[str]] = None
    dimensionExponentForMass: Union[str, list[str]] = None
    dimensionExponentForThermodynamicTemperature: Union[str, list[str]] = None
    dimensionExponentForTime: Union[str, list[str]] = None
    dimensionlessExponent: Union[str, list[str]] = None

@dataclass(repr=False)
class QuantityKindDimensionVectorImperial(QuantityKindDimensionVector):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["QuantityKindDimensionVector_Imperial"]
    class_class_curie: ClassVar[str] = "qudt:QuantityKindDimensionVector_Imperial"
    class_name: ClassVar[str] = "QuantityKindDimensionVector_Imperial"
    class_model_uri: ClassVar[URIRef] = QUDT.QuantityKindDimensionVectorImperial

    dimensionExponentForAmountOfSubstance: Union[str, list[str]] = None
    dimensionExponentForElectricCurrent: Union[str, list[str]] = None
    dimensionExponentForLength: Union[str, list[str]] = None
    dimensionExponentForLuminousIntensity: Union[str, list[str]] = None
    dimensionExponentForMass: Union[str, list[str]] = None
    dimensionExponentForThermodynamicTemperature: Union[str, list[str]] = None
    dimensionExponentForTime: Union[str, list[str]] = None
    dimensionlessExponent: Union[str, list[str]] = None

@dataclass(repr=False)
class QuantityKindDimensionVectorSI(QuantityKindDimensionVector):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["QuantityKindDimensionVector_SI"]
    class_class_curie: ClassVar[str] = "qudt:QuantityKindDimensionVector_SI"
    class_name: ClassVar[str] = "QuantityKindDimensionVector_SI"
    class_model_uri: ClassVar[URIRef] = QUDT.QuantityKindDimensionVectorSI

    dimensionExponentForAmountOfSubstance: Union[str, list[str]] = None
    dimensionExponentForElectricCurrent: Union[str, list[str]] = None
    dimensionExponentForLength: Union[str, list[str]] = None
    dimensionExponentForLuminousIntensity: Union[str, list[str]] = None
    dimensionExponentForMass: Union[str, list[str]] = None
    dimensionExponentForThermodynamicTemperature: Union[str, list[str]] = None
    dimensionExponentForTime: Union[str, list[str]] = None
    dimensionlessExponent: Union[str, list[str]] = None

@dataclass(repr=False)
class QuantityValue(Quantifiable):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["QuantityValue"]
    class_class_curie: ClassVar[str] = "qudt:QuantityValue"
    class_name: ClassVar[str] = "QuantityValue"
    class_model_uri: ClassVar[URIRef] = QUDT.QuantityValue

    hasUnit: Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]] = empty_list()
    guidance: Optional[Union[str, list[str]]] = empty_list()
    id: Optional[Union[str, list[str]]] = empty_list()
    hasRule: Optional[Union[Union[dict, "Rule"], list[Union[dict, "Rule"]]]] = empty_list()
    isReplacedBy: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[Union[str, list[str]]] = empty_list()
    abbreviation: Optional[Union[str, list[str]]] = empty_list()
    deprecated: Optional[Union[str, list[str]]] = empty_list()
    plainTextDescription: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.hasUnit, list):
            self.hasUnit = [self.hasUnit] if self.hasUnit is not None else []
        self.hasUnit = [v if isinstance(v, Unit) else Unit(**as_dict(v)) for v in self.hasUnit]

        if not isinstance(self.guidance, list):
            self.guidance = [self.guidance] if self.guidance is not None else []
        self.guidance = [v if isinstance(v, str) else str(v) for v in self.guidance]

        if not isinstance(self.id, list):
            self.id = [self.id] if self.id is not None else []
        self.id = [v if isinstance(v, str) else str(v) for v in self.id]

        if not isinstance(self.hasRule, list):
            self.hasRule = [self.hasRule] if self.hasRule is not None else []
        self.hasRule = [v if isinstance(v, Rule) else Rule(**as_dict(v)) for v in self.hasRule]

        if not isinstance(self.isReplacedBy, list):
            self.isReplacedBy = [self.isReplacedBy] if self.isReplacedBy is not None else []
        self.isReplacedBy = [v if isinstance(v, str) else str(v) for v in self.isReplacedBy]

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.abbreviation, list):
            self.abbreviation = [self.abbreviation] if self.abbreviation is not None else []
        self.abbreviation = [v if isinstance(v, str) else str(v) for v in self.abbreviation]

        if not isinstance(self.deprecated, list):
            self.deprecated = [self.deprecated] if self.deprecated is not None else []
        self.deprecated = [v if isinstance(v, str) else str(v) for v in self.deprecated]

        if not isinstance(self.plainTextDescription, list):
            self.plainTextDescription = [self.plainTextDescription] if self.plainTextDescription is not None else []
        self.plainTextDescription = [v if isinstance(v, str) else str(v) for v in self.plainTextDescription]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConstantValue(QuantityValue):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["ConstantValue"]
    class_class_curie: ClassVar[str] = "qudt:ConstantValue"
    class_name: ClassVar[str] = "ConstantValue"
    class_model_uri: ClassVar[URIRef] = QUDT.ConstantValue

    exactConstant: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.exactConstant, list):
            self.exactConstant = [self.exactConstant] if self.exactConstant is not None else []
        self.exactConstant = [v if isinstance(v, str) else str(v) for v in self.exactConstant]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ScalarDatatype(Datatype):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["ScalarDatatype"]
    class_class_curie: ClassVar[str] = "qudt:ScalarDatatype"
    class_name: ClassVar[str] = "ScalarDatatype"
    class_model_uri: ClassVar[URIRef] = QUDT.ScalarDatatype

    rdfsDatatype: Optional[Union[Union[dict, Datatype], list[Union[dict, Datatype]]]] = empty_list()
    bits: Optional[Union[str, list[str]]] = empty_list()
    bytes: Optional[Union[str, list[str]]] = empty_list()
    length: Optional[Union[str, list[str]]] = empty_list()
    maxExclusive: Optional[Union[str, list[str]]] = empty_list()
    maxInclusive: Optional[Union[str, list[str]]] = empty_list()
    minExclusive: Optional[Union[str, list[str]]] = empty_list()
    minInclusive: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.rdfsDatatype, list):
            self.rdfsDatatype = [self.rdfsDatatype] if self.rdfsDatatype is not None else []
        self.rdfsDatatype = [v if isinstance(v, Datatype) else Datatype(**as_dict(v)) for v in self.rdfsDatatype]

        if not isinstance(self.bits, list):
            self.bits = [self.bits] if self.bits is not None else []
        self.bits = [v if isinstance(v, str) else str(v) for v in self.bits]

        if not isinstance(self.bytes, list):
            self.bytes = [self.bytes] if self.bytes is not None else []
        self.bytes = [v if isinstance(v, str) else str(v) for v in self.bytes]

        if not isinstance(self.length, list):
            self.length = [self.length] if self.length is not None else []
        self.length = [v if isinstance(v, str) else str(v) for v in self.length]

        if not isinstance(self.maxExclusive, list):
            self.maxExclusive = [self.maxExclusive] if self.maxExclusive is not None else []
        self.maxExclusive = [v if isinstance(v, str) else str(v) for v in self.maxExclusive]

        if not isinstance(self.maxInclusive, list):
            self.maxInclusive = [self.maxInclusive] if self.maxInclusive is not None else []
        self.maxInclusive = [v if isinstance(v, str) else str(v) for v in self.maxInclusive]

        if not isinstance(self.minExclusive, list):
            self.minExclusive = [self.minExclusive] if self.minExclusive is not None else []
        self.minExclusive = [v if isinstance(v, str) else str(v) for v in self.minExclusive]

        if not isinstance(self.minInclusive, list):
            self.minInclusive = [self.minInclusive] if self.minInclusive is not None else []
        self.minInclusive = [v if isinstance(v, str) else str(v) for v in self.minInclusive]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Scale(Concept):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Scale"]
    class_class_curie: ClassVar[str] = "qudt:Scale"
    class_name: ClassVar[str] = "Scale"
    class_model_uri: ClassVar[URIRef] = QUDT.Scale

    permissibleMaths: Optional[Union[Union[dict, MathsFunctionType], list[Union[dict, MathsFunctionType]]]] = empty_list()
    permissibleTransformation: Optional[Union[Union[dict, "TransformType"], list[Union[dict, "TransformType"]]]] = empty_list()
    scaleType: Optional[Union[Union[dict, "ScaleType"], list[Union[dict, "ScaleType"]]]] = empty_list()
    dataStructure: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.permissibleMaths, list):
            self.permissibleMaths = [self.permissibleMaths] if self.permissibleMaths is not None else []
        self.permissibleMaths = [v if isinstance(v, MathsFunctionType) else MathsFunctionType(**as_dict(v)) for v in self.permissibleMaths]

        if not isinstance(self.permissibleTransformation, list):
            self.permissibleTransformation = [self.permissibleTransformation] if self.permissibleTransformation is not None else []
        self.permissibleTransformation = [v if isinstance(v, TransformType) else TransformType(**as_dict(v)) for v in self.permissibleTransformation]

        if not isinstance(self.scaleType, list):
            self.scaleType = [self.scaleType] if self.scaleType is not None else []
        self.scaleType = [v if isinstance(v, ScaleType) else ScaleType(**as_dict(v)) for v in self.scaleType]

        if not isinstance(self.dataStructure, list):
            self.dataStructure = [self.dataStructure] if self.dataStructure is not None else []
        self.dataStructure = [v if isinstance(v, str) else str(v) for v in self.dataStructure]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnumerationScale(Scale):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["EnumerationScale"]
    class_class_curie: ClassVar[str] = "qudt:EnumerationScale"
    class_name: ClassVar[str] = "EnumerationScale"
    class_model_uri: ClassVar[URIRef] = QUDT.EnumerationScale

    element: Union[Union[dict, "EnumeratedValue"], list[Union[dict, "EnumeratedValue"]]] = None
    guidance: Optional[Union[str, list[str]]] = empty_list()
    id: Optional[Union[str, list[str]]] = empty_list()
    hasRule: Optional[Union[Union[dict, "Rule"], list[Union[dict, "Rule"]]]] = empty_list()
    isReplacedBy: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[Union[str, list[str]]] = empty_list()
    abbreviation: Optional[Union[str, list[str]]] = empty_list()
    deprecated: Optional[Union[str, list[str]]] = empty_list()
    plainTextDescription: Optional[Union[str, list[str]]] = empty_list()
    default: Optional[Union[Union[dict, "EnumeratedValue"], list[Union[dict, "EnumeratedValue"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.element):
            self.MissingRequiredField("element")
        if not isinstance(self.element, list):
            self.element = [self.element] if self.element is not None else []
        self.element = [v if isinstance(v, EnumeratedValue) else EnumeratedValue(**as_dict(v)) for v in self.element]

        if not isinstance(self.guidance, list):
            self.guidance = [self.guidance] if self.guidance is not None else []
        self.guidance = [v if isinstance(v, str) else str(v) for v in self.guidance]

        if not isinstance(self.id, list):
            self.id = [self.id] if self.id is not None else []
        self.id = [v if isinstance(v, str) else str(v) for v in self.id]

        if not isinstance(self.hasRule, list):
            self.hasRule = [self.hasRule] if self.hasRule is not None else []
        self.hasRule = [v if isinstance(v, Rule) else Rule(**as_dict(v)) for v in self.hasRule]

        if not isinstance(self.isReplacedBy, list):
            self.isReplacedBy = [self.isReplacedBy] if self.isReplacedBy is not None else []
        self.isReplacedBy = [v if isinstance(v, str) else str(v) for v in self.isReplacedBy]

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.abbreviation, list):
            self.abbreviation = [self.abbreviation] if self.abbreviation is not None else []
        self.abbreviation = [v if isinstance(v, str) else str(v) for v in self.abbreviation]

        if not isinstance(self.deprecated, list):
            self.deprecated = [self.deprecated] if self.deprecated is not None else []
        self.deprecated = [v if isinstance(v, str) else str(v) for v in self.deprecated]

        if not isinstance(self.plainTextDescription, list):
            self.plainTextDescription = [self.plainTextDescription] if self.plainTextDescription is not None else []
        self.plainTextDescription = [v if isinstance(v, str) else str(v) for v in self.plainTextDescription]

        if not isinstance(self.default, list):
            self.default = [self.default] if self.default is not None else []
        self.default = [v if isinstance(v, EnumeratedValue) else EnumeratedValue(**as_dict(v)) for v in self.default]

        super().__post_init__(**kwargs)


class IntervalScale(Scale):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["IntervalScale"]
    class_class_curie: ClassVar[str] = "qudt:IntervalScale"
    class_name: ClassVar[str] = "IntervalScale"
    class_model_uri: ClassVar[URIRef] = QUDT.IntervalScale


class NominalScale(Scale):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["NominalScale"]
    class_class_curie: ClassVar[str] = "qudt:NominalScale"
    class_name: ClassVar[str] = "NominalScale"
    class_model_uri: ClassVar[URIRef] = QUDT.NominalScale


@dataclass(repr=False)
class OrdinalScale(Scale):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["OrdinalScale"]
    class_class_curie: ClassVar[str] = "qudt:OrdinalScale"
    class_name: ClassVar[str] = "OrdinalScale"
    class_model_uri: ClassVar[URIRef] = QUDT.OrdinalScale

    order: Union[str, list[str]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.order):
            self.MissingRequiredField("order")
        if not isinstance(self.order, list):
            self.order = [self.order] if self.order is not None else []
        self.order = [v if isinstance(v, str) else str(v) for v in self.order]

        super().__post_init__(**kwargs)


class RatioScale(Scale):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["RatioScale"]
    class_class_curie: ClassVar[str] = "qudt:RatioScale"
    class_name: ClassVar[str] = "RatioScale"
    class_model_uri: ClassVar[URIRef] = QUDT.RatioScale


class SignednessType(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["SignednessType"]
    class_class_curie: ClassVar[str] = "qudt:SignednessType"
    class_name: ClassVar[str] = "SignednessType"
    class_model_uri: ClassVar[URIRef] = QUDT.SignednessType


class Statement(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RDF["Statement"]
    class_class_curie: ClassVar[str] = "rdf:Statement"
    class_name: ClassVar[str] = "Statement"
    class_model_uri: ClassVar[URIRef] = QUDT.Statement


class StringEncodingType(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["StringEncodingType"]
    class_class_curie: ClassVar[str] = "qudt:StringEncodingType"
    class_name: ClassVar[str] = "StringEncodingType"
    class_model_uri: ClassVar[URIRef] = QUDT.StringEncodingType


@dataclass(repr=False)
class DateTimeStringEncodingType(StringEncodingType):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["DateTimeStringEncodingType"]
    class_class_curie: ClassVar[str] = "qudt:DateTimeStringEncodingType"
    class_name: ClassVar[str] = "DateTimeStringEncodingType"
    class_model_uri: ClassVar[URIRef] = QUDT.DateTimeStringEncodingType

    allowedPattern: Union[str, list[str]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.allowedPattern):
            self.MissingRequiredField("allowedPattern")
        if not isinstance(self.allowedPattern, list):
            self.allowedPattern = [self.allowedPattern] if self.allowedPattern is not None else []
        self.allowedPattern = [v if isinstance(v, str) else str(v) for v in self.allowedPattern]

        super().__post_init__(**kwargs)


class Symbol(Concept):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Symbol"]
    class_class_curie: ClassVar[str] = "qudt:Symbol"
    class_name: ClassVar[str] = "Symbol"
    class_model_uri: ClassVar[URIRef] = QUDT.Symbol


class SymmetricRelation(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["SymmetricRelation"]
    class_class_curie: ClassVar[str] = "qudt:SymmetricRelation"
    class_name: ClassVar[str] = "SymmetricRelation"
    class_model_uri: ClassVar[URIRef] = QUDT.SymmetricRelation


@dataclass(repr=False)
class SystemOfQuantityKinds(Concept):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["SystemOfQuantityKinds"]
    class_class_curie: ClassVar[str] = "qudt:SystemOfQuantityKinds"
    class_name: ClassVar[str] = "SystemOfQuantityKinds"
    class_model_uri: ClassVar[URIRef] = QUDT.SystemOfQuantityKinds

    baseDimensionEnumeration: Optional[Union[Union[dict, Enumeration], list[Union[dict, Enumeration]]]] = empty_list()
    hasBaseQuantityKind: Optional[Union[Union[dict, "QuantityKind"], list[Union[dict, "QuantityKind"]]]] = empty_list()
    hasQuantityKind: Optional[Union[Union[dict, "QuantityKind"], list[Union[dict, "QuantityKind"]]]] = empty_list()
    hasUnitSystem: Optional[Union[Union[dict, "SystemOfUnits"], list[Union[dict, "SystemOfUnits"]]]] = empty_list()
    systemDerivedQuantityKind: Optional[Union[Union[dict, "QuantityKind"], list[Union[dict, "QuantityKind"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.baseDimensionEnumeration, list):
            self.baseDimensionEnumeration = [self.baseDimensionEnumeration] if self.baseDimensionEnumeration is not None else []
        self.baseDimensionEnumeration = [v if isinstance(v, Enumeration) else Enumeration(**as_dict(v)) for v in self.baseDimensionEnumeration]

        if not isinstance(self.hasBaseQuantityKind, list):
            self.hasBaseQuantityKind = [self.hasBaseQuantityKind] if self.hasBaseQuantityKind is not None else []
        self.hasBaseQuantityKind = [v if isinstance(v, QuantityKind) else QuantityKind(**as_dict(v)) for v in self.hasBaseQuantityKind]

        if not isinstance(self.hasQuantityKind, list):
            self.hasQuantityKind = [self.hasQuantityKind] if self.hasQuantityKind is not None else []
        self.hasQuantityKind = [v if isinstance(v, QuantityKind) else QuantityKind(**as_dict(v)) for v in self.hasQuantityKind]

        if not isinstance(self.hasUnitSystem, list):
            self.hasUnitSystem = [self.hasUnitSystem] if self.hasUnitSystem is not None else []
        self.hasUnitSystem = [v if isinstance(v, SystemOfUnits) else SystemOfUnits(**as_dict(v)) for v in self.hasUnitSystem]

        if not isinstance(self.systemDerivedQuantityKind, list):
            self.systemDerivedQuantityKind = [self.systemDerivedQuantityKind] if self.systemDerivedQuantityKind is not None else []
        self.systemDerivedQuantityKind = [v if isinstance(v, QuantityKind) else QuantityKind(**as_dict(v)) for v in self.systemDerivedQuantityKind]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UserQuantityKind(AbstractQuantityKind):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["UserQuantityKind"]
    class_class_curie: ClassVar[str] = "qudt:UserQuantityKind"
    class_name: ClassVar[str] = "UserQuantityKind"
    class_model_uri: ClassVar[URIRef] = QUDT.UserQuantityKind

    hasQuantityKind: Union[Union[dict, "QuantityKind"], list[Union[dict, "QuantityKind"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.hasQuantityKind):
            self.MissingRequiredField("hasQuantityKind")
        if not isinstance(self.hasQuantityKind, list):
            self.hasQuantityKind = [self.hasQuantityKind] if self.hasQuantityKind is not None else []
        self.hasQuantityKind = [v if isinstance(v, QuantityKind) else QuantityKind(**as_dict(v)) for v in self.hasQuantityKind]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Verifiable(Error3):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Verifiable"]
    class_class_curie: ClassVar[str] = "qudt:Verifiable"
    class_name: ClassVar[str] = "Verifiable"
    class_model_uri: ClassVar[URIRef] = QUDT.Verifiable

    isoNormativeReference: Optional[Union[str, list[str]]] = empty_list()
    normativeReference: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.isoNormativeReference, list):
            self.isoNormativeReference = [self.isoNormativeReference] if self.isoNormativeReference is not None else []
        self.isoNormativeReference = [v if isinstance(v, str) else str(v) for v in self.isoNormativeReference]

        if not isinstance(self.normativeReference, list):
            self.normativeReference = [self.normativeReference] if self.normativeReference is not None else []
        self.normativeReference = [v if isinstance(v, str) else str(v) for v in self.normativeReference]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Comment(Verifiable):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Comment"]
    class_class_curie: ClassVar[str] = "qudt:Comment"
    class_name: ClassVar[str] = "Comment"
    class_model_uri: ClassVar[URIRef] = QUDT.Comment

    rationale: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.rationale, list):
            self.rationale = [self.rationale] if self.rationale is not None else []
        self.rationale = [v if isinstance(v, str) else str(v) for v in self.rationale]

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnumeratedValue(Verifiable):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["EnumeratedValue"]
    class_class_curie: ClassVar[str] = "qudt:EnumeratedValue"
    class_name: ClassVar[str] = "EnumeratedValue"
    class_model_uri: ClassVar[URIRef] = QUDT.EnumeratedValue

    altSymbol: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[Union[str, list[str]]] = empty_list()
    abbreviation: Optional[Union[str, list[str]]] = empty_list()
    symbol: Optional[Union[str, list[str]]] = empty_list()
    guidance: Optional[Union[str, list[str]]] = empty_list()
    id: Optional[Union[str, list[str]]] = empty_list()
    hasRule: Optional[Union[Union[dict, "Rule"], list[Union[dict, "Rule"]]]] = empty_list()
    isReplacedBy: Optional[Union[str, list[str]]] = empty_list()
    deprecated: Optional[Union[str, list[str]]] = empty_list()
    plainTextDescription: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.altSymbol, list):
            self.altSymbol = [self.altSymbol] if self.altSymbol is not None else []
        self.altSymbol = [v if isinstance(v, str) else str(v) for v in self.altSymbol]

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.abbreviation, list):
            self.abbreviation = [self.abbreviation] if self.abbreviation is not None else []
        self.abbreviation = [v if isinstance(v, str) else str(v) for v in self.abbreviation]

        if not isinstance(self.symbol, list):
            self.symbol = [self.symbol] if self.symbol is not None else []
        self.symbol = [v if isinstance(v, str) else str(v) for v in self.symbol]

        if not isinstance(self.guidance, list):
            self.guidance = [self.guidance] if self.guidance is not None else []
        self.guidance = [v if isinstance(v, str) else str(v) for v in self.guidance]

        if not isinstance(self.id, list):
            self.id = [self.id] if self.id is not None else []
        self.id = [v if isinstance(v, str) else str(v) for v in self.id]

        if not isinstance(self.hasRule, list):
            self.hasRule = [self.hasRule] if self.hasRule is not None else []
        self.hasRule = [v if isinstance(v, Rule) else Rule(**as_dict(v)) for v in self.hasRule]

        if not isinstance(self.isReplacedBy, list):
            self.isReplacedBy = [self.isReplacedBy] if self.isReplacedBy is not None else []
        self.isReplacedBy = [v if isinstance(v, str) else str(v) for v in self.isReplacedBy]

        if not isinstance(self.deprecated, list):
            self.deprecated = [self.deprecated] if self.deprecated is not None else []
        self.deprecated = [v if isinstance(v, str) else str(v) for v in self.deprecated]

        if not isinstance(self.plainTextDescription, list):
            self.plainTextDescription = [self.plainTextDescription] if self.plainTextDescription is not None else []
        self.plainTextDescription = [v if isinstance(v, str) else str(v) for v in self.plainTextDescription]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CardinalityType(EnumeratedValue):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["CardinalityType"]
    class_class_curie: ClassVar[str] = "qudt:CardinalityType"
    class_name: ClassVar[str] = "CardinalityType"
    class_model_uri: ClassVar[URIRef] = QUDT.CardinalityType

    literal: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.literal, list):
            self.literal = [self.literal] if self.literal is not None else []
        self.literal = [v if isinstance(v, str) else str(v) for v in self.literal]

        super().__post_init__(**kwargs)


class EndianType(EnumeratedValue):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["EndianType"]
    class_class_curie: ClassVar[str] = "qudt:EndianType"
    class_name: ClassVar[str] = "EndianType"
    class_model_uri: ClassVar[URIRef] = QUDT.EndianType


class NISTSP811Comment(Comment):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["NIST_SP811_Comment"]
    class_class_curie: ClassVar[str] = "qudt:NIST_SP811_Comment"
    class_name: ClassVar[str] = "NIST_SP811_Comment"
    class_model_uri: ClassVar[URIRef] = QUDT.NISTSP811Comment


@dataclass(repr=False)
class OrderedType(EnumeratedValue):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["OrderedType"]
    class_class_curie: ClassVar[str] = "qudt:OrderedType"
    class_name: ClassVar[str] = "OrderedType"
    class_model_uri: ClassVar[URIRef] = QUDT.OrderedType

    literal: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.literal, list):
            self.literal = [self.literal] if self.literal is not None else []
        self.literal = [v if isinstance(v, str) else str(v) for v in self.literal]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Prefix(Verifiable):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Prefix"]
    class_class_curie: ClassVar[str] = "qudt:Prefix"
    class_name: ClassVar[str] = "Prefix"
    class_model_uri: ClassVar[URIRef] = QUDT.Prefix

    exactMatch: Optional[Union[Union[dict, "Prefix"], list[Union[dict, "Prefix"]]]] = empty_list()
    ucumCode: Optional[Union[Union[dict, "UCUMcs-term"], list[Union[dict, "UCUMcs-term"]]]] = empty_list()
    altSymbol: Optional[Union[str, list[str]]] = empty_list()
    latexSymbol: Optional[Union[str, list[str]]] = empty_list()
    symbol: Optional[Union[str, list[str]]] = empty_list()
    prefixMultiplier: Optional[Union[str, list[str]]] = empty_list()
    guidance: Optional[Union[str, list[str]]] = empty_list()
    id: Optional[Union[str, list[str]]] = empty_list()
    hasRule: Optional[Union[Union[dict, "Rule"], list[Union[dict, "Rule"]]]] = empty_list()
    isReplacedBy: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[Union[str, list[str]]] = empty_list()
    abbreviation: Optional[Union[str, list[str]]] = empty_list()
    deprecated: Optional[Union[str, list[str]]] = empty_list()
    plainTextDescription: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.exactMatch, list):
            self.exactMatch = [self.exactMatch] if self.exactMatch is not None else []
        self.exactMatch = [v if isinstance(v, Prefix) else Prefix(**as_dict(v)) for v in self.exactMatch]

        if not isinstance(self.ucumCode, list):
            self.ucumCode = [self.ucumCode] if self.ucumCode is not None else []
        self.ucumCode = [v if isinstance(v, UCUMcs-term) else UCUMcs-term(**as_dict(v)) for v in self.ucumCode]

        if not isinstance(self.altSymbol, list):
            self.altSymbol = [self.altSymbol] if self.altSymbol is not None else []
        self.altSymbol = [v if isinstance(v, str) else str(v) for v in self.altSymbol]

        if not isinstance(self.latexSymbol, list):
            self.latexSymbol = [self.latexSymbol] if self.latexSymbol is not None else []
        self.latexSymbol = [v if isinstance(v, str) else str(v) for v in self.latexSymbol]

        if not isinstance(self.symbol, list):
            self.symbol = [self.symbol] if self.symbol is not None else []
        self.symbol = [v if isinstance(v, str) else str(v) for v in self.symbol]

        if not isinstance(self.prefixMultiplier, list):
            self.prefixMultiplier = [self.prefixMultiplier] if self.prefixMultiplier is not None else []
        self.prefixMultiplier = [v if isinstance(v, str) else str(v) for v in self.prefixMultiplier]

        if not isinstance(self.guidance, list):
            self.guidance = [self.guidance] if self.guidance is not None else []
        self.guidance = [v if isinstance(v, str) else str(v) for v in self.guidance]

        if not isinstance(self.id, list):
            self.id = [self.id] if self.id is not None else []
        self.id = [v if isinstance(v, str) else str(v) for v in self.id]

        if not isinstance(self.hasRule, list):
            self.hasRule = [self.hasRule] if self.hasRule is not None else []
        self.hasRule = [v if isinstance(v, Rule) else Rule(**as_dict(v)) for v in self.hasRule]

        if not isinstance(self.isReplacedBy, list):
            self.isReplacedBy = [self.isReplacedBy] if self.isReplacedBy is not None else []
        self.isReplacedBy = [v if isinstance(v, str) else str(v) for v in self.isReplacedBy]

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.abbreviation, list):
            self.abbreviation = [self.abbreviation] if self.abbreviation is not None else []
        self.abbreviation = [v if isinstance(v, str) else str(v) for v in self.abbreviation]

        if not isinstance(self.deprecated, list):
            self.deprecated = [self.deprecated] if self.deprecated is not None else []
        self.deprecated = [v if isinstance(v, str) else str(v) for v in self.deprecated]

        if not isinstance(self.plainTextDescription, list):
            self.plainTextDescription = [self.plainTextDescription] if self.plainTextDescription is not None else []
        self.plainTextDescription = [v if isinstance(v, str) else str(v) for v in self.plainTextDescription]

        super().__post_init__(**kwargs)


class BinaryPrefix(Prefix):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["BinaryPrefix"]
    class_class_curie: ClassVar[str] = "qudt:BinaryPrefix"
    class_name: ClassVar[str] = "BinaryPrefix"
    class_model_uri: ClassVar[URIRef] = QUDT.BinaryPrefix


class DecimalPrefix(Prefix):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["DecimalPrefix"]
    class_class_curie: ClassVar[str] = "qudt:DecimalPrefix"
    class_name: ClassVar[str] = "DecimalPrefix"
    class_model_uri: ClassVar[URIRef] = QUDT.DecimalPrefix


@dataclass(repr=False)
class QuantityKind(Verifiable):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["QuantityKind"]
    class_class_curie: ClassVar[str] = "qudt:QuantityKind"
    class_name: ClassVar[str] = "QuantityKind"
    class_model_uri: ClassVar[URIRef] = QUDT.QuantityKind

    belongsToSystemOfQuantities: Optional[Union[Union[dict, SystemOfQuantityKinds], list[Union[dict, SystemOfQuantityKinds]]]] = empty_list()
    dimensionVectorForSI: Optional[Union[Union[dict, QuantityKindDimensionVectorSI], list[Union[dict, QuantityKindDimensionVectorSI]]]] = empty_list()
    exactMatch: Optional[Union[Union[dict, "QuantityKind"], list[Union[dict, "QuantityKind"]]]] = empty_list()
    hasDimensionVector: Optional[Union[Union[dict, QuantityKindDimensionVector], list[Union[dict, QuantityKindDimensionVector]]]] = empty_list()
    iec61360Code: Optional[Union[str, list[str]]] = empty_list()
    applicableCGSUnit: Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]] = empty_list()
    applicableISOUnit: Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]] = empty_list()
    applicableImperialUnit: Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]] = empty_list()
    applicableSIUnit: Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]] = empty_list()
    applicableUSCustomaryUnit: Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]] = empty_list()
    applicableUnit: Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]] = empty_list()
    qkdvDenominator: Optional[Union[Union[dict, QuantityKindDimensionVector], list[Union[dict, QuantityKindDimensionVector]]]] = empty_list()
    qkdvNumerator: Optional[Union[Union[dict, QuantityKindDimensionVector], list[Union[dict, QuantityKindDimensionVector]]]] = empty_list()
    latexDefinition: Optional[Union[str, list[str]]] = empty_list()
    mathMLdefinition: Optional[Union[str, list[str]]] = empty_list()
    guidance: Optional[Union[str, list[str]]] = empty_list()
    id: Optional[Union[str, list[str]]] = empty_list()
    hasRule: Optional[Union[Union[dict, "Rule"], list[Union[dict, "Rule"]]]] = empty_list()
    isReplacedBy: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[Union[str, list[str]]] = empty_list()
    abbreviation: Optional[Union[str, list[str]]] = empty_list()
    deprecated: Optional[Union[str, list[str]]] = empty_list()
    plainTextDescription: Optional[Union[str, list[str]]] = empty_list()
    broader: Optional[Union[dict, "QuantityKind"]] = None
    altSymbol: Optional[Union[str, list[str]]] = empty_list()
    latexSymbol: Optional[Union[str, list[str]]] = empty_list()
    symbol: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.belongsToSystemOfQuantities, list):
            self.belongsToSystemOfQuantities = [self.belongsToSystemOfQuantities] if self.belongsToSystemOfQuantities is not None else []
        self.belongsToSystemOfQuantities = [v if isinstance(v, SystemOfQuantityKinds) else SystemOfQuantityKinds(**as_dict(v)) for v in self.belongsToSystemOfQuantities]

        if not isinstance(self.dimensionVectorForSI, list):
            self.dimensionVectorForSI = [self.dimensionVectorForSI] if self.dimensionVectorForSI is not None else []
        self.dimensionVectorForSI = [v if isinstance(v, QuantityKindDimensionVectorSI) else QuantityKindDimensionVectorSI(**as_dict(v)) for v in self.dimensionVectorForSI]

        if not isinstance(self.exactMatch, list):
            self.exactMatch = [self.exactMatch] if self.exactMatch is not None else []
        self.exactMatch = [v if isinstance(v, QuantityKind) else QuantityKind(**as_dict(v)) for v in self.exactMatch]

        if not isinstance(self.hasDimensionVector, list):
            self.hasDimensionVector = [self.hasDimensionVector] if self.hasDimensionVector is not None else []
        self.hasDimensionVector = [v if isinstance(v, QuantityKindDimensionVector) else QuantityKindDimensionVector(**as_dict(v)) for v in self.hasDimensionVector]

        if not isinstance(self.iec61360Code, list):
            self.iec61360Code = [self.iec61360Code] if self.iec61360Code is not None else []
        self.iec61360Code = [v if isinstance(v, str) else str(v) for v in self.iec61360Code]

        if not isinstance(self.applicableCGSUnit, list):
            self.applicableCGSUnit = [self.applicableCGSUnit] if self.applicableCGSUnit is not None else []
        self.applicableCGSUnit = [v if isinstance(v, Unit) else Unit(**as_dict(v)) for v in self.applicableCGSUnit]

        if not isinstance(self.applicableISOUnit, list):
            self.applicableISOUnit = [self.applicableISOUnit] if self.applicableISOUnit is not None else []
        self.applicableISOUnit = [v if isinstance(v, Unit) else Unit(**as_dict(v)) for v in self.applicableISOUnit]

        if not isinstance(self.applicableImperialUnit, list):
            self.applicableImperialUnit = [self.applicableImperialUnit] if self.applicableImperialUnit is not None else []
        self.applicableImperialUnit = [v if isinstance(v, Unit) else Unit(**as_dict(v)) for v in self.applicableImperialUnit]

        if not isinstance(self.applicableSIUnit, list):
            self.applicableSIUnit = [self.applicableSIUnit] if self.applicableSIUnit is not None else []
        self.applicableSIUnit = [v if isinstance(v, Unit) else Unit(**as_dict(v)) for v in self.applicableSIUnit]

        if not isinstance(self.applicableUSCustomaryUnit, list):
            self.applicableUSCustomaryUnit = [self.applicableUSCustomaryUnit] if self.applicableUSCustomaryUnit is not None else []
        self.applicableUSCustomaryUnit = [v if isinstance(v, Unit) else Unit(**as_dict(v)) for v in self.applicableUSCustomaryUnit]

        if not isinstance(self.applicableUnit, list):
            self.applicableUnit = [self.applicableUnit] if self.applicableUnit is not None else []
        self.applicableUnit = [v if isinstance(v, Unit) else Unit(**as_dict(v)) for v in self.applicableUnit]

        if not isinstance(self.qkdvDenominator, list):
            self.qkdvDenominator = [self.qkdvDenominator] if self.qkdvDenominator is not None else []
        self.qkdvDenominator = [v if isinstance(v, QuantityKindDimensionVector) else QuantityKindDimensionVector(**as_dict(v)) for v in self.qkdvDenominator]

        if not isinstance(self.qkdvNumerator, list):
            self.qkdvNumerator = [self.qkdvNumerator] if self.qkdvNumerator is not None else []
        self.qkdvNumerator = [v if isinstance(v, QuantityKindDimensionVector) else QuantityKindDimensionVector(**as_dict(v)) for v in self.qkdvNumerator]

        if not isinstance(self.latexDefinition, list):
            self.latexDefinition = [self.latexDefinition] if self.latexDefinition is not None else []
        self.latexDefinition = [v if isinstance(v, str) else str(v) for v in self.latexDefinition]

        if not isinstance(self.mathMLdefinition, list):
            self.mathMLdefinition = [self.mathMLdefinition] if self.mathMLdefinition is not None else []
        self.mathMLdefinition = [v if isinstance(v, str) else str(v) for v in self.mathMLdefinition]

        if not isinstance(self.guidance, list):
            self.guidance = [self.guidance] if self.guidance is not None else []
        self.guidance = [v if isinstance(v, str) else str(v) for v in self.guidance]

        if not isinstance(self.id, list):
            self.id = [self.id] if self.id is not None else []
        self.id = [v if isinstance(v, str) else str(v) for v in self.id]

        if not isinstance(self.hasRule, list):
            self.hasRule = [self.hasRule] if self.hasRule is not None else []
        self.hasRule = [v if isinstance(v, Rule) else Rule(**as_dict(v)) for v in self.hasRule]

        if not isinstance(self.isReplacedBy, list):
            self.isReplacedBy = [self.isReplacedBy] if self.isReplacedBy is not None else []
        self.isReplacedBy = [v if isinstance(v, str) else str(v) for v in self.isReplacedBy]

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.abbreviation, list):
            self.abbreviation = [self.abbreviation] if self.abbreviation is not None else []
        self.abbreviation = [v if isinstance(v, str) else str(v) for v in self.abbreviation]

        if not isinstance(self.deprecated, list):
            self.deprecated = [self.deprecated] if self.deprecated is not None else []
        self.deprecated = [v if isinstance(v, str) else str(v) for v in self.deprecated]

        if not isinstance(self.plainTextDescription, list):
            self.plainTextDescription = [self.plainTextDescription] if self.plainTextDescription is not None else []
        self.plainTextDescription = [v if isinstance(v, str) else str(v) for v in self.plainTextDescription]

        if self.broader is not None and not isinstance(self.broader, QuantityKind):
            self.broader = QuantityKind(**as_dict(self.broader))

        if not isinstance(self.altSymbol, list):
            self.altSymbol = [self.altSymbol] if self.altSymbol is not None else []
        self.altSymbol = [v if isinstance(v, str) else str(v) for v in self.altSymbol]

        if not isinstance(self.latexSymbol, list):
            self.latexSymbol = [self.latexSymbol] if self.latexSymbol is not None else []
        self.latexSymbol = [v if isinstance(v, str) else str(v) for v in self.latexSymbol]

        if not isinstance(self.symbol, list):
            self.symbol = [self.symbol] if self.symbol is not None else []
        self.symbol = [v if isinstance(v, str) else str(v) for v in self.symbol]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantityType(EnumeratedValue):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["QuantityType"]
    class_class_curie: ClassVar[str] = "qudt:QuantityType"
    class_name: ClassVar[str] = "QuantityType"
    class_model_uri: ClassVar[URIRef] = QUDT.QuantityType

    value: Optional[Union[Union[dict, QuantityKind], list[Union[dict, QuantityKind]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.value, list):
            self.value = [self.value] if self.value is not None else []
        self.value = [v if isinstance(v, QuantityKind) else QuantityKind(**as_dict(v)) for v in self.value]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Rule(Verifiable):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Rule"]
    class_class_curie: ClassVar[str] = "qudt:Rule"
    class_name: ClassVar[str] = "Rule"
    class_model_uri: ClassVar[URIRef] = QUDT.Rule

    ruleType: Optional[Union[Union[dict, "RuleType"], list[Union[dict, "RuleType"]]]] = empty_list()
    rationale: Optional[Union[str, list[str]]] = empty_list()
    guidance: Optional[Union[str, list[str]]] = empty_list()
    id: Optional[Union[str, list[str]]] = empty_list()
    hasRule: Optional[Union[Union[dict, "Rule"], list[Union[dict, "Rule"]]]] = empty_list()
    isReplacedBy: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[Union[str, list[str]]] = empty_list()
    abbreviation: Optional[Union[str, list[str]]] = empty_list()
    deprecated: Optional[Union[str, list[str]]] = empty_list()
    plainTextDescription: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.ruleType, list):
            self.ruleType = [self.ruleType] if self.ruleType is not None else []
        self.ruleType = [v if isinstance(v, RuleType) else RuleType(**as_dict(v)) for v in self.ruleType]

        if not isinstance(self.rationale, list):
            self.rationale = [self.rationale] if self.rationale is not None else []
        self.rationale = [v if isinstance(v, str) else str(v) for v in self.rationale]

        if not isinstance(self.guidance, list):
            self.guidance = [self.guidance] if self.guidance is not None else []
        self.guidance = [v if isinstance(v, str) else str(v) for v in self.guidance]

        if not isinstance(self.id, list):
            self.id = [self.id] if self.id is not None else []
        self.id = [v if isinstance(v, str) else str(v) for v in self.id]

        if not isinstance(self.hasRule, list):
            self.hasRule = [self.hasRule] if self.hasRule is not None else []
        self.hasRule = [v if isinstance(v, Rule) else Rule(**as_dict(v)) for v in self.hasRule]

        if not isinstance(self.isReplacedBy, list):
            self.isReplacedBy = [self.isReplacedBy] if self.isReplacedBy is not None else []
        self.isReplacedBy = [v if isinstance(v, str) else str(v) for v in self.isReplacedBy]

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.abbreviation, list):
            self.abbreviation = [self.abbreviation] if self.abbreviation is not None else []
        self.abbreviation = [v if isinstance(v, str) else str(v) for v in self.abbreviation]

        if not isinstance(self.deprecated, list):
            self.deprecated = [self.deprecated] if self.deprecated is not None else []
        self.deprecated = [v if isinstance(v, str) else str(v) for v in self.deprecated]

        if not isinstance(self.plainTextDescription, list):
            self.plainTextDescription = [self.plainTextDescription] if self.plainTextDescription is not None else []
        self.plainTextDescription = [v if isinstance(v, str) else str(v) for v in self.plainTextDescription]

        super().__post_init__(**kwargs)


class RuleType(EnumeratedValue):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["RuleType"]
    class_class_curie: ClassVar[str] = "qudt:RuleType"
    class_name: ClassVar[str] = "RuleType"
    class_model_uri: ClassVar[URIRef] = QUDT.RuleType


@dataclass(repr=False)
class ScaleType(EnumeratedValue):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["ScaleType"]
    class_class_curie: ClassVar[str] = "qudt:ScaleType"
    class_name: ClassVar[str] = "ScaleType"
    class_model_uri: ClassVar[URIRef] = QUDT.ScaleType

    permissibleMaths: Optional[Union[Union[dict, MathsFunctionType], list[Union[dict, MathsFunctionType]]]] = empty_list()
    permissibleTransformation: Optional[Union[Union[dict, "TransformType"], list[Union[dict, "TransformType"]]]] = empty_list()
    dataStructure: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.permissibleMaths, list):
            self.permissibleMaths = [self.permissibleMaths] if self.permissibleMaths is not None else []
        self.permissibleMaths = [v if isinstance(v, MathsFunctionType) else MathsFunctionType(**as_dict(v)) for v in self.permissibleMaths]

        if not isinstance(self.permissibleTransformation, list):
            self.permissibleTransformation = [self.permissibleTransformation] if self.permissibleTransformation is not None else []
        self.permissibleTransformation = [v if isinstance(v, TransformType) else TransformType(**as_dict(v)) for v in self.permissibleTransformation]

        if not isinstance(self.dataStructure, list):
            self.dataStructure = [self.dataStructure] if self.dataStructure is not None else []
        self.dataStructure = [v if isinstance(v, str) else str(v) for v in self.dataStructure]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SystemOfUnits(Verifiable):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["SystemOfUnits"]
    class_class_curie: ClassVar[str] = "qudt:SystemOfUnits"
    class_name: ClassVar[str] = "SystemOfUnits"
    class_model_uri: ClassVar[URIRef] = QUDT.SystemOfUnits

    applicablePhysicalConstant: Optional[Union[Union[dict, PhysicalConstant], list[Union[dict, PhysicalConstant]]]] = empty_list()
    hasAllowedUnit: Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]] = empty_list()
    hasBaseUnit: Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]] = empty_list()
    hasCoherentUnit: Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]] = empty_list()
    hasDefinedUnit: Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]] = empty_list()
    hasDerivedCoherentUnit: Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]] = empty_list()
    hasDerivedUnit: Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]] = empty_list()
    hasUnit: Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]] = empty_list()
    prefix: Optional[Union[Union[dict, Prefix], list[Union[dict, Prefix]]]] = empty_list()
    guidance: Optional[Union[str, list[str]]] = empty_list()
    id: Optional[Union[str, list[str]]] = empty_list()
    hasRule: Optional[Union[Union[dict, Rule], list[Union[dict, Rule]]]] = empty_list()
    isReplacedBy: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[Union[str, list[str]]] = empty_list()
    abbreviation: Optional[Union[str, list[str]]] = empty_list()
    deprecated: Optional[Union[str, list[str]]] = empty_list()
    plainTextDescription: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.applicablePhysicalConstant, list):
            self.applicablePhysicalConstant = [self.applicablePhysicalConstant] if self.applicablePhysicalConstant is not None else []
        self.applicablePhysicalConstant = [v if isinstance(v, PhysicalConstant) else PhysicalConstant(**as_dict(v)) for v in self.applicablePhysicalConstant]

        if not isinstance(self.hasAllowedUnit, list):
            self.hasAllowedUnit = [self.hasAllowedUnit] if self.hasAllowedUnit is not None else []
        self.hasAllowedUnit = [v if isinstance(v, Unit) else Unit(**as_dict(v)) for v in self.hasAllowedUnit]

        if not isinstance(self.hasBaseUnit, list):
            self.hasBaseUnit = [self.hasBaseUnit] if self.hasBaseUnit is not None else []
        self.hasBaseUnit = [v if isinstance(v, Unit) else Unit(**as_dict(v)) for v in self.hasBaseUnit]

        if not isinstance(self.hasCoherentUnit, list):
            self.hasCoherentUnit = [self.hasCoherentUnit] if self.hasCoherentUnit is not None else []
        self.hasCoherentUnit = [v if isinstance(v, Unit) else Unit(**as_dict(v)) for v in self.hasCoherentUnit]

        if not isinstance(self.hasDefinedUnit, list):
            self.hasDefinedUnit = [self.hasDefinedUnit] if self.hasDefinedUnit is not None else []
        self.hasDefinedUnit = [v if isinstance(v, Unit) else Unit(**as_dict(v)) for v in self.hasDefinedUnit]

        if not isinstance(self.hasDerivedCoherentUnit, list):
            self.hasDerivedCoherentUnit = [self.hasDerivedCoherentUnit] if self.hasDerivedCoherentUnit is not None else []
        self.hasDerivedCoherentUnit = [v if isinstance(v, Unit) else Unit(**as_dict(v)) for v in self.hasDerivedCoherentUnit]

        if not isinstance(self.hasDerivedUnit, list):
            self.hasDerivedUnit = [self.hasDerivedUnit] if self.hasDerivedUnit is not None else []
        self.hasDerivedUnit = [v if isinstance(v, Unit) else Unit(**as_dict(v)) for v in self.hasDerivedUnit]

        if not isinstance(self.hasUnit, list):
            self.hasUnit = [self.hasUnit] if self.hasUnit is not None else []
        self.hasUnit = [v if isinstance(v, Unit) else Unit(**as_dict(v)) for v in self.hasUnit]

        if not isinstance(self.prefix, list):
            self.prefix = [self.prefix] if self.prefix is not None else []
        self.prefix = [v if isinstance(v, Prefix) else Prefix(**as_dict(v)) for v in self.prefix]

        if not isinstance(self.guidance, list):
            self.guidance = [self.guidance] if self.guidance is not None else []
        self.guidance = [v if isinstance(v, str) else str(v) for v in self.guidance]

        if not isinstance(self.id, list):
            self.id = [self.id] if self.id is not None else []
        self.id = [v if isinstance(v, str) else str(v) for v in self.id]

        if not isinstance(self.hasRule, list):
            self.hasRule = [self.hasRule] if self.hasRule is not None else []
        self.hasRule = [v if isinstance(v, Rule) else Rule(**as_dict(v)) for v in self.hasRule]

        if not isinstance(self.isReplacedBy, list):
            self.isReplacedBy = [self.isReplacedBy] if self.isReplacedBy is not None else []
        self.isReplacedBy = [v if isinstance(v, str) else str(v) for v in self.isReplacedBy]

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.abbreviation, list):
            self.abbreviation = [self.abbreviation] if self.abbreviation is not None else []
        self.abbreviation = [v if isinstance(v, str) else str(v) for v in self.abbreviation]

        if not isinstance(self.deprecated, list):
            self.deprecated = [self.deprecated] if self.deprecated is not None else []
        self.deprecated = [v if isinstance(v, str) else str(v) for v in self.deprecated]

        if not isinstance(self.plainTextDescription, list):
            self.plainTextDescription = [self.plainTextDescription] if self.plainTextDescription is not None else []
        self.plainTextDescription = [v if isinstance(v, str) else str(v) for v in self.plainTextDescription]

        super().__post_init__(**kwargs)


class TransformType(EnumeratedValue):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["TransformType"]
    class_class_curie: ClassVar[str] = "qudt:TransformType"
    class_name: ClassVar[str] = "TransformType"
    class_model_uri: ClassVar[URIRef] = QUDT.TransformType


@dataclass(repr=False)
class Unit(Verifiable):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Unit"]
    class_class_curie: ClassVar[str] = "qudt:Unit"
    class_name: ClassVar[str] = "Unit"
    class_model_uri: ClassVar[URIRef] = QUDT.Unit

    hasReciprocalUnit: Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]] = empty_list()
    isUnitOfSystem: Optional[Union[Union[dict, SystemOfUnits], list[Union[dict, SystemOfUnits]]]] = empty_list()
    omUnit: Optional[Union[str, list[str]]] = empty_list()
    unitFor: Optional[Union[str, list[str]]] = empty_list()
    applicableSystem: Optional[Union[Union[dict, SystemOfUnits], list[Union[dict, SystemOfUnits]]]] = empty_list()
    definedUnitOfSystem: Optional[Union[Union[dict, SystemOfUnits], list[Union[dict, SystemOfUnits]]]] = empty_list()
    derivedCoherentUnitOfSystem: Optional[Union[Union[dict, SystemOfUnits], list[Union[dict, SystemOfUnits]]]] = empty_list()
    derivedUnitOfSystem: Optional[Union[Union[dict, SystemOfUnits], list[Union[dict, SystemOfUnits]]]] = empty_list()
    exactMatch: Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]] = empty_list()
    hasDimensionVector: Optional[Union[Union[dict, QuantityKindDimensionVector], list[Union[dict, QuantityKindDimensionVector]]]] = empty_list()
    hasFactorUnit: Optional[Union[Union[dict, "Class"], list[Union[dict, "Class"]]]] = empty_list()
    hasQuantityKind: Optional[Union[Union[dict, QuantityKind], list[Union[dict, QuantityKind]]]] = empty_list()
    iec61360Code: Optional[Union[str, list[str]]] = empty_list()
    prefix: Optional[Union[Union[dict, Prefix], list[Union[dict, Prefix]]]] = empty_list()
    qkdvDenominator: Optional[Union[Union[dict, QuantityKindDimensionVector], list[Union[dict, QuantityKindDimensionVector]]]] = empty_list()
    qkdvNumerator: Optional[Union[Union[dict, QuantityKindDimensionVector], list[Union[dict, QuantityKindDimensionVector]]]] = empty_list()
    scalingOf: Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]] = empty_list()
    ucumCode: Optional[Union[Union[dict, "UCUMcs"], list[Union[dict, "UCUMcs"]]]] = empty_list()
    udunitsCode: Optional[Union[str, list[str]]] = empty_list()
    uneceCommonCode: Optional[Union[str, list[str]]] = empty_list()
    altSymbol: Optional[Union[str, list[str]]] = empty_list()
    latexDefinition: Optional[Union[str, list[str]]] = empty_list()
    latexSymbol: Optional[Union[str, list[str]]] = empty_list()
    siUnitsExpression: Optional[Union[str, list[str]]] = empty_list()
    symbol: Optional[Union[str, list[str]]] = empty_list()
    conversionMultiplier: Optional[Union[str, list[str]]] = empty_list()
    conversionMultiplierSN: Optional[Union[str, list[str]]] = empty_list()
    conversionOffset: Optional[Union[str, list[str]]] = empty_list()
    conversionOffsetSN: Optional[Union[str, list[str]]] = empty_list()
    factorUnitScalar: Optional[Union[str, list[str]]] = empty_list()
    mathMLdefinition: Optional[Union[str, list[str]]] = empty_list()
    guidance: Optional[Union[str, list[str]]] = empty_list()
    id: Optional[Union[str, list[str]]] = empty_list()
    hasRule: Optional[Union[Union[dict, Rule], list[Union[dict, Rule]]]] = empty_list()
    isReplacedBy: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[Union[str, list[str]]] = empty_list()
    abbreviation: Optional[Union[str, list[str]]] = empty_list()
    deprecated: Optional[Union[str, list[str]]] = empty_list()
    plainTextDescription: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.hasReciprocalUnit, list):
            self.hasReciprocalUnit = [self.hasReciprocalUnit] if self.hasReciprocalUnit is not None else []
        self.hasReciprocalUnit = [v if isinstance(v, Unit) else Unit(**as_dict(v)) for v in self.hasReciprocalUnit]

        if not isinstance(self.isUnitOfSystem, list):
            self.isUnitOfSystem = [self.isUnitOfSystem] if self.isUnitOfSystem is not None else []
        self.isUnitOfSystem = [v if isinstance(v, SystemOfUnits) else SystemOfUnits(**as_dict(v)) for v in self.isUnitOfSystem]

        if not isinstance(self.omUnit, list):
            self.omUnit = [self.omUnit] if self.omUnit is not None else []
        self.omUnit = [v if isinstance(v, str) else str(v) for v in self.omUnit]

        if not isinstance(self.unitFor, list):
            self.unitFor = [self.unitFor] if self.unitFor is not None else []
        self.unitFor = [v if isinstance(v, str) else str(v) for v in self.unitFor]

        if not isinstance(self.applicableSystem, list):
            self.applicableSystem = [self.applicableSystem] if self.applicableSystem is not None else []
        self.applicableSystem = [v if isinstance(v, SystemOfUnits) else SystemOfUnits(**as_dict(v)) for v in self.applicableSystem]

        if not isinstance(self.definedUnitOfSystem, list):
            self.definedUnitOfSystem = [self.definedUnitOfSystem] if self.definedUnitOfSystem is not None else []
        self.definedUnitOfSystem = [v if isinstance(v, SystemOfUnits) else SystemOfUnits(**as_dict(v)) for v in self.definedUnitOfSystem]

        if not isinstance(self.derivedCoherentUnitOfSystem, list):
            self.derivedCoherentUnitOfSystem = [self.derivedCoherentUnitOfSystem] if self.derivedCoherentUnitOfSystem is not None else []
        self.derivedCoherentUnitOfSystem = [v if isinstance(v, SystemOfUnits) else SystemOfUnits(**as_dict(v)) for v in self.derivedCoherentUnitOfSystem]

        if not isinstance(self.derivedUnitOfSystem, list):
            self.derivedUnitOfSystem = [self.derivedUnitOfSystem] if self.derivedUnitOfSystem is not None else []
        self.derivedUnitOfSystem = [v if isinstance(v, SystemOfUnits) else SystemOfUnits(**as_dict(v)) for v in self.derivedUnitOfSystem]

        if not isinstance(self.exactMatch, list):
            self.exactMatch = [self.exactMatch] if self.exactMatch is not None else []
        self.exactMatch = [v if isinstance(v, Unit) else Unit(**as_dict(v)) for v in self.exactMatch]

        if not isinstance(self.hasDimensionVector, list):
            self.hasDimensionVector = [self.hasDimensionVector] if self.hasDimensionVector is not None else []
        self.hasDimensionVector = [v if isinstance(v, QuantityKindDimensionVector) else QuantityKindDimensionVector(**as_dict(v)) for v in self.hasDimensionVector]

        if not isinstance(self.hasFactorUnit, list):
            self.hasFactorUnit = [self.hasFactorUnit] if self.hasFactorUnit is not None else []
        self.hasFactorUnit = [v if isinstance(v, Class) else Class(**as_dict(v)) for v in self.hasFactorUnit]

        if not isinstance(self.hasQuantityKind, list):
            self.hasQuantityKind = [self.hasQuantityKind] if self.hasQuantityKind is not None else []
        self.hasQuantityKind = [v if isinstance(v, QuantityKind) else QuantityKind(**as_dict(v)) for v in self.hasQuantityKind]

        if not isinstance(self.iec61360Code, list):
            self.iec61360Code = [self.iec61360Code] if self.iec61360Code is not None else []
        self.iec61360Code = [v if isinstance(v, str) else str(v) for v in self.iec61360Code]

        if not isinstance(self.prefix, list):
            self.prefix = [self.prefix] if self.prefix is not None else []
        self.prefix = [v if isinstance(v, Prefix) else Prefix(**as_dict(v)) for v in self.prefix]

        if not isinstance(self.qkdvDenominator, list):
            self.qkdvDenominator = [self.qkdvDenominator] if self.qkdvDenominator is not None else []
        self.qkdvDenominator = [v if isinstance(v, QuantityKindDimensionVector) else QuantityKindDimensionVector(**as_dict(v)) for v in self.qkdvDenominator]

        if not isinstance(self.qkdvNumerator, list):
            self.qkdvNumerator = [self.qkdvNumerator] if self.qkdvNumerator is not None else []
        self.qkdvNumerator = [v if isinstance(v, QuantityKindDimensionVector) else QuantityKindDimensionVector(**as_dict(v)) for v in self.qkdvNumerator]

        if not isinstance(self.scalingOf, list):
            self.scalingOf = [self.scalingOf] if self.scalingOf is not None else []
        self.scalingOf = [v if isinstance(v, Unit) else Unit(**as_dict(v)) for v in self.scalingOf]

        if not isinstance(self.ucumCode, list):
            self.ucumCode = [self.ucumCode] if self.ucumCode is not None else []
        self.ucumCode = [v if isinstance(v, UCUMcs) else UCUMcs(**as_dict(v)) for v in self.ucumCode]

        if not isinstance(self.udunitsCode, list):
            self.udunitsCode = [self.udunitsCode] if self.udunitsCode is not None else []
        self.udunitsCode = [v if isinstance(v, str) else str(v) for v in self.udunitsCode]

        if not isinstance(self.uneceCommonCode, list):
            self.uneceCommonCode = [self.uneceCommonCode] if self.uneceCommonCode is not None else []
        self.uneceCommonCode = [v if isinstance(v, str) else str(v) for v in self.uneceCommonCode]

        if not isinstance(self.altSymbol, list):
            self.altSymbol = [self.altSymbol] if self.altSymbol is not None else []
        self.altSymbol = [v if isinstance(v, str) else str(v) for v in self.altSymbol]

        if not isinstance(self.latexDefinition, list):
            self.latexDefinition = [self.latexDefinition] if self.latexDefinition is not None else []
        self.latexDefinition = [v if isinstance(v, str) else str(v) for v in self.latexDefinition]

        if not isinstance(self.latexSymbol, list):
            self.latexSymbol = [self.latexSymbol] if self.latexSymbol is not None else []
        self.latexSymbol = [v if isinstance(v, str) else str(v) for v in self.latexSymbol]

        if not isinstance(self.siUnitsExpression, list):
            self.siUnitsExpression = [self.siUnitsExpression] if self.siUnitsExpression is not None else []
        self.siUnitsExpression = [v if isinstance(v, str) else str(v) for v in self.siUnitsExpression]

        if not isinstance(self.symbol, list):
            self.symbol = [self.symbol] if self.symbol is not None else []
        self.symbol = [v if isinstance(v, str) else str(v) for v in self.symbol]

        if not isinstance(self.conversionMultiplier, list):
            self.conversionMultiplier = [self.conversionMultiplier] if self.conversionMultiplier is not None else []
        self.conversionMultiplier = [v if isinstance(v, str) else str(v) for v in self.conversionMultiplier]

        if not isinstance(self.conversionMultiplierSN, list):
            self.conversionMultiplierSN = [self.conversionMultiplierSN] if self.conversionMultiplierSN is not None else []
        self.conversionMultiplierSN = [v if isinstance(v, str) else str(v) for v in self.conversionMultiplierSN]

        if not isinstance(self.conversionOffset, list):
            self.conversionOffset = [self.conversionOffset] if self.conversionOffset is not None else []
        self.conversionOffset = [v if isinstance(v, str) else str(v) for v in self.conversionOffset]

        if not isinstance(self.conversionOffsetSN, list):
            self.conversionOffsetSN = [self.conversionOffsetSN] if self.conversionOffsetSN is not None else []
        self.conversionOffsetSN = [v if isinstance(v, str) else str(v) for v in self.conversionOffsetSN]

        if not isinstance(self.factorUnitScalar, list):
            self.factorUnitScalar = [self.factorUnitScalar] if self.factorUnitScalar is not None else []
        self.factorUnitScalar = [v if isinstance(v, str) else str(v) for v in self.factorUnitScalar]

        if not isinstance(self.mathMLdefinition, list):
            self.mathMLdefinition = [self.mathMLdefinition] if self.mathMLdefinition is not None else []
        self.mathMLdefinition = [v if isinstance(v, str) else str(v) for v in self.mathMLdefinition]

        if not isinstance(self.guidance, list):
            self.guidance = [self.guidance] if self.guidance is not None else []
        self.guidance = [v if isinstance(v, str) else str(v) for v in self.guidance]

        if not isinstance(self.id, list):
            self.id = [self.id] if self.id is not None else []
        self.id = [v if isinstance(v, str) else str(v) for v in self.id]

        if not isinstance(self.hasRule, list):
            self.hasRule = [self.hasRule] if self.hasRule is not None else []
        self.hasRule = [v if isinstance(v, Rule) else Rule(**as_dict(v)) for v in self.hasRule]

        if not isinstance(self.isReplacedBy, list):
            self.isReplacedBy = [self.isReplacedBy] if self.isReplacedBy is not None else []
        self.isReplacedBy = [v if isinstance(v, str) else str(v) for v in self.isReplacedBy]

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.abbreviation, list):
            self.abbreviation = [self.abbreviation] if self.abbreviation is not None else []
        self.abbreviation = [v if isinstance(v, str) else str(v) for v in self.abbreviation]

        if not isinstance(self.deprecated, list):
            self.deprecated = [self.deprecated] if self.deprecated is not None else []
        self.deprecated = [v if isinstance(v, str) else str(v) for v in self.deprecated]

        if not isinstance(self.plainTextDescription, list):
            self.plainTextDescription = [self.plainTextDescription] if self.plainTextDescription is not None else []
        self.plainTextDescription = [v if isinstance(v, str) else str(v) for v in self.plainTextDescription]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContextualUnit(Unit):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["ContextualUnit"]
    class_class_curie: ClassVar[str] = "qudt:ContextualUnit"
    class_name: ClassVar[str] = "ContextualUnit"
    class_model_uri: ClassVar[URIRef] = QUDT.ContextualUnit

    broader: Optional[Union[dict, Unit]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.broader is not None and not isinstance(self.broader, Unit):
            self.broader = Unit(**as_dict(self.broader))

        super().__post_init__(**kwargs)


class DerivedUnit(Unit):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["DerivedUnit"]
    class_class_curie: ClassVar[str] = "qudt:DerivedUnit"
    class_name: ClassVar[str] = "DerivedUnit"
    class_model_uri: ClassVar[URIRef] = QUDT.DerivedUnit


class DimensionlessUnit(Unit):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["DimensionlessUnit"]
    class_class_curie: ClassVar[str] = "qudt:DimensionlessUnit"
    class_name: ClassVar[str] = "DimensionlessUnit"
    class_model_uri: ClassVar[URIRef] = QUDT.DimensionlessUnit


class AngleUnit(DimensionlessUnit):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["AngleUnit"]
    class_class_curie: ClassVar[str] = "qudt:AngleUnit"
    class_name: ClassVar[str] = "AngleUnit"
    class_model_uri: ClassVar[URIRef] = QUDT.AngleUnit


class CountingUnit(DimensionlessUnit):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["CountingUnit"]
    class_class_curie: ClassVar[str] = "qudt:CountingUnit"
    class_name: ClassVar[str] = "CountingUnit"
    class_model_uri: ClassVar[URIRef] = QUDT.CountingUnit


@dataclass(repr=False)
class CurrencyUnit(DimensionlessUnit):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["CurrencyUnit"]
    class_class_curie: ClassVar[str] = "qudt:CurrencyUnit"
    class_name: ClassVar[str] = "CurrencyUnit"
    class_model_uri: ClassVar[URIRef] = QUDT.CurrencyUnit

    currencyCode: Optional[Union[str, list[str]]] = empty_list()
    currencyExponent: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.currencyCode, list):
            self.currencyCode = [self.currencyCode] if self.currencyCode is not None else []
        self.currencyCode = [v if isinstance(v, str) else str(v) for v in self.currencyCode]

        if not isinstance(self.currencyExponent, list):
            self.currencyExponent = [self.currencyExponent] if self.currencyExponent is not None else []
        self.currencyExponent = [v if isinstance(v, str) else str(v) for v in self.currencyExponent]

        super().__post_init__(**kwargs)


class LogarithmicUnit(DimensionlessUnit):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["LogarithmicUnit"]
    class_class_curie: ClassVar[str] = "qudt:LogarithmicUnit"
    class_name: ClassVar[str] = "LogarithmicUnit"
    class_model_uri: ClassVar[URIRef] = QUDT.LogarithmicUnit


class PlaneAngleUnit(AngleUnit):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["PlaneAngleUnit"]
    class_class_curie: ClassVar[str] = "qudt:PlaneAngleUnit"
    class_name: ClassVar[str] = "PlaneAngleUnit"
    class_model_uri: ClassVar[URIRef] = QUDT.PlaneAngleUnit


class SolidAngleUnit(AngleUnit):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["SolidAngleUnit"]
    class_class_curie: ClassVar[str] = "qudt:SolidAngleUnit"
    class_name: ClassVar[str] = "SolidAngleUnit"
    class_model_uri: ClassVar[URIRef] = QUDT.SolidAngleUnit


class CatalogEntry(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VAEM["CatalogEntry"]
    class_class_curie: ClassVar[str] = "vaem:CatalogEntry"
    class_name: ClassVar[str] = "CatalogEntry"
    class_model_uri: ClassVar[URIRef] = QUDT.CatalogEntry


class List(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RDF["List"]
    class_class_curie: ClassVar[str] = "rdf:List"
    class_name: ClassVar[str] = "List"
    class_model_uri: ClassVar[URIRef] = QUDT.List


class Class(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL["Class"]
    class_class_curie: ClassVar[str] = "owl:Class"
    class_name: ClassVar[str] = "Class"
    class_model_uri: ClassVar[URIRef] = QUDT.Class


class AspectClass(Class):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["AspectClass"]
    class_class_curie: ClassVar[str] = "qudt:AspectClass"
    class_name: ClassVar[str] = "AspectClass"
    class_model_uri: ClassVar[URIRef] = QUDT.AspectClass


class Resource(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RDFS["Resource"]
    class_class_curie: ClassVar[str] = "rdfs:Resource"
    class_name: ClassVar[str] = "Resource"
    class_model_uri: ClassVar[URIRef] = QUDT.Resource


class GDay(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = XSD["gDay"]
    class_class_curie: ClassVar[str] = "xsd:gDay"
    class_name: ClassVar[str] = "gDay"
    class_model_uri: ClassVar[URIRef] = QUDT.GDay


class GMonth(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = XSD["gMonth"]
    class_class_curie: ClassVar[str] = "xsd:gMonth"
    class_name: ClassVar[str] = "gMonth"
    class_model_uri: ClassVar[URIRef] = QUDT.GMonth


class GMonthDay(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = XSD["gMonthDay"]
    class_class_curie: ClassVar[str] = "xsd:gMonthDay"
    class_name: ClassVar[str] = "gMonthDay"
    class_model_uri: ClassVar[URIRef] = QUDT.GMonthDay


class GYear(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = XSD["gYear"]
    class_class_curie: ClassVar[str] = "xsd:gYear"
    class_name: ClassVar[str] = "gYear"
    class_model_uri: ClassVar[URIRef] = QUDT.GYear


class GYearMonth(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = XSD["gYearMonth"]
    class_class_curie: ClassVar[str] = "xsd:gYearMonth"
    class_name: ClassVar[str] = "gYearMonth"
    class_model_uri: ClassVar[URIRef] = QUDT.GYearMonth


class Ontology(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL["Ontology"]
    class_class_curie: ClassVar[str] = "owl:Ontology"
    class_name: ClassVar[str] = "Ontology"
    class_model_uri: ClassVar[URIRef] = QUDT.Ontology


class LatexString(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["LatexString"]
    class_class_curie: ClassVar[str] = "qudt:LatexString"
    class_name: ClassVar[str] = "LatexString"
    class_model_uri: ClassVar[URIRef] = QUDT.LatexString


class UCUMcs(Resource):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["UCUMcs"]
    class_class_curie: ClassVar[str] = "qudt:UCUMcs"
    class_name: ClassVar[str] = "UCUMcs"
    class_model_uri: ClassVar[URIRef] = QUDT.UCUMcs


class UCUMcs-term(Resource):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["UCUMcs-term"]
    class_class_curie: ClassVar[str] = "qudt:UCUMcs-term"
    class_name: ClassVar[str] = "UCUMcs-term"
    class_model_uri: ClassVar[URIRef] = QUDT.UCUMcs-term


class ValueUnion(Resource):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["ValueUnion"]
    class_class_curie: ClassVar[str] = "qudt:ValueUnion"
    class_name: ClassVar[str] = "valueUnion"
    class_model_uri: ClassVar[URIRef] = QUDT.ValueUnion


# Enumerations


# Slots
class slots:
    pass

slots.isReplacedBy = Slot(uri=DCTERMS.isReplacedBy, name="isReplacedBy", curie=DCTERMS.curie('isReplacedBy'),
                   model_uri=QUDT.isReplacedBy, domain=None, range=Optional[Union[str, list[str]]])

slots.ansiSQLName = Slot(uri=QUDT.ansiSQLName, name="ansiSQLName", curie=QUDT.curie('ansiSQLName'),
                   model_uri=QUDT.ansiSQLName, domain=None, range=Optional[Union[str, list[str]]])

slots.applicableCGSUnit = Slot(uri=QUDT.applicableCGSUnit, name="applicableCGSUnit", curie=QUDT.curie('applicableCGSUnit'),
                   model_uri=QUDT.applicableCGSUnit, domain=None, range=Optional[Union[Union[dict, Unit], list[Union[dict, Unit]]]])

slots.applicableISOUnit = Slot(uri=QUDT.applicableISOUnit, name="applicableISOUnit", curie=QUDT.curie('applicableISOUnit'),
                   model_uri=QUDT.applicableISOUnit, domain=None, range=Optional[Union[Union[dict, Unit], list[Union[dict, Unit]]]])

slots.applicableImperialUnit = Slot(uri=QUDT.applicableImperialUnit, name="applicableImperialUnit", curie=QUDT.curie('applicableImperialUnit'),
                   model_uri=QUDT.applicableImperialUnit, domain=None, range=Optional[Union[Union[dict, Unit], list[Union[dict, Unit]]]])

slots.applicablePhysicalConstant = Slot(uri=QUDT.applicablePhysicalConstant, name="applicablePhysicalConstant", curie=QUDT.curie('applicablePhysicalConstant'),
                   model_uri=QUDT.applicablePhysicalConstant, domain=None, range=Optional[Union[str, list[str]]])

slots.applicablePlanckUnit = Slot(uri=QUDT.applicablePlanckUnit, name="applicablePlanckUnit", curie=QUDT.curie('applicablePlanckUnit'),
                   model_uri=QUDT.applicablePlanckUnit, domain=None, range=Optional[Union[Union[dict, Unit], list[Union[dict, Unit]]]])

slots.applicableSIUnit = Slot(uri=QUDT.applicableSIUnit, name="applicableSIUnit", curie=QUDT.curie('applicableSIUnit'),
                   model_uri=QUDT.applicableSIUnit, domain=None, range=Optional[Union[Union[dict, Unit], list[Union[dict, Unit]]]])

slots.applicableSystem = Slot(uri=QUDT.applicableSystem, name="applicableSystem", curie=QUDT.curie('applicableSystem'),
                   model_uri=QUDT.applicableSystem, domain=None, range=Optional[Union[str, list[str]]])

slots.applicableUSCustomaryUnit = Slot(uri=QUDT.applicableUSCustomaryUnit, name="applicableUSCustomaryUnit", curie=QUDT.curie('applicableUSCustomaryUnit'),
                   model_uri=QUDT.applicableUSCustomaryUnit, domain=None, range=Optional[Union[Union[dict, Unit], list[Union[dict, Unit]]]])

slots.applicableUnit = Slot(uri=QUDT.applicableUnit, name="applicableUnit", curie=QUDT.curie('applicableUnit'),
                   model_uri=QUDT.applicableUnit, domain=None, range=Optional[Union[Union[dict, Unit], list[Union[dict, Unit]]]])

slots.baseDimensionEnumeration = Slot(uri=QUDT.baseDimensionEnumeration, name="baseDimensionEnumeration", curie=QUDT.curie('baseDimensionEnumeration'),
                   model_uri=QUDT.baseDimensionEnumeration, domain=None, range=Optional[Union[Union[dict, Enumeration], list[Union[dict, Enumeration]]]])

slots.baseUnitOfSystem = Slot(uri=QUDT.baseUnitOfSystem, name="baseUnitOfSystem", curie=QUDT.curie('baseUnitOfSystem'),
                   model_uri=QUDT.baseUnitOfSystem, domain=None, range=Optional[Union[Union[dict, SystemOfUnits], list[Union[dict, SystemOfUnits]]]])

slots.basis = Slot(uri=QUDT.basis, name="basis", curie=QUDT.curie('basis'),
                   model_uri=QUDT.basis, domain=None, range=Optional[Union[str, list[str]]])

slots.belongsToSystemOfQuantities = Slot(uri=QUDT.belongsToSystemOfQuantities, name="belongsToSystemOfQuantities", curie=QUDT.curie('belongsToSystemOfQuantities'),
                   model_uri=QUDT.belongsToSystemOfQuantities, domain=None, range=Optional[Union[Union[dict, SystemOfQuantityKinds], list[Union[dict, SystemOfQuantityKinds]]]])

slots.bitOrder = Slot(uri=QUDT.bitOrder, name="bitOrder", curie=QUDT.curie('bitOrder'),
                   model_uri=QUDT.bitOrder, domain=None, range=Optional[Union[Union[dict, EndianType], list[Union[dict, EndianType]]]])

slots.byteOrder = Slot(uri=QUDT.byteOrder, name="byteOrder", curie=QUDT.curie('byteOrder'),
                   model_uri=QUDT.byteOrder, domain=None, range=Optional[Union[Union[dict, EndianType], list[Union[dict, EndianType]]]])

slots.cName = Slot(uri=QUDT.cName, name="cName", curie=QUDT.curie('cName'),
                   model_uri=QUDT.cName, domain=None, range=Optional[Union[str, list[str]]])

slots.cardinality = Slot(uri=QUDT.cardinality, name="cardinality", curie=QUDT.curie('cardinality'),
                   model_uri=QUDT.cardinality, domain=None, range=Optional[Union[str, list[str]]])

slots.categorizedAs = Slot(uri=QUDT.categorizedAs, name="categorizedAs", curie=QUDT.curie('categorizedAs'),
                   model_uri=QUDT.categorizedAs, domain=None, range=Optional[Union[str, list[str]]])

slots.coherentUnitSystem = Slot(uri=QUDT.coherentUnitSystem, name="coherentUnitSystem", curie=QUDT.curie('coherentUnitSystem'),
                   model_uri=QUDT.coherentUnitSystem, domain=None, range=Optional[Union[str, list[str]]])

slots.dataEncoding = Slot(uri=QUDT.dataEncoding, name="dataEncoding", curie=QUDT.curie('dataEncoding'),
                   model_uri=QUDT.dataEncoding, domain=None, range=Optional[Union[Union[dict, DataEncoding], list[Union[dict, DataEncoding]]]])

slots.datatype = Slot(uri=QUDT.datatype, name="datatype", curie=QUDT.curie('datatype'),
                   model_uri=QUDT.datatype, domain=None, range=Optional[Union[str, list[str]]])

slots.default = Slot(uri=QUDT.default, name="default", curie=QUDT.curie('default'),
                   model_uri=QUDT.default, domain=None, range=Optional[Union[str, list[str]]])

slots.definedUnitOfSystem = Slot(uri=QUDT.definedUnitOfSystem, name="definedUnitOfSystem", curie=QUDT.curie('definedUnitOfSystem'),
                   model_uri=QUDT.definedUnitOfSystem, domain=None, range=Optional[Union[Union[dict, SystemOfUnits], list[Union[dict, SystemOfUnits]]]])

slots.denominatorDimensionVector = Slot(uri=QUDT.denominatorDimensionVector, name="denominatorDimensionVector", curie=QUDT.curie('denominatorDimensionVector'),
                   model_uri=QUDT.denominatorDimensionVector, domain=None, range=Optional[Union[Union[dict, QuantityKindDimensionVector], list[Union[dict, QuantityKindDimensionVector]]]])

slots.derivedCoherentUnitOfSystem = Slot(uri=QUDT.derivedCoherentUnitOfSystem, name="derivedCoherentUnitOfSystem", curie=QUDT.curie('derivedCoherentUnitOfSystem'),
                   model_uri=QUDT.derivedCoherentUnitOfSystem, domain=None, range=Optional[Union[Union[dict, SystemOfUnits], list[Union[dict, SystemOfUnits]]]])

slots.derivedNonCoherentUnitOfSystem = Slot(uri=QUDT.derivedNonCoherentUnitOfSystem, name="derivedNonCoherentUnitOfSystem", curie=QUDT.curie('derivedNonCoherentUnitOfSystem'),
                   model_uri=QUDT.derivedNonCoherentUnitOfSystem, domain=None, range=Optional[Union[Union[dict, SystemOfUnits], list[Union[dict, SystemOfUnits]]]])

slots.derivedUnitOfSystem = Slot(uri=QUDT.derivedUnitOfSystem, name="derivedUnitOfSystem", curie=QUDT.curie('derivedUnitOfSystem'),
                   model_uri=QUDT.derivedUnitOfSystem, domain=None, range=Optional[Union[Union[dict, SystemOfUnits], list[Union[dict, SystemOfUnits]]]])

slots.dimensionInverse = Slot(uri=QUDT.dimensionInverse, name="dimensionInverse", curie=QUDT.curie('dimensionInverse'),
                   model_uri=QUDT.dimensionInverse, domain=None, range=Optional[Union[str, list[str]]])

slots.dimensionVectorForSI = Slot(uri=QUDT.dimensionVectorForSI, name="dimensionVectorForSI", curie=QUDT.curie('dimensionVectorForSI'),
                   model_uri=QUDT.dimensionVectorForSI, domain=None, range=Optional[Union[Union[dict, QuantityKindDimensionVectorSI], list[Union[dict, QuantityKindDimensionVectorSI]]]])

slots.element = Slot(uri=QUDT.element, name="element", curie=QUDT.curie('element'),
                   model_uri=QUDT.element, domain=None, range=Optional[Union[str, list[str]]])

slots.elementKind = Slot(uri=QUDT.elementKind, name="elementKind", curie=QUDT.curie('elementKind'),
                   model_uri=QUDT.elementKind, domain=None, range=Optional[Union[str, list[str]]])

slots.encoding = Slot(uri=QUDT.encoding, name="encoding", curie=QUDT.curie('encoding'),
                   model_uri=QUDT.encoding, domain=None, range=Optional[Union[str, list[str]]])

slots.enumeratedValue = Slot(uri=QUDT.enumeratedValue, name="enumeratedValue", curie=QUDT.curie('enumeratedValue'),
                   model_uri=QUDT.enumeratedValue, domain=None, range=Optional[Union[Union[dict, EnumeratedValue], list[Union[dict, EnumeratedValue]]]])

slots.enumeration = Slot(uri=QUDT.enumeration, name="enumeration", curie=QUDT.curie('enumeration'),
                   model_uri=QUDT.enumeration, domain=None, range=Optional[Union[Union[dict, Enumeration], list[Union[dict, Enumeration]]]])

slots.exactMatch = Slot(uri=QUDT.exactMatch, name="exactMatch", curie=QUDT.curie('exactMatch'),
                   model_uri=QUDT.exactMatch, domain=None, range=Optional[Union[str, list[str]]])

slots.exponent = Slot(uri=QUDT.exponent, name="exponent", curie=QUDT.curie('exponent'),
                   model_uri=QUDT.exponent, domain=None, range=Optional[Union[str, list[str]]])

slots.figure = Slot(uri=QUDT.figure, name="figure", curie=QUDT.curie('figure'),
                   model_uri=QUDT.figure, domain=None, range=Optional[Union[Union[dict, Figure], list[Union[dict, Figure]]]])

slots.hasAllowedUnit = Slot(uri=QUDT.hasAllowedUnit, name="hasAllowedUnit", curie=QUDT.curie('hasAllowedUnit'),
                   model_uri=QUDT.hasAllowedUnit, domain=None, range=Optional[Union[Union[dict, Unit], list[Union[dict, Unit]]]])

slots.hasBaseQuantityKind = Slot(uri=QUDT.hasBaseQuantityKind, name="hasBaseQuantityKind", curie=QUDT.curie('hasBaseQuantityKind'),
                   model_uri=QUDT.hasBaseQuantityKind, domain=None, range=Optional[Union[Union[dict, QuantityKind], list[Union[dict, QuantityKind]]]])

slots.hasBaseUnit = Slot(uri=QUDT.hasBaseUnit, name="hasBaseUnit", curie=QUDT.curie('hasBaseUnit'),
                   model_uri=QUDT.hasBaseUnit, domain=None, range=Optional[Union[Union[dict, Unit], list[Union[dict, Unit]]]])

slots.hasCoherentUnit = Slot(uri=QUDT.hasCoherentUnit, name="hasCoherentUnit", curie=QUDT.curie('hasCoherentUnit'),
                   model_uri=QUDT.hasCoherentUnit, domain=None, range=Optional[Union[Union[dict, Unit], list[Union[dict, Unit]]]])

slots.hasDefinedUnit = Slot(uri=QUDT.hasDefinedUnit, name="hasDefinedUnit", curie=QUDT.curie('hasDefinedUnit'),
                   model_uri=QUDT.hasDefinedUnit, domain=None, range=Optional[Union[Union[dict, Unit], list[Union[dict, Unit]]]])

slots.hasDenominatorPart = Slot(uri=QUDT.hasDenominatorPart, name="hasDenominatorPart", curie=QUDT.curie('hasDenominatorPart'),
                   model_uri=QUDT.hasDenominatorPart, domain=None, range=Optional[Union[str, list[str]]])

slots.hasDerivedCoherentUnit = Slot(uri=QUDT.hasDerivedCoherentUnit, name="hasDerivedCoherentUnit", curie=QUDT.curie('hasDerivedCoherentUnit'),
                   model_uri=QUDT.hasDerivedCoherentUnit, domain=None, range=Optional[Union[Union[dict, Unit], list[Union[dict, Unit]]]])

slots.hasDerivedNonCoherentUnit = Slot(uri=QUDT.hasDerivedNonCoherentUnit, name="hasDerivedNonCoherentUnit", curie=QUDT.curie('hasDerivedNonCoherentUnit'),
                   model_uri=QUDT.hasDerivedNonCoherentUnit, domain=None, range=Optional[Union[str, list[str]]])

slots.hasDerivedUnit = Slot(uri=QUDT.hasDerivedUnit, name="hasDerivedUnit", curie=QUDT.curie('hasDerivedUnit'),
                   model_uri=QUDT.hasDerivedUnit, domain=None, range=Optional[Union[str, list[str]]])

slots.hasDimension = Slot(uri=QUDT.hasDimension, name="hasDimension", curie=QUDT.curie('hasDimension'),
                   model_uri=QUDT.hasDimension, domain=None, range=Optional[Union[str, list[str]]])

slots.hasDimensionExpression = Slot(uri=QUDT.hasDimensionExpression, name="hasDimensionExpression", curie=QUDT.curie('hasDimensionExpression'),
                   model_uri=QUDT.hasDimensionExpression, domain=None, range=Optional[Union[str, list[str]]])

slots.hasDimensionVector = Slot(uri=QUDT.hasDimensionVector, name="hasDimensionVector", curie=QUDT.curie('hasDimensionVector'),
                   model_uri=QUDT.hasDimensionVector, domain=None, range=Optional[Union[Union[dict, QuantityKindDimensionVector], list[Union[dict, QuantityKindDimensionVector]]]])

slots.hasFactorUnit = Slot(uri=QUDT.hasFactorUnit, name="hasFactorUnit", curie=QUDT.curie('hasFactorUnit'),
                   model_uri=QUDT.hasFactorUnit, domain=None, range=Optional[Union[str, list[str]]])

slots.hasNumeratorPart = Slot(uri=QUDT.hasNumeratorPart, name="hasNumeratorPart", curie=QUDT.curie('hasNumeratorPart'),
                   model_uri=QUDT.hasNumeratorPart, domain=None, range=Optional[Union[str, list[str]]])

slots.hasPrefixUnit = Slot(uri=QUDT.hasPrefixUnit, name="hasPrefixUnit", curie=QUDT.curie('hasPrefixUnit'),
                   model_uri=QUDT.hasPrefixUnit, domain=None, range=Optional[Union[Union[dict, Unit], list[Union[dict, Unit]]]])

slots.hasQuantity = Slot(uri=QUDT.hasQuantity, name="hasQuantity", curie=QUDT.curie('hasQuantity'),
                   model_uri=QUDT.hasQuantity, domain=None, range=Optional[Union[Union[dict, Quantity], list[Union[dict, Quantity]]]])

slots.hasQuantityKind = Slot(uri=QUDT.hasQuantityKind, name="hasQuantityKind", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=QUDT.hasQuantityKind, domain=None, range=Optional[Union[Union[dict, QuantityKind], list[Union[dict, QuantityKind]]]])

slots.hasReciprocalUnit = Slot(uri=QUDT.hasReciprocalUnit, name="hasReciprocalUnit", curie=QUDT.curie('hasReciprocalUnit'),
                   model_uri=QUDT.hasReciprocalUnit, domain=None, range=Optional[Union[Union[dict, Unit], list[Union[dict, Unit]]]])

slots.hasReferenceQuantityKind = Slot(uri=QUDT.hasReferenceQuantityKind, name="hasReferenceQuantityKind", curie=QUDT.curie('hasReferenceQuantityKind'),
                   model_uri=QUDT.hasReferenceQuantityKind, domain=None, range=Optional[Union[str, list[str]]])

slots.hasRule = Slot(uri=QUDT.hasRule, name="hasRule", curie=QUDT.curie('hasRule'),
                   model_uri=QUDT.hasRule, domain=None, range=Optional[Union[str, list[str]]])

slots.hasUnit = Slot(uri=QUDT.hasUnit, name="hasUnit", curie=QUDT.curie('hasUnit'),
                   model_uri=QUDT.hasUnit, domain=None, range=Optional[Union[Union[dict, Unit], list[Union[dict, Unit]]]])

slots.hasUnitSystem = Slot(uri=QUDT.hasUnitSystem, name="hasUnitSystem", curie=QUDT.curie('hasUnitSystem'),
                   model_uri=QUDT.hasUnitSystem, domain=None, range=Optional[Union[str, list[str]]])

slots.hasVocabulary = Slot(uri=QUDT.hasVocabulary, name="hasVocabulary", curie=QUDT.curie('hasVocabulary'),
                   model_uri=QUDT.hasVocabulary, domain=None, range=Optional[Union[Union[dict, Ontology], list[Union[dict, Ontology]]]])

slots.isDimensionInSystem = Slot(uri=QUDT.isDimensionInSystem, name="isDimensionInSystem", curie=QUDT.curie('isDimensionInSystem'),
                   model_uri=QUDT.isDimensionInSystem, domain=None, range=Optional[Union[str, list[str]]])

slots.isUnitOfSystem = Slot(uri=QUDT.isUnitOfSystem, name="isUnitOfSystem", curie=QUDT.curie('isUnitOfSystem'),
                   model_uri=QUDT.isUnitOfSystem, domain=None, range=Optional[Union[Union[dict, SystemOfUnits], list[Union[dict, SystemOfUnits]]]])

slots.numeratorDimensionVector = Slot(uri=QUDT.numeratorDimensionVector, name="numeratorDimensionVector", curie=QUDT.curie('numeratorDimensionVector'),
                   model_uri=QUDT.numeratorDimensionVector, domain=None, range=Optional[Union[Union[dict, QuantityKindDimensionVector], list[Union[dict, QuantityKindDimensionVector]]]])

slots.omUnit = Slot(uri=QUDT.omUnit, name="omUnit", curie=QUDT.curie('omUnit'),
                   model_uri=QUDT.omUnit, domain=None, range=Optional[Union[str, list[str]]])

slots.oracleSQLName = Slot(uri=QUDT.oracleSQLName, name="oracleSQLName", curie=QUDT.curie('oracleSQLName'),
                   model_uri=QUDT.oracleSQLName, domain=None, range=Optional[Union[str, list[str]]])

slots.orderedType = Slot(uri=QUDT.orderedType, name="orderedType", curie=QUDT.curie('orderedType'),
                   model_uri=QUDT.orderedType, domain=None, range=Optional[Union[str, list[str]]])

slots.permissibleMaths = Slot(uri=QUDT.permissibleMaths, name="permissibleMaths", curie=QUDT.curie('permissibleMaths'),
                   model_uri=QUDT.permissibleMaths, domain=None, range=Optional[Union[str, list[str]]])

slots.permissibleTransformation = Slot(uri=QUDT.permissibleTransformation, name="permissibleTransformation", curie=QUDT.curie('permissibleTransformation'),
                   model_uri=QUDT.permissibleTransformation, domain=None, range=Optional[Union[str, list[str]]])

slots.prefix = Slot(uri=QUDT.prefix, name="prefix", curie=QUDT.curie('prefix'),
                   model_uri=QUDT.prefix, domain=None, range=Optional[Union[Union[dict, Prefix], list[Union[dict, Prefix]]]])

slots.protocolBuffersName = Slot(uri=QUDT.protocolBuffersName, name="protocolBuffersName", curie=QUDT.curie('protocolBuffersName'),
                   model_uri=QUDT.protocolBuffersName, domain=None, range=Optional[Union[str, list[str]]])

slots.pythonName = Slot(uri=QUDT.pythonName, name="pythonName", curie=QUDT.curie('pythonName'),
                   model_uri=QUDT.pythonName, domain=None, range=Optional[Union[str, list[str]]])

slots.qkdvDenominator = Slot(uri=QUDT.qkdvDenominator, name="qkdvDenominator", curie=QUDT.curie('qkdvDenominator'),
                   model_uri=QUDT.qkdvDenominator, domain=None, range=Optional[Union[Union[dict, QuantityKindDimensionVector], list[Union[dict, QuantityKindDimensionVector]]]])

slots.qkdvNumerator = Slot(uri=QUDT.qkdvNumerator, name="qkdvNumerator", curie=QUDT.curie('qkdvNumerator'),
                   model_uri=QUDT.qkdvNumerator, domain=None, range=Optional[Union[Union[dict, QuantityKindDimensionVector], list[Union[dict, QuantityKindDimensionVector]]]])

slots.quantity = Slot(uri=QUDT.quantity, name="quantity", curie=QUDT.curie('quantity'),
                   model_uri=QUDT.quantity, domain=None, range=Optional[Union[str, list[str]]])

slots.quantityValue = Slot(uri=QUDT.quantityValue, name="quantityValue", curie=QUDT.curie('quantityValue'),
                   model_uri=QUDT.quantityValue, domain=None, range=Optional[Union[Union[dict, QuantityValue], list[Union[dict, QuantityValue]]]])

slots.reference = Slot(uri=QUDT.reference, name="reference", curie=QUDT.curie('reference'),
                   model_uri=QUDT.reference, domain=None, range=Optional[Union[str, list[str]]])

slots.referenceUnit = Slot(uri=QUDT.referenceUnit, name="referenceUnit", curie=QUDT.curie('referenceUnit'),
                   model_uri=QUDT.referenceUnit, domain=None, range=Optional[Union[str, list[str]]])

slots.relevantQuantityKind = Slot(uri=QUDT.relevantQuantityKind, name="relevantQuantityKind", curie=QUDT.curie('relevantQuantityKind'),
                   model_uri=QUDT.relevantQuantityKind, domain=None, range=Optional[Union[Union[dict, QuantityKind], list[Union[dict, QuantityKind]]]])

slots.relevantUnit = Slot(uri=QUDT.relevantUnit, name="relevantUnit", curie=QUDT.curie('relevantUnit'),
                   model_uri=QUDT.relevantUnit, domain=None, range=Optional[Union[Union[dict, Unit], list[Union[dict, Unit]]]])

slots.ruleType = Slot(uri=QUDT.ruleType, name="ruleType", curie=QUDT.curie('ruleType'),
                   model_uri=QUDT.ruleType, domain=None, range=Optional[Union[str, list[str]]])

slots.scaleType = Slot(uri=QUDT.scaleType, name="scaleType", curie=QUDT.curie('scaleType'),
                   model_uri=QUDT.scaleType, domain=None, range=Optional[Union[str, list[str]]])

slots.scalingOf = Slot(uri=QUDT.scalingOf, name="scalingOf", curie=QUDT.curie('scalingOf'),
                   model_uri=QUDT.scalingOf, domain=None, range=Optional[Union[str, list[str]]])

slots.siExactMatch = Slot(uri=QUDT.siExactMatch, name="siExactMatch", curie=QUDT.curie('siExactMatch'),
                   model_uri=QUDT.siExactMatch, domain=None, range=Optional[Union[str, list[str]]])

slots.systemDefinition = Slot(uri=QUDT.systemDefinition, name="systemDefinition", curie=QUDT.curie('systemDefinition'),
                   model_uri=QUDT.systemDefinition, domain=None, range=Optional[Union[str, list[str]]])

slots.systemDerivedQuantityKind = Slot(uri=QUDT.systemDerivedQuantityKind, name="systemDerivedQuantityKind", curie=QUDT.curie('systemDerivedQuantityKind'),
                   model_uri=QUDT.systemDerivedQuantityKind, domain=None, range=Optional[Union[Union[dict, QuantityKind], list[Union[dict, QuantityKind]]]])

slots.systemDimension = Slot(uri=QUDT.systemDimension, name="systemDimension", curie=QUDT.curie('systemDimension'),
                   model_uri=QUDT.systemDimension, domain=None, range=Optional[Union[str, list[str]]])

slots.unitFor = Slot(uri=QUDT.unitFor, name="unitFor", curie=QUDT.curie('unitFor'),
                   model_uri=QUDT.unitFor, domain=None, range=Optional[Union[str, list[str]]])

slots.valueQuantity = Slot(uri=QUDT.valueQuantity, name="valueQuantity", curie=QUDT.curie('valueQuantity'),
                   model_uri=QUDT.valueQuantity, domain=None, range=Optional[Union[str, list[str]]])

slots.vbName = Slot(uri=QUDT.vbName, name="vbName", curie=QUDT.curie('vbName'),
                   model_uri=QUDT.vbName, domain=None, range=Optional[Union[str, list[str]]])

slots.supersededBy = Slot(uri=VOAG.supersededBy, name="supersededBy", curie=VOAG.curie('supersededBy'),
                   model_uri=QUDT.supersededBy, domain=None, range=Optional[Union[str, list[str]]])

slots.wasDerivedFrom = Slot(uri=PROV.wasDerivedFrom, name="wasDerivedFrom", curie=PROV.curie('wasDerivedFrom'),
                   model_uri=QUDT.wasDerivedFrom, domain=None, range=Optional[Union[Union[dict, Concept], list[Union[dict, Concept]]]])

slots.description = Slot(uri=DC.description, name="description", curie=DC.curie('description'),
                   model_uri=QUDT.description, domain=None, range=Optional[Union[str, list[str]]])

slots.abbreviation = Slot(uri=QUDT.abbreviation, name="abbreviation", curie=QUDT.curie('abbreviation'),
                   model_uri=QUDT.abbreviation, domain=None, range=Optional[Union[str, list[str]]])

slots.acronym = Slot(uri=QUDT.acronym, name="acronym", curie=QUDT.curie('acronym'),
                   model_uri=QUDT.acronym, domain=None, range=Optional[Union[str, list[str]]])

slots.allowedPattern = Slot(uri=QUDT.allowedPattern, name="allowedPattern", curie=QUDT.curie('allowedPattern'),
                   model_uri=QUDT.allowedPattern, domain=None, range=Optional[Union[str, list[str]]])

slots.altSymbol = Slot(uri=QUDT.altSymbol, name="altSymbol", curie=QUDT.curie('altSymbol'),
                   model_uri=QUDT.altSymbol, domain=None, range=Optional[Union[str, list[str]]])

slots.bits = Slot(uri=QUDT.bits, name="bits", curie=QUDT.curie('bits'),
                   model_uri=QUDT.bits, domain=None, range=Optional[Union[str, list[str]]])

slots.bounded = Slot(uri=QUDT.bounded, name="bounded", curie=QUDT.curie('bounded'),
                   model_uri=QUDT.bounded, domain=None, range=Optional[Union[str, list[str]]])

slots.bytes = Slot(uri=QUDT.bytes, name="bytes", curie=QUDT.curie('bytes'),
                   model_uri=QUDT.bytes, domain=None, range=Optional[Union[str, list[str]]])

slots.conversionMultiplier = Slot(uri=QUDT.conversionMultiplier, name="conversionMultiplier", curie=QUDT.curie('conversionMultiplier'),
                   model_uri=QUDT.conversionMultiplier, domain=None, range=Optional[Union[str, list[str]]])

slots.conversionMultiplierSN = Slot(uri=QUDT.conversionMultiplierSN, name="conversionMultiplierSN", curie=QUDT.curie('conversionMultiplierSN'),
                   model_uri=QUDT.conversionMultiplierSN, domain=None, range=Optional[Union[str, list[str]]])

slots.conversionOffset = Slot(uri=QUDT.conversionOffset, name="conversionOffset", curie=QUDT.curie('conversionOffset'),
                   model_uri=QUDT.conversionOffset, domain=None, range=Optional[Union[str, list[str]]])

slots.conversionOffsetSN = Slot(uri=QUDT.conversionOffsetSN, name="conversionOffsetSN", curie=QUDT.curie('conversionOffsetSN'),
                   model_uri=QUDT.conversionOffsetSN, domain=None, range=Optional[Union[str, list[str]]])

slots.currencyCode = Slot(uri=QUDT.currencyCode, name="currencyCode", curie=QUDT.curie('currencyCode'),
                   model_uri=QUDT.currencyCode, domain=None, range=Optional[Union[str, list[str]]])

slots.currencyExponent = Slot(uri=QUDT.currencyExponent, name="currencyExponent", curie=QUDT.curie('currencyExponent'),
                   model_uri=QUDT.currencyExponent, domain=None, range=Optional[Union[str, list[str]]])

slots.currencyNumber = Slot(uri=QUDT.currencyNumber, name="currencyNumber", curie=QUDT.curie('currencyNumber'),
                   model_uri=QUDT.currencyNumber, domain=None, range=Optional[Union[str, list[str]]])

slots.dataStructure = Slot(uri=QUDT.dataStructure, name="dataStructure", curie=QUDT.curie('dataStructure'),
                   model_uri=QUDT.dataStructure, domain=None, range=Optional[Union[str, list[str]]])

slots.deprecated = Slot(uri=QUDT.deprecated, name="deprecated", curie=QUDT.curie('deprecated'),
                   model_uri=QUDT.deprecated, domain=None, range=Optional[Union[str, list[str]]])

slots.dimensionExponent = Slot(uri=QUDT.dimensionExponent, name="dimensionExponent", curie=QUDT.curie('dimensionExponent'),
                   model_uri=QUDT.dimensionExponent, domain=None, range=Optional[Union[str, list[str]]])

slots.dimensionExponentForAmountOfSubstance = Slot(uri=QUDT.dimensionExponentForAmountOfSubstance, name="dimensionExponentForAmountOfSubstance", curie=QUDT.curie('dimensionExponentForAmountOfSubstance'),
                   model_uri=QUDT.dimensionExponentForAmountOfSubstance, domain=None, range=Optional[Union[str, list[str]]])

slots.dimensionExponentForElectricCurrent = Slot(uri=QUDT.dimensionExponentForElectricCurrent, name="dimensionExponentForElectricCurrent", curie=QUDT.curie('dimensionExponentForElectricCurrent'),
                   model_uri=QUDT.dimensionExponentForElectricCurrent, domain=None, range=Optional[Union[str, list[str]]])

slots.dimensionExponentForLength = Slot(uri=QUDT.dimensionExponentForLength, name="dimensionExponentForLength", curie=QUDT.curie('dimensionExponentForLength'),
                   model_uri=QUDT.dimensionExponentForLength, domain=None, range=Optional[Union[str, list[str]]])

slots.dimensionExponentForLuminousIntensity = Slot(uri=QUDT.dimensionExponentForLuminousIntensity, name="dimensionExponentForLuminousIntensity", curie=QUDT.curie('dimensionExponentForLuminousIntensity'),
                   model_uri=QUDT.dimensionExponentForLuminousIntensity, domain=None, range=Optional[Union[str, list[str]]])

slots.dimensionExponentForMass = Slot(uri=QUDT.dimensionExponentForMass, name="dimensionExponentForMass", curie=QUDT.curie('dimensionExponentForMass'),
                   model_uri=QUDT.dimensionExponentForMass, domain=None, range=Optional[Union[str, list[str]]])

slots.dimensionExponentForThermodynamicTemperature = Slot(uri=QUDT.dimensionExponentForThermodynamicTemperature, name="dimensionExponentForThermodynamicTemperature", curie=QUDT.curie('dimensionExponentForThermodynamicTemperature'),
                   model_uri=QUDT.dimensionExponentForThermodynamicTemperature, domain=None, range=Optional[Union[str, list[str]]])

slots.dimensionExponentForTime = Slot(uri=QUDT.dimensionExponentForTime, name="dimensionExponentForTime", curie=QUDT.curie('dimensionExponentForTime'),
                   model_uri=QUDT.dimensionExponentForTime, domain=None, range=Optional[Union[str, list[str]]])

slots.dimensionlessExponent = Slot(uri=QUDT.dimensionlessExponent, name="dimensionlessExponent", curie=QUDT.curie('dimensionlessExponent'),
                   model_uri=QUDT.dimensionlessExponent, domain=None, range=Optional[Union[str, list[str]]])

slots.exactConstant = Slot(uri=QUDT.exactConstant, name="exactConstant", curie=QUDT.curie('exactConstant'),
                   model_uri=QUDT.exactConstant, domain=None, range=Optional[Union[str, list[str]]])

slots.factorUnitScalar = Slot(uri=QUDT.factorUnitScalar, name="factorUnitScalar", curie=QUDT.curie('factorUnitScalar'),
                   model_uri=QUDT.factorUnitScalar, domain=None, range=Optional[Union[str, list[str]]])

slots.fieldCode = Slot(uri=QUDT.fieldCode, name="fieldCode", curie=QUDT.curie('fieldCode'),
                   model_uri=QUDT.fieldCode, domain=None, range=Optional[Union[str, list[str]]])

slots.figureCaption = Slot(uri=QUDT.figureCaption, name="figureCaption", curie=QUDT.curie('figureCaption'),
                   model_uri=QUDT.figureCaption, domain=None, range=Optional[Union[str, list[str]]])

slots.figureLabel = Slot(uri=QUDT.figureLabel, name="figureLabel", curie=QUDT.curie('figureLabel'),
                   model_uri=QUDT.figureLabel, domain=None, range=Optional[Union[str, list[str]]])

slots.guidance = Slot(uri=QUDT.guidance, name="guidance", curie=QUDT.curie('guidance'),
                   model_uri=QUDT.guidance, domain=None, range=Optional[Union[str, list[str]]])

slots.hasCitation = Slot(uri=QUDT.hasCitation, name="hasCitation", curie=QUDT.curie('hasCitation'),
                   model_uri=QUDT.hasCitation, domain=None, range=Optional[Union[str, list[str]]])

slots.height = Slot(uri=QUDT.height, name="height", curie=QUDT.curie('height'),
                   model_uri=QUDT.height, domain=None, range=Optional[Union[str, list[str]]])

slots.id = Slot(uri=QUDT.id, name="id", curie=QUDT.curie('id'),
                   model_uri=QUDT.id, domain=None, range=Optional[Union[str, list[str]]])

slots.iec61360Code = Slot(uri=QUDT.iec61360Code, name="iec61360Code", curie=QUDT.curie('iec61360Code'),
                   model_uri=QUDT.iec61360Code, domain=None, range=Optional[Union[str, list[str]]])

slots.image = Slot(uri=QUDT.image, name="image", curie=QUDT.curie('image'),
                   model_uri=QUDT.image, domain=None, range=Optional[Union[str, list[str]]])

slots.imageLocation = Slot(uri=QUDT.imageLocation, name="imageLocation", curie=QUDT.curie('imageLocation'),
                   model_uri=QUDT.imageLocation, domain=None, range=Optional[Union[str, list[str]]])

slots.isDeltaQuantity = Slot(uri=QUDT.isDeltaQuantity, name="isDeltaQuantity", curie=QUDT.curie('isDeltaQuantity'),
                   model_uri=QUDT.isDeltaQuantity, domain=None, range=Optional[Union[str, list[str]]])

slots.isMetricUnit = Slot(uri=QUDT.isMetricUnit, name="isMetricUnit", curie=QUDT.curie('isMetricUnit'),
                   model_uri=QUDT.isMetricUnit, domain=None, range=Optional[Union[str, list[str]]])

slots.isoNormativeReference = Slot(uri=QUDT.isoNormativeReference, name="isoNormativeReference", curie=QUDT.curie('isoNormativeReference'),
                   model_uri=QUDT.isoNormativeReference, domain=None, range=Optional[Union[str, list[str]]])

slots.javaName = Slot(uri=QUDT.javaName, name="javaName", curie=QUDT.curie('javaName'),
                   model_uri=QUDT.javaName, domain=None, range=Optional[Union[str, list[str]]])

slots.jsName = Slot(uri=QUDT.jsName, name="jsName", curie=QUDT.curie('jsName'),
                   model_uri=QUDT.jsName, domain=None, range=Optional[Union[str, list[str]]])

slots.landscape = Slot(uri=QUDT.landscape, name="landscape", curie=QUDT.curie('landscape'),
                   model_uri=QUDT.landscape, domain=None, range=Optional[Union[str, list[str]]])

slots.latexDefinition = Slot(uri=QUDT.latexDefinition, name="latexDefinition", curie=QUDT.curie('latexDefinition'),
                   model_uri=QUDT.latexDefinition, domain=None, range=Optional[Union[str, list[str]]])

slots.latexSymbol = Slot(uri=QUDT.latexSymbol, name="latexSymbol", curie=QUDT.curie('latexSymbol'),
                   model_uri=QUDT.latexSymbol, domain=None, range=Optional[Union[str, list[str]]])

slots.length = Slot(uri=QUDT.length, name="length", curie=QUDT.curie('length'),
                   model_uri=QUDT.length, domain=None, range=Optional[Union[str, list[str]]])

slots.lowerBound = Slot(uri=QUDT.lowerBound, name="lowerBound", curie=QUDT.curie('lowerBound'),
                   model_uri=QUDT.lowerBound, domain=None, range=Optional[Union[str, list[str]]])

slots.mathDefinition = Slot(uri=QUDT.mathDefinition, name="mathDefinition", curie=QUDT.curie('mathDefinition'),
                   model_uri=QUDT.mathDefinition, domain=None, range=Optional[Union[str, list[str]]])

slots.mathMLdefinition = Slot(uri=QUDT.mathMLdefinition, name="mathMLdefinition", curie=QUDT.curie('mathMLdefinition'),
                   model_uri=QUDT.mathMLdefinition, domain=None, range=Optional[Union[str, list[str]]])

slots.matlabName = Slot(uri=QUDT.matlabName, name="matlabName", curie=QUDT.curie('matlabName'),
                   model_uri=QUDT.matlabName, domain=None, range=Optional[Union[str, list[str]]])

slots.maxExclusive = Slot(uri=QUDT.maxExclusive, name="maxExclusive", curie=QUDT.curie('maxExclusive'),
                   model_uri=QUDT.maxExclusive, domain=None, range=Optional[Union[str, list[str]]])

slots.maxInclusive = Slot(uri=QUDT.maxInclusive, name="maxInclusive", curie=QUDT.curie('maxInclusive'),
                   model_uri=QUDT.maxInclusive, domain=None, range=Optional[Union[str, list[str]]])

slots.microsoftSQLServerName = Slot(uri=QUDT.microsoftSQLServerName, name="microsoftSQLServerName", curie=QUDT.curie('microsoftSQLServerName'),
                   model_uri=QUDT.microsoftSQLServerName, domain=None, range=Optional[Union[str, list[str]]])

slots.minExclusive = Slot(uri=QUDT.minExclusive, name="minExclusive", curie=QUDT.curie('minExclusive'),
                   model_uri=QUDT.minExclusive, domain=None, range=Optional[Union[str, list[str]]])

slots.minInclusive = Slot(uri=QUDT.minInclusive, name="minInclusive", curie=QUDT.curie('minInclusive'),
                   model_uri=QUDT.minInclusive, domain=None, range=Optional[Union[str, list[str]]])

slots.mySQLName = Slot(uri=QUDT.mySQLName, name="mySQLName", curie=QUDT.curie('mySQLName'),
                   model_uri=QUDT.mySQLName, domain=None, range=Optional[Union[str, list[str]]])

slots.negativeDeltaLimit = Slot(uri=QUDT.negativeDeltaLimit, name="negativeDeltaLimit", curie=QUDT.curie('negativeDeltaLimit'),
                   model_uri=QUDT.negativeDeltaLimit, domain=None, range=Optional[Union[str, list[str]]])

slots.normativeReference = Slot(uri=QUDT.normativeReference, name="normativeReference", curie=QUDT.curie('normativeReference'),
                   model_uri=QUDT.normativeReference, domain=None, range=Optional[Union[str, list[str]]])

slots.numericValue = Slot(uri=QUDT.numericValue, name="numericValue", curie=QUDT.curie('numericValue'),
                   model_uri=QUDT.numericValue, domain=None, range=Optional[Union[Union[dict, NumericUnion], list[Union[dict, NumericUnion]]]])

slots.odbcName = Slot(uri=QUDT.odbcName, name="odbcName", curie=QUDT.curie('odbcName'),
                   model_uri=QUDT.odbcName, domain=None, range=Optional[Union[str, list[str]]])

slots.oleDBName = Slot(uri=QUDT.oleDBName, name="oleDBName", curie=QUDT.curie('oleDBName'),
                   model_uri=QUDT.oleDBName, domain=None, range=Optional[Union[str, list[str]]])

slots.onlineReference = Slot(uri=QUDT.onlineReference, name="onlineReference", curie=QUDT.curie('onlineReference'),
                   model_uri=QUDT.onlineReference, domain=None, range=Optional[Union[str, list[str]]])

slots.order = Slot(uri=QUDT.order, name="order", curie=QUDT.curie('order'),
                   model_uri=QUDT.order, domain=None, range=Optional[Union[str, list[str]]])

slots.outOfScope = Slot(uri=QUDT.outOfScope, name="outOfScope", curie=QUDT.curie('outOfScope'),
                   model_uri=QUDT.outOfScope, domain=None, range=Optional[Union[str, list[str]]])

slots.plainTextDescription = Slot(uri=QUDT.plainTextDescription, name="plainTextDescription", curie=QUDT.curie('plainTextDescription'),
                   model_uri=QUDT.plainTextDescription, domain=None, range=Optional[Union[str, list[str]]])

slots.positiveDeltaLimit = Slot(uri=QUDT.positiveDeltaLimit, name="positiveDeltaLimit", curie=QUDT.curie('positiveDeltaLimit'),
                   model_uri=QUDT.positiveDeltaLimit, domain=None, range=Optional[Union[str, list[str]]])

slots.prefixMultiplier = Slot(uri=QUDT.prefixMultiplier, name="prefixMultiplier", curie=QUDT.curie('prefixMultiplier'),
                   model_uri=QUDT.prefixMultiplier, domain=None, range=Optional[Union[str, list[str]]])

slots.prefixMultiplierSN = Slot(uri=QUDT.prefixMultiplierSN, name="prefixMultiplierSN", curie=QUDT.curie('prefixMultiplierSN'),
                   model_uri=QUDT.prefixMultiplierSN, domain=None, range=Optional[Union[str, list[str]]])

slots.rationale = Slot(uri=QUDT.rationale, name="rationale", curie=QUDT.curie('rationale'),
                   model_uri=QUDT.rationale, domain=None, range=Optional[Union[str, list[str]]])

slots.rdfsDatatype = Slot(uri=QUDT.rdfsDatatype, name="rdfsDatatype", curie=QUDT.curie('rdfsDatatype'),
                   model_uri=QUDT.rdfsDatatype, domain=None, range=Optional[Union[str, list[str]]])

slots.relativeStandardUncertainty = Slot(uri=QUDT.relativeStandardUncertainty, name="relativeStandardUncertainty", curie=QUDT.curie('relativeStandardUncertainty'),
                   model_uri=QUDT.relativeStandardUncertainty, domain=None, range=Optional[Union[str, list[str]]])

slots.siUnitsExpression = Slot(uri=QUDT.siUnitsExpression, name="siUnitsExpression", curie=QUDT.curie('siUnitsExpression'),
                   model_uri=QUDT.siUnitsExpression, domain=None, range=Optional[Union[str, list[str]]])

slots.standardUncertainty = Slot(uri=QUDT.standardUncertainty, name="standardUncertainty", curie=QUDT.curie('standardUncertainty'),
                   model_uri=QUDT.standardUncertainty, domain=None, range=Optional[Union[str, list[str]]])

slots.standardUncertaintySN = Slot(uri=QUDT.standardUncertaintySN, name="standardUncertaintySN", curie=QUDT.curie('standardUncertaintySN'),
                   model_uri=QUDT.standardUncertaintySN, domain=None, range=Optional[Union[str, list[str]]])

slots.symbol = Slot(uri=QUDT.symbol, name="symbol", curie=QUDT.curie('symbol'),
                   model_uri=QUDT.symbol, domain=None, range=Optional[Union[str, list[str]]])

slots.ucumCode = Slot(uri=QUDT.ucumCode, name="ucumCode", curie=QUDT.curie('ucumCode'),
                   model_uri=QUDT.ucumCode, domain=None, range=Optional[Union[str, list[str]]])

slots.udunitsCode = Slot(uri=QUDT.udunitsCode, name="udunitsCode", curie=QUDT.curie('udunitsCode'),
                   model_uri=QUDT.udunitsCode, domain=None, range=Optional[Union[str, list[str]]])

slots.uneceCommonCode = Slot(uri=QUDT.uneceCommonCode, name="uneceCommonCode", curie=QUDT.curie('uneceCommonCode'),
                   model_uri=QUDT.uneceCommonCode, domain=None, range=Optional[Union[str, list[str]]])

slots.upperBound = Slot(uri=QUDT.upperBound, name="upperBound", curie=QUDT.curie('upperBound'),
                   model_uri=QUDT.upperBound, domain=None, range=Optional[Union[str, list[str]]])

slots.url = Slot(uri=QUDT.url, name="url", curie=QUDT.curie('url'),
                   model_uri=QUDT.url, domain=None, range=Optional[Union[str, list[str]]])

slots.value = Slot(uri=QUDT.value, name="value", curie=QUDT.curie('value'),
                   model_uri=QUDT.value, domain=None, range=Optional[Union[str, list[str]]])

slots.valueSN = Slot(uri=QUDT.valueSN, name="valueSN", curie=QUDT.curie('valueSN'),
                   model_uri=QUDT.valueSN, domain=None, range=Optional[Union[str, list[str]]])

slots.vectorMagnitude = Slot(uri=QUDT.vectorMagnitude, name="vectorMagnitude", curie=QUDT.curie('vectorMagnitude'),
                   model_uri=QUDT.vectorMagnitude, domain=None, range=Optional[Union[str, list[str]]])

slots.width = Slot(uri=QUDT.width, name="width", curie=QUDT.curie('width'),
                   model_uri=QUDT.width, domain=None, range=Optional[Union[str, list[str]]])

slots.literal = Slot(uri=DTYPE.literal, name="literal", curie=DTYPE.curie('literal'),
                   model_uri=QUDT.literal, domain=None, range=Optional[Union[str, list[str]]])

slots.abstract = Slot(uri=DCTERMS.abstract, name="abstract", curie=DCTERMS.curie('abstract'),
                   model_uri=QUDT.abstract, domain=None, range=Optional[Union[str, list[str]]])

slots.creator = Slot(uri=DCTERMS.creator, name="creator", curie=DCTERMS.curie('creator'),
                   model_uri=QUDT.creator, domain=None, range=Optional[Union[str, list[str]]])

slots.rights = Slot(uri=DCTERMS.rights, name="rights", curie=DCTERMS.curie('rights'),
                   model_uri=QUDT.rights, domain=None, range=Optional[Union[str, list[str]]])

slots.source = Slot(uri=DCTERMS.source, name="source", curie=DCTERMS.curie('source'),
                   model_uri=QUDT.source, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.subject = Slot(uri=DCTERMS.subject, name="subject", curie=DCTERMS.curie('subject'),
                   model_uri=QUDT.subject, domain=None, range=Optional[Union[str, list[str]]])

slots.title = Slot(uri=DCTERMS.title, name="title", curie=DCTERMS.curie('title'),
                   model_uri=QUDT.title, domain=None, range=Optional[Union[str, list[str]]])

slots.dbpediaMatch = Slot(uri=QUDT.dbpediaMatch, name="dbpediaMatch", curie=QUDT.curie('dbpediaMatch'),
                   model_uri=QUDT.dbpediaMatch, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.example = Slot(uri=QUDT.example, name="example", curie=QUDT.curie('example'),
                   model_uri=QUDT.example, domain=None, range=Optional[Union[str, list[str]]])

slots.expression = Slot(uri=QUDT.expression, name="expression", curie=QUDT.curie('expression'),
                   model_uri=QUDT.expression, domain=None, range=Optional[Union[str, list[str]]])

slots.informativeReference = Slot(uri=QUDT.informativeReference, name="informativeReference", curie=QUDT.curie('informativeReference'),
                   model_uri=QUDT.informativeReference, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.wikidataMatch = Slot(uri=QUDT.wikidataMatch, name="wikidataMatch", curie=QUDT.curie('wikidataMatch'),
                   model_uri=QUDT.wikidataMatch, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.graphName = Slot(uri=VAEM.graphName, name="graphName", curie=VAEM.curie('graphName'),
                   model_uri=QUDT.graphName, domain=None, range=Optional[Union[str, list[str]]])

slots.graphTitle = Slot(uri=VAEM.graphTitle, name="graphTitle", curie=VAEM.curie('graphTitle'),
                   model_uri=QUDT.graphTitle, domain=None, range=Optional[Union[str, list[str]]])

slots.isMetadataFor = Slot(uri=VAEM.isMetadataFor, name="isMetadataFor", curie=VAEM.curie('isMetadataFor'),
                   model_uri=QUDT.isMetadataFor, domain=None, range=Optional[Union[str, list[str]]])

slots.website = Slot(uri=VAEM.website, name="website", curie=VAEM.curie('website'),
                   model_uri=QUDT.website, domain=None, range=Optional[Union[str, list[str]]])

slots.pattern = Slot(uri=XSD.pattern, name="pattern", curie=XSD.curie('pattern'),
                   model_uri=QUDT.pattern, domain=None, range=Optional[Union[str, list[str]]])

slots.maxCardinality = Slot(uri=OWL.maxCardinality, name="maxCardinality", curie=OWL.curie('maxCardinality'),
                   model_uri=QUDT.maxCardinality, domain=None, range=Optional[Union[str, list[str]]])

slots.minCardinality = Slot(uri=OWL.minCardinality, name="minCardinality", curie=OWL.curie('minCardinality'),
                   model_uri=QUDT.minCardinality, domain=None, range=Optional[Union[str, list[str]]])

slots.created = Slot(uri=QUDT.created, name="created", curie=QUDT.curie('created'),
                   model_uri=QUDT.created, domain=None, range=Optional[Union[Union[str, XSDDate], list[Union[str, XSDDate]]]])

slots.modified = Slot(uri=QUDT.modified, name="modified", curie=QUDT.curie('modified'),
                   model_uri=QUDT.modified, domain=None, range=Optional[Union[Union[str, XSDDate], list[Union[str, XSDDate]]]])

slots.broader = Slot(uri=QUDT.broader, name="broader", curie=QUDT.curie('broader'),
                   model_uri=QUDT.broader, domain=None, range=Optional[Union[dict, QuantityKind]])

slots.AbstractQuantityKind_broader = Slot(uri=QUDT.broader, name="AbstractQuantityKind_broader", curie=QUDT.curie('broader'),
                   model_uri=QUDT.AbstractQuantityKind_broader, domain=AbstractQuantityKind, range=Optional[Union[dict, "QuantityKind"]])

slots.AbstractQuantityKind_altSymbol = Slot(uri=QUDT.altSymbol, name="AbstractQuantityKind_altSymbol", curie=QUDT.curie('altSymbol'),
                   model_uri=QUDT.AbstractQuantityKind_altSymbol, domain=AbstractQuantityKind, range=Optional[Union[str, list[str]]])

slots.AbstractQuantityKind_latexSymbol = Slot(uri=QUDT.latexSymbol, name="AbstractQuantityKind_latexSymbol", curie=QUDT.curie('latexSymbol'),
                   model_uri=QUDT.AbstractQuantityKind_latexSymbol, domain=AbstractQuantityKind, range=Optional[Union[str, list[str]]])

slots.AbstractQuantityKind_symbol = Slot(uri=QUDT.symbol, name="AbstractQuantityKind_symbol", curie=QUDT.curie('symbol'),
                   model_uri=QUDT.AbstractQuantityKind_symbol, domain=AbstractQuantityKind, range=Optional[Union[str, list[str]]])

slots.BaseDimensionMagnitude_hasBaseQuantityKind = Slot(uri=QUDT.hasBaseQuantityKind, name="BaseDimensionMagnitude_hasBaseQuantityKind", curie=QUDT.curie('hasBaseQuantityKind'),
                   model_uri=QUDT.BaseDimensionMagnitude_hasBaseQuantityKind, domain=BaseDimensionMagnitude, range=Union[Union[dict, "QuantityKind"], list[Union[dict, "QuantityKind"]]])

slots.BaseDimensionMagnitude_vectorMagnitude = Slot(uri=QUDT.vectorMagnitude, name="BaseDimensionMagnitude_vectorMagnitude", curie=QUDT.curie('vectorMagnitude'),
                   model_uri=QUDT.BaseDimensionMagnitude_vectorMagnitude, domain=BaseDimensionMagnitude, range=Union[float, list[float]])

slots.CardinalityType_literal = Slot(uri=DTYPE.literal, name="CardinalityType_literal", curie=DTYPE.curie('literal'),
                   model_uri=QUDT.CardinalityType_literal, domain=CardinalityType, range=Optional[Union[str, list[str]]])

slots.Citation_description = Slot(uri=DC.description, name="Citation_description", curie=DC.curie('description'),
                   model_uri=QUDT.Citation_description, domain=Citation, range=Union[str, list[str]])

slots.Citation_url = Slot(uri=QUDT.url, name="Citation_url", curie=QUDT.curie('url'),
                   model_uri=QUDT.Citation_url, domain=Citation, range=Optional[Union[str, list[str]]])

slots.Comment_rationale = Slot(uri=QUDT.rationale, name="Comment_rationale", curie=QUDT.curie('rationale'),
                   model_uri=QUDT.Comment_rationale, domain=Comment, range=Optional[Union[str, list[str]]])

slots.Comment_description = Slot(uri=DC.description, name="Comment_description", curie=DC.curie('description'),
                   model_uri=QUDT.Comment_description, domain=Comment, range=Optional[Union[str, list[str]]])

slots.Concept_hasRule = Slot(uri=QUDT.hasRule, name="Concept_hasRule", curie=QUDT.curie('hasRule'),
                   model_uri=QUDT.Concept_hasRule, domain=Concept, range=Optional[Union[Union[dict, "Rule"], list[Union[dict, "Rule"]]]])

slots.Concept_isReplacedBy = Slot(uri=DCTERMS.isReplacedBy, name="Concept_isReplacedBy", curie=DCTERMS.curie('isReplacedBy'),
                   model_uri=QUDT.Concept_isReplacedBy, domain=Concept, range=Optional[Union[str, list[str]]])

slots.Concept_description = Slot(uri=DC.description, name="Concept_description", curie=DC.curie('description'),
                   model_uri=QUDT.Concept_description, domain=Concept, range=Optional[Union[str, list[str]]])

slots.Concept_abbreviation = Slot(uri=QUDT.abbreviation, name="Concept_abbreviation", curie=QUDT.curie('abbreviation'),
                   model_uri=QUDT.Concept_abbreviation, domain=Concept, range=Optional[Union[str, list[str]]])

slots.Concept_deprecated = Slot(uri=QUDT.deprecated, name="Concept_deprecated", curie=QUDT.curie('deprecated'),
                   model_uri=QUDT.Concept_deprecated, domain=Concept, range=Optional[Union[str, list[str]]])

slots.Concept_id = Slot(uri=QUDT.id, name="Concept_id", curie=QUDT.curie('id'),
                   model_uri=QUDT.Concept_id, domain=Concept, range=Optional[Union[str, list[str]]])

slots.Concept_plainTextDescription = Slot(uri=QUDT.plainTextDescription, name="Concept_plainTextDescription", curie=QUDT.curie('plainTextDescription'),
                   model_uri=QUDT.Concept_plainTextDescription, domain=Concept, range=Optional[Union[str, list[str]]])

slots.ConstantValue_exactConstant = Slot(uri=QUDT.exactConstant, name="ConstantValue_exactConstant", curie=QUDT.curie('exactConstant'),
                   model_uri=QUDT.ConstantValue_exactConstant, domain=ConstantValue, range=Optional[Union[str, list[str]]])

slots.ContextualUnit_broader = Slot(uri=QUDT.broader, name="ContextualUnit_broader", curie=QUDT.curie('broader'),
                   model_uri=QUDT.ContextualUnit_broader, domain=ContextualUnit, range=Optional[Union[dict, Unit]])

slots.CurrencyUnit_currencyCode = Slot(uri=QUDT.currencyCode, name="CurrencyUnit_currencyCode", curie=QUDT.curie('currencyCode'),
                   model_uri=QUDT.CurrencyUnit_currencyCode, domain=CurrencyUnit, range=Optional[Union[str, list[str]]])

slots.CurrencyUnit_currencyExponent = Slot(uri=QUDT.currencyExponent, name="CurrencyUnit_currencyExponent", curie=QUDT.curie('currencyExponent'),
                   model_uri=QUDT.CurrencyUnit_currencyExponent, domain=CurrencyUnit, range=Optional[Union[str, list[str]]])

slots.DataEncoding_bitOrder = Slot(uri=QUDT.bitOrder, name="DataEncoding_bitOrder", curie=QUDT.curie('bitOrder'),
                   model_uri=QUDT.DataEncoding_bitOrder, domain=DataEncoding, range=Optional[Union[Union[dict, "EndianType"], list[Union[dict, "EndianType"]]]])

slots.DataEncoding_encoding = Slot(uri=QUDT.encoding, name="DataEncoding_encoding", curie=QUDT.curie('encoding'),
                   model_uri=QUDT.DataEncoding_encoding, domain=DataEncoding, range=Optional[Union[Union[dict, "Encoding"], list[Union[dict, "Encoding"]]]])

slots.DataEncoding_byteOrder = Slot(uri=QUDT.byteOrder, name="DataEncoding_byteOrder", curie=QUDT.curie('byteOrder'),
                   model_uri=QUDT.DataEncoding_byteOrder, domain=DataEncoding, range=Optional[Union[Union[dict, "EndianType"], list[Union[dict, "EndianType"]]]])

slots.DataItem_value = Slot(uri=QUDT.value, name="DataItem_value", curie=QUDT.curie('value'),
                   model_uri=QUDT.DataItem_value, domain=DataItem, range=Optional[Union[str, list[str]]])

slots.Datatype_basis = Slot(uri=QUDT.basis, name="Datatype_basis", curie=QUDT.curie('basis'),
                   model_uri=QUDT.Datatype_basis, domain=Datatype, range=Optional[Union[Union[dict, "Datatype"], list[Union[dict, "Datatype"]]]])

slots.Datatype_cardinality = Slot(uri=QUDT.cardinality, name="Datatype_cardinality", curie=QUDT.curie('cardinality'),
                   model_uri=QUDT.Datatype_cardinality, domain=Datatype, range=Optional[Union[Union[dict, "CardinalityType"], list[Union[dict, "CardinalityType"]]]])

slots.Datatype_orderedType = Slot(uri=QUDT.orderedType, name="Datatype_orderedType", curie=QUDT.curie('orderedType'),
                   model_uri=QUDT.Datatype_orderedType, domain=Datatype, range=Optional[Union[Union[dict, "OrderedType"], list[Union[dict, "OrderedType"]]]])

slots.Datatype_ansiSQLName = Slot(uri=QUDT.ansiSQLName, name="Datatype_ansiSQLName", curie=QUDT.curie('ansiSQLName'),
                   model_uri=QUDT.Datatype_ansiSQLName, domain=Datatype, range=Optional[Union[str, list[str]]])

slots.Datatype_cName = Slot(uri=QUDT.cName, name="Datatype_cName", curie=QUDT.curie('cName'),
                   model_uri=QUDT.Datatype_cName, domain=Datatype, range=Optional[Union[str, list[str]]])

slots.Datatype_oracleSQLName = Slot(uri=QUDT.oracleSQLName, name="Datatype_oracleSQLName", curie=QUDT.curie('oracleSQLName'),
                   model_uri=QUDT.Datatype_oracleSQLName, domain=Datatype, range=Optional[Union[str, list[str]]])

slots.Datatype_protocolBuffersName = Slot(uri=QUDT.protocolBuffersName, name="Datatype_protocolBuffersName", curie=QUDT.curie('protocolBuffersName'),
                   model_uri=QUDT.Datatype_protocolBuffersName, domain=Datatype, range=Optional[Union[str, list[str]]])

slots.Datatype_pythonName = Slot(uri=QUDT.pythonName, name="Datatype_pythonName", curie=QUDT.curie('pythonName'),
                   model_uri=QUDT.Datatype_pythonName, domain=Datatype, range=Optional[Union[str, list[str]]])

slots.Datatype_vbName = Slot(uri=QUDT.vbName, name="Datatype_vbName", curie=QUDT.curie('vbName'),
                   model_uri=QUDT.Datatype_vbName, domain=Datatype, range=Optional[Union[str, list[str]]])

slots.Datatype_bounded = Slot(uri=QUDT.bounded, name="Datatype_bounded", curie=QUDT.curie('bounded'),
                   model_uri=QUDT.Datatype_bounded, domain=Datatype, range=Optional[Union[str, list[str]]])

slots.Datatype_id = Slot(uri=QUDT.id, name="Datatype_id", curie=QUDT.curie('id'),
                   model_uri=QUDT.Datatype_id, domain=Datatype, range=Optional[Union[str, list[str]]])

slots.Datatype_javaName = Slot(uri=QUDT.javaName, name="Datatype_javaName", curie=QUDT.curie('javaName'),
                   model_uri=QUDT.Datatype_javaName, domain=Datatype, range=Optional[Union[str, list[str]]])

slots.Datatype_jsName = Slot(uri=QUDT.jsName, name="Datatype_jsName", curie=QUDT.curie('jsName'),
                   model_uri=QUDT.Datatype_jsName, domain=Datatype, range=Optional[Union[str, list[str]]])

slots.Datatype_matlabName = Slot(uri=QUDT.matlabName, name="Datatype_matlabName", curie=QUDT.curie('matlabName'),
                   model_uri=QUDT.Datatype_matlabName, domain=Datatype, range=Optional[Union[str, list[str]]])

slots.Datatype_microsoftSQLServerName = Slot(uri=QUDT.microsoftSQLServerName, name="Datatype_microsoftSQLServerName", curie=QUDT.curie('microsoftSQLServerName'),
                   model_uri=QUDT.Datatype_microsoftSQLServerName, domain=Datatype, range=Optional[Union[str, list[str]]])

slots.Datatype_mySQLName = Slot(uri=QUDT.mySQLName, name="Datatype_mySQLName", curie=QUDT.curie('mySQLName'),
                   model_uri=QUDT.Datatype_mySQLName, domain=Datatype, range=Optional[Union[str, list[str]]])

slots.Datatype_odbcName = Slot(uri=QUDT.odbcName, name="Datatype_odbcName", curie=QUDT.curie('odbcName'),
                   model_uri=QUDT.Datatype_odbcName, domain=Datatype, range=Optional[Union[str, list[str]]])

slots.Datatype_oleDBName = Slot(uri=QUDT.oleDBName, name="Datatype_oleDBName", curie=QUDT.curie('oleDBName'),
                   model_uri=QUDT.Datatype_oleDBName, domain=Datatype, range=Optional[Union[str, list[str]]])

slots.DateTimeStringEncodingType_allowedPattern = Slot(uri=QUDT.allowedPattern, name="DateTimeStringEncodingType_allowedPattern", curie=QUDT.curie('allowedPattern'),
                   model_uri=QUDT.DateTimeStringEncodingType_allowedPattern, domain=DateTimeStringEncodingType, range=Union[str, list[str]])

slots.Encoding_bits = Slot(uri=QUDT.bits, name="Encoding_bits", curie=QUDT.curie('bits'),
                   model_uri=QUDT.Encoding_bits, domain=Encoding, range=Optional[Union[str, list[str]]])

slots.Encoding_bytes = Slot(uri=QUDT.bytes, name="Encoding_bytes", curie=QUDT.curie('bytes'),
                   model_uri=QUDT.Encoding_bytes, domain=Encoding, range=Optional[Union[str, list[str]]])

slots.EnumeratedQuantity_enumeratedValue = Slot(uri=QUDT.enumeratedValue, name="EnumeratedQuantity_enumeratedValue", curie=QUDT.curie('enumeratedValue'),
                   model_uri=QUDT.EnumeratedQuantity_enumeratedValue, domain=EnumeratedQuantity, range=Optional[Union[Union[dict, "EnumeratedValue"], list[Union[dict, "EnumeratedValue"]]]])

slots.EnumeratedQuantity_enumeration = Slot(uri=QUDT.enumeration, name="EnumeratedQuantity_enumeration", curie=QUDT.curie('enumeration'),
                   model_uri=QUDT.EnumeratedQuantity_enumeration, domain=EnumeratedQuantity, range=Optional[Union[Union[dict, "Enumeration"], list[Union[dict, "Enumeration"]]]])

slots.EnumeratedValue_altSymbol = Slot(uri=QUDT.altSymbol, name="EnumeratedValue_altSymbol", curie=QUDT.curie('altSymbol'),
                   model_uri=QUDT.EnumeratedValue_altSymbol, domain=EnumeratedValue, range=Optional[Union[str, list[str]]])

slots.EnumeratedValue_description = Slot(uri=DC.description, name="EnumeratedValue_description", curie=DC.curie('description'),
                   model_uri=QUDT.EnumeratedValue_description, domain=EnumeratedValue, range=Optional[Union[str, list[str]]])

slots.EnumeratedValue_abbreviation = Slot(uri=QUDT.abbreviation, name="EnumeratedValue_abbreviation", curie=QUDT.curie('abbreviation'),
                   model_uri=QUDT.EnumeratedValue_abbreviation, domain=EnumeratedValue, range=Optional[Union[str, list[str]]])

slots.EnumeratedValue_symbol = Slot(uri=QUDT.symbol, name="EnumeratedValue_symbol", curie=QUDT.curie('symbol'),
                   model_uri=QUDT.EnumeratedValue_symbol, domain=EnumeratedValue, range=Optional[Union[str, list[str]]])

slots.Enumeration_default = Slot(uri=QUDT.default, name="Enumeration_default", curie=QUDT.curie('default'),
                   model_uri=QUDT.Enumeration_default, domain=Enumeration, range=Optional[Union[Union[dict, "EnumeratedValue"], list[Union[dict, "EnumeratedValue"]]]])

slots.Enumeration_element = Slot(uri=QUDT.element, name="Enumeration_element", curie=QUDT.curie('element'),
                   model_uri=QUDT.Enumeration_element, domain=Enumeration, range=Union[Union[dict, "EnumeratedValue"], list[Union[dict, "EnumeratedValue"]]])

slots.Enumeration_abbreviation = Slot(uri=QUDT.abbreviation, name="Enumeration_abbreviation", curie=QUDT.curie('abbreviation'),
                   model_uri=QUDT.Enumeration_abbreviation, domain=Enumeration, range=Optional[Union[str, list[str]]])

slots.Figure_imageLocation = Slot(uri=QUDT.imageLocation, name="Figure_imageLocation", curie=QUDT.curie('imageLocation'),
                   model_uri=QUDT.Figure_imageLocation, domain=Figure, range=Union[str, list[str]])

slots.Figure_figureCaption = Slot(uri=QUDT.figureCaption, name="Figure_figureCaption", curie=QUDT.curie('figureCaption'),
                   model_uri=QUDT.Figure_figureCaption, domain=Figure, range=Optional[Union[str, list[str]]])

slots.Figure_figureLabel = Slot(uri=QUDT.figureLabel, name="Figure_figureLabel", curie=QUDT.curie('figureLabel'),
                   model_uri=QUDT.Figure_figureLabel, domain=Figure, range=Optional[Union[str, list[str]]])

slots.Figure_height = Slot(uri=QUDT.height, name="Figure_height", curie=QUDT.curie('height'),
                   model_uri=QUDT.Figure_height, domain=Figure, range=Optional[Union[str, list[str]]])

slots.Figure_image = Slot(uri=QUDT.image, name="Figure_image", curie=QUDT.curie('image'),
                   model_uri=QUDT.Figure_image, domain=Figure, range=Optional[Union[str, list[str]]])

slots.Figure_landscape = Slot(uri=QUDT.landscape, name="Figure_landscape", curie=QUDT.curie('landscape'),
                   model_uri=QUDT.Figure_landscape, domain=Figure, range=Optional[Union[str, list[str]]])

slots.Figure_width = Slot(uri=QUDT.width, name="Figure_width", curie=QUDT.curie('width'),
                   model_uri=QUDT.Figure_width, domain=Figure, range=Optional[Union[str, list[str]]])

slots.OrderedType_literal = Slot(uri=DTYPE.literal, name="OrderedType_literal", curie=DTYPE.curie('literal'),
                   model_uri=QUDT.OrderedType_literal, domain=OrderedType, range=Optional[Union[str, list[str]]])

slots.OrdinalScale_order = Slot(uri=QUDT.order, name="OrdinalScale_order", curie=QUDT.curie('order'),
                   model_uri=QUDT.OrdinalScale_order, domain=OrdinalScale, range=Union[str, list[str]])

slots.Organization_url = Slot(uri=QUDT.url, name="Organization_url", curie=QUDT.curie('url'),
                   model_uri=QUDT.Organization_url, domain=Organization, range=Optional[Union[str, list[str]]])

slots.PhysicalConstant_applicableSystem = Slot(uri=QUDT.applicableSystem, name="PhysicalConstant_applicableSystem", curie=QUDT.curie('applicableSystem'),
                   model_uri=QUDT.PhysicalConstant_applicableSystem, domain=PhysicalConstant, range=Optional[Union[Union[dict, "SystemOfUnits"], list[Union[dict, "SystemOfUnits"]]]])

slots.PhysicalConstant_applicableUnit = Slot(uri=QUDT.applicableUnit, name="PhysicalConstant_applicableUnit", curie=QUDT.curie('applicableUnit'),
                   model_uri=QUDT.PhysicalConstant_applicableUnit, domain=PhysicalConstant, range=Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]])

slots.PhysicalConstant_exactMatch = Slot(uri=QUDT.exactMatch, name="PhysicalConstant_exactMatch", curie=QUDT.curie('exactMatch'),
                   model_uri=QUDT.PhysicalConstant_exactMatch, domain=PhysicalConstant, range=Optional[Union[Union[dict, "PhysicalConstant"], list[Union[dict, "PhysicalConstant"]]]])

slots.PhysicalConstant_hasDimensionVector = Slot(uri=QUDT.hasDimensionVector, name="PhysicalConstant_hasDimensionVector", curie=QUDT.curie('hasDimensionVector'),
                   model_uri=QUDT.PhysicalConstant_hasDimensionVector, domain=PhysicalConstant, range=Optional[Union[Union[dict, "QuantityKindDimensionVector"], list[Union[dict, "QuantityKindDimensionVector"]]]])

slots.PhysicalConstant_ucumCode = Slot(uri=QUDT.ucumCode, name="PhysicalConstant_ucumCode", curie=QUDT.curie('ucumCode'),
                   model_uri=QUDT.PhysicalConstant_ucumCode, domain=PhysicalConstant, range=Optional[Union[str, list[str]]])

slots.PhysicalConstant_exactConstant = Slot(uri=QUDT.exactConstant, name="PhysicalConstant_exactConstant", curie=QUDT.curie('exactConstant'),
                   model_uri=QUDT.PhysicalConstant_exactConstant, domain=PhysicalConstant, range=Optional[Union[Union[bool, Bool], list[Union[bool, Bool]]]])

slots.PhysicalConstant_altSymbol = Slot(uri=QUDT.altSymbol, name="PhysicalConstant_altSymbol", curie=QUDT.curie('altSymbol'),
                   model_uri=QUDT.PhysicalConstant_altSymbol, domain=PhysicalConstant, range=Optional[Union[str, list[str]]])

slots.PhysicalConstant_isoNormativeReference = Slot(uri=QUDT.isoNormativeReference, name="PhysicalConstant_isoNormativeReference", curie=QUDT.curie('isoNormativeReference'),
                   model_uri=QUDT.PhysicalConstant_isoNormativeReference, domain=PhysicalConstant, range=Optional[Union[str, list[str]]])

slots.PhysicalConstant_latexSymbol = Slot(uri=QUDT.latexSymbol, name="PhysicalConstant_latexSymbol", curie=QUDT.curie('latexSymbol'),
                   model_uri=QUDT.PhysicalConstant_latexSymbol, domain=PhysicalConstant, range=Optional[Union[str, list[str]]])

slots.PhysicalConstant_normativeReference = Slot(uri=QUDT.normativeReference, name="PhysicalConstant_normativeReference", curie=QUDT.curie('normativeReference'),
                   model_uri=QUDT.PhysicalConstant_normativeReference, domain=PhysicalConstant, range=Optional[Union[str, list[str]]])

slots.PhysicalConstant_symbol = Slot(uri=QUDT.symbol, name="PhysicalConstant_symbol", curie=QUDT.curie('symbol'),
                   model_uri=QUDT.PhysicalConstant_symbol, domain=PhysicalConstant, range=Optional[Union[str, list[str]]])

slots.PhysicalConstant_latexDefinition = Slot(uri=QUDT.latexDefinition, name="PhysicalConstant_latexDefinition", curie=QUDT.curie('latexDefinition'),
                   model_uri=QUDT.PhysicalConstant_latexDefinition, domain=PhysicalConstant, range=Optional[Union[str, list[str]]])

slots.PhysicalConstant_mathMLdefinition = Slot(uri=QUDT.mathMLdefinition, name="PhysicalConstant_mathMLdefinition", curie=QUDT.curie('mathMLdefinition'),
                   model_uri=QUDT.PhysicalConstant_mathMLdefinition, domain=PhysicalConstant, range=Optional[Union[str, list[str]]])

slots.Prefix_exactMatch = Slot(uri=QUDT.exactMatch, name="Prefix_exactMatch", curie=QUDT.curie('exactMatch'),
                   model_uri=QUDT.Prefix_exactMatch, domain=Prefix, range=Optional[Union[Union[dict, "Prefix"], list[Union[dict, "Prefix"]]]])

slots.Prefix_ucumCode = Slot(uri=QUDT.ucumCode, name="Prefix_ucumCode", curie=QUDT.curie('ucumCode'),
                   model_uri=QUDT.Prefix_ucumCode, domain=Prefix, range=Optional[Union[Union[dict, "UCUMcs-term"], list[Union[dict, "UCUMcs-term"]]]])

slots.Prefix_altSymbol = Slot(uri=QUDT.altSymbol, name="Prefix_altSymbol", curie=QUDT.curie('altSymbol'),
                   model_uri=QUDT.Prefix_altSymbol, domain=Prefix, range=Optional[Union[str, list[str]]])

slots.Prefix_latexSymbol = Slot(uri=QUDT.latexSymbol, name="Prefix_latexSymbol", curie=QUDT.curie('latexSymbol'),
                   model_uri=QUDT.Prefix_latexSymbol, domain=Prefix, range=Optional[Union[str, list[str]]])

slots.Prefix_symbol = Slot(uri=QUDT.symbol, name="Prefix_symbol", curie=QUDT.curie('symbol'),
                   model_uri=QUDT.Prefix_symbol, domain=Prefix, range=Optional[Union[str, list[str]]])

slots.Prefix_prefixMultiplier = Slot(uri=QUDT.prefixMultiplier, name="Prefix_prefixMultiplier", curie=QUDT.curie('prefixMultiplier'),
                   model_uri=QUDT.Prefix_prefixMultiplier, domain=Prefix, range=Optional[Union[str, list[str]]])

slots.Quantifiable_dataEncoding = Slot(uri=QUDT.dataEncoding, name="Quantifiable_dataEncoding", curie=QUDT.curie('dataEncoding'),
                   model_uri=QUDT.Quantifiable_dataEncoding, domain=Quantifiable, range=Optional[Union[Union[dict, DataEncoding], list[Union[dict, DataEncoding]]]])

slots.Quantifiable_datatype = Slot(uri=QUDT.datatype, name="Quantifiable_datatype", curie=QUDT.curie('datatype'),
                   model_uri=QUDT.Quantifiable_datatype, domain=Quantifiable, range=Optional[Union[Union[dict, Datatype], list[Union[dict, Datatype]]]])

slots.Quantifiable_hasUnit = Slot(uri=QUDT.hasUnit, name="Quantifiable_hasUnit", curie=QUDT.curie('hasUnit'),
                   model_uri=QUDT.Quantifiable_hasUnit, domain=Quantifiable, range=Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]])

slots.Quantifiable_relativeStandardUncertainty = Slot(uri=QUDT.relativeStandardUncertainty, name="Quantifiable_relativeStandardUncertainty", curie=QUDT.curie('relativeStandardUncertainty'),
                   model_uri=QUDT.Quantifiable_relativeStandardUncertainty, domain=Quantifiable, range=Optional[Union[float, list[float]]])

slots.Quantifiable_standardUncertainty = Slot(uri=QUDT.standardUncertainty, name="Quantifiable_standardUncertainty", curie=QUDT.curie('standardUncertainty'),
                   model_uri=QUDT.Quantifiable_standardUncertainty, domain=Quantifiable, range=Optional[Union[Decimal, list[Decimal]]])

slots.Quantifiable_standardUncertaintySN = Slot(uri=QUDT.standardUncertaintySN, name="Quantifiable_standardUncertaintySN", curie=QUDT.curie('standardUncertaintySN'),
                   model_uri=QUDT.Quantifiable_standardUncertaintySN, domain=Quantifiable, range=Optional[Union[float, list[float]]])

slots.Quantifiable_value = Slot(uri=QUDT.value, name="Quantifiable_value", curie=QUDT.curie('value'),
                   model_uri=QUDT.Quantifiable_value, domain=Quantifiable, range=Optional[Union[str, list[str]]])

slots.Quantifiable_valueSN = Slot(uri=QUDT.valueSN, name="Quantifiable_valueSN", curie=QUDT.curie('valueSN'),
                   model_uri=QUDT.Quantifiable_valueSN, domain=Quantifiable, range=Optional[Union[str, list[str]]])

slots.Quantity_hasQuantityKind = Slot(uri=QUDT.hasQuantityKind, name="Quantity_hasQuantityKind", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=QUDT.Quantity_hasQuantityKind, domain=Quantity, range=Optional[Union[Union[dict, "QuantityKind"], list[Union[dict, "QuantityKind"]]]])

slots.Quantity_quantityValue = Slot(uri=QUDT.quantityValue, name="Quantity_quantityValue", curie=QUDT.curie('quantityValue'),
                   model_uri=QUDT.Quantity_quantityValue, domain=Quantity, range=Optional[Union[Union[dict, "QuantityValue"], list[Union[dict, "QuantityValue"]]]])

slots.Quantity_isDeltaQuantity = Slot(uri=QUDT.isDeltaQuantity, name="Quantity_isDeltaQuantity", curie=QUDT.curie('isDeltaQuantity'),
                   model_uri=QUDT.Quantity_isDeltaQuantity, domain=Quantity, range=Optional[Union[Union[bool, Bool], list[Union[bool, Bool]]]])

slots.QuantityKind_dimensionVectorForSI = Slot(uri=QUDT.dimensionVectorForSI, name="QuantityKind_dimensionVectorForSI", curie=QUDT.curie('dimensionVectorForSI'),
                   model_uri=QUDT.QuantityKind_dimensionVectorForSI, domain=QuantityKind, range=Optional[Union[Union[dict, QuantityKindDimensionVectorSI], list[Union[dict, QuantityKindDimensionVectorSI]]]])

slots.QuantityKind_exactMatch = Slot(uri=QUDT.exactMatch, name="QuantityKind_exactMatch", curie=QUDT.curie('exactMatch'),
                   model_uri=QUDT.QuantityKind_exactMatch, domain=QuantityKind, range=Optional[Union[Union[dict, "QuantityKind"], list[Union[dict, "QuantityKind"]]]])

slots.QuantityKind_hasDimensionVector = Slot(uri=QUDT.hasDimensionVector, name="QuantityKind_hasDimensionVector", curie=QUDT.curie('hasDimensionVector'),
                   model_uri=QUDT.QuantityKind_hasDimensionVector, domain=QuantityKind, range=Optional[Union[Union[dict, QuantityKindDimensionVector], list[Union[dict, QuantityKindDimensionVector]]]])

slots.QuantityKind_iec61360Code = Slot(uri=QUDT.iec61360Code, name="QuantityKind_iec61360Code", curie=QUDT.curie('iec61360Code'),
                   model_uri=QUDT.QuantityKind_iec61360Code, domain=QuantityKind, range=Optional[Union[str, list[str]]])

slots.QuantityKind_applicableCGSUnit = Slot(uri=QUDT.applicableCGSUnit, name="QuantityKind_applicableCGSUnit", curie=QUDT.curie('applicableCGSUnit'),
                   model_uri=QUDT.QuantityKind_applicableCGSUnit, domain=QuantityKind, range=Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]])

slots.QuantityKind_applicableISOUnit = Slot(uri=QUDT.applicableISOUnit, name="QuantityKind_applicableISOUnit", curie=QUDT.curie('applicableISOUnit'),
                   model_uri=QUDT.QuantityKind_applicableISOUnit, domain=QuantityKind, range=Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]])

slots.QuantityKind_applicableImperialUnit = Slot(uri=QUDT.applicableImperialUnit, name="QuantityKind_applicableImperialUnit", curie=QUDT.curie('applicableImperialUnit'),
                   model_uri=QUDT.QuantityKind_applicableImperialUnit, domain=QuantityKind, range=Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]])

slots.QuantityKind_applicableSIUnit = Slot(uri=QUDT.applicableSIUnit, name="QuantityKind_applicableSIUnit", curie=QUDT.curie('applicableSIUnit'),
                   model_uri=QUDT.QuantityKind_applicableSIUnit, domain=QuantityKind, range=Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]])

slots.QuantityKind_applicableUSCustomaryUnit = Slot(uri=QUDT.applicableUSCustomaryUnit, name="QuantityKind_applicableUSCustomaryUnit", curie=QUDT.curie('applicableUSCustomaryUnit'),
                   model_uri=QUDT.QuantityKind_applicableUSCustomaryUnit, domain=QuantityKind, range=Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]])

slots.QuantityKind_applicableUnit = Slot(uri=QUDT.applicableUnit, name="QuantityKind_applicableUnit", curie=QUDT.curie('applicableUnit'),
                   model_uri=QUDT.QuantityKind_applicableUnit, domain=QuantityKind, range=Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]])

slots.QuantityKind_qkdvDenominator = Slot(uri=QUDT.qkdvDenominator, name="QuantityKind_qkdvDenominator", curie=QUDT.curie('qkdvDenominator'),
                   model_uri=QUDT.QuantityKind_qkdvDenominator, domain=QuantityKind, range=Optional[Union[Union[dict, QuantityKindDimensionVector], list[Union[dict, QuantityKindDimensionVector]]]])

slots.QuantityKind_qkdvNumerator = Slot(uri=QUDT.qkdvNumerator, name="QuantityKind_qkdvNumerator", curie=QUDT.curie('qkdvNumerator'),
                   model_uri=QUDT.QuantityKind_qkdvNumerator, domain=QuantityKind, range=Optional[Union[Union[dict, QuantityKindDimensionVector], list[Union[dict, QuantityKindDimensionVector]]]])

slots.QuantityKind_latexDefinition = Slot(uri=QUDT.latexDefinition, name="QuantityKind_latexDefinition", curie=QUDT.curie('latexDefinition'),
                   model_uri=QUDT.QuantityKind_latexDefinition, domain=QuantityKind, range=Optional[Union[str, list[str]]])

slots.QuantityKind_mathMLdefinition = Slot(uri=QUDT.mathMLdefinition, name="QuantityKind_mathMLdefinition", curie=QUDT.curie('mathMLdefinition'),
                   model_uri=QUDT.QuantityKind_mathMLdefinition, domain=QuantityKind, range=Optional[Union[str, list[str]]])

slots.QuantityKindDimensionVector_hasReferenceQuantityKind = Slot(uri=QUDT.hasReferenceQuantityKind, name="QuantityKindDimensionVector_hasReferenceQuantityKind", curie=QUDT.curie('hasReferenceQuantityKind'),
                   model_uri=QUDT.QuantityKindDimensionVector_hasReferenceQuantityKind, domain=QuantityKindDimensionVector, range=Optional[Union[Union[dict, "QuantityKind"], list[Union[dict, "QuantityKind"]]]])

slots.QuantityKindDimensionVector_latexSymbol = Slot(uri=QUDT.latexSymbol, name="QuantityKindDimensionVector_latexSymbol", curie=QUDT.curie('latexSymbol'),
                   model_uri=QUDT.QuantityKindDimensionVector_latexSymbol, domain=QuantityKindDimensionVector, range=Optional[Union[str, list[str]]])

slots.QuantityKindDimensionVector_dimensionExponentForAmountOfSubstance = Slot(uri=QUDT.dimensionExponentForAmountOfSubstance, name="QuantityKindDimensionVector_dimensionExponentForAmountOfSubstance", curie=QUDT.curie('dimensionExponentForAmountOfSubstance'),
                   model_uri=QUDT.QuantityKindDimensionVector_dimensionExponentForAmountOfSubstance, domain=QuantityKindDimensionVector, range=Union[str, list[str]])

slots.QuantityKindDimensionVector_dimensionExponentForElectricCurrent = Slot(uri=QUDT.dimensionExponentForElectricCurrent, name="QuantityKindDimensionVector_dimensionExponentForElectricCurrent", curie=QUDT.curie('dimensionExponentForElectricCurrent'),
                   model_uri=QUDT.QuantityKindDimensionVector_dimensionExponentForElectricCurrent, domain=QuantityKindDimensionVector, range=Union[str, list[str]])

slots.QuantityKindDimensionVector_dimensionExponentForLength = Slot(uri=QUDT.dimensionExponentForLength, name="QuantityKindDimensionVector_dimensionExponentForLength", curie=QUDT.curie('dimensionExponentForLength'),
                   model_uri=QUDT.QuantityKindDimensionVector_dimensionExponentForLength, domain=QuantityKindDimensionVector, range=Union[str, list[str]])

slots.QuantityKindDimensionVector_dimensionExponentForLuminousIntensity = Slot(uri=QUDT.dimensionExponentForLuminousIntensity, name="QuantityKindDimensionVector_dimensionExponentForLuminousIntensity", curie=QUDT.curie('dimensionExponentForLuminousIntensity'),
                   model_uri=QUDT.QuantityKindDimensionVector_dimensionExponentForLuminousIntensity, domain=QuantityKindDimensionVector, range=Union[str, list[str]])

slots.QuantityKindDimensionVector_dimensionExponentForMass = Slot(uri=QUDT.dimensionExponentForMass, name="QuantityKindDimensionVector_dimensionExponentForMass", curie=QUDT.curie('dimensionExponentForMass'),
                   model_uri=QUDT.QuantityKindDimensionVector_dimensionExponentForMass, domain=QuantityKindDimensionVector, range=Union[str, list[str]])

slots.QuantityKindDimensionVector_dimensionExponentForThermodynamicTemperature = Slot(uri=QUDT.dimensionExponentForThermodynamicTemperature, name="QuantityKindDimensionVector_dimensionExponentForThermodynamicTemperature", curie=QUDT.curie('dimensionExponentForThermodynamicTemperature'),
                   model_uri=QUDT.QuantityKindDimensionVector_dimensionExponentForThermodynamicTemperature, domain=QuantityKindDimensionVector, range=Union[str, list[str]])

slots.QuantityKindDimensionVector_dimensionExponentForTime = Slot(uri=QUDT.dimensionExponentForTime, name="QuantityKindDimensionVector_dimensionExponentForTime", curie=QUDT.curie('dimensionExponentForTime'),
                   model_uri=QUDT.QuantityKindDimensionVector_dimensionExponentForTime, domain=QuantityKindDimensionVector, range=Union[str, list[str]])

slots.QuantityKindDimensionVector_dimensionlessExponent = Slot(uri=QUDT.dimensionlessExponent, name="QuantityKindDimensionVector_dimensionlessExponent", curie=QUDT.curie('dimensionlessExponent'),
                   model_uri=QUDT.QuantityKindDimensionVector_dimensionlessExponent, domain=QuantityKindDimensionVector, range=Union[str, list[str]])

slots.QuantityKindDimensionVector_latexDefinition = Slot(uri=QUDT.latexDefinition, name="QuantityKindDimensionVector_latexDefinition", curie=QUDT.curie('latexDefinition'),
                   model_uri=QUDT.QuantityKindDimensionVector_latexDefinition, domain=QuantityKindDimensionVector, range=Optional[Union[str, list[str]]])

slots.QuantityType_value = Slot(uri=QUDT.value, name="QuantityType_value", curie=QUDT.curie('value'),
                   model_uri=QUDT.QuantityType_value, domain=QuantityType, range=Optional[Union[Union[dict, QuantityKind], list[Union[dict, QuantityKind]]]])

slots.QuantityValue_hasUnit = Slot(uri=QUDT.hasUnit, name="QuantityValue_hasUnit", curie=QUDT.curie('hasUnit'),
                   model_uri=QUDT.QuantityValue_hasUnit, domain=QuantityValue, range=Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]])

slots.Rule_ruleType = Slot(uri=QUDT.ruleType, name="Rule_ruleType", curie=QUDT.curie('ruleType'),
                   model_uri=QUDT.Rule_ruleType, domain=Rule, range=Optional[Union[Union[dict, "RuleType"], list[Union[dict, "RuleType"]]]])

slots.Rule_rationale = Slot(uri=QUDT.rationale, name="Rule_rationale", curie=QUDT.curie('rationale'),
                   model_uri=QUDT.Rule_rationale, domain=Rule, range=Optional[Union[str, list[str]]])

slots.ScalarDatatype_rdfsDatatype = Slot(uri=QUDT.rdfsDatatype, name="ScalarDatatype_rdfsDatatype", curie=QUDT.curie('rdfsDatatype'),
                   model_uri=QUDT.ScalarDatatype_rdfsDatatype, domain=ScalarDatatype, range=Optional[Union[Union[dict, Datatype], list[Union[dict, Datatype]]]])

slots.ScalarDatatype_bits = Slot(uri=QUDT.bits, name="ScalarDatatype_bits", curie=QUDT.curie('bits'),
                   model_uri=QUDT.ScalarDatatype_bits, domain=ScalarDatatype, range=Optional[Union[str, list[str]]])

slots.ScalarDatatype_bytes = Slot(uri=QUDT.bytes, name="ScalarDatatype_bytes", curie=QUDT.curie('bytes'),
                   model_uri=QUDT.ScalarDatatype_bytes, domain=ScalarDatatype, range=Optional[Union[str, list[str]]])

slots.ScalarDatatype_length = Slot(uri=QUDT.length, name="ScalarDatatype_length", curie=QUDT.curie('length'),
                   model_uri=QUDT.ScalarDatatype_length, domain=ScalarDatatype, range=Optional[Union[str, list[str]]])

slots.ScalarDatatype_maxExclusive = Slot(uri=QUDT.maxExclusive, name="ScalarDatatype_maxExclusive", curie=QUDT.curie('maxExclusive'),
                   model_uri=QUDT.ScalarDatatype_maxExclusive, domain=ScalarDatatype, range=Optional[Union[str, list[str]]])

slots.ScalarDatatype_maxInclusive = Slot(uri=QUDT.maxInclusive, name="ScalarDatatype_maxInclusive", curie=QUDT.curie('maxInclusive'),
                   model_uri=QUDT.ScalarDatatype_maxInclusive, domain=ScalarDatatype, range=Optional[Union[str, list[str]]])

slots.ScalarDatatype_minExclusive = Slot(uri=QUDT.minExclusive, name="ScalarDatatype_minExclusive", curie=QUDT.curie('minExclusive'),
                   model_uri=QUDT.ScalarDatatype_minExclusive, domain=ScalarDatatype, range=Optional[Union[str, list[str]]])

slots.ScalarDatatype_minInclusive = Slot(uri=QUDT.minInclusive, name="ScalarDatatype_minInclusive", curie=QUDT.curie('minInclusive'),
                   model_uri=QUDT.ScalarDatatype_minInclusive, domain=ScalarDatatype, range=Optional[Union[str, list[str]]])

slots.Scale_permissibleMaths = Slot(uri=QUDT.permissibleMaths, name="Scale_permissibleMaths", curie=QUDT.curie('permissibleMaths'),
                   model_uri=QUDT.Scale_permissibleMaths, domain=Scale, range=Optional[Union[Union[dict, MathsFunctionType], list[Union[dict, MathsFunctionType]]]])

slots.Scale_permissibleTransformation = Slot(uri=QUDT.permissibleTransformation, name="Scale_permissibleTransformation", curie=QUDT.curie('permissibleTransformation'),
                   model_uri=QUDT.Scale_permissibleTransformation, domain=Scale, range=Optional[Union[Union[dict, "TransformType"], list[Union[dict, "TransformType"]]]])

slots.Scale_scaleType = Slot(uri=QUDT.scaleType, name="Scale_scaleType", curie=QUDT.curie('scaleType'),
                   model_uri=QUDT.Scale_scaleType, domain=Scale, range=Optional[Union[Union[dict, "ScaleType"], list[Union[dict, "ScaleType"]]]])

slots.Scale_dataStructure = Slot(uri=QUDT.dataStructure, name="Scale_dataStructure", curie=QUDT.curie('dataStructure'),
                   model_uri=QUDT.Scale_dataStructure, domain=Scale, range=Optional[Union[str, list[str]]])

slots.ScaleType_permissibleMaths = Slot(uri=QUDT.permissibleMaths, name="ScaleType_permissibleMaths", curie=QUDT.curie('permissibleMaths'),
                   model_uri=QUDT.ScaleType_permissibleMaths, domain=ScaleType, range=Optional[Union[Union[dict, MathsFunctionType], list[Union[dict, MathsFunctionType]]]])

slots.ScaleType_permissibleTransformation = Slot(uri=QUDT.permissibleTransformation, name="ScaleType_permissibleTransformation", curie=QUDT.curie('permissibleTransformation'),
                   model_uri=QUDT.ScaleType_permissibleTransformation, domain=ScaleType, range=Optional[Union[Union[dict, "TransformType"], list[Union[dict, "TransformType"]]]])

slots.ScaleType_dataStructure = Slot(uri=QUDT.dataStructure, name="ScaleType_dataStructure", curie=QUDT.curie('dataStructure'),
                   model_uri=QUDT.ScaleType_dataStructure, domain=ScaleType, range=Optional[Union[str, list[str]]])

slots.SystemOfQuantityKinds_baseDimensionEnumeration = Slot(uri=QUDT.baseDimensionEnumeration, name="SystemOfQuantityKinds_baseDimensionEnumeration", curie=QUDT.curie('baseDimensionEnumeration'),
                   model_uri=QUDT.SystemOfQuantityKinds_baseDimensionEnumeration, domain=SystemOfQuantityKinds, range=Optional[Union[Union[dict, Enumeration], list[Union[dict, Enumeration]]]])

slots.SystemOfQuantityKinds_hasBaseQuantityKind = Slot(uri=QUDT.hasBaseQuantityKind, name="SystemOfQuantityKinds_hasBaseQuantityKind", curie=QUDT.curie('hasBaseQuantityKind'),
                   model_uri=QUDT.SystemOfQuantityKinds_hasBaseQuantityKind, domain=SystemOfQuantityKinds, range=Optional[Union[Union[dict, "QuantityKind"], list[Union[dict, "QuantityKind"]]]])

slots.SystemOfQuantityKinds_hasQuantityKind = Slot(uri=QUDT.hasQuantityKind, name="SystemOfQuantityKinds_hasQuantityKind", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=QUDT.SystemOfQuantityKinds_hasQuantityKind, domain=SystemOfQuantityKinds, range=Optional[Union[Union[dict, "QuantityKind"], list[Union[dict, "QuantityKind"]]]])

slots.SystemOfQuantityKinds_hasUnitSystem = Slot(uri=QUDT.hasUnitSystem, name="SystemOfQuantityKinds_hasUnitSystem", curie=QUDT.curie('hasUnitSystem'),
                   model_uri=QUDT.SystemOfQuantityKinds_hasUnitSystem, domain=SystemOfQuantityKinds, range=Optional[Union[Union[dict, "SystemOfUnits"], list[Union[dict, "SystemOfUnits"]]]])

slots.SystemOfQuantityKinds_systemDerivedQuantityKind = Slot(uri=QUDT.systemDerivedQuantityKind, name="SystemOfQuantityKinds_systemDerivedQuantityKind", curie=QUDT.curie('systemDerivedQuantityKind'),
                   model_uri=QUDT.SystemOfQuantityKinds_systemDerivedQuantityKind, domain=SystemOfQuantityKinds, range=Optional[Union[Union[dict, "QuantityKind"], list[Union[dict, "QuantityKind"]]]])

slots.SystemOfUnits_applicablePhysicalConstant = Slot(uri=QUDT.applicablePhysicalConstant, name="SystemOfUnits_applicablePhysicalConstant", curie=QUDT.curie('applicablePhysicalConstant'),
                   model_uri=QUDT.SystemOfUnits_applicablePhysicalConstant, domain=SystemOfUnits, range=Optional[Union[Union[dict, PhysicalConstant], list[Union[dict, PhysicalConstant]]]])

slots.SystemOfUnits_hasAllowedUnit = Slot(uri=QUDT.hasAllowedUnit, name="SystemOfUnits_hasAllowedUnit", curie=QUDT.curie('hasAllowedUnit'),
                   model_uri=QUDT.SystemOfUnits_hasAllowedUnit, domain=SystemOfUnits, range=Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]])

slots.SystemOfUnits_hasBaseUnit = Slot(uri=QUDT.hasBaseUnit, name="SystemOfUnits_hasBaseUnit", curie=QUDT.curie('hasBaseUnit'),
                   model_uri=QUDT.SystemOfUnits_hasBaseUnit, domain=SystemOfUnits, range=Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]])

slots.SystemOfUnits_hasCoherentUnit = Slot(uri=QUDT.hasCoherentUnit, name="SystemOfUnits_hasCoherentUnit", curie=QUDT.curie('hasCoherentUnit'),
                   model_uri=QUDT.SystemOfUnits_hasCoherentUnit, domain=SystemOfUnits, range=Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]])

slots.SystemOfUnits_hasDefinedUnit = Slot(uri=QUDT.hasDefinedUnit, name="SystemOfUnits_hasDefinedUnit", curie=QUDT.curie('hasDefinedUnit'),
                   model_uri=QUDT.SystemOfUnits_hasDefinedUnit, domain=SystemOfUnits, range=Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]])

slots.SystemOfUnits_hasDerivedCoherentUnit = Slot(uri=QUDT.hasDerivedCoherentUnit, name="SystemOfUnits_hasDerivedCoherentUnit", curie=QUDT.curie('hasDerivedCoherentUnit'),
                   model_uri=QUDT.SystemOfUnits_hasDerivedCoherentUnit, domain=SystemOfUnits, range=Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]])

slots.SystemOfUnits_hasDerivedUnit = Slot(uri=QUDT.hasDerivedUnit, name="SystemOfUnits_hasDerivedUnit", curie=QUDT.curie('hasDerivedUnit'),
                   model_uri=QUDT.SystemOfUnits_hasDerivedUnit, domain=SystemOfUnits, range=Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]])

slots.SystemOfUnits_hasUnit = Slot(uri=QUDT.hasUnit, name="SystemOfUnits_hasUnit", curie=QUDT.curie('hasUnit'),
                   model_uri=QUDT.SystemOfUnits_hasUnit, domain=SystemOfUnits, range=Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]])

slots.SystemOfUnits_prefix = Slot(uri=QUDT.prefix, name="SystemOfUnits_prefix", curie=QUDT.curie('prefix'),
                   model_uri=QUDT.SystemOfUnits_prefix, domain=SystemOfUnits, range=Optional[Union[Union[dict, Prefix], list[Union[dict, Prefix]]]])

slots.Unit_applicableSystem = Slot(uri=QUDT.applicableSystem, name="Unit_applicableSystem", curie=QUDT.curie('applicableSystem'),
                   model_uri=QUDT.Unit_applicableSystem, domain=Unit, range=Optional[Union[Union[dict, SystemOfUnits], list[Union[dict, SystemOfUnits]]]])

slots.Unit_definedUnitOfSystem = Slot(uri=QUDT.definedUnitOfSystem, name="Unit_definedUnitOfSystem", curie=QUDT.curie('definedUnitOfSystem'),
                   model_uri=QUDT.Unit_definedUnitOfSystem, domain=Unit, range=Optional[Union[Union[dict, SystemOfUnits], list[Union[dict, SystemOfUnits]]]])

slots.Unit_derivedCoherentUnitOfSystem = Slot(uri=QUDT.derivedCoherentUnitOfSystem, name="Unit_derivedCoherentUnitOfSystem", curie=QUDT.curie('derivedCoherentUnitOfSystem'),
                   model_uri=QUDT.Unit_derivedCoherentUnitOfSystem, domain=Unit, range=Optional[Union[Union[dict, SystemOfUnits], list[Union[dict, SystemOfUnits]]]])

slots.Unit_derivedUnitOfSystem = Slot(uri=QUDT.derivedUnitOfSystem, name="Unit_derivedUnitOfSystem", curie=QUDT.curie('derivedUnitOfSystem'),
                   model_uri=QUDT.Unit_derivedUnitOfSystem, domain=Unit, range=Optional[Union[Union[dict, SystemOfUnits], list[Union[dict, SystemOfUnits]]]])

slots.Unit_exactMatch = Slot(uri=QUDT.exactMatch, name="Unit_exactMatch", curie=QUDT.curie('exactMatch'),
                   model_uri=QUDT.Unit_exactMatch, domain=Unit, range=Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]])

slots.Unit_hasDimensionVector = Slot(uri=QUDT.hasDimensionVector, name="Unit_hasDimensionVector", curie=QUDT.curie('hasDimensionVector'),
                   model_uri=QUDT.Unit_hasDimensionVector, domain=Unit, range=Optional[Union[Union[dict, QuantityKindDimensionVector], list[Union[dict, QuantityKindDimensionVector]]]])

slots.Unit_hasFactorUnit = Slot(uri=QUDT.hasFactorUnit, name="Unit_hasFactorUnit", curie=QUDT.curie('hasFactorUnit'),
                   model_uri=QUDT.Unit_hasFactorUnit, domain=Unit, range=Optional[Union[Union[dict, "Class"], list[Union[dict, "Class"]]]])

slots.Unit_hasQuantityKind = Slot(uri=QUDT.hasQuantityKind, name="Unit_hasQuantityKind", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=QUDT.Unit_hasQuantityKind, domain=Unit, range=Optional[Union[Union[dict, QuantityKind], list[Union[dict, QuantityKind]]]])

slots.Unit_iec61360Code = Slot(uri=QUDT.iec61360Code, name="Unit_iec61360Code", curie=QUDT.curie('iec61360Code'),
                   model_uri=QUDT.Unit_iec61360Code, domain=Unit, range=Optional[Union[str, list[str]]])

slots.Unit_prefix = Slot(uri=QUDT.prefix, name="Unit_prefix", curie=QUDT.curie('prefix'),
                   model_uri=QUDT.Unit_prefix, domain=Unit, range=Optional[Union[Union[dict, Prefix], list[Union[dict, Prefix]]]])

slots.Unit_qkdvDenominator = Slot(uri=QUDT.qkdvDenominator, name="Unit_qkdvDenominator", curie=QUDT.curie('qkdvDenominator'),
                   model_uri=QUDT.Unit_qkdvDenominator, domain=Unit, range=Optional[Union[Union[dict, QuantityKindDimensionVector], list[Union[dict, QuantityKindDimensionVector]]]])

slots.Unit_qkdvNumerator = Slot(uri=QUDT.qkdvNumerator, name="Unit_qkdvNumerator", curie=QUDT.curie('qkdvNumerator'),
                   model_uri=QUDT.Unit_qkdvNumerator, domain=Unit, range=Optional[Union[Union[dict, QuantityKindDimensionVector], list[Union[dict, QuantityKindDimensionVector]]]])

slots.Unit_scalingOf = Slot(uri=QUDT.scalingOf, name="Unit_scalingOf", curie=QUDT.curie('scalingOf'),
                   model_uri=QUDT.Unit_scalingOf, domain=Unit, range=Optional[Union[Union[dict, "Unit"], list[Union[dict, "Unit"]]]])

slots.Unit_ucumCode = Slot(uri=QUDT.ucumCode, name="Unit_ucumCode", curie=QUDT.curie('ucumCode'),
                   model_uri=QUDT.Unit_ucumCode, domain=Unit, range=Optional[Union[Union[dict, "UCUMcs"], list[Union[dict, "UCUMcs"]]]])

slots.Unit_udunitsCode = Slot(uri=QUDT.udunitsCode, name="Unit_udunitsCode", curie=QUDT.curie('udunitsCode'),
                   model_uri=QUDT.Unit_udunitsCode, domain=Unit, range=Optional[Union[str, list[str]]])

slots.Unit_uneceCommonCode = Slot(uri=QUDT.uneceCommonCode, name="Unit_uneceCommonCode", curie=QUDT.curie('uneceCommonCode'),
                   model_uri=QUDT.Unit_uneceCommonCode, domain=Unit, range=Optional[Union[str, list[str]]])

slots.Unit_altSymbol = Slot(uri=QUDT.altSymbol, name="Unit_altSymbol", curie=QUDT.curie('altSymbol'),
                   model_uri=QUDT.Unit_altSymbol, domain=Unit, range=Optional[Union[str, list[str]]])

slots.Unit_latexDefinition = Slot(uri=QUDT.latexDefinition, name="Unit_latexDefinition", curie=QUDT.curie('latexDefinition'),
                   model_uri=QUDT.Unit_latexDefinition, domain=Unit, range=Optional[Union[str, list[str]]])

slots.Unit_latexSymbol = Slot(uri=QUDT.latexSymbol, name="Unit_latexSymbol", curie=QUDT.curie('latexSymbol'),
                   model_uri=QUDT.Unit_latexSymbol, domain=Unit, range=Optional[Union[str, list[str]]])

slots.Unit_siUnitsExpression = Slot(uri=QUDT.siUnitsExpression, name="Unit_siUnitsExpression", curie=QUDT.curie('siUnitsExpression'),
                   model_uri=QUDT.Unit_siUnitsExpression, domain=Unit, range=Optional[Union[str, list[str]]])

slots.Unit_symbol = Slot(uri=QUDT.symbol, name="Unit_symbol", curie=QUDT.curie('symbol'),
                   model_uri=QUDT.Unit_symbol, domain=Unit, range=Optional[Union[str, list[str]]])

slots.Unit_conversionMultiplier = Slot(uri=QUDT.conversionMultiplier, name="Unit_conversionMultiplier", curie=QUDT.curie('conversionMultiplier'),
                   model_uri=QUDT.Unit_conversionMultiplier, domain=Unit, range=Optional[Union[str, list[str]]])

slots.Unit_conversionMultiplierSN = Slot(uri=QUDT.conversionMultiplierSN, name="Unit_conversionMultiplierSN", curie=QUDT.curie('conversionMultiplierSN'),
                   model_uri=QUDT.Unit_conversionMultiplierSN, domain=Unit, range=Optional[Union[str, list[str]]])

slots.Unit_conversionOffset = Slot(uri=QUDT.conversionOffset, name="Unit_conversionOffset", curie=QUDT.curie('conversionOffset'),
                   model_uri=QUDT.Unit_conversionOffset, domain=Unit, range=Optional[Union[str, list[str]]])

slots.Unit_conversionOffsetSN = Slot(uri=QUDT.conversionOffsetSN, name="Unit_conversionOffsetSN", curie=QUDT.curie('conversionOffsetSN'),
                   model_uri=QUDT.Unit_conversionOffsetSN, domain=Unit, range=Optional[Union[str, list[str]]])

slots.Unit_factorUnitScalar = Slot(uri=QUDT.factorUnitScalar, name="Unit_factorUnitScalar", curie=QUDT.curie('factorUnitScalar'),
                   model_uri=QUDT.Unit_factorUnitScalar, domain=Unit, range=Optional[Union[str, list[str]]])

slots.Unit_mathMLdefinition = Slot(uri=QUDT.mathMLdefinition, name="Unit_mathMLdefinition", curie=QUDT.curie('mathMLdefinition'),
                   model_uri=QUDT.Unit_mathMLdefinition, domain=Unit, range=Optional[Union[str, list[str]]])

slots.UserQuantityKind_hasQuantityKind = Slot(uri=QUDT.hasQuantityKind, name="UserQuantityKind_hasQuantityKind", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=QUDT.UserQuantityKind_hasQuantityKind, domain=UserQuantityKind, range=Union[Union[dict, "QuantityKind"], list[Union[dict, "QuantityKind"]]])

slots.Verifiable_isoNormativeReference = Slot(uri=QUDT.isoNormativeReference, name="Verifiable_isoNormativeReference", curie=QUDT.curie('isoNormativeReference'),
                   model_uri=QUDT.Verifiable_isoNormativeReference, domain=Verifiable, range=Optional[Union[str, list[str]]])

slots.Verifiable_normativeReference = Slot(uri=QUDT.normativeReference, name="Verifiable_normativeReference", curie=QUDT.curie('normativeReference'),
                   model_uri=QUDT.Verifiable_normativeReference, domain=Verifiable, range=Optional[Union[str, list[str]]])
