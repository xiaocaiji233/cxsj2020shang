import json


def file_load(path, name):
    with open(path + name, encoding='UTF-8') as f:
        result = json.load(f)
    return result
