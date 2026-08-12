import json


def stringify(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    return str(value)


def generate_diff(file_path1, file_path2):
    with open(file_path1) as f1:
        data1 = json.load(f1)

    with open(file_path2) as f2:
        data2 = json.load(f2)

    keys = sorted(data1.keys() | data2.keys())
    lines = []

    for key in keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                lines.append(f"    {key}: {stringify(data1[key])}")
            else:
                lines.append(f"  - {key}: {stringify(data1[key])}")
                lines.append(f"  + {key}: {stringify(data2[key])}")
        elif key in data1:
            lines.append(f"  - {key}: {stringify(data1[key])}")
        elif key in data2:
            lines.append(f"  + {key}: {stringify(data2[key])}")

    result = "{\n" + "\n".join(lines) + "\n}"
    return result