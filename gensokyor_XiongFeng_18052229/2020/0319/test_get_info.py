import get_info
from pprint import pprint
import json
import time


def get_issues(url):  # 获取issues并存储为json文件
    # pprint(get_info.once('https://api.github.com/repos/tensorflow/tensorflow').json())
    # print(get_info.UserAgent(verify_ssl=False).random)
    results = get_info.info_pages(url)
    pprint(results)
    num = 0
    for i in results:
        print(num)
        file_name = str(num + 1)
        f = open('/json/' + file_name + '.json', 'w')
        json.dump(i, f)
        num += 1


if __name__ == '__main__':
    # get_issues('https://api.github.com/repos/tensorflow/tensorflow/issues')
    # get_info.single_issue('https://api.github.com/repos/tensorflow/tensorflow/issues', 2)
    n = 29
    while True:  # 循环获取issues,需要人工值守多次运行并更改n值,原因github反爬虫
        n += 1
        get_info.single_issue('https://api.github.com/repos/tensorflow/tensorflow/issues', n)
        time.sleep(10)
