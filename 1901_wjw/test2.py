# -*- coding: utf-8 -*-
import nltk


tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
paragraph = 'My name is Tom. I am a boy. I like soccer!'
sentences = tokenizer.tokenize(paragraph)
words = WordPunctTokenizer().tokenize(sentences)
tags = nltk.pos_tag(words)
tags = [];
for tokens in words:
    tags.append(nltk.pos_tag(tokens))

print(sentences)
print(words)
print(tags)