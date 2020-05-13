import re
import jieba
import time
import gensim
import multiprocessing
import jieba.posseg as psg
from gensim.models import KeyedVectors, word2vec, Word2Vec
import pprint

jieba.load_userdict('stop_words.txt')


# 创建停用词表
def stopwordlist():
    stopwords = [line.strip() for line in open('stop_words.txt', encoding='UTF-8').readlines()]
    return stopwords


stopwords = stopwordlist()
sentences_cut = []
f = open('test.txt', encoding='utf-8')  # 打开中文文档
paragraph = f.read()
# 结巴分词

cuts = jieba.cut(paragraph, cut_all=False)
# pprint.pprint(cuts)
new_cuts = []
for cut in cuts:
    if cut not in stopwords:
        new_cuts.append(cut)
        # pprint.pprint(cut)
# pprint.pprint(stopwords)
res = ' '.join(new_cuts)
sentences_cut.append(res)


with open('sentence.txt', 'w', encoding='utf-8') as f:
    for ele in sentences_cut:
        ele = ele + '\n'
        f.write(ele)

sentences = list(word2vec.LineSentence('sentence.txt'))

# 训练方式1
model = Word2Vec(sentences, size=2, min_count=5, window=5, sg=2, workers=multiprocessing.cpu_count())
# print(model)

model.save('word2vec.model')
model.wv.save_word2vec_format('word2vec.vector')

t1 = time.time()
model = Word2Vec.load('word2vec.model')
t2 = time.time()
print(model)
print(".model load time %.4f" % (t2 - t1))
