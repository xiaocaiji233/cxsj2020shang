import json_read


def seperate(path: str):
    orin = json_read.file_load(path + 'word_devided.txt')
    pos = []
    neg = []
    for i in orin:
        if i[0] == '1':
            pos.append(i[1])
        elif i[0] == '0':
            neg.append(i[1])
    return {'positive': pos, 'negative': neg}


def test_process(path: str):
    import jieba_devide
    orin = open(path, encoding="UTF-8").read()
    flag = []
    words = []
    rows = jieba_devide.doc2row(orin)
    for i in rows:
        flag.append(i[0])
        words.append(jieba_devide.ch_jieba(i[2:]))
    return flag, words


def seperate_save(path: str):
    to_save = seperate(path)
    f_pos = open(path + 'pos.txt', 'w')
    f_neg = open(path + 'neg.txt', 'w')
    json_read.file_save(path, 'pos.txt', to_save['positive'])
    json_read.file_save(path, 'neg.txt', to_save['negative'])
    # json.dump(to_save['positive'], f_pos)
    # json.dump(to_save['negative'], f_neg)
    f_pos.close()
    f_neg.close()
    # print(to_save['positive'][2,0:3])


if __name__ == '__main__':
    seperate_save('./res/processed/')
