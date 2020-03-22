import json_read
import os


def get_filename(path):
    all_included = os.listdir(path)
    result = [i for i in all_included if '.json' in i]
    return result


def all_load(path):
    result = []
    names = get_filename(path)
    for i in names:
        fullname = path + i
        result.append(json_read.file_load(fullname))
    return result
