from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish


def format_diff(diff, format_name):
    if format_name == "stylish":
        return format_stylish(diff)
    elif format_name == "plain":
        return format_plain(diff)
    raise ValueError(f"Unsupported format: {format_name}")