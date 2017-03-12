#-*- coding: utf-8 -*-
import distance

#词语相似度(字母重合度)
word1="decisive"
word2="decicive"
sen1=["whatsapp","messenger"]
sen2=["whatsapp","facebook"]
print distance.jaccard(word1,word2)

#词语相似度（编辑距离）
print distance.levenshtein(word1,word2)
print distance.hamming(word1,word2,normalized=True)

#词组/句子相似度（编辑距离）
print distance.levenshtein(sen1,sen2)

#一组比较
tokens=["tubbemate","tubemmate","tube cas"]
print sorted(distance.ilevenshtein("tubemate", tokens))
