import yaml
from gendiff. 


def difference():
    with open('gendiff/filepath1', 'r') as f:
        filepath1 = yaml.safe_load(f)
    with open('gendiff/filepath2', 'r') as f:
        filepath2 = yaml.safe_load(f)

    result = generate_diff(filepath1, filepath2)
    excepted_result = '{
    - follow: false
      host: hexlet.io
    - proxy: 123.234.53.22
    - timeout: 50
    + timeout: 20
    + verbose: true
    }'

