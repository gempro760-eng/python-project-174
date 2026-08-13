import json
import os
import yaml


def parse_data(file_path):
    _, extension = os.path.splitext(file_path)
    extension = extension.lower()

    with open(file_path) as f:
        if extension == ".json":
            return json.load(f)
        elif extension in (".yaml", ".yml"):
            return yaml.safe_load(f)
        else:
            raise ValueError(f"Unsupported file format: {extension}")