"""CLI tool for patching LinkML QUDT schema."""

from pathlib import Path

import typer

from linkml_qudt.schema_patcher import patch_schema

app = typer.Typer()


@app.command()
def main(schema_file: Path) -> None:
    """Patch a LinkML QUDT schema file."""
    if not schema_file.exists():
        typer.echo(f"Error: {schema_file} does not exist", err=True)
        raise typer.Exit(1)

    patch_schema(schema_file)
    typer.echo(f"Patched {schema_file}")


if __name__ == "__main__":
    app()
