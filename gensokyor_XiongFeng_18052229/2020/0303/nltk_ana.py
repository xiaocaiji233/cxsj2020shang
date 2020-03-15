import nltk_fun
import collections


def wcollec(p):
    ss=nltk_fun.splitSentence(p)
    ws = nltk_fun.p2w(ss)
    c = collections.Counter()
    for i in ws:
        c[i] += 1
    for (i, j) in c.most_common(10):
        print("%s:%s" % (i, j))
    return c


def tagcollc(p):
    w_tags = nltk_fun.wordtag_set(p)
    c = collections.Counter()
    for i in w_tags:
        x = i[1]
        c[x] += 1
    for (i, j) in c.most_common(10):
        print("%s:%s" % (i, j))
    return c


if __name__ == "__main__":
    p = "My name is Van. I'm an artist, a performance artist. I'm hired for people to perform the fantacies, the deep dark fantacies."
    wcollec(p)
    tagcollc(p)