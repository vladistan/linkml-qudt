import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _():
    from ruamel.yaml import YAML

    return (YAML,)


@app.cell
def _():
    SCHEMA = "src/linkml_qudt/schema/linkml_qudt.yaml"
    return (SCHEMA,)


@app.cell
def _(YAML):
    yaml = YAML()
    # yaml.indent(mapping=2, sequence=0, offset=2)
    return (yaml,)


@app.cell
def _(SCHEMA, yaml):
    with open(SCHEMA, "r") as file:
        content = yaml.load(file)
    return (content,)


@app.cell
def _(content):
    for slot in content["slots"].values():
        if slot.get("range") == "anyURI":
            slot["range"] = "uri"
    return


@app.cell
def _(content):
    content["classes"]["Thing"] = {
        "description": "The root class for all QUDT concepts",
        "class_uri": "owl:Thing",
    }
    return


@app.cell
def _(content):
    if "is_a" in content["slots"]["literal"]:
        del content["slots"]["literal"]["is_a"]
    if "is_a" in content["slots"]["ucumCode"]:
        del content["slots"]["ucumCode"]["is_a"]

    content["slots"]["rationale"]["range"] = "string"
    content["slots"]["guidance"]["range"] = "string"
    content["slots"]["hasDerivedCoherentUnit"]["is_a"] = "hasDerivedUnit"
    content["slots"]["hasDerivedCoherentUnit"]["mixins"] = ["hasCoherentUnit"]

    return


@app.cell
def _(content):
    if "is_a" in content["classes"]["Statement"]:
        del content["classes"]["Statement"]["is_a"]
    if "is_a" in content["classes"]["NumericUnion"]:
        del content["classes"]["NumericUnion"]["is_a"]

    if "mixins" in content["classes"]["Comment"]:
        del content["classes"]["Comment"]["mixins"]
    if "mixins" in content["classes"]["PhysicalConstant"]:
        del content["classes"]["PhysicalConstant"]["mixins"]
    if "mixins" in content["classes"]["Verifiable"]:
        del content["classes"]["Verifiable"]["mixins"]
    if "mixins" in content["classes"]["Enumeration"]:
        del content["classes"]["Enumeration"]["mixins"]

    content["classes"]["Enumeration"]["is_a"] = "Concept"
    content["classes"]["EnumerationScale"]["is_a"] = "Scale"
    content["classes"]["EnumerationScale"]["mixins"] = ["Enumeration"]
    content["classes"]["Verifiable"]["is_a"] = "Aspect"
    content["classes"]["EnumeratedValue"]["mixins"] = ["Concept"]
    content["classes"]["BaseDimensionMagnitude"]["slot_usage"]["vectorMagnitude"][
        "range"
    ] = "float"
    content["classes"]["PhysicalConstant"]["slot_usage"]["exactConstant"]["range"] = (
        "boolean"
    )

    content["classes"]["Quantifiable"]["slot_usage"]["relativeStandardUncertainty"][
        "range"
    ] = "double"
    content["classes"]["Quantifiable"]["slot_usage"]["standardUncertainty"]["range"] = (
        "decimal"
    )
    content["classes"]["Quantifiable"]["slot_usage"]["standardUncertaintySN"][
        "range"
    ] = "double"
    content["classes"]["Quantity"]["slot_usage"]["isDeltaQuantity"]["range"] = "boolean"

    content["classes"]["Verifiable"]["slot_usage"]["wikidataMatch"] = {
        "required": False
    }
    content["classes"]["Verifiable"]["slot_usage"]["dbpediaMatch"] = {"required": False}

    return


@app.cell
def _():
    return


@app.cell
def _(content):
    content["version"] = "0.0.2"
    content["title"] = "QUDT Ontology in LinkML"
    content["description"] = (
        "This is a LinkML representation of the QUDT (Quantities, Units, Dimensions and Types) ontology. QUDT provides a comprehensive vocabulary for describing physical quantities, units of measure, and their relationships in a machine-readable format."
    )
    content["license"] = "CC-BY-4.0"

    if "Error1" in content["classes"]:
        del content["classes"]["Error1"]
    if "Error1" in content["classes"]:
        del content["classes"]["Error2"]
    if "Error1" in content["classes"]:
        del content["classes"]["Error3"]
    return


@app.cell
def _(content):
    content["prefixes"]["rdf"] = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    content["prefixes"]["owl"] = "http://www.w3.org/2002/07/owl#"
    content["prefixes"]["rdfs"] = "http://www.w3.org/2000/01/rdf-schema#"
    content["prefixes"]["dc"] = "http://purl.org/dc/elements/1.1/"
    content["prefixes"]["dcterms"] = "http://purl.org/dc/terms/"
    content["prefixes"]["prov"] = "http://www.w3.org/ns/prov#"
    content["prefixes"]["voag"] = "http://voag.linkedmodel.org/schema/voag#"
    content["prefixes"]["vaem"] = "http://www.linkedmodel.org/schema/vaem#"
    content["prefixes"]["dtype"] = "http://www.linkedmodel.org/schema/dtype#"
    return


@app.cell
def _(content):
    content.move_to_end("imports")
    content.move_to_end("prefixes")
    content.move_to_end("default_prefix")
    content.move_to_end("classes")
    content.move_to_end("slots")

    content["classes"].move_to_end("Thing", last=False)
    return


@app.cell
def _(SCHEMA, content, yaml):
    with open(SCHEMA, "w") as ofile:
        yaml.dump(content, ofile)
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
