import jieba_devide
import gensim


test_exa=jieba_devide.outwords("res/ch.txt","UTF-8")
lda=gensim.models.LdaModel.load("lad.model")
bow=dictionary.doc2bow(test_exa)
print(lda.get_document_topics(bow))