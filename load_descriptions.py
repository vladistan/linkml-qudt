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
    t = [(s,p,o) for s, p, o in g]
    return (t,)


@app.cell
def _(t):
    t[0:2]
    return


@app.cell
def _(g):
    q = g.query("""
    SELECT ?s ?o 
    WHERE {
      VALUES ?type { owl:ObjectProperty owl:DatatypeProperty }
      ?s dcterms:description ?o ;
         a ?type .
  
    }
    """)
    return (q,)


@app.cell
def _(q):
    descrs = {s.replace('http://qudt.org/schema/qudt/','') : o for s, o in q}
    return (descrs,)


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
    SCHEMA = 'src/linkml_qudt/schema/linkml_qudt.yaml'
    return (SCHEMA,)


@app.cell
def _(YAML):
    yaml = YAML()
    return (yaml,)


@app.cell
def _(SCHEMA, yaml):
    with open(SCHEMA, 'r') as file:
     content = yaml.load(file)
    return (content,)


@app.cell
def _(content):
    slots = content['slots']
    return (slots,)


@app.cell
def _(slots):
    slots['applicableSystem']['description'] = 'The system to which this quantity applies.'
    return


@app.cell
def _(descrs, slots):
    for slot, desc in descrs.items():
      if slot in slots:
        slots[slot]['description'] = str(desc)
    return


@app.cell
def _(SCHEMA, content, yaml):
    with open(SCHEMA, 'w') as ofile:
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
