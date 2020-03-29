import nltk
import nltk.data
from nltk.corpus import stopwords
import pprint


# nltk.data.path.append(r"E:\py_space\NLTK_DATA\nltk_data")
# set(stopwords.words('english'))


def splitSentence(p):  # p->sents
    nltk.data.path.append(r"E:\py_space\NLTK_DATA\nltk_data")
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentence = tokenizer.tokenize(p)
    return sentence


def wordtokenizer(s):  # sent->ws
    nltk.data.path.append(r"E:\py_space\NLTK_DATA\nltk_data")
    w = nltk.tokenize.WordPunctTokenizer().tokenize(s)
    return w


def p2w(ss):  # sents->ws
    nltk.data.path.append(r"E:\py_space\NLTK_DATA\nltk_data")
    set(stopwords.words('english'))
    stopword = stopwords.words('english')
    stopword += ['\'', '.', ',', '?', '!', ':', '\"', '/', '-', '+', '*', '', '', '\\f', '\\n', '/', '*', '//','@']
    ws = []
    for i in ss:
        # print(i)
        w = wordtokenizer(i)
        for j in w:
            if j not in stopword:
                ws.append(j)
    return ws


def wordtag_set(s):  # string->tags
    ss = splitSentence(s)
    w_tagss = []
    token = ['\'', '.', ',', '?', '!', ':', '\"', '/', '-', '+', '*', '', '', '\\f', '\\n', '/', '*', '//']
    for i in ss:
        w_tags = nltk.pos_tag(nltk.word_tokenize(i))
        for j in w_tags:
            if j[0] not in token:
                w_tagss.append(j)
    return w_tagss


if __name__ == '__main__':
    nltk.data.path.append(r"E:\py_space\NLTK_DATA\nltk_data")
    p = "My name is Van. I'm an artist, a performance artist. I'm hired for people to perform the fantacies, the deep dark fantacies."
    s = splitSentence(p)
    print('|'.join(s))
    w = p2w(s)
    print("|".join(w))
    pprint.pprint(wordtag_set(p))
