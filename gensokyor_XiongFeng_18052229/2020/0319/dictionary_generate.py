import gensim


def totallist(devidedpieces: dict):  # 获取总集
    times = devidedpieces.keys()
    total = []
    for i in times:
        total += devidedpieces[i]
    return total


def generate_dict(orin: list):  # 生成lda模型
    dictionary = gensim.corpora.Dictionary(orin)
    corpus = [dictionary.doc2bow(text) for text in dictionary]
    lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=5)
    lda.save("lda.model")
    return {dictionary: dictionary, corpus: corpus, lda: lda}


def get_allmat(devidedpieces: dict):  # 对外接口
    total = totallist(devidedpieces)
    allthing_you_need = generate_dict(total)
    return allthing_you_need
