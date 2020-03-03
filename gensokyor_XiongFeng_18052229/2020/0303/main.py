import input_article_ch
import jieba_test
import collections

a=input_article_ch.readarticle("res/ch.txt")
a=a.strip().replace("\n","").replace("\r","")
b=jieba_test.ch_jieba(a)
c=collections.Counter()
for i in b:
    if(len(i)>1):
        c[i]+=1
for (i,j)in c.most_common(10):
    print("%s:%s"%(i,j))

