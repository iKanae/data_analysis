import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import math
import nltk

def loadfile(url):
    fr=open(url)
    dataset=[]
    labels=[]
    allwordlist=[]
    for line in fr:
        lineArr=line.strip('\n')
        tokens=nltk.word_tokenize(lineArr)
        token=set(tokens)
        labels.append(tokens[0:1])
        dataset.append(tokens[1:])
        allwordlist+=tokens[1:]
    allwordlist=list(set(allwordlist))
    return dataset,labels,allwordlist


def trainNB(url):
    dataset,labels,allwordlist=loadfile(url)
    wordmatrix=createwordmatrix(dataset,labels,allwordlist)
    pbmatrix=(wordmatrix+1)/(len(wordmatrix[0])+np.shape(wordmatrix)[0])
    return allwordlist,wordmatrix,pbmatrix

def testNB(url,allwordlist,wordmatrix,pbmatrix):
    fr=open(url)
    dataset=[]
    for line in fr:
        lineArr=line.strip('\n')
        tokens=nltk.word_tokenize(lineArr)
        token=list(set(tokens))
        dataset.append(tokens)
    testmatrix=np.zeros([len(dataset),len(allwordlist)])

    for wordlist in dataset:
        for word in allwordlist:
            if word in wordlist:
                testmatrix[dataset.index(wordlist)][allwordlist.index(word)]=1
            else:
                testmatrix[dataset.index(wordlist)][allwordlist.index(word)]=0
    return 0


def createwordmatrix(dataset,labels,allwordlist):
    labelset=list(set(map(lambda x: x[0], [y for y in labels])))
    wordlist=[]
    wordmatrix=np.zeros([len(dataset),len(allwordlist)])
    pamatrix=np.zeros([len(labelset),len(allwordlist)])
    for lists in dataset:
        for word in lists:
            if word in allwordlist:
                wordmatrix[dataset.index(lists)][allwordlist.index(word)]=1

    sumvector=np.zeros([len(labelset),len(allwordlist)])
    for label in labelset:
        for testlabel in labels:
            if testlabel==label:
                sumvector[labelset.index(label)]=sumvector[labelset.index(label)]+wordmatrix[labels.index(label)]

    print sumvector
    '''
    for label in labelset:
        for word in allwordlist:
            pamatrix[labelset.index(label)][allwordlist.index(word)]
    '''


    '''
    for label in labelset:
        for i in range(len(allwordlist)):
            index=labelset.index(label)
            if allwordlist[i] in wordlist[labelset.index(label)]:
                wordmatrix[labelset.index(label)][i]=1
    '''
    return sumvector

url="/home/kanae/spam.txt"
url1="/home/kanae/spam1.txt"
#=loadfile(url)
#print labels

#labels=[[1],[1],[3],[2],[1]]
#print set(labels[:][0])
allwordlist,wordmatrix,pbmatrix=trainNB(url)
print wordmatrix
#print np.zeros([2,3])
#a=np.zeros([2,3])
#b=np.ones([2,3])
#print a+b