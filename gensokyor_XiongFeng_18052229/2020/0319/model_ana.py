import issues_process
import time_pieces_generate
import devide_issues
import nltk_process
import collections
import gensim
import json


def get_all_resources(issues_path: str, release_path: str):
    issues = issues_process.issues_process(issues_path)
    times = time_pieces_generate.port(release_path)
    ana_res = devide_issues.match(issues, times)
    processed = nltk_process.bodies_process(ana_res)
    to_de = get_to_delete(processed)
    # pprint(to_de)
    for i, j in processed.items():
        for k in to_de:
            while k in j:
                j.remove(k)

    return processed


def get_to_delete(all_editon: dict):
    limit = len(all_editon.keys()) / 3 - 1
    releases_name = all_editon.keys()
    c = collections.Counter()
    for i in releases_name:
        uni = set_unique(all_editon[i])
        # pprint(uni)
        for j in uni:
            c[j] += 1
    to_delete = []
    for i, j in c.items():
        if float(j) > limit:
            to_delete.append(i)
    return to_delete


def set_unique(arr: list):
    unsort_unique = list(set(arr))
    unsort_unique.sort(key=arr.index)

    return unsort_unique


def generateTR(p: dict):  # 分析语料库并生成lda模型,输出关键词信息预测指定文档
    # 加载语料
    train = [j for i, j in p.items()]

    # pprint(train)

    # 使用语料生成lda模型
    dictionary = gensim.corpora.Dictionary(train)
    corpus = [dictionary.doc2bow(text) for text in train]
    # lda = gensim.models.LdaModel(corpus=corpus, id2word=dictionary, num_topics=20)
    num_topics = 10
    num_top_words = 10
    lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary,
                                          num_topics=num_topics)  # 载入语料,并使其向量化后按照词频划分出5种主题
    lda.save("lda.model")  # 保存模型
    text_num = len(train)
    for i in lda.show_topics():
        # lda.print_topic(i, topn=num_top_words)
        print(i[0], ':', i[1])


def save_processed(processed_data: list):
    f = open('./processed.txt', 'w+')
    json.dump(processed, f)


def load_processed():
    readed = open('./processed.txt', encoding='UTF')
    result = json.load(readed)
    return result


def dict2lists(orin: dict):
    results = []
    for i, j in orin.items():
        results.append(j)
    return results


if __name__ == '__main__':
    from pprint import pprint

    processed = get_all_resources('./json/', './json/release/')
    # processed=dict2lists(processed)
    save_processed(processed)
    processed = load_processed()
    generateTR(processed)
