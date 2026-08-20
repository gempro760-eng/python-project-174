import json
import subprocess
import sys

from gendiff import generate_diff
from gendiff.diff_builder import build_diff
from gendiff.parser import parse_data


def test_generate_diff_json_nested():
    file1 = "tests/fixtures/file1.json"
    file2 = "tests/fixtures/file2.json"

    with open("tests/fixtures/stylish_result.txt", encoding="utf-8") as f:
        expected = f.read().strip()

    assert generate_diff(file1, file2) == expected


def test_generate_diff_yaml_nested():
    file1 = "tests/fixtures/file1.yml"
    file2 = "tests/fixtures/file2.yml"

    with open("tests/fixtures/stylish_result.txt", encoding="utf-8") as f:
        expected = f.read().strip()

    assert generate_diff(file1, file2) == expected


def test_generate_diff_plain():
    file1 = "tests/fixtures/file1.json"
    file2 = "tests/fixtures/file2.json"

    with open("tests/fixtures/plain_result.txt", encoding="utf-8") as f:
        expected = f.read().strip()

    assert generate_diff(file1, file2, "plain") == expected


def test_generate_diff_json_format():
    file1 = "tests/fixtures/file1.json"
    file2 = "tests/fixtures/file2.json"

    result = generate_diff(file1, file2, "json")
    # Verificamos que sea un JSON válido parseable por Python
    parsed_json = json.loads(result)
    assert isinstance(parsed_json, list)
    common = next(node for node in parsed_json if node["key"] == "common")
    assert common["type"] == "nested"
    assert "children" in common

    setting3 = next(
        node for node in common["children"] if node["key"] == "setting3"
    )
    assert setting3 == {
        "key": "setting3",
        "type": "changed",
        "old_value": True,
        "new_value": None,
    }


def test_generate_diff_yaml_extension_yaml(tmp_path):
    file1 = tmp_path / "file1.yaml"
    file2 = tmp_path / "file2.yaml"
    file1.write_text("common:\n  setting: value\n", encoding="utf-8")
    file2.write_text("common:\n  setting: updated\n", encoding="utf-8")

    result = generate_diff(str(file1), str(file2), "plain")

    assert result == (
        "Property 'common.setting' was updated. "
        "From 'value' to 'updated'"
    )


def test_generate_diff_equal_files(tmp_path):
    file1 = tmp_path / "file1.json"
    file2 = tmp_path / "file2.json"
    content = '{"enabled": true, "items": [1, 2]}'
    file1.write_text(content, encoding="utf-8")
    file2.write_text(content, encoding="utf-8")

    assert generate_diff(str(file1), str(file2)) == (
        "{\n"
        "    enabled: true\n"
        "    items: [1, 2]\n"
        "}"
    )


def test_diff_tree_uses_children():
    data1 = parse_data("tests/fixtures/file1.json")
    data2 = parse_data("tests/fixtures/file2.json")

    diff = build_diff(data1, data2)

    common = next(node for node in diff if node["key"] == "common")
    assert common["type"] == "nested"
    assert isinstance(common["children"], list)


def test_plain_lists_are_complex_values(tmp_path):
    file1 = tmp_path / "file1.json"
    file2 = tmp_path / "file2.json"
    file1.write_text("{}", encoding="utf-8")
    file2.write_text('{"items": [1, 2]}', encoding="utf-8")

    result = generate_diff(str(file1), str(file2), "plain")

    assert result == "Property 'items' was added with value: [complex value]"


def test_generate_diff_object_and_scalar_changes(tmp_path):
    file1 = tmp_path / "file1.json"
    file2 = tmp_path / "file2.json"
    file1.write_text('{"object": {"key": "value"}, "scalar": "text"}')
    file2.write_text('{"object": "updated", "scalar": {"key": "value"}}')

    result = generate_diff(str(file1), str(file2), "plain")

    assert result == (
        "Property 'object' was updated. From [complex value] to 'updated'\n"
        "Property 'scalar' was updated. "
        "From 'text' to [complex value]"
    )


def test_parse_data_rejects_unsupported_extension(tmp_path):
    file_path = tmp_path / "config.txt"
    file_path.write_text("content", encoding="utf-8")

    try:
        parse_data(str(file_path))
    except ValueError as error:
        assert str(error) == "Unsupported file format: .txt"
    else:
        raise AssertionError("parse_data accepted an unsupported extension")


def test_cli_help_and_invalid_format():
    help_result = subprocess.run(
        [sys.executable, "-m", "gendiff.scripts.gendiff", "--help"],
        capture_output=True,
        text=True,
        check=False,
    )
    invalid_result = subprocess.run(
        [
            sys.executable,
            "-m",
            "gendiff.scripts.gendiff",
            "--format",
            "unknown",
            "file1.json",
            "file2.json",
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert help_result.returncode == 0
    assert "Compares two configuration files" in help_result.stdout
    assert invalid_result.returncode == 2
    assert "invalid choice" in invalid_result.stderr