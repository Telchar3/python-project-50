import json
from gendiff.generate_diff2 import generate_diff
def test_generate_diff():
    with open('gendiff/file1.json', 'r') as f:
        file1_data = json.load(f)

    with open('gendiff/file2.json', 'r') as f:
        file2_data = json.load(f)
    
    result = generate_diff(file1_data, file2_data)
    excepted_result = '- follow: False\n  host: hexlet.io\n- proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n+ verbose: True'
    assert result == excepted_result
