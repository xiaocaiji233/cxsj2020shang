import random
import sklearn
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import dictionary_seperate
import pos_neg_seperate


# train:list
# [[corpus:dict,tag:str].......]
def training(train: list, classifier):
    classifier = SklearnClassifier(classifier)
    classifier.train(train)
    return classifier


def predict_per(classifier, single_sample):
    return classifier.classify(single_sample)


def predicts(classifier, samples):
    return classifier.classify_many(samples)


def ana(corpus_path: str, features_num: int, classifier):
    posfeatures, negfeaatures = dictionary_seperate.build_feature(corpus_path, features_num)
    random.shuffle(posfeatures)
    random.shuffle(negfeaatures)
    posi = int(len(posfeatures) * 0.9)
    nesi = int(len(negfeaatures) * 0.9)
    test = posfeatures[:posi] + negfeaatures[:nesi]
    train = posfeatures[posi + 1:] + negfeaatures[nesi + 1:]
    flags, test_words = pos_neg_seperate.test_process(test)
    filter = training(train, classifier)
    preds = predicts(filter, test_words)
    n = 0
    s = len(preds)
    for i in range(0, s):
        if preds[i] == flags[i]:
            n += 1
    return n / s


if __name__ == '__main__':
    print('BernoulliNB`s accuracy is %f' % ana('./res/processed/', 2000, BernoulliNB()))
    print('MultinomiaNB`s accuracy is %f' % ana('./res/processed/', 2000, MultinomialNB()))
    print('LogisticRegression`s accuracy is %f' % ana('./res/processed/', 2000, LogisticRegression(solver='lbfgs')))
    print('SVC`s accuracy is %f' % ana('./res/processed/', 2000, SVC(gamma='scale')))
    print('LinearSVC`s accuracy is %f' % ana('./res/processed/', 2000, LinearSVC()))
    # print('NuSVC`s accuracy is %f' %score(NuSVC()))
