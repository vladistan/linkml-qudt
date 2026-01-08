"""Library module for patching LinkML QUDT schema."""

from pathlib import Path

from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap


def load_schema(path: Path) -> CommentedMap:
    yaml = YAML()
    with open(path) as f:
        return yaml.load(f)


def save_schema(content: CommentedMap, path: Path) -> None:
    yaml = YAML()
    with open(path, "w") as f:
        yaml.dump(content, f)


def fix_slot_ranges(content: CommentedMap) -> None:
    for slot in content["slots"].values():
        if slot.get("range") == "anyURI":
            slot["range"] = "uri"


def add_thing_class(content: CommentedMap) -> None:
    content["classes"]["Thing"] = {
        "description": "The root class for all QUDT concepts",
        "class_uri": "owl:Thing",
    }


def fix_slot_inheritance(content: CommentedMap) -> None:
    slots = content["slots"]

    # Remove problematic is_a
    for slot_name in ["literal", "ucumCode"]:
        if slot_name in slots and "is_a" in slots[slot_name]:
            del slots[slot_name]["is_a"]

    # Fix ranges
    slots["rationale"]["range"] = "string"
    slots["guidance"]["range"] = "string"

    # Fix hasDerivedCoherentUnit inheritance
    slots["hasDerivedCoherentUnit"]["is_a"] = "hasDerivedUnit"
    slots["hasDerivedCoherentUnit"]["mixins"] = ["hasCoherentUnit"]


def fix_class_inheritance(content: CommentedMap) -> None:
    classes = content["classes"]

    def set_is_a(class_name: str, parent: str) -> None:
        classes[class_name]["is_a"] = parent

    def set_slot_range(class_name: str, slot_name: str, range_type: str) -> None:
        classes[class_name]["slot_usage"][slot_name]["range"] = range_type

    def set_slot_required(class_name: str, slot_name: str, required: bool) -> None:
        classes[class_name]["slot_usage"][slot_name] = {"required": required}

    def set_mixins(class_name: str, mixins: list[str]) -> None:
        classes[class_name]["mixins"] = mixins

    # Remove problematic is_a
    for class_name in ["Statement", "NumericUnion"]:
        if class_name in classes and "is_a" in classes[class_name]:
            del classes[class_name]["is_a"]

    # Remove problematic mixins
    for class_name in ["Comment", "PhysicalConstant", "Verifiable", "Enumeration"]:
        if class_name in classes and "mixins" in classes[class_name]:
            del classes[class_name]["mixins"]

    # Fix class hierarchies
    set_is_a("Enumeration", "Concept")
    set_is_a("EnumerationScale", "Scale")
    set_is_a("Verifiable", "Aspect")
    set_mixins("EnumerationScale", ["Enumeration"])
    set_mixins("EnumeratedValue", ["Concept"])

    # Fix slot_usage ranges
    set_slot_range("BaseDimensionMagnitude", "vectorMagnitude", "float")
    set_slot_range("PhysicalConstant", "exactConstant", "boolean")
    set_slot_range("Quantifiable", "relativeStandardUncertainty", "double")
    set_slot_range("Quantifiable", "standardUncertainty", "decimal")
    set_slot_range("Quantifiable", "standardUncertaintySN", "double")
    set_slot_range("Quantity", "isDeltaQuantity", "boolean")

    # Fix required flags
    set_slot_required("Verifiable", "wikidataMatch", False)
    set_slot_required("Verifiable", "dbpediaMatch", False)


def fix_metadata(content: CommentedMap) -> None:
    content["version"] = "0.0.2"

    # Remove Error classes
    for class_name in ["Error1", "Error2", "Error3"]:
        if class_name in content["classes"]:
            del content["classes"][class_name]


def add_prefixes(content: CommentedMap) -> None:
    prefixes = content["prefixes"]
    prefixes["rdf"] = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    prefixes["owl"] = "http://www.w3.org/2002/07/owl#"
    prefixes["rdfs"] = "http://www.w3.org/2000/01/rdf-schema#"
    prefixes["dc"] = "http://purl.org/dc/elements/1.1/"
    prefixes["dcterms"] = "http://purl.org/dc/terms/"
    prefixes["prov"] = "http://www.w3.org/ns/prov#"
    prefixes["voag"] = "http://voag.linkedmodel.org/schema/voag#"
    prefixes["vaem"] = "http://www.linkedmodel.org/schema/vaem#"
    prefixes["dtype"] = "http://www.linkedmodel.org/schema/dtype#"


def reorder_keys(content: CommentedMap) -> CommentedMap:
    desired_order = [
        "id",
        "name",
        "title",
        "version",
        "description",
        "license",
        "imports",
        "prefixes",
        "default_curi_maps",
        "default_prefix",
        "default_range",
        "classes",
        "types",
        "enums",
        "slots",
    ]

    new_content = CommentedMap()
    for key in desired_order:
        if key in content:
            new_content[key] = content[key]
    # Add remaining keys
    for key in content:
        if key not in new_content:
            new_content[key] = content[key]
    return new_content


def patch_schema(path: Path) -> None:
    content = load_schema(path)

    fix_slot_ranges(content)
    add_thing_class(content)
    fix_slot_inheritance(content)
    fix_class_inheritance(content)
    fix_metadata(content)
    add_prefixes(content)
    content = reorder_keys(content)

    save_schema(content, path)
