import release_process


def get_releases(releases):  # 获取所有release的发布时间
    times = []
    for i in releases:
        times.append(i["published_at"])
    times.sort()  # 时间排序
    return times


def port(path: str):
    origin = release_process.issues_process(path)
    processed = get_releases(origin)
    return processed


if __name__ == '__main__':
    test = port('json/release/')
    print(test)
#     print('1950-21-01' != '1950-21-01')
#     print('1950-21-01' == '1950-21-01')
#     print('1950-21-01' > '1950-21-02')
#     print('1950-21-01' < '1950-21-02')
