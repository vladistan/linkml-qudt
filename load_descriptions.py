import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Load Descriptions
    """)
    return


@app.cell
def _():
    from rdflib import Graph

    return (Graph,)


@app.cell
def _(Graph):
    g = Graph()
    return (g,)


@app.cell
def _(g):
    with open("original/qudt.ttl", "rb") as f:
        g.parse(file=f, format="turtle")
    return


@app.cell
def _(g):
    t = [(s, p, o) for s, p, o in g]
    return (t,)


@app.cell
def _(t):
    t[0:2]
    return


@app.cell
def _(g):
    q = g.query("""
    SELECT ?s ?desc ?comment ?label
    WHERE {
      VALUES ?type { owl:ObjectProperty owl:DatatypeProperty owl:AnnotationProperty }
      ?s a ?type .
      OPTIONAL { ?s dcterms:description ?desc }
      OPTIONAL { ?s rdfs:comment ?comment }
      OPTIONAL { ?s rdfs:label ?label }
    }
    """)
    return (q,)


@app.cell
def _(q):
    [(p, d, c, l) for p, d, c, l in q if "atch" in str(p)]
    return


@app.cell
def _(q):
    def _build_descrs():
        def strip(uri):
            return str(uri).replace("http://qudt.org/schema/qudt/", "")

        result = {}
        for s, desc, comment, label in q:
            key = strip(s)
            if desc:
                result[key] = str(desc)
            elif comment and key not in result:
                result[key] = str(comment)
            elif label and key not in result:
                result[key] = str(label)
        return result

    descrs = _build_descrs()
    return (descrs,)


@app.cell
def _():
    # Query Classes
    return


@app.cell
def _(g):
    class_q = g.query("""
    SELECT ?s ?desc ?comment ?label
    WHERE {
      VALUES ?type { owl:Class rdfs:Datatype }
      ?s a ?type .
      OPTIONAL { ?s dcterms:description ?desc }
      OPTIONAL { ?s rdfs:comment ?comment }
      OPTIONAL { ?s rdfs:label ?label }
    }
    """)
    return (class_q,)


@app.cell
def _(class_q):
    def _build_class_descr():
        def strip(uri):
            return str(uri).replace("http://qudt.org/schema/qudt/", "")

        result = {}
        for s, desc, comment, label in class_q:
            key = strip(s)
            if desc:
                result[key] = str(desc)
            elif comment and key not in result:
                result[key] = str(comment)
            elif label and key not in result:
                result[key] = str(label)
        return result

    class_descr = _build_class_descr()
    return (class_descr,)


@app.cell
def _(class_descr):
    class_descr["LatexString"]
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Patch the Schema
    """)
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
    return (yaml,)


@app.cell
def _(SCHEMA, yaml):
    with open(SCHEMA, "r") as file:
        content = yaml.load(file)
    return (content,)


@app.cell
def _(content):
    slots = content["slots"]
    return (slots,)


@app.cell
def _(slots):
    slots["applicableSystem"]["description"] = (
        "The system to which this quantity applies."
    )
    return


@app.cell
def _(descrs, slots):
    for slot, desc in descrs.items():
        if slot in slots:
            slots[slot]["description"] = str(desc)
    return


@app.cell
def _(content):
    classes = content["classes"]
    return (classes,)


@app.cell
def _(class_descr, classes):
    for cls, clss_desc in class_descr.items():
        if cls in classes:
            classes[cls]["description"] = str(clss_desc)
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
