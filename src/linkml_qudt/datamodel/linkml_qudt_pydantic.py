from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )

    @model_serializer(mode='wrap', when_used='unless-none')
    def treat_empty_lists_as_none(
            self, handler: SerializerFunctionWrapHandler,
            info: SerializationInfo) -> dict[str, Any]:
        if info.exclude_none:
            _instance = self.model_copy()
            for field, field_info in type(_instance).model_fields.items():
                if getattr(_instance, field) == [] and not(
                        field_info.is_required()):
                    setattr(_instance, field, None)
        else:
            _instance = self
        return handler(_instance, info)



class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'qudt',
     'description': 'qudt',
     'id': 'http://qudt.org/3.1.6/schema/qudt',
     'imports': ['linkml:types'],
     'name': 'qudt',
     'prefixes': {'dc': {'prefix_prefix': 'dc',
                         'prefix_reference': 'http://purl.org/dc/elements/1.1/'},
                  'dcterms': {'prefix_prefix': 'dcterms',
                              'prefix_reference': 'http://purl.org/dc/terms/'},
                  'dtype': {'prefix_prefix': 'dtype',
                            'prefix_reference': 'http://www.linkedmodel.org/schema/dtype#'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'owl': {'prefix_prefix': 'owl',
                          'prefix_reference': 'http://www.w3.org/2002/07/owl#'},
                  'prov': {'prefix_prefix': 'prov',
                           'prefix_reference': 'http://www.w3.org/ns/prov#'},
                  'qudt': {'prefix_prefix': 'qudt',
                           'prefix_reference': 'https://w3id.org/None/'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'},
                  'rdfs': {'prefix_prefix': 'rdfs',
                           'prefix_reference': 'http://www.w3.org/2000/01/rdf-schema#'},
                  'vaem': {'prefix_prefix': 'vaem',
                           'prefix_reference': 'http://www.linkedmodel.org/schema/vaem#'},
                  'voag': {'prefix_prefix': 'voag',
                           'prefix_reference': 'http://voag.linkedmodel.org/schema/voag#'}},
     'source_file': 'src/linkml_qudt/schema/linkml_qudt.yaml'} )


class Thing(ConfiguredBaseModel):
    """
    The root class for all QUDT concepts
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'owl:Thing', 'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    pass


class Error2(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'http://org.semanticweb.owlapi/error#Error2',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    pass


class Error3(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'http://org.semanticweb.owlapi/error#Error3',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    pass


class Aspect(Thing):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Aspect',
         'comments': ['An aspect is an abstract type class that defines properties '
                      'that can be reused.^^rdf:HTML'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    pass


class Concept(Thing):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Concept',
         'comments': ['The root class for all QUDT concepts.^^rdf:HTML'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'slot_usage': {'abbreviation': {'multivalued': False, 'name': 'abbreviation'},
                        'deprecated': {'multivalued': False, 'name': 'deprecated'},
                        'description': {'multivalued': False, 'name': 'description'},
                        'hasRule': {'name': 'hasRule', 'range': 'Rule'},
                        'id': {'multivalued': False, 'name': 'id'},
                        'isReplacedBy': {'multivalued': False, 'name': 'isReplacedBy'},
                        'plainTextDescription': {'multivalued': False,
                                                 'name': 'plainTextDescription'}}})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class AbstractQuantityKind(Concept):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:AbstractQuantityKind',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'slot_usage': {'altSymbol': {'name': 'altSymbol', 'required': False},
                        'broader': {'name': 'broader', 'range': 'QuantityKind'},
                        'latexSymbol': {'name': 'latexSymbol', 'required': False},
                        'symbol': {'multivalued': False, 'name': 'symbol'}}})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class BaseDimensionMagnitude(Concept):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:BaseDimensionMagnitude',
         'comments': ['<p class=\\"lm-para\\">A <em>Dimension</em> expresses a '
                      'magnitude for a base quantiy kind such as mass, length and '
                      'time.</p>\n'
                      '<p class=\\"lm-para\\">DEPRECATED - each exponent is expressed '
                      'as a property. Keep until a validaiton of this has been '
                      'done.</p>^^rdf:HTML'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'slot_usage': {'hasBaseQuantityKind': {'multivalued': False,
                                                'name': 'hasBaseQuantityKind',
                                                'range': 'QuantityKind',
                                                'required': True},
                        'vectorMagnitude': {'multivalued': False,
                                            'name': 'vectorMagnitude',
                                            'range': 'float',
                                            'required': True}}})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class Citation(Concept):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Citation',
         'comments': ['Provides a simple way of making citations.^^rdf:HTML'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'slot_usage': {'description': {'multivalued': False,
                                        'name': 'description',
                                        'required': True},
                        'url': {'multivalued': False, 'name': 'url'}}})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class DataEncoding(Aspect):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:DataEncoding',
         'comments': ['<p><em>Data Encoding</em> expresses the properties that specify '
                      'how data is represented at the bit and byte level. These '
                      'properties are applicable to describing raw '
                      'data.</p>^^rdf:HTML'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'slot_usage': {'bitOrder': {'multivalued': False,
                                     'name': 'bitOrder',
                                     'range': 'EndianType'},
                        'byteOrder': {'multivalued': False, 'name': 'byteOrder'},
                        'encoding': {'multivalued': False,
                                     'name': 'encoding',
                                     'range': 'Encoding'}}})

    pass


class DataItem(Concept):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:DataItem',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'slot_usage': {'value': {'multivalued': False,
                                  'name': 'value',
                                  'range': 'string'}}})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class Datatype(Concept):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'rdfs:Datatype',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'slot_usage': {'ansiSQLName': {'multivalued': False, 'name': 'ansiSQLName'},
                        'basis': {'multivalued': False,
                                  'name': 'basis',
                                  'range': 'Datatype'},
                        'bounded': {'multivalued': False, 'name': 'bounded'},
                        'cName': {'multivalued': False, 'name': 'cName'},
                        'cardinality': {'multivalued': False,
                                        'name': 'cardinality',
                                        'range': 'CardinalityType'},
                        'id': {'multivalued': False, 'name': 'id'},
                        'javaName': {'multivalued': False, 'name': 'javaName'},
                        'jsName': {'multivalued': False, 'name': 'jsName'},
                        'matlabName': {'multivalued': False, 'name': 'matlabName'},
                        'microsoftSQLServerName': {'multivalued': False,
                                                   'name': 'microsoftSQLServerName'},
                        'mySQLName': {'multivalued': False, 'name': 'mySQLName'},
                        'odbcName': {'multivalued': False, 'name': 'odbcName'},
                        'oleDBName': {'multivalued': False, 'name': 'oleDBName'},
                        'oracleSQLName': {'multivalued': False,
                                          'name': 'oracleSQLName'},
                        'orderedType': {'multivalued': False,
                                        'name': 'orderedType',
                                        'range': 'OrderedType'},
                        'protocolBuffersName': {'multivalued': False,
                                                'name': 'protocolBuffersName'},
                        'pythonName': {'multivalued': False, 'name': 'pythonName'},
                        'vbName': {'multivalued': False, 'name': 'vbName'}}})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class Discipline(Concept):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Discipline',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class Encoding(Concept):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Encoding',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'slot_usage': {'bits': {'multivalued': False, 'name': 'bits'},
                        'bytes': {'multivalued': False, 'name': 'bytes'}}})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class BitEncodingType(Encoding):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:BitEncodingType',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class BooleanEncodingType(Encoding):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:BooleanEncodingType',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class ByteEncodingType(Encoding):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:ByteEncodingType',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class CharEncodingType(Encoding):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:CharEncodingType',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class EnumeratedQuantity(Concept):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:EnumeratedQuantity',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'slot_usage': {'enumeratedValue': {'name': 'enumeratedValue',
                                            'range': 'EnumeratedValue'},
                        'enumeration': {'name': 'enumeration', 'range': 'Enumeration'}}})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class Enumeration(Concept):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Enumeration',
         'comments': ['<p>An enumeration is a set of literals from which a single '
                      'value is selected. Each literal can have a tag as an integer '
                      'within a standard encoding appropriate to the range of integer '
                      'values. Consistency of enumeration types will allow them, and '
                      'the enumerated values, to be referred to unambiguously either '
                      'through symbolic name or encoding. Enumerated values are also '
                      'controlled vocabularies and as such need to be standardized. '
                      'Without this consistency enumeration literals can be stated '
                      'differently and result in  data conflicts and '
                      'misinterpretations.</p>\n'
                      '\n'
                      '<p>The tags are a set of positive whole numbers, not '
                      'necessarily contiguous and having no numerical significance, '
                      'each corresponding to the associated literal identifier. An '
                      'order attribute can also be given on the enumeration elements. '
                      'An enumeration can itself be a member of an enumeration. This '
                      'allows enumerations to be enumerated in a selection. '
                      'Enumerations are also subclasses of <em>Scalar Datatype</em>. '
                      'This allows them to be used as the reference of a datatype '
                      'specification.</p>^^rdf:HTML'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'slot_usage': {'abbreviation': {'multivalued': False, 'name': 'abbreviation'},
                        'default': {'multivalued': False,
                                    'name': 'default',
                                    'range': 'EnumeratedValue'},
                        'element': {'name': 'element',
                                    'range': 'EnumeratedValue',
                                    'required': True}}})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class Figure(Concept):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Figure',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'slot_usage': {'figureCaption': {'multivalued': False,
                                          'name': 'figureCaption'},
                        'figureLabel': {'multivalued': False, 'name': 'figureLabel'},
                        'height': {'multivalued': False, 'name': 'height'},
                        'image': {'multivalued': False, 'name': 'image'},
                        'imageLocation': {'multivalued': False,
                                          'name': 'imageLocation',
                                          'required': True},
                        'landscape': {'multivalued': False, 'name': 'landscape'},
                        'width': {'multivalued': False, 'name': 'width'}}})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class FloatingPointEncodingType(Encoding):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:FloatingPointEncodingType',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class IntegerEncodingType(Encoding):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:IntegerEncodingType',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class MathsFunctionType(Concept):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:MathsFunctionType',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class NumericUnion(Concept):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:NumericUnion',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'mixins': ['Concept']})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class Organization(Concept):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Organization',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'slot_usage': {'url': {'name': 'url', 'required': False}}})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class Quantifiable(Aspect):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Quantifiable',
         'comments': ['<p><em>Quantifiable</em> ascribes to some thing the capability '
                      'of being measured, observed, or counted.</p>^^rdf:HTML'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'slot_usage': {'dataEncoding': {'multivalued': False,
                                         'name': 'dataEncoding',
                                         'range': 'DataEncoding'},
                        'datatype': {'multivalued': False,
                                     'name': 'datatype',
                                     'range': 'Datatype'},
                        'hasUnit': {'multivalued': False,
                                    'name': 'hasUnit',
                                    'range': 'Unit'},
                        'relativeStandardUncertainty': {'multivalued': False,
                                                        'name': 'relativeStandardUncertainty',
                                                        'range': 'double'},
                        'standardUncertainty': {'multivalued': False,
                                                'name': 'standardUncertainty',
                                                'range': 'decimal'},
                        'standardUncertaintySN': {'name': 'standardUncertaintySN',
                                                  'range': 'double'},
                        'value': {'multivalued': False, 'name': 'value'},
                        'valueSN': {'multivalued': False, 'name': 'valueSN'}}})

    pass


class Quantity(Quantifiable, Concept):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Quantity',
         'comments': ['<p class=\\"lm-para\\">A <b>quantity</b> is the measurement of '
                      'an observable property of a particular object, event, or '
                      'physical system. \n'
                      '  A quantity is always associated with the context of '
                      'measurement (i.e. the thing measured, the measured value, the '
                      'accuracy of measurement, etc.) whereas the \n'
                      '  underlying <b>quantity kind</b> is independent of any '
                      'particular measurement. Thus, length is a quantity kind while '
                      'the height of a rocket is a specific \n'
                      '  quantity of length; its magnitude that may be expressed in '
                      'meters, feet, inches, etc. Examples of physical quantities '
                      'include physical constants, such as \n'
                      "  the speed of light in a vacuum, Planck's constant, the "
                      'electric permittivity of free space, and the fine structure '
                      'constant. </p>\n'
                      '<p class=\\"lm-para\\">In other words, quantities are '
                      'quantifiable aspects of the world, such as the duration of a '
                      'movie, the distance between two points, \n'
                      'velocity of a car, the pressure of the atmosphere, and a '
                      "person's weight; and units are used to describe their numerical "
                      'measure.</p> \n'
                      '<p class=\\"lm-para\\">Many <b>quantity kinds</b> are related '
                      'to each other by various physical laws, and as a result, the '
                      'associated units of some quantity \n'
                      'kinds can be expressed as products (or ratios) of powers of '
                      'other quantity kinds (e.g., momentum is mass times velocity and '
                      'velocity is defined as distance \n'
                      'divided by time). In this way, some quantities can be '
                      'calculated from other measured quantities using their '
                      'associations to the quantity kinds in these \n'
                      'expressions. These quantity kind relationships are also '
                      'discussed in dimensional analysis. Those that cannot be so '
                      'expressed can be regarded \n'
                      'as \\"fundamental\\" in this sense.</p>\n'
                      '<p class=\\"lm-para\\">A quantity is distinguished from a '
                      '\\"quantity kind\\" in that the former carries a value and the '
                      'latter is a type specifier.</p>^^rdf:HTML'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'mixins': ['Concept'],
         'slot_usage': {'hasQuantityKind': {'name': 'hasQuantityKind',
                                            'range': 'QuantityKind',
                                            'required': False},
                        'isDeltaQuantity': {'name': 'isDeltaQuantity',
                                            'range': 'boolean'},
                        'quantityValue': {'name': 'quantityValue',
                                          'range': 'QuantityValue'}}})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class PhysicalConstant(Quantity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:PhysicalConstant',
         'comments': ['A physical constant is a physical quantity that is generally '
                      'believed to be both universal in nature and constant in time. '
                      'It can be contrasted with a mathematical constant, which is a '
                      'fixed numerical value but does not directly involve any '
                      'physical measurement. There are many physical constants in '
                      'science, some of the most widely recognized being the speed of '
                      "light in vacuum c, Newton's gravitational constant G, Planck's "
                      'constant h, the electric permittivity of free space ε0, and the '
                      'elementary charge e. Physical constants can take many '
                      'dimensional forms, or may be dimensionless depending on the '
                      'system of quantities and units used.^^rdf:HTML'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'slot_usage': {'altSymbol': {'name': 'altSymbol', 'required': False},
                        'applicableSystem': {'name': 'applicableSystem',
                                             'range': 'SystemOfUnits'},
                        'applicableUnit': {'name': 'applicableUnit', 'range': 'Unit'},
                        'dbpediaMatch': {'name': 'dbpediaMatch', 'range': 'uri'},
                        'exactConstant': {'name': 'exactConstant', 'range': 'boolean'},
                        'exactMatch': {'name': 'exactMatch',
                                       'range': 'PhysicalConstant'},
                        'hasDimensionVector': {'name': 'hasDimensionVector',
                                               'range': 'QuantityKindDimensionVector'},
                        'isoNormativeReference': {'name': 'isoNormativeReference',
                                                  'required': False},
                        'latexDefinition': {'multivalued': False,
                                            'name': 'latexDefinition'},
                        'latexSymbol': {'name': 'latexSymbol', 'required': False},
                        'mathMLdefinition': {'multivalued': False,
                                             'name': 'mathMLdefinition'},
                        'normativeReference': {'name': 'normativeReference',
                                               'required': False},
                        'symbol': {'name': 'symbol', 'required': False},
                        'ucumCode': {'name': 'ucumCode', 'required': False}}})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class QuantityKindDimensionVector(Concept):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:QuantityKindDimensionVector',
         'comments': ['<p class=\\"lm-para\\">A  <em>Quantity Kind Dimension '
                      'Vector</em> describes the dimensionality of a quantity kind in '
                      'the context of a system of units. In the SI system of units, '
                      'the dimensions of a quantity kind are expressed as a product of '
                      'the basic physical dimensions mass ($M$), length ($L$), time '
                      '($T$) current ($I$), amount of substance ($N$), luminous '
                      'intensity ($J$) and absolute temperature ($\\\\theta$) as $dim '
                      '\\\\, Q = L^{\\\\alpha} \\\\, M^{\\\\beta} \\\\, T^{\\\\gamma} '
                      '\\\\, I ^{\\\\delta} \\\\, \\\\theta ^{\\\\epsilon} \\\\, '
                      'N^{\\\\eta} \\\\, J ^{\\\\nu}$.</p>\n'
                      '\n'
                      '<p class=\\"lm-para\\">The rational powers of the dimensional '
                      'exponents, $\\\\alpha, \\\\, \\\\beta, \\\\, \\\\gamma, \\\\, '
                      '\\\\delta, \\\\, \\\\epsilon, \\\\, \\\\eta, \\\\, \\\\nu$, are '
                      'positive, negative, or zero.</p>\n'
                      '\n'
                      '<p class=\\"lm-para\\">For example, the dimension of the '
                      'physical quantity kind $\\\\it{speed}$ is '
                      '$\\\\boxed{length/time}$, $L/T$ or $LT^{-1}$, and the dimension '
                      'of the physical quantity kind force is $\\\\boxed{mass '
                      '\\\\times acceleration}$ or $\\\\boxed{mass \\\\times '
                      '(length/time)/time}$, $ML/T^2$ or $MLT^{-2}$ '
                      'respectively.</p>^^rdf:HTML'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'slot_usage': {'dimensionExponentForAmountOfSubstance': {'multivalued': False,
                                                                  'name': 'dimensionExponentForAmountOfSubstance',
                                                                  'required': True},
                        'dimensionExponentForElectricCurrent': {'multivalued': False,
                                                                'name': 'dimensionExponentForElectricCurrent',
                                                                'required': True},
                        'dimensionExponentForLength': {'multivalued': False,
                                                       'name': 'dimensionExponentForLength',
                                                       'required': True},
                        'dimensionExponentForLuminousIntensity': {'multivalued': False,
                                                                  'name': 'dimensionExponentForLuminousIntensity',
                                                                  'required': True},
                        'dimensionExponentForMass': {'multivalued': False,
                                                     'name': 'dimensionExponentForMass',
                                                     'required': True},
                        'dimensionExponentForThermodynamicTemperature': {'multivalued': False,
                                                                         'name': 'dimensionExponentForThermodynamicTemperature',
                                                                         'required': True},
                        'dimensionExponentForTime': {'multivalued': False,
                                                     'name': 'dimensionExponentForTime',
                                                     'required': True},
                        'dimensionlessExponent': {'multivalued': False,
                                                  'name': 'dimensionlessExponent',
                                                  'required': True},
                        'hasReferenceQuantityKind': {'name': 'hasReferenceQuantityKind',
                                                     'range': 'QuantityKind'},
                        'latexDefinition': {'multivalued': False,
                                            'name': 'latexDefinition'},
                        'latexSymbol': {'name': 'latexSymbol', 'required': False}}})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class QuantityKindDimensionVectorCGS(QuantityKindDimensionVector):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:QuantityKindDimensionVector_CGS',
         'comments': ['A <em>CGS Dimension Vector</em> is used to specify the '
                      'dimensions for a C.G.S. quantity kind.^^rdf:HTML'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class QuantityKindDimensionVectorCGS-EMU(QuantityKindDimensionVectorCGS):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:QuantityKindDimensionVector_CGS-EMU',
         'comments': ['A <em>CGS EMU Dimension Vector</em> is used to specify the '
                      'dimensions for EMU C.G.S. quantity kind.^^rdf:HTML'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class QuantityKindDimensionVectorCGS-ESU(QuantityKindDimensionVectorCGS):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:QuantityKindDimensionVector_CGS-ESU',
         'comments': ['A <em>CGS ESU Dimension Vector</em> is used to specify the '
                      'dimensions for ESU C.G.S. quantity kind.^^rdf:HTML'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class QuantityKindDimensionVectorCGS-GAUSS(QuantityKindDimensionVectorCGS):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:QuantityKindDimensionVector_CGS-GAUSS',
         'comments': ['A <em>CGS GAUSS Dimension Vector</em> is used to specify the '
                      'dimensions for Gaussioan C.G.S. quantity kind.^^rdf:HTML'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class QuantityKindDimensionVectorCGS-LH(QuantityKindDimensionVectorCGS):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:QuantityKindDimensionVector_CGS-LH',
         'comments': ['A <em>CGS LH Dimension Vector</em> is used to specify the '
                      'dimensions for Lorentz-Heaviside C.G.S. quantity '
                      'kind.^^rdf:HTML'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class QuantityKindDimensionVectorISO(QuantityKindDimensionVector):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:QuantityKindDimensionVector_ISO',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class QuantityKindDimensionVectorImperial(QuantityKindDimensionVector):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:QuantityKindDimensionVector_Imperial',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class QuantityKindDimensionVectorSI(QuantityKindDimensionVector):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:QuantityKindDimensionVector_SI',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class QuantityValue(Quantifiable, Concept):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:QuantityValue',
         'comments': ['A <i>Quantity Value</i> expresses the magnitude and kind of a '
                      'quantity and is given by the product of a numerical value '
                      '<code>n</code> and a unit of measure <code>U</code>. The number '
                      'multiplying the unit is referred to as the numerical value of '
                      'the quantity expressed in that unit. Refer to <a '
                      'href=\\"http://physics.nist.gov/Pubs/SP811/sec07.html\\">NIST '
                      'SP 811 section 7</a> for more on quantity values.^^rdf:HTML'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'mixins': ['Concept'],
         'slot_usage': {'hasUnit': {'multivalued': False, 'name': 'hasUnit'}}})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class ConstantValue(QuantityValue):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:ConstantValue',
         'comments': ['Used to specify the values of a constant.^^rdf:HTML'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'slot_usage': {'exactConstant': {'name': 'exactConstant', 'required': False}}})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class ScalarDatatype(Datatype):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:ScalarDatatype',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'slot_usage': {'bits': {'multivalued': False, 'name': 'bits'},
                        'bytes': {'multivalued': False, 'name': 'bytes'},
                        'length': {'multivalued': False, 'name': 'length'},
                        'maxExclusive': {'multivalued': False, 'name': 'maxExclusive'},
                        'maxInclusive': {'multivalued': False, 'name': 'maxInclusive'},
                        'minExclusive': {'multivalued': False, 'name': 'minExclusive'},
                        'minInclusive': {'multivalued': False, 'name': 'minInclusive'},
                        'rdfsDatatype': {'multivalued': False,
                                         'name': 'rdfsDatatype',
                                         'range': 'Datatype'}}})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class Scale(Concept):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Scale',
         'comments': ['Scales (also called \\"scales of measurement\\" or \\"levels of '
                      'measurement\\")  are expressions that typically refer to the '
                      'theory of scale types.^^rdf:HTML'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'slot_usage': {'dataStructure': {'multivalued': False,
                                          'name': 'dataStructure'},
                        'permissibleMaths': {'name': 'permissibleMaths',
                                             'range': 'MathsFunctionType'},
                        'permissibleTransformation': {'name': 'permissibleTransformation',
                                                      'range': 'TransformType'},
                        'scaleType': {'multivalued': False,
                                      'name': 'scaleType',
                                      'range': 'ScaleType'}}})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class EnumerationScale(Scale, Enumeration):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:EnumerationScale',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'mixins': ['Enumeration']})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class IntervalScale(Scale):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:IntervalScale',
         'comments': ['<p>The interval type allows for the degree of difference '
                      'between items, but not the ratio between them. Examples include '
                      'temperature with the Celsius scale, which has two defined '
                      'points (the freezing and boiling point of water at specific '
                      'conditions) and then separated into 100 intervals, date when '
                      'measured from an arbitrary epoch (such as AD), percentage such '
                      'as a percentage return on a stock,[16] location in Cartesian '
                      'coordinates, and direction measured in degrees from true or '
                      'magnetic north. Ratios are not meaningful since 20 °C cannot be '
                      'said to be \\"twice as hot\\" as 10 °C, nor can '
                      'multiplication/division be carried out between any two dates '
                      'directly. However, ratios of differences can be expressed; for '
                      'example, one difference can be twice another. Interval type '
                      'variables are sometimes also called \\"scaled variables\\", but '
                      'the formal mathematical term is an affine space (in this case '
                      'an affine line).</p>\n'
                      '<p>Characteristics: median, percentile &amp; Monotonic '
                      'increasing (order (&lt;) &amp; totally ordered '
                      'set</p>^^rdf:HTML',
                      'median, percentile & Monotonic increasing (order (<)) & totally '
                      'ordered set^^rdf:HTML'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class NominalScale(Scale):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:NominalScale',
         'comments': ['A nominal scale differentiates between items or subjects based '
                      'only on their names or (meta-)categories and other qualitative '
                      'classifications they belong to; thus dichotomous data involves '
                      'the construction of classifications as well as the '
                      'classification of items. Discovery of an exception to a '
                      'classification can be viewed as progress. Numbers may be used '
                      'to represent the variables but the numbers do not have '
                      'numerical value or relationship: For example, a Globally unique '
                      'identifier. Examples of these classifications include gender, '
                      'nationality, ethnicity, language, genre, style, biological '
                      'species, and form. In a university one could also use hall of '
                      'affiliation as an example.^^rdf:HTML'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class OrdinalScale(Scale):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:OrdinalScale',
         'comments': ['The ordinal type allows for rank order (1st, 2nd, 3rd, etc.) by '
                      'which data can be sorted, but still does not allow for relative '
                      'degree of difference between them. Examples include, on one '
                      'hand, dichotomous data with dichotomous (or dichotomized) '
                      "values such as 'sick' vs. 'healthy' when measuring health, "
                      "'guilty' vs. 'innocent' when making judgments in courts, "
                      "'wrong/false' vs. 'right/true' when measuring truth value, and, "
                      'on the other hand, non-dichotomous data consisting of a '
                      "spectrum of values, such as 'completely agree', 'mostly agree', "
                      "'mostly disagree', 'completely disagree' when measuring "
                      'opinion.^^rdf:HTML'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'slot_usage': {'order': {'multivalued': False,
                                  'name': 'order',
                                  'required': True}}})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class RatioScale(Scale):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:RatioScale',
         'comments': ['The ratio type takes its name from the fact that measurement is '
                      'the estimation of the ratio between a magnitude of a continuous '
                      'quantity and a unit magnitude of the same kind (Michell, 1997, '
                      '1999). A ratio scale possesses a meaningful (unique and '
                      'non-arbitrary) zero value. Most measurement in the physical '
                      'sciences and engineering is done on ratio scales. Examples '
                      'include mass, length, duration, plane angle, energy and '
                      'electric charge. In contrast to interval scales, ratios are now '
                      'meaningful because having a non-arbitrary zero point makes it '
                      'meaningful to say, for example, that one object has \\"twice '
                      'the length\\" of another (= is \\"twice as long\\"). Very '
                      'informally, many ratio scales can be described as specifying '
                      '\\"how much\\" of something (i.e. an amount or magnitude) or '
                      '\\"how many\\" (a count). The Kelvin temperature scale is a '
                      'ratio scale because it has a unique, non-arbitrary zero point '
                      'called absolute zero.^^rdf:HTML'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class SignednessType(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:SignednessType',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    pass


class Statement(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'rdf:Statement',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    pass


class StringEncodingType(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:StringEncodingType',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    pass


class DateTimeStringEncodingType(StringEncodingType):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:DateTimeStringEncodingType',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'slot_usage': {'allowedPattern': {'name': 'allowedPattern', 'required': True}}})

    pass


class Symbol(Concept):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Symbol', 'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class SymmetricRelation(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:SymmetricRelation',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    pass


class SystemOfQuantityKinds(Concept):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:SystemOfQuantityKinds',
         'comments': ['A system of quantity kinds is a set of one or more quantity '
                      'kinds together with a set of zero or more algebraic equations '
                      'that define relationships between quantity kinds in the set. In '
                      'the physical sciences, the equations relating quantity kinds '
                      'are typically physical laws and definitional relations, and '
                      'constants of proportionality. Examples include Newton’s First '
                      'Law of Motion, Coulomb’s Law, and the definition of velocity as '
                      'the instantaneous change in position.  In almost all cases, the '
                      'system identifies a subset of base quantity kinds. The base set '
                      'is chosen so that all other quantity kinds of interest can be '
                      'derived from the base quantity kinds and the algebraic '
                      'equations. If the unit system is explicitly associated with a '
                      'quantity kind system, then the unit system must define at least '
                      'one unit for each quantity kind.  From a scientific point of '
                      'view, the division of quantities into base quantities and '
                      'derived quantities is a matter of convention.^^rdf:HTML'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'slot_usage': {'baseDimensionEnumeration': {'multivalued': False,
                                                     'name': 'baseDimensionEnumeration',
                                                     'range': 'Enumeration'},
                        'hasBaseQuantityKind': {'name': 'hasBaseQuantityKind',
                                                'range': 'QuantityKind'},
                        'hasQuantityKind': {'name': 'hasQuantityKind',
                                            'range': 'QuantityKind',
                                            'required': False},
                        'hasUnitSystem': {'name': 'hasUnitSystem',
                                          'range': 'SystemOfUnits'},
                        'systemDerivedQuantityKind': {'name': 'systemDerivedQuantityKind',
                                                      'range': 'QuantityKind'}}})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class UserQuantityKind(AbstractQuantityKind):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:UserQuantityKind',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'slot_usage': {'hasQuantityKind': {'multivalued': False,
                                            'name': 'hasQuantityKind',
                                            'range': 'QuantityKind',
                                            'required': True}}})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class Verifiable(Aspect, Error3, Error2):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Verifiable',
         'comments': ['An aspect class that holds properties that provide external '
                      'knowledge and specifications of a given resource.'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'mixins': ['Error2', 'Aspect'],
         'slot_usage': {'isoNormativeReference': {'name': 'isoNormativeReference',
                                                  'required': False},
                        'normativeReference': {'name': 'normativeReference',
                                               'required': False}}})

    pass


class Comment(Verifiable, Thing):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Comment',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'mixins': ['Thing'],
         'slot_usage': {'description': {'multivalued': False, 'name': 'description'},
                        'rationale': {'name': 'rationale', 'required': False}}})

    pass


class EnumeratedValue(Verifiable, Concept):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:EnumeratedValue',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'mixins': ['Concept'],
         'slot_usage': {'abbreviation': {'multivalued': False, 'name': 'abbreviation'},
                        'altSymbol': {'name': 'altSymbol', 'required': False},
                        'description': {'multivalued': False, 'name': 'description'},
                        'symbol': {'multivalued': False, 'name': 'symbol'}}})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class CardinalityType(EnumeratedValue):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:CardinalityType',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'slot_usage': {'literal': {'multivalued': False, 'name': 'literal'}}})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class EndianType(EnumeratedValue):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:EndianType',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class NISTSP811Comment(Comment):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:NIST_SP811_Comment',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    pass


class OrderedType(EnumeratedValue):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:OrderedType',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'slot_usage': {'literal': {'multivalued': False, 'name': 'literal'}}})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class Prefix(Verifiable, Concept):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Prefix',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'mixins': ['Concept'],
         'slot_usage': {'altSymbol': {'name': 'altSymbol', 'required': False},
                        'exactMatch': {'name': 'exactMatch', 'range': 'Prefix'},
                        'latexSymbol': {'name': 'latexSymbol', 'required': False},
                        'prefixMultiplier': {'multivalued': False,
                                             'name': 'prefixMultiplier'},
                        'symbol': {'name': 'symbol', 'required': False},
                        'ucumCode': {'name': 'ucumCode', 'range': 'UCUMcs-term'}}})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class BinaryPrefix(Prefix):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:BinaryPrefix',
         'comments': ['A <em>Binary Prefix</em> is a prefix for multiples of units in '
                      'data processing, data transmission, and digital information, '
                      'notably the bit and the byte, to indicate multiplication by a '
                      'power of 2.'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class DecimalPrefix(Prefix):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:DecimalPrefix',
         'comments': ['A <em>Decimal Prefix</em> is a prefix for multiples of units '
                      'that are powers of 10.'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class QuantityKind(Verifiable, AbstractQuantityKind):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:QuantityKind',
         'comments': ['A <b>Quantity Kind</b> is any observable property that can be  '
                      'measured and quantified numerically. Familiar examples include '
                      'physical properties such as length, mass, time, force, energy, '
                      'power, electric charge, etc. Less familiar examples include '
                      'currency, interest rate, price to earning ratio, and '
                      'information capacity.^^rdf:HTML'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'mixins': ['AbstractQuantityKind'],
         'slot_usage': {'applicableCGSUnit': {'name': 'applicableCGSUnit',
                                              'required': False},
                        'applicableISOUnit': {'name': 'applicableISOUnit',
                                              'required': False},
                        'applicableImperialUnit': {'name': 'applicableImperialUnit',
                                                   'required': False},
                        'applicableSIUnit': {'name': 'applicableSIUnit',
                                             'required': False},
                        'applicableUSCustomaryUnit': {'name': 'applicableUSCustomaryUnit',
                                                      'required': False},
                        'applicableUnit': {'name': 'applicableUnit', 'required': False},
                        'dimensionVectorForSI': {'multivalued': False,
                                                 'name': 'dimensionVectorForSI',
                                                 'range': 'QuantityKindDimensionVector_SI'},
                        'exactMatch': {'name': 'exactMatch', 'range': 'QuantityKind'},
                        'hasDimensionVector': {'name': 'hasDimensionVector',
                                               'range': 'QuantityKindDimensionVector'},
                        'iec61360Code': {'name': 'iec61360Code', 'range': 'string'},
                        'latexDefinition': {'multivalued': False,
                                            'name': 'latexDefinition'},
                        'mathMLdefinition': {'multivalued': False,
                                             'name': 'mathMLdefinition'},
                        'qkdvDenominator': {'multivalued': False,
                                            'name': 'qkdvDenominator'},
                        'qkdvNumerator': {'multivalued': False,
                                          'name': 'qkdvNumerator'}}})

    belongsToSystemOfQuantities: Optional[list[SystemOfQuantityKinds]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind'], 'slot_uri': 'qudt:belongsToSystemOfQuantities'} })
    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class QuantityType(EnumeratedValue):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:QuantityType',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'slot_usage': {'value': {'name': 'value', 'range': 'QuantityKind'}}})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class Rule(Verifiable, Concept):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Rule',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'mixins': ['Concept'],
         'slot_usage': {'rationale': {'name': 'rationale', 'required': False},
                        'ruleType': {'name': 'ruleType', 'range': 'RuleType'}}})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class RuleType(EnumeratedValue):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:RuleType',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class ScaleType(EnumeratedValue):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:ScaleType',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'slot_usage': {'dataStructure': {'multivalued': False,
                                          'name': 'dataStructure'},
                        'permissibleMaths': {'name': 'permissibleMaths',
                                             'range': 'MathsFunctionType'},
                        'permissibleTransformation': {'name': 'permissibleTransformation',
                                                      'range': 'TransformType'}}})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class SystemOfUnits(Verifiable, Concept):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:SystemOfUnits',
         'comments': ['A system of units is a set of units which are chosen as the '
                      'reference scales for some set of quantity kinds together with '
                      'the definitions of each unit. Units may be defined by '
                      'experimental observation or by proportion to another unit not '
                      'included in the system. If the unit system is explicitly '
                      'associated with a quantity kind system, then the unit system '
                      'must define at least one unit for each quantity '
                      'kind.^^rdf:HTML'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'mixins': ['Concept'],
         'slot_usage': {'applicablePhysicalConstant': {'name': 'applicablePhysicalConstant',
                                                       'range': 'PhysicalConstant'},
                        'hasAllowedUnit': {'name': 'hasAllowedUnit', 'range': 'Unit'},
                        'hasBaseUnit': {'name': 'hasBaseUnit', 'range': 'Unit'},
                        'hasCoherentUnit': {'name': 'hasCoherentUnit', 'range': 'Unit'},
                        'hasDefinedUnit': {'name': 'hasDefinedUnit', 'range': 'Unit'},
                        'hasDerivedCoherentUnit': {'name': 'hasDerivedCoherentUnit',
                                                   'range': 'Unit'},
                        'hasDerivedUnit': {'name': 'hasDerivedUnit', 'range': 'Unit'},
                        'hasUnit': {'name': 'hasUnit', 'range': 'Unit'},
                        'prefix': {'name': 'prefix', 'range': 'Prefix'}}})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class TransformType(EnumeratedValue):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:TransformType',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class Unit(Verifiable, Concept):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Unit',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'mixins': ['Concept'],
         'slot_usage': {'altSymbol': {'name': 'altSymbol', 'required': False},
                        'applicableSystem': {'name': 'applicableSystem',
                                             'range': 'SystemOfUnits'},
                        'conversionMultiplier': {'multivalued': False,
                                                 'name': 'conversionMultiplier'},
                        'conversionMultiplierSN': {'multivalued': False,
                                                   'name': 'conversionMultiplierSN'},
                        'conversionOffset': {'multivalued': False,
                                             'name': 'conversionOffset'},
                        'conversionOffsetSN': {'multivalued': False,
                                               'name': 'conversionOffsetSN'},
                        'definedUnitOfSystem': {'name': 'definedUnitOfSystem',
                                                'range': 'SystemOfUnits'},
                        'derivedCoherentUnitOfSystem': {'name': 'derivedCoherentUnitOfSystem',
                                                        'range': 'SystemOfUnits'},
                        'derivedUnitOfSystem': {'name': 'derivedUnitOfSystem',
                                                'range': 'SystemOfUnits'},
                        'exactMatch': {'name': 'exactMatch', 'range': 'Unit'},
                        'factorUnitScalar': {'multivalued': False,
                                             'name': 'factorUnitScalar'},
                        'hasDimensionVector': {'multivalued': False,
                                               'name': 'hasDimensionVector',
                                               'range': 'QuantityKindDimensionVector'},
                        'hasFactorUnit': {'name': 'hasFactorUnit', 'range': 'Class'},
                        'hasQuantityKind': {'name': 'hasQuantityKind',
                                            'range': 'QuantityKind'},
                        'iec61360Code': {'name': 'iec61360Code', 'range': 'string'},
                        'latexDefinition': {'name': 'latexDefinition',
                                            'required': False},
                        'latexSymbol': {'name': 'latexSymbol', 'required': False},
                        'mathMLdefinition': {'multivalued': False,
                                             'name': 'mathMLdefinition'},
                        'prefix': {'name': 'prefix', 'range': 'Prefix'},
                        'qkdvDenominator': {'multivalued': False,
                                            'name': 'qkdvDenominator',
                                            'range': 'QuantityKindDimensionVector'},
                        'qkdvNumerator': {'multivalued': False,
                                          'name': 'qkdvNumerator',
                                          'range': 'QuantityKindDimensionVector'},
                        'scalingOf': {'name': 'scalingOf', 'range': 'Unit'},
                        'siUnitsExpression': {'name': 'siUnitsExpression',
                                              'required': False},
                        'symbol': {'name': 'symbol', 'required': False},
                        'ucumCode': {'name': 'ucumCode', 'range': 'UCUMcs'},
                        'udunitsCode': {'name': 'udunitsCode', 'range': 'string'},
                        'uneceCommonCode': {'name': 'uneceCommonCode',
                                            'range': 'string'}}})

    hasReciprocalUnit: Optional[list[Unit]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:hasReciprocalUnit'} })
    isUnitOfSystem: Optional[list[SystemOfUnits]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:isUnitOfSystem'} })
    omUnit: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:omUnit'} })
    unitFor: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:unitFor'} })
    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class ContextualUnit(Unit):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:ContextualUnit',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'slot_usage': {'broader': {'name': 'broader', 'range': 'Unit'}}})

    hasReciprocalUnit: Optional[list[Unit]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:hasReciprocalUnit'} })
    isUnitOfSystem: Optional[list[SystemOfUnits]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:isUnitOfSystem'} })
    omUnit: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:omUnit'} })
    unitFor: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:unitFor'} })
    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class DerivedUnit(Unit):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:DerivedUnit',
         'comments': ['A DerivedUnit is a type specification for units that are '
                      'derived from other units.^^rdf:HTML'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    hasReciprocalUnit: Optional[list[Unit]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:hasReciprocalUnit'} })
    isUnitOfSystem: Optional[list[SystemOfUnits]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:isUnitOfSystem'} })
    omUnit: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:omUnit'} })
    unitFor: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:unitFor'} })
    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class DimensionlessUnit(Unit):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:DimensionlessUnit',
         'comments': ['A Dimensionless Unit is a quantity for which all the exponents '
                      'of the factors corresponding to the base quantities in its '
                      'quantity dimension are zero.^^rdf:HTML'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    hasReciprocalUnit: Optional[list[Unit]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:hasReciprocalUnit'} })
    isUnitOfSystem: Optional[list[SystemOfUnits]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:isUnitOfSystem'} })
    omUnit: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:omUnit'} })
    unitFor: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:unitFor'} })
    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class AngleUnit(DimensionlessUnit):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:AngleUnit',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    hasReciprocalUnit: Optional[list[Unit]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:hasReciprocalUnit'} })
    isUnitOfSystem: Optional[list[SystemOfUnits]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:isUnitOfSystem'} })
    omUnit: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:omUnit'} })
    unitFor: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:unitFor'} })
    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class CountingUnit(DimensionlessUnit):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:CountingUnit',
         'comments': ['Used for all units that express counts. Examples are Atomic '
                      'Number, Number, Number per Year, Percent and Sample per '
                      'Second.^^rdf:HTML'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    hasReciprocalUnit: Optional[list[Unit]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:hasReciprocalUnit'} })
    isUnitOfSystem: Optional[list[SystemOfUnits]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:isUnitOfSystem'} })
    omUnit: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:omUnit'} })
    unitFor: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:unitFor'} })
    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class CurrencyUnit(DimensionlessUnit):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:CurrencyUnit',
         'comments': ['Currency Units have their own subclass of unit because: (a) '
                      "they have additonal properites such as 'country' and (b) their "
                      'URIs do not conform to the same rules as other units.^^rdf:HTML',
                      'Used for all units that express currency.^^rdf:HTML'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt',
         'slot_usage': {'currencyCode': {'multivalued': False, 'name': 'currencyCode'},
                        'currencyExponent': {'multivalued': False,
                                             'name': 'currencyExponent'}}})

    hasReciprocalUnit: Optional[list[Unit]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:hasReciprocalUnit'} })
    isUnitOfSystem: Optional[list[SystemOfUnits]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:isUnitOfSystem'} })
    omUnit: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:omUnit'} })
    unitFor: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:unitFor'} })
    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class LogarithmicUnit(DimensionlessUnit):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:LogarithmicUnit',
         'comments': ['Logarithmic units are abstract mathematical units that can be '
                      'used to express any quantities (physical or mathematical) that '
                      'are defined on a logarithmic scale, that is, as being '
                      'proportional to the value of a logarithm function. Examples of '
                      'logarithmic units include common units of information and '
                      'entropy, such as the bit, and the byte, as well as units of '
                      'relative signal strength magnitude such as the '
                      'decibel.^^rdf:HTML'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    hasReciprocalUnit: Optional[list[Unit]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:hasReciprocalUnit'} })
    isUnitOfSystem: Optional[list[SystemOfUnits]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:isUnitOfSystem'} })
    omUnit: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:omUnit'} })
    unitFor: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:unitFor'} })
    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class PlaneAngleUnit(AngleUnit):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:PlaneAngleUnit',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    hasReciprocalUnit: Optional[list[Unit]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:hasReciprocalUnit'} })
    isUnitOfSystem: Optional[list[SystemOfUnits]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:isUnitOfSystem'} })
    omUnit: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:omUnit'} })
    unitFor: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:unitFor'} })
    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class SolidAngleUnit(AngleUnit):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:SolidAngleUnit',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    hasReciprocalUnit: Optional[list[Unit]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:hasReciprocalUnit'} })
    isUnitOfSystem: Optional[list[SystemOfUnits]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:isUnitOfSystem'} })
    omUnit: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:omUnit'} })
    unitFor: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:unitFor'} })
    guidance: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class CatalogEntry(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'vaem:CatalogEntry',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    pass


class List(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'rdf:List', 'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    pass


class Class(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'owl:Class', 'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    pass


class AspectClass(Class):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:AspectClass',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    pass


class Resource(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'rdfs:Resource',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    pass


class GDay(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'xsd:gDay', 'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    pass


class GMonth(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'xsd:gMonth', 'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    pass


class GMonthDay(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'xsd:gMonthDay',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    pass


class GYear(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'xsd:gYear', 'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    pass


class GYearMonth(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'xsd:gYearMonth',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    pass


class Ontology(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'owl:Ontology',
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    pass


class LatexString(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:LatexString',
         'comments': ['A type of string in which some characters may be wrapped with '
                      "'$' and '$ characters for LaTeX rendering."],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    pass


class UCUMcs(Resource):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Lexical pattern for the case-sensitive version of UCUM code'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    pass


class UCUMcs-term(Resource):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Lexical pattern for the terminal symbols in the case-sensitive '
                      'version of UCUM code'],
         'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    pass


class ValueUnion(Resource):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://qudt.org/3.1.6/schema/qudt'})

    pass


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Thing.model_rebuild()
Error2.model_rebuild()
Error3.model_rebuild()
Aspect.model_rebuild()
Concept.model_rebuild()
AbstractQuantityKind.model_rebuild()
BaseDimensionMagnitude.model_rebuild()
Citation.model_rebuild()
DataEncoding.model_rebuild()
DataItem.model_rebuild()
Datatype.model_rebuild()
Discipline.model_rebuild()
Encoding.model_rebuild()
BitEncodingType.model_rebuild()
BooleanEncodingType.model_rebuild()
ByteEncodingType.model_rebuild()
CharEncodingType.model_rebuild()
EnumeratedQuantity.model_rebuild()
Enumeration.model_rebuild()
Figure.model_rebuild()
FloatingPointEncodingType.model_rebuild()
IntegerEncodingType.model_rebuild()
MathsFunctionType.model_rebuild()
NumericUnion.model_rebuild()
Organization.model_rebuild()
Quantifiable.model_rebuild()
Quantity.model_rebuild()
PhysicalConstant.model_rebuild()
QuantityKindDimensionVector.model_rebuild()
QuantityKindDimensionVectorCGS.model_rebuild()
QuantityKindDimensionVectorCGS-EMU.model_rebuild()
QuantityKindDimensionVectorCGS-ESU.model_rebuild()
QuantityKindDimensionVectorCGS-GAUSS.model_rebuild()
QuantityKindDimensionVectorCGS-LH.model_rebuild()
QuantityKindDimensionVectorISO.model_rebuild()
QuantityKindDimensionVectorImperial.model_rebuild()
QuantityKindDimensionVectorSI.model_rebuild()
QuantityValue.model_rebuild()
ConstantValue.model_rebuild()
ScalarDatatype.model_rebuild()
Scale.model_rebuild()
EnumerationScale.model_rebuild()
IntervalScale.model_rebuild()
NominalScale.model_rebuild()
OrdinalScale.model_rebuild()
RatioScale.model_rebuild()
SignednessType.model_rebuild()
Statement.model_rebuild()
StringEncodingType.model_rebuild()
DateTimeStringEncodingType.model_rebuild()
Symbol.model_rebuild()
SymmetricRelation.model_rebuild()
SystemOfQuantityKinds.model_rebuild()
UserQuantityKind.model_rebuild()
Verifiable.model_rebuild()
Comment.model_rebuild()
EnumeratedValue.model_rebuild()
CardinalityType.model_rebuild()
EndianType.model_rebuild()
NISTSP811Comment.model_rebuild()
OrderedType.model_rebuild()
Prefix.model_rebuild()
BinaryPrefix.model_rebuild()
DecimalPrefix.model_rebuild()
QuantityKind.model_rebuild()
QuantityType.model_rebuild()
Rule.model_rebuild()
RuleType.model_rebuild()
ScaleType.model_rebuild()
SystemOfUnits.model_rebuild()
TransformType.model_rebuild()
Unit.model_rebuild()
ContextualUnit.model_rebuild()
DerivedUnit.model_rebuild()
DimensionlessUnit.model_rebuild()
AngleUnit.model_rebuild()
CountingUnit.model_rebuild()
CurrencyUnit.model_rebuild()
LogarithmicUnit.model_rebuild()
PlaneAngleUnit.model_rebuild()
SolidAngleUnit.model_rebuild()
CatalogEntry.model_rebuild()
List.model_rebuild()
Class.model_rebuild()
AspectClass.model_rebuild()
Resource.model_rebuild()
GDay.model_rebuild()
GMonth.model_rebuild()
GMonthDay.model_rebuild()
GYear.model_rebuild()
GYearMonth.model_rebuild()
Ontology.model_rebuild()
LatexString.model_rebuild()
UCUMcs.model_rebuild()
UCUMcs-term.model_rebuild()
ValueUnion.model_rebuild()
