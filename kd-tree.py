# -*- coding:utf-8 -*-

import numpy as np

class KD_node:
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
                di = i
        datalist.sort(key=lambda x: x[di])
        root=datalist[lens/2]
        tree=KD_node(root=root,di=di)
        tree.left=createKdtree(datalist[0:(lens/2)])
        tree.right=createKdtree(datalist[lens/2+1:lens])
        return tree

def dist(a,b):
    m=0
    for i in range(len(a)):
        m=m+(a[i]-b[i])*(a[i]-b[i])
    return np.sqrt(m)

def findKnn(goal,tree):
    root=tree.root
    dis=dist(goal,root)
    while root:
        dis_left=dist(goal,tree.left.root)
        dis_right=dist(goal,tree.right.root)
    return dis


#data=[[2,3],[5,4],[9,6],[4,7],[8,1],[7,2]]
#data_tree=createKdtree(data)
#data2=[[2,3]]