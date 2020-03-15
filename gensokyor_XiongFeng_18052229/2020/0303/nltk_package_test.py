import nltk_fun
import nltk_ana
import pprint

res = open("res/en.txt", encoding="UTF-8", newline=None).read()
res = res.strip().replace("\n", "").replace("\r", "").replace('\t', '').replace('\f', '')
ss = nltk_fun.splitSentence(res)  # 分句
# print("|".join(ss))
# ws = nltk_fun.p2w(ss)  # 分词测试
# print("|".join(ws))
# ana_ws = nltk_ana.wcollec(res)  # 词频
# pprint.pprint(ana_ws)
# ana_tags = nltk_ana.tagcollc(res)  # 词性频率
# pprint.pprint(ana_tags)
