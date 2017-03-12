#-*- coding: utf-8 -*-
from gensim.models import word2vec

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences=word2vec.Text8Corpus('/home/ikanae/123_result.txt')
model=word2vec.Word2Vec(sentences,size=200,min_count=2)

#调用已存储的模型
model=word2vec.Word2Vec.load('sim1.model')

#输出模型
print model

#模型预测-得到相近词
wordlist=model.most_similar(u'令狐冲')
for item in wordlist:
    print item[0]

#模型预测-两词的相似度
y1=model.similarity(u'令狐冲',u'岳灵珊')
print "sim1:",y1

#模型预测-相近词与相似度词组
y2=model.most_similar(u'令狐冲',topn=20)
for item in y2:
    print item[0],item[1]


print model[u'令狐冲']

model.save(u"sim1.model")
