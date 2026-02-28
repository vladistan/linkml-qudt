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
    # QUDT Schema Subsetting Tool

    This notebook allows you to extract a subset of the QUDT schema by selecting
    specific classes. It will recursively include all dependencies:

    - Parent classes (via `is_a`)
    - Mixin classes
    - Slots used by the classes
    - Types/Enums referenced as slot ranges
    - Classes referenced as slot ranges (recursively)

    The export process automatically handles common conflicts:
    - Removes standard LinkML types (already provided by `linkml:types`)
    - Removes/renames classes that conflict with OWL/RDFS base classes
    - Renames slots that commonly conflict (description, id, value)
    - Fixes dangling references to removed classes
    - Converts prefixes to simple format for compatibility
    """)
    return


@app.cell
def _():
    from linkml_runtime.utils.schemaview import SchemaView
    from linkml_runtime.dumpers import yaml_dumper
    from linkml_runtime.linkml_model import SchemaDefinition
    from pathlib import Path
    import copy
    import re

    return Path, SchemaDefinition, SchemaView, yaml_dumper, copy, re


@app.cell
def _(Path):
    SCHEMA_PATH = Path("src/linkml_qudt/schema/linkml_qudt.yaml")
    return (SCHEMA_PATH,)


@app.cell
def _(SCHEMA_PATH, SchemaView):
    sv = SchemaView(str(SCHEMA_PATH))
    return (sv,)


@app.cell
def _(sv):
    # Get all class names for the dropdown
    all_classes = sorted(sv.all_classes().keys())
    return (all_classes,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Select Classes to Include

    Select the classes you want at the root of your subset. The tool will
    automatically include all dependencies.
    """)
    return


@app.cell
def _(all_classes, mo):
    # Create a multiselect dropdown for class selection
    class_selector = mo.ui.multiselect(
        options=all_classes,
        label="Select classes to include",
        value=["Unit", "QuantityKind"],  # Default selection
    )
    class_selector
    return (class_selector,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Dependency Extraction Options
    """)
    return


@app.cell
def _(mo):
    include_ancestors = mo.ui.checkbox(
        value=True, label="Include ancestor classes (is_a chain)"
    )
    include_mixins = mo.ui.checkbox(value=True, label="Include mixin classes")
    include_slot_ranges = mo.ui.checkbox(
        value=True, label="Recursively include classes from slot ranges"
    )

    mo.vstack([include_ancestors, include_mixins, include_slot_ranges])
    return include_ancestors, include_mixins, include_slot_ranges


@app.cell
def _(sv):
    def get_class_dependencies(
        class_names: list[str],
        sv,
        include_ancestors: bool = True,
        include_mixins: bool = True,
        include_slot_ranges: bool = True,
        max_depth: int = 50,
    ) -> dict:
        """
        Recursively extract all dependencies for a set of classes.

        Returns a dict with:
        - classes: set of class names
        - slots: set of slot names
        - enums: set of enum names
        - types: set of type names
        """
        classes_to_include = set()
        slots_to_include = set()
        enums_to_include = set()
        types_to_include = set()

        # Queue of classes to process
        queue = list(class_names)
        processed = set()
        depth = 0

        all_classes = set(sv.all_classes().keys())
        all_enums = set(sv.all_enums().keys())
        all_types = set(sv.all_types().keys())
        all_slots = set(sv.all_slots().keys())

        def add_range_dependency(range_type, next_queue, processed):
            """Helper to add a range type to appropriate collection."""
            if not range_type:
                return
            if range_type in all_classes:
                if include_slot_ranges and range_type not in processed:
                    next_queue.append(range_type)
            elif range_type in all_enums:
                enums_to_include.add(range_type)
            elif range_type in all_types:
                types_to_include.add(range_type)

        while queue and depth < max_depth:
            depth += 1
            next_queue = []

            for class_name in queue:
                if class_name in processed:
                    continue
                if class_name not in all_classes:
                    continue

                processed.add(class_name)
                classes_to_include.add(class_name)

                cls = sv.get_class(class_name)
                if cls is None:
                    continue

                # Get ancestor classes (is_a chain)
                if include_ancestors and cls.is_a:
                    if cls.is_a not in processed:
                        next_queue.append(cls.is_a)

                # Get mixin classes
                if include_mixins and cls.mixins:
                    for mixin in cls.mixins:
                        if mixin not in processed:
                            next_queue.append(mixin)

                # Get all slots for this class (including inherited via induced_slots)
                try:
                    induced_slots = sv.class_induced_slots(class_name)
                except Exception:
                    induced_slots = []

                for slot in induced_slots:
                    slot_name = slot.name
                    slots_to_include.add(slot_name)
                    add_range_dependency(slot.range, next_queue, processed)

                # IMPORTANT: Also collect slots from slot_usage
                # slot_usage entries define how inherited slots are used in this class
                # and may specify different ranges
                if cls.slot_usage:
                    for slot_name, slot_usage in cls.slot_usage.items():
                        # Add the slot itself
                        slots_to_include.add(slot_name)
                        # Check for range override
                        add_range_dependency(slot_usage.range, next_queue, processed)

                # Check direct slots defined on the class
                if cls.slots:
                    for slot_name in cls.slots:
                        slots_to_include.add(slot_name)
                        slot_def = sv.get_slot(slot_name)
                        if slot_def:
                            add_range_dependency(slot_def.range, next_queue, processed)

                # Also check attributes if present
                if cls.attributes:
                    for attr_name, attr_def in cls.attributes.items():
                        slots_to_include.add(attr_name)
                        add_range_dependency(attr_def.range, next_queue, processed)

            queue = next_queue

        # Also add slot inheritance chains (is_a for slots)
        slots_with_parents = set()
        for slot_name in list(slots_to_include):  # Make a copy since we modify
            slot = sv.get_slot(slot_name)
            if slot:
                # Walk up the is_a chain for slots
                current = slot
                visited = set()
                while current and current.name not in visited:
                    visited.add(current.name)
                    slots_with_parents.add(current.name)
                    if current.is_a and current.is_a in all_slots:
                        current = sv.get_slot(current.is_a)
                    else:
                        break

        slots_to_include.update(slots_with_parents)

        # Add slot mixins as well
        for slot_name in list(slots_to_include):
            slot = sv.get_slot(slot_name)
            if slot and slot.mixins:
                for mixin in slot.mixins:
                    if mixin in all_slots:
                        slots_to_include.add(mixin)

        return {
            "classes": classes_to_include,
            "slots": slots_to_include,
            "enums": enums_to_include,
            "types": types_to_include,
        }

    return (get_class_dependencies,)


@app.cell
def _(
    class_selector,
    get_class_dependencies,
    include_ancestors,
    include_mixins,
    include_slot_ranges,
    sv,
):
    # Compute dependencies based on current selection
    selected_classes = class_selector.value

    if selected_classes:
        dependencies = get_class_dependencies(
            selected_classes,
            sv,
            include_ancestors=include_ancestors.value,
            include_mixins=include_mixins.value,
            include_slot_ranges=include_slot_ranges.value,
        )
    else:
        dependencies = {
            "classes": set(),
            "slots": set(),
            "enums": set(),
            "types": set(),
        }

    return selected_classes, dependencies


@app.cell
def _(dependencies, mo):
    mo.md(f"""
    ## Dependency Summary

    Based on your selection, the subset will include:

    - **Classes**: {len(dependencies["classes"])}
    - **Slots**: {len(dependencies["slots"])}
    - **Enums**: {len(dependencies["enums"])}
    - **Types**: {len(dependencies["types"])}
    """)
    return


@app.cell
def _(dependencies, mo):
    # Show the classes that will be included
    classes_list = sorted(dependencies["classes"])
    mo.accordion(
        {
            "Classes to include": mo.ui.table(
                data=[{"Class": c} for c in classes_list],
                selection=None,
            ),
            "Slots to include": mo.ui.table(
                data=[{"Slot": s} for s in sorted(dependencies["slots"])],
                selection=None,
            ),
            "Enums to include": mo.ui.table(
                data=[{"Enum": e} for e in sorted(dependencies["enums"])],
                selection=None,
            )
            if dependencies["enums"]
            else mo.md("*No enums*"),
            "Types to include": mo.ui.table(
                data=[{"Type": t} for t in sorted(dependencies["types"])],
                selection=None,
            )
            if dependencies["types"]
            else mo.md("*No custom types*"),
        }
    )
    return (classes_list,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Generate Subset Schema
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Export Options

    Configure how conflicts should be handled when the schema is imported into another project.
    """)
    return


@app.cell
def _(mo):
    # Export conflict handling options
    remove_base_classes = mo.ui.checkbox(
        value=True,
        label="Remove OWL/RDFS base classes (Thing, Resource, Class) - use importing schema's definitions",
    )
    remove_standard_types = mo.ui.checkbox(
        value=True,
        label="Remove standard LinkML types (string, boolean, etc.) - provided by linkml:types",
    )
    rename_common_slots = mo.ui.checkbox(
        value=True,
        label="Rename common conflicting slots (description, id, value) with 'qudt_' prefix",
    )
    fix_qudt_prefix = mo.ui.checkbox(
        value=True, label="Fix QUDT prefix to http://qudt.org/schema/qudt/"
    )

    mo.vstack(
        [
            remove_base_classes,
            remove_standard_types,
            rename_common_slots,
            fix_qudt_prefix,
        ]
    )
    return (
        remove_base_classes,
        remove_standard_types,
        rename_common_slots,
        fix_qudt_prefix,
    )


@app.cell
def _(mo):
    schema_name_input = mo.ui.text(
        value="qudt_subset",
        label="Schema name",
        placeholder="Enter schema name",
    )
    schema_name_input
    return (schema_name_input,)


@app.cell
def _(SchemaDefinition, copy):
    def create_subset_schema(
        sv, dependencies: dict, schema_name: str = "qudt_subset"
    ) -> SchemaDefinition:
        """Create a new schema containing only the selected elements."""

        source_schema = sv.schema

        # Create new schema with basic metadata
        subset = SchemaDefinition(
            id=f"http://qudt.org/subset/{schema_name}",
            name=schema_name,
            title="QUDT Subset Schema",
            description=f"A subset of QUDT containing {len(dependencies['classes'])} classes",
            version="0.0.1",
            license=source_schema.license,
        )

        # Copy prefixes
        if source_schema.prefixes:
            subset.prefixes = copy.deepcopy(dict(source_schema.prefixes))

        # Copy default_prefix
        subset.default_prefix = source_schema.default_prefix

        # Copy imports
        if source_schema.imports:
            subset.imports = list(source_schema.imports)

        # Add classes (deep copy to avoid modifying originals)
        for class_name in dependencies["classes"]:
            cls = sv.get_class(class_name)
            if cls:
                subset.classes[class_name] = copy.deepcopy(cls)

        # Add slots (deep copy)
        for slot_name in dependencies["slots"]:
            slot = sv.get_slot(slot_name)
            if slot:
                subset.slots[slot_name] = copy.deepcopy(slot)

        # Add enums (deep copy)
        for enum_name in dependencies["enums"]:
            enum = sv.get_enum(enum_name)
            if enum:
                subset.enums[enum_name] = copy.deepcopy(enum)

        # Add types (deep copy)
        for type_name in dependencies["types"]:
            type_def = sv.get_type(type_name)
            if type_def:
                subset.types[type_name] = copy.deepcopy(type_def)

        return subset

    return (create_subset_schema,)


@app.cell
def _():
    def post_process_schema(
        schema: dict,
        remove_base_classes: bool = True,
        remove_standard_types: bool = True,
        rename_common_slots: bool = True,
        fix_qudt_prefix: bool = True,
    ) -> tuple[dict, list[str]]:
        """
        Post-process the schema dict to handle common conflicts.

        Returns the modified schema dict and a list of changes made.
        """
        changes = []

        # Standard LinkML types that should not be redefined
        LINKML_STANDARD_TYPES = {
            "string",
            "integer",
            "boolean",
            "float",
            "double",
            "decimal",
            "time",
            "date",
            "datetime",
            "date_or_datetime",
            "uriorcurie",
            "curie",
            "uri",
            "ncname",
            "objectidentifier",
            "nodeidentifier",
            "jsonpointer",
            "jsonpath",
            "sparqlpath",
        }

        # OWL/RDFS base classes that commonly conflict
        BASE_CLASSES_TO_REMOVE = {"Thing", "Resource", "Class"}

        # Common slot names that conflict with other schemas
        SLOTS_TO_RENAME = {"description", "id", "value"}

        # Fix QUDT prefix
        if fix_qudt_prefix and "prefixes" in schema:
            if "qudt" in schema["prefixes"]:
                old_val = schema["prefixes"]["qudt"]
                # Handle both simple and expanded prefix formats
                if isinstance(old_val, dict):
                    if (
                        old_val.get("prefix_reference")
                        != "http://qudt.org/schema/qudt/"
                    ):
                        old_ref = old_val.get("prefix_reference", "unknown")
                        schema["prefixes"]["qudt"] = "http://qudt.org/schema/qudt/"
                        changes.append(
                            f"Fixed qudt prefix: {old_ref} -> http://qudt.org/schema/qudt/"
                        )
                elif old_val != "http://qudt.org/schema/qudt/":
                    schema["prefixes"]["qudt"] = "http://qudt.org/schema/qudt/"
                    changes.append(
                        f"Fixed qudt prefix: {old_val} -> http://qudt.org/schema/qudt/"
                    )

        # Convert expanded prefix format to simple format
        if "prefixes" in schema:
            new_prefixes = {}
            for prefix_name, prefix_val in schema["prefixes"].items():
                if isinstance(prefix_val, dict) and "prefix_reference" in prefix_val:
                    new_prefixes[prefix_name] = prefix_val["prefix_reference"]
                    changes.append(f"Simplified prefix format: {prefix_name}")
                else:
                    new_prefixes[prefix_name] = prefix_val
            schema["prefixes"] = new_prefixes

        # Remove standard types
        if remove_standard_types and "types" in schema:
            removed_types = []
            for type_name in list(schema["types"].keys()):
                if type_name in LINKML_STANDARD_TYPES:
                    del schema["types"][type_name]
                    removed_types.append(type_name)
            if removed_types:
                changes.append(f"Removed standard types: {', '.join(removed_types)}")
            # Remove empty types section
            if not schema["types"]:
                del schema["types"]

        # Remove base classes
        removed_classes = set()
        if remove_base_classes and "classes" in schema:
            for cls_name in list(schema["classes"].keys()):
                if cls_name in BASE_CLASSES_TO_REMOVE:
                    del schema["classes"][cls_name]
                    removed_classes.add(cls_name)
                    changes.append(f"Removed base class: {cls_name}")

        # Fix dangling class references (is_a, mixins, ranges)
        if removed_classes and "classes" in schema:
            for cls_name, cls_def in schema["classes"].items():
                # Fix is_a references
                if cls_def.get("is_a") in removed_classes:
                    old_parent = cls_def["is_a"]
                    cls_def["is_a"] = "Thing"  # Will use importing schema's Thing
                    changes.append(
                        f"Changed {cls_name}.is_a from {old_parent} to Thing"
                    )

                # Fix mixin references
                if "mixins" in cls_def:
                    new_mixins = [
                        m for m in cls_def["mixins"] if m not in removed_classes
                    ]
                    if len(new_mixins) != len(cls_def["mixins"]):
                        removed = set(cls_def["mixins"]) - set(new_mixins)
                        changes.append(
                            f"Removed mixins from {cls_name}: {', '.join(removed)}"
                        )
                        cls_def["mixins"] = new_mixins
                    if not cls_def["mixins"]:
                        del cls_def["mixins"]

                # Fix slot_usage ranges
                if "slot_usage" in cls_def:
                    for slot_name, usage in cls_def["slot_usage"].items():
                        if usage.get("range") in removed_classes:
                            old_range = usage["range"]
                            del usage["range"]
                            changes.append(
                                f"Removed range override {old_range} from {cls_name}.{slot_name}"
                            )

        # Fix slot ranges that reference removed classes
        if removed_classes and "slots" in schema:
            for slot_name, slot_def in schema["slots"].items():
                if slot_def.get("range") in removed_classes:
                    old_range = slot_def["range"]
                    del slot_def["range"]
                    changes.append(f"Removed range {old_range} from slot {slot_name}")

        # Rename common conflicting slots
        if rename_common_slots:
            slot_renames = {}
            if "slots" in schema:
                for old_name in list(schema["slots"].keys()):
                    if old_name in SLOTS_TO_RENAME:
                        new_name = f"qudt_{old_name}"
                        slot_renames[old_name] = new_name
                        schema["slots"][new_name] = schema["slots"].pop(old_name)
                        schema["slots"][new_name]["name"] = new_name
                        changes.append(f"Renamed slot: {old_name} -> {new_name}")

            # Update class references to renamed slots
            if slot_renames and "classes" in schema:
                for cls_name, cls_def in schema["classes"].items():
                    # Update slots list
                    if "slots" in cls_def:
                        cls_def["slots"] = [
                            slot_renames.get(s, s) for s in cls_def["slots"]
                        ]

                    # Update slot_usage keys
                    if "slot_usage" in cls_def:
                        new_slot_usage = {}
                        for slot_name, usage in cls_def["slot_usage"].items():
                            new_name = slot_renames.get(slot_name, slot_name)
                            if new_name != slot_name:
                                usage["name"] = new_name
                            new_slot_usage[new_name] = usage
                        cls_def["slot_usage"] = new_slot_usage

        return schema, changes

    return (post_process_schema,)


@app.cell
def _(create_subset_schema, dependencies, schema_name_input, sv):
    # Generate the subset schema
    if dependencies["classes"]:
        subset_schema = create_subset_schema(sv, dependencies, schema_name_input.value)
    else:
        subset_schema = None
    return (subset_schema,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Export Schema
    """)
    return


@app.cell
def _(mo):
    output_path_input = mo.ui.text(
        value="qudt_subset.yaml",
        label="Output file path",
        placeholder="Enter output file path",
    )
    output_path_input
    return (output_path_input,)


@app.cell
def _(mo):
    # State for tracking save results
    get_save_result, set_save_result = mo.state("")
    get_changes_made, set_changes_made = mo.state([])
    return get_save_result, set_save_result, get_changes_made, set_changes_made


@app.cell
def _(
    Path,
    fix_qudt_prefix,
    mo,
    output_path_input,
    post_process_schema,
    remove_base_classes,
    remove_standard_types,
    rename_common_slots,
    set_changes_made,
    set_save_result,
    subset_schema,
    yaml_dumper,
):
    import yaml as pyyaml

    def save_schema_with_fixes():
        if not subset_schema:
            return "No schema to save", []

        output_path = Path(output_path_input.value)

        # First dump to YAML string, then load as dict for post-processing
        yaml_str = yaml_dumper.dumps(subset_schema)
        schema_dict = pyyaml.safe_load(yaml_str)

        # Apply post-processing fixes
        schema_dict, changes = post_process_schema(
            schema_dict,
            remove_base_classes=remove_base_classes.value,
            remove_standard_types=remove_standard_types.value,
            rename_common_slots=rename_common_slots.value,
            fix_qudt_prefix=fix_qudt_prefix.value,
        )

        # Write the processed schema
        with open(output_path, "w") as f:
            pyyaml.dump(
                schema_dict,
                f,
                default_flow_style=False,
                sort_keys=False,
                allow_unicode=True,
            )

        return f"Schema saved to {output_path}", changes

    def on_save_click(_):
        result, changes = save_schema_with_fixes()
        set_save_result(result)
        set_changes_made(changes)

    save_button = mo.ui.button(
        label="Save Schema (with conflict fixes)",
        on_click=on_save_click,
    )
    save_button
    return save_button, pyyaml, save_schema_with_fixes


@app.cell
def _(get_changes_made, get_save_result, mo):
    # Display save results
    _save_result = get_save_result()
    _changes_made = get_changes_made()
    if _save_result:
        result_md = f"**{_save_result}**\n\n"
        if _changes_made:
            result_md += "### Changes Applied:\n\n"
            for change in _changes_made:
                result_md += f"- {change}\n"
        else:
            result_md += "*No post-processing changes needed*"
        mo.md(result_md)
    else:
        mo.md("")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Validation

    After saving, validate the subset schema to ensure it can be loaded.
    """)
    return


@app.cell
def _(mo):
    # State for validation results
    get_validation_result, set_validation_result = mo.state("")
    return get_validation_result, set_validation_result


@app.cell
def _(
    Path,
    SchemaView,
    get_validation_result,
    mo,
    output_path_input,
    set_validation_result,
):
    def validate_subset():
        output_path = Path(output_path_input.value)
        if output_path.exists():
            try:
                # Try to load the schema to validate it
                test_sv = SchemaView(str(output_path))
                classes = list(test_sv.all_classes().keys())
                slots = list(test_sv.all_slots().keys())
                return f"Schema is valid! Contains {len(classes)} classes and {len(slots)} slots."
            except Exception as e:
                return f"Validation error: {e}"
        return "File does not exist yet. Save the schema first."

    def on_validate_click(_):
        set_validation_result(validate_subset())

    validate_button = mo.ui.button(
        label="Validate Saved Schema",
        on_click=on_validate_click,
    )

    _validation_result = get_validation_result()
    mo.vstack(
        [
            validate_button,
            mo.md(_validation_result) if _validation_result else mo.md(""),
        ]
    )
    return validate_button, validate_subset


@app.cell
def _(mo):
    mo.md(r"""
    ## Preview Generated YAML

    Preview the raw YAML output (before post-processing fixes).
    """)
    return


@app.cell
def _(mo, subset_schema, yaml_dumper):
    # Generate YAML preview
    if subset_schema:
        yaml_preview = yaml_dumper.dumps(subset_schema)
        mo.accordion(
            {
                "YAML Preview (first 5000 chars)": mo.md(
                    f"```yaml\n{yaml_preview[:5000]}{'...' if len(yaml_preview) > 5000 else ''}\n```"
                )
            }
        )
    else:
        mo.md("*Select at least one class to generate a schema*")
    return


if __name__ == "__main__":
    app.run()
