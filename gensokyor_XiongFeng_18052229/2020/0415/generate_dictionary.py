from nltk.probability import FreqDist, ConditionalFreqDist
from nltk.metrics import BigramAssocMeasures
import json_read


def get_features(path, number):
    poswords = []
    negwords = []
    json_loaded = json_read.file_load(path + 'pos.txt')
    for i in json_loaded:
        poswords.extend(i)
    json_loaded = json_read.file_load(path + 'neg.txt')
    for i in json_loaded:
        negwords.extend(i)
    word_fd = FreqDist()  # 统计全集词频
    cond_word_fd = ConditionalFreqDist()
    # 条件词频
    for word in poswords:
        word_fd[word] += 1
        cond_word_fd['pos'][word] += 1
    for word in negwords:
        word_fd[word] += 1
        cond_word_fd['neg'][word] += 1
    # 积极词num
    pos_word_count = cond_word_fd['pos'].N()
    # 消极词num
    neg_word_count = cond_word_fd['neg'].N()
    # 总词num
    total_word_count = pos_word_count + neg_word_count
    # 所有词的信息量
    word_scores = {}
    for word, freq in word_fd.items():
        # 计算相关程度
        pos_score = BigramAssocMeasures.chi_sq(cond_word_fd['pos'][word], (freq, pos_word_count), total_word_count)
        neg_score = BigramAssocMeasures.chi_sq(cond_word_fd['neg'][word], (freq, neg_word_count), total_word_count)
        word_scores[word] = pos_score + neg_score
        # 按信息量排序
    best_vals = sorted(word_scores.items(), key=lambda item: item[1], reverse=True)[:number]
    best_words = set([w for w, s in best_vals])

    return dict([(word, True) for word in best_words])


if __name__ == '__main__':
    import pprint

    features = get_features('./res/processed/', 100)
    pprint.pprint(features)
