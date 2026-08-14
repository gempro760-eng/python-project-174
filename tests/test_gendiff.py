import json

from gendiff import generate_diff


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
    assert len(parsed_json) > 0