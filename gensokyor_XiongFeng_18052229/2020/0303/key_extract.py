import jieba_devide
import gensim
import os


# from pprint import pprint

def generateTR(p, pn):  # 分析语料库并生成lda模型,输出指定文档的关键词信息
    # 加载语料
    train = []
    corpus_path = p
    file_list = os.listdir(corpus_path)
    for i in file_list:
        full_name = corpus_path + i
        train.append(jieba_devide.outwords(full_name, "UTF-8"))
    # pprint(train)

    # 使用语料生成lda模型
    dictionary = gensim.corpora.Dictionary(train)
    corpus = [dictionary.doc2bow(text) for text in train]
    # lda = gensim.models.LdaModel(corpus=corpus, id2word=dictionary, num_topics=20)
    lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=5)  # 载入语料,并使其向量化后按照词频划分出5种主题
    # for topic in lda.print_topic(num_words=8):#something wrong!!
    #     print(topic)
    lda.save("lda.model")  # 保存模型

    # 载入待分析的doc,并预测
    test_exa = jieba_devide.outwords(pn, "UTF-8")  # 对新doc做分词处理
    # lda = gensim.models.ldamodel.LdaModel.load("lda.model")#.LdaModel.load("lda.model")
    bow = dictionary.doc2bow(test_exa)  #
    doc_lda = lda[bow]
    # print(lda.get_document_topics(bow))
    # print(doc_lda)

    # 打印分析结果
    for topic in doc_lda:
        print("%s\t%f\n" % (lda.print_topic(topic[0]), topic[1]))
