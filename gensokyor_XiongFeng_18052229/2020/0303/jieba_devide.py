import jieba
import jieba.posseg
import collections


def collect_single_word(a, co):  # 统计单个词的出现次数
    b = outwords(a, co)
    print("/".join(b))
    c = collections.Counter()
    for i in b:
        c[i] += 1
    for (i, j) in c.most_common(10):
        print("%s:%s" % (i, j))
    return c


def collect_posseg(a, co="UTF-8"):  # 输出词性的次数
    b = outposseg(a)
    c = collections.Counter()
    for i in b:
        x = i.flag
        c[x] += 1
    for (i, j) in c.most_common(10):
        print("%s:%s" % (i, j))
    return c


def loaddoc(a, co):  # 载入文档
    b = open(a, encoding=co).read()
    return b


def outwords(a, co):  # 输出分词结果
    b = loaddoc(a, co)
    b = b.strip().replace("\n", "").replace("\r", "")
    return ch_jieba(b)


def outposseg(a):  # 返回词性分词结果
    b = loaddoc(a, "UTF-8")
    seg = jieba.posseg.cut(b)
    return seg


def ch_jieba(a):  # 返回分词结果
    b = jieba.cut(a)
    list = load_stopwords()
    ana = [x for x in b if x not in list and len(x) > 1]
    return ana


def load_stopwords():  # 载入停用词
    file_name = "stopwords.txt"
    stop_list = [sw.replace('\n', '') for sw in open(file_name, encoding="UTF-8").readlines()]
    return stop_list
