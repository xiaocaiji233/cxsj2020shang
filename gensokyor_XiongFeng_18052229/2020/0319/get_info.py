import requests
from fake_useragent import UserAgent
import time
import json


def authorize():
    key = open('github_access.txt', encoding='UTF-8').read()  # 自行创建授权码,载入
    return key


def once(url):  # 用于获取项目总信息
    uas = UserAgent(verify_ssl=False)
    ua = uas.random
    key = authorize()
    header = {"User-Agent": ua, 'Authorization': 'token ' + key}
    # url+=''
    info = requests.get(url=url, headers=header).json()
    return info;


def info_pages(urlorigin):  # 用于获取issues,releases
    uas = UserAgent(verify_ssl=False)
    n = 0
    per = '?per_page=100&page='
    total = []
    key = authorize()

    while 1:
        n += 1
        # if n % 10 == 0:
        time.sleep(30)
        # if n % 3 == 1 and n != 1:
        #     time.sleep(10)
        print(n)
        rand = n % 7
        if rand == 0:
            ua = uas.random
        elif rand == 1:
            ua = uas.ie
        elif rand == 2:
            ua = uas.opera
        elif rand == 3:
            ua = uas.chrome
        elif rand == 4:
            ua = uas.firefox
        elif rand == 5:
            ua = uas.safari
        elif rand == 6:
            ua = uas.random
        header = {"User-Agent": ua, 'Authorization': 'token ' + key}
        urlp = urlorigin + per + str(n)
        info = requests.get(urlp, headers=header).json()
        if n > 1:
            if info == total[n - 2]:
                break
        # if n == 4:
        #     break
        total.append(info)
        # break
    total.pop()
    return total


def single_issue(urlorigin, page):  # 获取单页issues
    key = authorize()
    uas = UserAgent(verify_ssl=False)
    per = '?per_page=100&page='
    header = {"User-Agent": uas.Chrome, 'Authorization': 'token ' + key}
    urlp = urlorigin + per + str(page)
    info = requests.get(urlp, headers=header).json()
    f = open('./json/' + str(page) + '.json', 'w+')  # 创建并保存json
    json.dump(info, f)
