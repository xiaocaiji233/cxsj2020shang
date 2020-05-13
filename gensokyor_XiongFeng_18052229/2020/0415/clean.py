import re


def cleantext(orin: str):
    textfile = open('./正则表达式.txt', encoding="UTF-8").read()
    orin = re.sub(textfile, '', orin)
    return orin


if __name__ == "__main__":
    test_text = '如果我们在输入的文本框中要阻止http://www.baidu.com这个URL，传统的方法是用上面的正则表达式去匹配文本框中的URL，读出所有的URL之后在跟要阻止的URL去比较，但是这种方法有一个'
    print(cleantext(test_text))
    textfile = open('./正则表达式.txt', encoding="UTF-8").read()
    print(textfile)
