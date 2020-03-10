import jieba_devide
import collections

source_file = "res/ch.txt"
b = jieba_devide.outwords(source_file)
print("/".join(b))
c = collections.Counter()
for i in b:
    if len(i) > 1:
        c[i] += 1
for (i, j) in c.most_common(10):
    print("%s:%s" % (i, j))
