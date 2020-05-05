import generate_dictionary
import json_read

# def str2features(text:str):
# 创建字典
def get_feature(path:str,num):
    return generate_dictionary.get_features(path, num)

def build_feature(path: str, num: int):
    feature = generate_dictionary.get_features(path, num)
    pos_features = []
    for items in json_read.file_load(path + 'pos.txt'):
        a = {}
        for item in items:
            if item in feature.keys():
                a[item] = 'True'
        per_doc_poswords = [a, 'pos']
        pos_features.append(per_doc_poswords)
    neg_features = []
    for items in json_read.file_load(path + 'neg.txt'):
        a = {}
        for item in items:
            if item in feature.keys():
                a[item] = 'True'
        per_doc_negwords = [a, 'neg']
        neg_features.append(per_doc_negwords)
    return pos_features, neg_features
