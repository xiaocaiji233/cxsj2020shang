def single_process(issue, options):  # 对单个dic进行简化,保留指定属性
    result = {}
    for i in options:
        result[i] = issue[i]
    return result


def json_process(json_file, options):  # 对单个json文件内容处理
    result = []
    for i in json_file:
        result.append(single_process(i, options))
    return result


def jsons_process(jsons, option):  # 对所有json文件进行处理并汇总
    result = []
    for i in jsons:
        result += json_process(i, option)
    return result


