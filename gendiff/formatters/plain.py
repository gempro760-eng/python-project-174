def stringify(value):
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def format_plain(diff, path=""):
    lines = []

    for node in diff:
        key = node["key"]
        current_path = f"{path}.{key}" if path else key
        node_type = node["type"]

        if node_type == "nested":
            lines.append(format_plain(node["children"], current_path))
        elif node_type == "added":
            val = stringify(node["value"])
            lines.append(
                f"Property '{current_path}' was added with value: {val}"
            )
        elif node_type == "removed":
            lines.append(f"Property '{current_path}' was removed")
        elif node_type == "changed":
            old_val = stringify(node["old_value"])
            new_val = stringify(node["new_value"])
            lines.append(
                f"Property '{current_path}' was updated. "
                f"From {old_val} to {new_val}"
            )

    return "\n".join(filter(None, lines))