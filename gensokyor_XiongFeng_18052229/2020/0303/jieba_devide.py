import jieba


def outwords(a,co):  # 输出分词结果
    b = open(a, encoding=co).read()
    b = b.strip().replace("\n", "").replace("\r", "")
    return ch_jieba(b)


def ch_jieba(a):  # 返回分词结果
    b = jieba.cut(a)
    list = load_stopwords()
    ana = [x for x in b if x not in list and len(x) > 1]
    return ana


def load_stopwords():  # 载入停用词
    file_name = "stopwords.txt"
    stop_list = [sw.replace('\n', '') for sw in open(file_name,encoding="UTF-8").readlines()]
    return stop_list
