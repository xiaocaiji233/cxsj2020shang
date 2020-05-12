import requests
import os
import json
import pprint

repos = ['uikit/uikit']

headers = {'Authorization': 'token 0b18f2b22b2f8cbed8d3ca7b264a69873242b955'}


# def readURLwithoutcache(cache, url):
#     cache = 'data/cache/%s' % cache
#     content = requests.get(url, headers=headers).content.decode()
#     folder = cache.rpartition('/')[0]
#     not os.path.isdir(folder) and os.makedirs(folder)
#     with open(cache, 'a', encoding='utf-8') as f:
#         f.write(content)
#     return content


def readURL(cache, url):
    # 看看该url是否访问过
    cache = 'data/cache/%s' % cache
    if os.path.isfile(cache):
        with open(cache, 'r', encoding='utf-8') as f:
            content = f.read()
        return content

    content = requests.get(url, headers=headers).content.decode()
    # 把文件内容保存下来，以免多次重复访问url，类似于缓存
    folder = cache.rpartition('/')[0]
    not os.path.isdir(folder) and os.makedirs(folder)
    with open(cache, 'w', encoding='utf-8') as f:
        f.write(content)
    return content


def getRepoInfo():
    title = []
    istime = []
    for repo in repos:
        repo_url = 'https://api.github.com/repos/%s' % repo  # 确定url
        issue_url = 'https://api.github.com/repos/%s/issues?page=1&per_page=999' % repo
        repoInfo = readURL('Repositories/reposInfo/%s' % repo, repo_url)  # 访问url得到数据
        repoInfo = repoInfo and json.loads(repoInfo)  # 将数据类型转换
        issueInfo = readURL('Repositories/issueInfo/%s' % repo, issue_url)
        issueInfo = issueInfo and json.loads(issueInfo)

    for issue in issueInfo:
        title = []
        istime = []
        title.append(issue['title'])
        istime.append((issue['updated_at'])[:10])
        f1 = open('title.json', 'a+', encoding='utf-8')
        f2 = open('istime.json', 'a+', encoding='utf-8')
        for t in f1.readlines():
            f1.write(t + '\n')
        for it in f2.readlines():
            f2.write(it + '\n')
        f.close()
        ftime.close()

    issue_all = [title, istime]
    return issue_all


# def getIssue():
#     count = 7
#     for repo in repos:
#         issue_url = 'https://api.github.com/repos/%s/issues?page=%s&per_page=999' % (repo, count)
#         issueInfo = readURLwithoutcache('Repositories/issueInfo/%s' % repo, issue_url)
#         issueInfo = issueInfo and json.loads(issueInfo)
#
#         while len(issueInfo) == 100:
#             count += 1
#             issue_url = 'https://api.github.com/repos/%s/issues?page=%s&per_page=999' % (repo, count)
#             issueInfo = readURLwithoutcache('Repositories/issueInfo/%s' % repo, issue_url)
#             issueInfo = issueInfo and json.loads(issueInfo)
#             print(count)
#             if len(issueInfo) <= 100:
#                 break


getRepoInfo()



