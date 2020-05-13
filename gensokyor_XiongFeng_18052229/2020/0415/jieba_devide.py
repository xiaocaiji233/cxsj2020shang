import jieba
import jieba.posseg
import clean


def loaddoc(a, co='UTF-8'):  # 载入文档
    b = open(a, encoding=co).read()
    return b


def doc2row(orin: str):
    return orin.split('\n')


def devide_single_row(orin: str):
    result = [orin[0], clean.cleantext(orin[2:])]
    if isinstance(result[1], tuple):
        result[1] = ''.join(result[1])
    return result


def res_devided(path: str, co='UTF-8'):
    file_res = loaddoc(path, co)
    result = []
    for i in doc2row(file_res):
        if len(i) > 1:
            result.append(devide_single_row(i))
    return result


def load_stopwords():  # 载入停用词
    file_name = "stopwords.txt"
    stop_list = [sw.replace('\n', '') for sw in open(file_name, encoding="UTF-8").readlines()]
    return stop_list


def res_modify(res: list):
    for i in res:
        if isinstance(i[1], str):
            i[1] = ch_jieba(str(i[1]))
        else:
            res.remove(i)
    return res


def corpora2word(path: str, co='UTF-8'):
    res = res_devided(path)
    return res_modify(res)


# def outwords(a, co):  # 输出分词结果
#     b = loaddoc(a, co)
#     b = b.strip().replace("\n", "").replace("\r", "")
#     return ch_jieba(b)


# def outposseg(a):  # 返回词性分词结果
#     b = loaddoc(a, "UTF-8")
#     seg = jieba.posseg.cut(b)
#     return seg


def ch_jieba(a):  # 返回分词结果
    b = jieba.cut(a)
    list = load_stopwords()
    ana = [x for x in b if x not in list and len(x) > 1]
    return ana


if __name__ == "__main__":
    import pprint
    import time
    import json

    # string_test = '这是一个35135测试用于测试/词性分词,包含了符号以及数字等字符.'
    # # pprint.pprint(i for i in jieba.posseg.cut(string_test))
    # a = jieba.posseg.cut(string_test)
    # time.sleep(5)
    # for i in a:
    #     # print(i)
    #     pprint.pprint(i)
    # testdata = '0,一公里不到，县医院那个天桥下右拐200米就到了！//@谢礼恒: 我靠。这个太霸道了！离224有好远？ //@古倒吃158:这个点我真心要找吃的[泪] //@敏一嘴:下次记到去吃哦@霜晨月xjm @九吃 @兰妹围脖 @赤脚在天涯 @古倒吃158 @小李老师健康煮艺 @美食小魔女'
    # pprint.pprint(testdata)
    # ch_jieba(testdata)
    # pprint.pprint(devide_single_row(testdata))
    # # file = loaddoc('res/corpora/corpora.csv', 'UTF-8')
    # pprint.pprint(file)
    save_data = corpora2word('res/corpora/corpora.csv')
    file = open('./res/processed/word_devided.txt', 'w')
    # save_test = 'sss'
    json.dump(save_data, file)
    pprint.pprint(corpora2word('res/corpora/corpora.csv'))
    # print(corpora2word('res/corpora/corpora.csv'))
