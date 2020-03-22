import json_process
import files_load


def issues_process(path):  # release载入并简化,保留"published_at"
    origin = files_load.all_load(path)
    processed = json_process.jsons_process(origin, ["published_at"])
    return processed


if __name__ == '__main__':  # 测试代码
    test = issues_process('json/release/')
    print(len(test))
