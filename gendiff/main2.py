import json
from generate_diff2 import generate_diff

def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

file_path1 = ('/home/telchar/python-project-50/gendiff/file1.json')
file_path2 = ('/home/telchar/python-project-50/gendiff/file2.json')

data1 = read_json(file_path1)
data2 = read_json(file_path2)

diff = generate_diff(data1, data2)
print(diff)
