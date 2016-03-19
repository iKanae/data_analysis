# -*- coding:utf-8 -*-

import numpy as np

class KD:
    def __init__(self,root=None,left=None,right=None,di=None,label=None):
        self.root = root
        self.left = left
        self.right = right
        self.di=di
        self.label=label

def createKdtree(datalist,labels):
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
        tree=KD(root=root,di=di,label=labels[lens/2])
        tree.left=createKdtree(datalist[0:(lens/2)],labels[0:(lens/2)])
        tree.right=createKdtree(datalist[lens/2+1:lens],labels[lens/2+1:lens])
        return tree

def dist(a,b):
    m=0
    for i in range(len(a)):
        m=m+(a[i]-b[i])*(a[i]-b[i])
    return np.sqrt(m)

def findKnn(goal,tree,k):
    root=tree.root
    min_dist=dist(goal,root)
    label=tree.label
    list=[]
    klist=[]
    count=1
    temp_tree=tree
    while temp_tree:
        list.append(temp_tree)
        dis=dist(goal,temp_tree.root)
        label=temp_tree.label
        if count<=k:
            klist.append([temp_tree.root,dis,label])
        if min_dist>dis:
            root=temp_tree.root
            if count>k:
                klist.sort(key=lambda x:x[1])
                klist.pop()
                klist.append([temp_tree.root,dis,label])
            min_dist=dis
        temp_di=temp_tree.di
        if goal[temp_di]<=temp_tree.root[temp_di]:
            temp_tree=temp_tree.left
        else:
            temp_tree=temp_tree.right
        count+=1

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
                    label=temp_tree.label

    temp_point=[root,min_dist,label]

    if temp_point not in klist:
        klist.sort(key=lambda x:x[1])
        klist.pop()
        klist.append(temp_point)

    return root, min_dist,label,klist


#test code
data=[[2,3],[5,4],[9,6],[4,7],[8,1],[7,2],[1,1],[9,10],[20,1],[3,6],[9,9],[11,2],[11,1]]
labels=["a","a","b","b","a","b","a","a","a","a","b","b","a"]
data_tree=createKdtree(data,labels)
list=findKnn([1,2],data_tree,3)[3]