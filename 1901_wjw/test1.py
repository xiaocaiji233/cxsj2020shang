# -*- coding: utf-8 -*-
import jieba
import re
import jieba.posseg as psg
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


# 词性统计
def count_cx(value):
    count = 0
    words = psg.cut(paragraph)
    for word, flag in words:
        if flag.startswith(value):
            count += 1
    return count


f = open('test.txt', encoding='utf-8')  # 打开中文文档
paragraph = f.read()
sentences = re.split('[。！!.？?]', paragraph)  # 分句
cut = jieba.cut_for_search(paragraph)  # 分词
words = psg.cut(paragraph)  # 词性标注
stopwordlist()

# 分句结果
print('分句结果：')
print(sentences)
# 分词结果
print('分词结果：')
print('|'.join(cut))

# 词性标注
print('词性标记结果：')
for word, flag in words:
    print('%s,%s' % (word, flag))

# 去停用词显示
print('去除停用词后结果')
print(movestopwords(sentences))
# 简单统计
print('形容词的个数为：%d，名词个数为：%d，动词个数为：%d' % (count_cx('a'), count_cx('n'), count_cx('v')))

f.close()
