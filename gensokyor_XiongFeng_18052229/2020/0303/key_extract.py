import jieba_devide
import gensim
import os


def generateTR(p):
    train = []
    corpus_path = p
    file_list = os.listdir(corpus_path)
    for i in file_list:
        full_name = corpus_path + i
        train.append(jieba_devide.outwords(full_name,"UTF-8"))
    dictionary = gensim.corpora.Dictionary(train)
    #corpus = [dictionary.doc2bow(text) for text in train]
    #lda = gensim.models.LdaModel(corpus=corpus, id2word=dictionary, num_topics=100)
    #lda.save("lad.model")

    test_exa = jieba_devide.outwords("res/ch.txt", "UTF-8")
    lda = gensim.models.LdaModel.load("lad.model")
    bow = dictionary.doc2bow(test_exa)
    print(lda.get_document_topics(bow))
