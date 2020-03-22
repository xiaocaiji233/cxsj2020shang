import release_process


def get_releases(releases):  # 获取所有release的发布时间
    times = []
    for i in releases:
        times.append(i["published_at"])
    times.sort()  # 时间排序
    return times


if __name__ == '__main__':
    test = get_releases([{"published_at": '2020-03-1'}, {"published_at": '2020-03-1'}, {"published_at": '2020-01-2'},
                         {"published_at": '2020-01-2'}, {"published_at": '2020-01-0'}, {"published_at": '2019-12-2'}])
    print(test)
#     print('1950-21-01' != '1950-21-01')
#     print('1950-21-01' == '1950-21-01')
#     print('1950-21-01' > '1950-21-02')
#     print('1950-21-01' < '1950-21-02')
