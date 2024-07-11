import yaml
from gendiff.generate_diff2 import generate_diff


def difference():
    with open('gendiff/filepath1', 'r') as f:
        filepath1 = yaml.safe_load(f)
    with open('gendiff/filepath2', 'r') as f:
        filepath2 = yaml.safe_load(f)

    result = generate_diff(filepath1, filepath2)
    excepted_result = '- follow: false\n  host: hexlet.io\n- proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n+ verbose: true'
    assert result == excepted_result
