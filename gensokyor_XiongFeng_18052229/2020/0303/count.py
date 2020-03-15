import jieba_devide
import collections

def collec(a):
    b = jieba_devide.outwords(a)
    print("/".join(b))
    c = collections.Counter()
    for i in b:
        if len(i) > 1:
            c[i] += 1
    for (i, j) in c.most_common(10):
        print("%s:%s" % (i, j))
