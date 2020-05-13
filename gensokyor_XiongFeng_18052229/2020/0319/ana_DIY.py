import issues_process
import time_pieces_generate
import devide_issues
import nltk_process
import collections


def get_all_resources(issues_path: str, release_path: str):
    issues = issues_process.issues_process(issues_path)
    times = time_pieces_generate.port(release_path)
    ana_res = devide_issues.match(issues, times)
    processed = nltk_process.bodies_process(ana_res)
    to_de = get_to_delete(processed)
    # pprint(to_de)
    for i, j in processed.items():
        for k in to_de:
            while k in j:
                j.remove(k)

    return processed


def get_to_delete(all_editon: dict):
    limit = len(all_editon.keys()) / 3 - 1
    releases_name = all_editon.keys()
    c = collections.Counter()
    for i in releases_name:
        uni = set_unique(all_editon[i])
        # pprint(uni)
        for j in uni:
            c[j] += 1
    to_delete = []
    for i, j in c.items():
        if float(j) > limit:
            to_delete.append(i)
    return to_delete


def set_unique(arr: list):
    unsort_unique = list(set(arr))
    unsort_unique.sort(key=arr.index)

    return unsort_unique


def single_ana(arr: list):
    c = collections.Counter()
    for i in arr:
        c[i] += 1
    return c


def ana(dic: dict):
    for i, j in dic.items():
        dic[i] = single_ana(j)
    return dic


if __name__ == '__main__':
    from pprint import pprint

    processed = get_all_resources('./json/', './json/release/')
    anaed = ana(processed)
    for i in anaed.keys():
        print('%s: ' % i, end='')
        for j, k in anaed[i].most_common(10):
            print('%s   ' % j, end='')
        print('\n')

    # pprint(get_all_resources('./json/', './json/release/'))
