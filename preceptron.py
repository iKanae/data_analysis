# -*- coding:utf-8 -*-
import numpy as np
import operator

def loadDataset():
    dataMat=[];lableMat=[]
    fr=open(".txt")
    for line in fr:
        lineArr=line.strip('\n').split(',')
        dataMat.append([float(lineArr[0]),float(lineArr[3])])
        lableMat.append(int(lineArr[4]))
    return dataMat,lableMat

def preceptron_test(data,labels):
    w=[1]*len(data[0])
    b=1
    a=0.00001
    n=20000
    for i in range(n):
        for sample in data:
            label=labels[data.index(sample)]
            #print sample,w,label,data.index(sample)
            dis=label*int((np.mat(sample)*np.mat(w).T+b))
            if dis<=0:
                w=w+a*label*np.mat(sample)
                b=b+a*label
    return w,b

def plotBestFit(w,b):
    import matplotlib.pyplot as plt
    weights=np.array(w)
    dataMat,labelMat=loadDataset()
    dataArr=np.array(dataMat)
    n=np.shape(dataArr)[0]
    xcord1=[]
    ycord1=[]
    xcord2=[]
    ycord2=[]
    for i in range(n):
        if int(labelMat[i])==1:
            xcord1.append(dataArr[i,0])
            ycord1.append(dataArr[i,1])
        else:
            xcord2.append(dataArr[i,0])
            ycord2.append(dataArr[i,1])
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.scatter(xcord1,ycord1,s=30,c='red',marker='s')
    ax.scatter(xcord2,ycord2,s=30,c='green')
    x=np.arange(0.0,15.0,0.1)
    y=(-b-weights[0][0]*x)/weights[0][1]
    ax.plot(x,y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()

def main():
    data,label=loadDataset()
    w,b=preceptron_test(data,label)
    print plotBestFit(w,b)