import json_process
import files_load


def issues_process(path):  # 载入并简化issues,保留"created_at", "body"
    origin = files_load.all_load(path)
    processed = json_process.jsons_process(origin, ["created_at", "body"])
    return processed


if __name__ == '__main__':  # 测试代码
    test = issues_process('json/')
    print(len(test))
