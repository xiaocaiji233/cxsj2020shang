import json_process
import files_load


def issues_process(path: str):  # 载入并简化issues,保留"created_at", "body"
    origin = files_load.all_load(path)
    processed = json_process.jsons_process(origin, ["created_at", "body"])
    for i in processed:
        i['created_at'] = i['created_at'][:9]
        # i["body"]=
        # str = ''
        # for j in i["body"]:
        #     str += j;
        # i['str'] = str
        # i.pop("body")

    return processed


if __name__ == '__main__':  # 测试代码
    from pprint import pprint

    test = issues_process('json/')
    print(len(test))
    pprint(test)
