INDENT_SIZE = 4


def stringify(value, depth):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if not isinstance(value, dict):
        return str(value)

    indent = " " * (depth * INDENT_SIZE)
    lines = []
    for key, val in sorted(value.items()):
        lines.append(f"{indent}    {key}: {stringify(val, depth + 1)}")

    result = "\n".join(lines)
    return f"{{\n{result}\n{indent}}}"


def format_stylish(diff, depth=1):
    indent = " " * (depth * INDENT_SIZE - 2)
    lines = []

    for node in diff:
        key = node['key']
        node_type = node['type']

        if node_type == 'nested':
            children = format_stylish(node['children'], depth + 1)
            lines.append(f"{indent}  {key}: {children}")
        elif node_type == 'added':
            val = stringify(node['value'], depth)
            lines.append(f"{indent}+ {key}: {val}")
        elif node_type == 'removed':
            val = stringify(node['value'], depth)
            lines.append(f"{indent}- {key}: {val}")
        elif node_type == 'unchanged':
            val = stringify(node['value'], depth)
            lines.append(f"{indent}  {key}: {val}")
        elif node_type == 'changed':
            old_val = stringify(node['old_value'], depth)
            new_val = stringify(node['new_value'], depth)
            lines.append(f"{indent}- {key}: {old_val}")
            lines.append(f"{indent}+ {key}: {new_val}")

    result = "\n".join(lines)
    closing_indent = " " * ((depth - 1) * INDENT_SIZE)
    return f"{{\n{result}\n{closing_indent}}}"