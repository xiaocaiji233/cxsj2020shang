import jieba
import re
import jieba.posseg as psg
import pandas as pd
import numpy as np
from collections import Counter

jieba.load_userdict('stop_words.txt')


# 创建停用词表
def stopwordlist():
    stopwords = [line.strip() for line in open('stop_words.txt', encoding='UTF-8').readlines()]
    return stopwords


# 去停用词
def movestopwords(sentences):
    stopwords = stopwordlist()
    out_words = ''
    for word in sentences:
        if word not in stopwords:
            if word != '\t':
                out_words += word
                out_words += " "
    return out_words


def clean(text):
    text = re.sub(r"(回复)?(//)?\s*@\S*?\s*(:| |$)", " ", text)  # 去除正文中的@和回复/转发中的用户名
    text = re.sub(r"\[\S+\]", "", text)      # 去除表情符号
    text = re.sub(r"#\S+#", "", text)      # 保留话题内容
    URL_REGEX = re.compile(
        r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s('
        r')<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))',
        re.IGNORECASE)
    text = re.sub(URL_REGEX, "", text)       # 去除网址
    text = text.replace("转发微博", "")       # 去除无意义的词语
    r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\n。！，]+'
    text = re.sub(r, "", text)
    text = re.sub(r"\s+", " ", text) # 合并正文中过多的空格
    return text.strip()


f = open('weibo_senti_100k.csv', 'r', encoding='utf-8')  # 打开中文文档
data = pd.read_csv(f)
record_num = int(data.describe().iloc[0, 0])
for i in range(record_num):
    record = data.iloc[i,:]
    review = record['review']
    print(clean(review))
# sentences = re.split('[。！!.？?]', paragraph)  # 分句
# cut = jieba.cut_for_search(paragraph)  # 分词
# words = psg.cut(paragraph)  # 词性标注
# final_sen = movestopwords(sentences)
# stopwordlist()
