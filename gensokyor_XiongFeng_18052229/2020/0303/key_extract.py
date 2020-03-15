import jieba_devide
import gensim
import os


def generateTR(p,pn):  # 分析语料库并生成lda模型,输出指定文档的关键词信息
    train = []
    corpus_path = p
    file_list = os.listdir(corpus_path)
    for i in file_list:
        full_name = corpus_path + i
        train.append(jieba_devide.outwords(full_name, "UTF-8"))
    dictionary = gensim.corpora.Dictionary(train)
    corpus = [dictionary.doc2bow(text) for text in train]
    lda = gensim.models.LdaModel(corpus=corpus, id2word=dictionary, num_topics=100)
    lda.save("lad.model")

    test_exa = jieba_devide.outwords(pn, "UTF-8")
    #lda = gensim.models.ldamodel.LdaModel.load("lad.model")#.LdaModel.load("lad.model")
    bow = dictionary.doc2bow(test_exa)
    doc_lda=lda[bow]
    print(lda.get_document_topics(bow))
    print(doc_lda)
    for topic in doc_lda:
        print("%s\t%f\n"%(lda.print_topic(topic[0]),topic[1]))
