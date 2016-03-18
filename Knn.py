# -*- coding:utf-8 -*-

from numpy import *
import operator
from numpy import ndarray
import numpy as np

#creating kd_tree
class KD:
    def __init__(self,root=None,left=None,right=None,di=None):
        self.root = root
        self.left = left
        self.right = right
        self.di=di

def createKdtree(datalist):
        lens=len(datalist)
        if lens==0:
            return
        dimension=len(datalist[0])
        maxvar=0
        di=0
        for i in range(dimension):
            list=[]
            for t in datalist:
                list.append(t[i])
            var=np.var(list)
            if var > maxvar:
                maxvar = var
                di = i.,nk.
        datalist.sort(key=lambda x: x[di])
        root=datalist[lens/2]
        tree=KD(root=root,di=di)
        tree.left=createKdtree(datalist[0:(lens/2)])
        tree.right=createKdtree(datalist[lens/2+1:lens])
        return tree

#count the distance
def dist(a,b):
    m=0
    for i in range(len(a)):
        m=m+(a[i]-b[i])*(a[i]-b[i])
    return np.sqrt(m)

def findKnn(goal,tree):
    root=tree.root
    min_dist=dist(goal,root)
    list=[]
    temp_tree=tree
    while temp_tree:
        list.append(temp_tree)
        dis=dist(goal,temp_tree.root)
        if min_dist>dis:
            root=temp_tree.root
            min_dist=dis
        temp_di=temp_tree.di
        if goal[temp_di]<=temp_tree.root[temp_di]:
            temp_tree=temp_tree.left
        else:
            temp_tree=temp_tree.right

    while list:
        back_tree=list.pop()
        temp_di=back_tree.di
        if abs(goal[temp_di] - back_tree.root[temp_di]) < min_dist:
            if goal[temp_di] <= back_tree.root[temp_di]:
                temp_tree = back_tree.right
            else:
                temp_tree = back_tree.left

            if temp_tree:
                list.append(temp_tree)
                temp_dist = dist(goal, temp_tree.root)
                if min_dist > temp_dist:
                    min_dist = temp_dist
                    root = temp_tree.root
    return root, min_dist

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

#for 2 dimensions
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
    classcount={},
    for i in range(k):
        votelabel=labels[classsorted[i]]
        classcount[votelabel]=classcount.get(votelabel,0)+1
    classsort=sorted(classcount.items(),key=lambda x:-x[1])
    #classsorted=sorted(classcount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return classsort[0][0]

def main():
    file=loadfile('.txt')
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




