# -*- coding:utf-8 -*-

import numpy as np

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
                di = i
        datalist.sort(key=lambda x: x[di])
        root=datalist[lens/2]
        tree=KD(root=root,di=di)
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

'''
data=[[2,3],[5,4],[9,6],[4,7],[8,1],[7,2]]
data_tree=createKdtree(data)
print findKnn([1,2],data_tree)
'''