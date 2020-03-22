import json_read
import os


def get_filename(path):  # 载入文件名且过滤非json文件
    all_included = os.listdir(path)
    result = [i for i in all_included if '.json' in i]
    return result


def all_load(path):  # 载入所有json
    result = []
    names = get_filename(path)
    for i in names:
        fullname = path + i
        result.append(json_read.file_load(fullname))
    return result
