import json
from pprint import pprint


def file_load(fullname):  # 载入单个json文件
    with open(fullname, encoding='UTF-8') as f:
        result = json.load(f)
        f.close()
    return result


if __name__ == '__main__':  # 测试代码
    test = file_load('json/', '34.json')
    for i in test:
        pprint(i['updated_at'])
        pprint(i['body'])
    # pprint(test)
