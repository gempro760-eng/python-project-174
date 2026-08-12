from gendiff import generate_diff


def test_generate_diff_json():
    file1 = "tests/fixtures/file1.json"
    file2 = "tests/fixtures/file2.json"

    with open("tests/fixtures/result.txt") as f:
        expected = f.read().strip()

    assert generate_diff(file1, file2) == expected