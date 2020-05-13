import json


def file_load(fullname):  # 载入单个json文件
    with open(fullname, encoding='UTF-8') as f:
        result = json.load(f)
        f.close()
    return result


def file_save(path: str, name: str, to_be_saved):
    f = open(path + name, 'w')

    json.dump(to_be_saved, f)


if __name__ == '__main__':  # 测试代码
    from pprint import pprint

    test = file_load('json/', '34.json')
    for i in test:
        pprint(i['updated_at'])
        pprint(i['body'])
    # pprint(test)
