# -*- coding:utf-8 -*-
import numpy as np

class mytree():
    def __init__(self,x=None,left=None,right=None,y=None):
        self.x = x
        self.left = left
        self.right = right
        self.y=y

def cutvalue(dataset,index):
    dataset=sorted(dataset,key=lambda x:x[0])
    dataseta=dataset[0:index]
    datasetb=dataset[index+1:]
    xalist=[x[1] for x in dataseta]
    xblist=[x[1] for x in datasetb]
    vara=np.var(xalist)*len(xalist)
    varb=np.var(xblist)*len(xblist)
    value=vara+varb
    return value

def createTree(dataset):
  num=len(dataset)
  #stop point
  if num<=2:
      return
  minnum=10000.0
  index=0
  x=0
  y=0
  dataset=sorted(dataset,key=lambda x:x[0])
  for i in range(num):
    value=cutvalue(dataset,i)
    if value<minnum:
        minnum=value
        x=dataset[i][0]
        y=dataset[i][1]
        index=i
  tree=mytree(x=x,y=y)
  dataset_left=dataset[0:index]
  dataset_right=dataset[index+1:]
  tree.left=createTree(dataset_left)
  tree.right=createTree(dataset_right)
  return tree