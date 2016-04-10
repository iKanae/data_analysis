# -*- coding:utf-8 -*-
import numpy as np
from math import log

class mytree():
    def __init__(self,x=None,left=None,right=None,y=None):
        self.x = x
        self.left = left
        self.right = right
        self.y=y

def shannon_Ent(labels):
    labels=np.array(labels)
    num=float(len(labels))
    sumlist=sum(labels)/num
    if sumlist!=1 and sumlist!=0:
        n=-sumlist*log(sumlist,2)-(1-sumlist)*log(1-sumlist,2)
    else:
        n=0
    return n

def choose_best_feature(dataset,labels):
    hd=shannon_Ent(labels)
    dataset=np.array(dataset)
    plist=[]
    hda=0
    hdb=0
    for j in range(len(dataset[0])):
        alist=[]
        blist=[]
        numa=0
        for i in range(len(dataset)):
            if dataset[i,j]==1:
                alist.append(labels[i])
                numa=numa+1
            else:
                blist.append(labels[i])
        hda=shannon_Ent(alist)
        hdb=shannon_Ent(blist)
        p=numa/float(len(dataset))
        n=hd-hda*p-hdb*(1-p)
        plist.append(n)
    return plist
