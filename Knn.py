# -*- coding:utf-8 -*-

from numpy import *
import operator
from numpy import ndarray

#load the file
def loadfile(file):
    url=str(file)
    tmp=open(url,"r")
    lines=tmp.readlines()
    dataset=[]
    labels=[]
    data=[]
    for line in lines:
        s=line.strip('\n').split(",")
        data.append(s)
        n=s[4]
        m=[]
        m.append(float(s[0]))
        m.append(float(s[1]))
        m.append(float(s[2]))
        m.append(float(s[3]))
        labels.append(n)
        dataset.append(m)
    return dataset,labels,data

# calculate Euclidean distance
def dist(vector1, vector2):
    return sqrt(sum(power(vector2 - vector1, 2)))

def knn(dataset,k,vector,j):
    list1=[]
    for i in range(0,len(dataset)):
        dis=float(dist(dataset[i,],vector))
        tmp=(j[i],dis)
        list1.append(tmp)
    list1=sorted(list1,key=lambda list1 : list1[1])
    print list1
    labels=list1[0:k]
    a=0
    b=0
    for i in labels:
        if i[0]=='a':
            a=a+1
        elif i[0]=='b':
            b=b+1
    if a>b:
        return 'a'
    elif a<b:
        return 'b'
    elif a==b:
        return "a or b"

def Knn(inX,dataset,labels,k):
    datasetsize=dataset.shape[0]
    #count the distance
    diffmat=tile(inX,(datasetsize,1))-dataset
    sqdiffmat=diffmat**2
    sqdistances=sqdiffmat.sum(axis=1)
    distances=sqdistances**0.5
    classsorted=distances.argsort()
    classcount={}
    for i in range(k):
        votelabel=labels[classsorted[i]]
        classcount[votelabel]=classcount.get(votelabel,0)+1
    classsort=sorted(classcount.items(),key=lambda x:-x[1])
    #classsorted=sorted(classcount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return classsort[0][0]

#print knn(dataset,100,[4,5,20],labels)
def main():
    file=loadfile('/home/kanae/iris.txt')
    labels=file[1]
    dataset=file[0]
    data=file[2]
    dataset=array(dataset)
    for j in range(1,len(data)+1):
        error=0
        for i in range(0,len(data)):
            label=Knn(dataset[i],dataset,labels,j)
            #print label
            #print data[i]
            if str(data[i][4]) != str(label):
                error=error+1
        print j,float(error)/float(len(data))
    return 0