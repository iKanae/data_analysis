#-*- coding: utf-8 -*-
import random
import math

#求圆周率
def cal_Pi(x):
    count_pi=0.0
    count_all=0.0
    while count_all<x:
        a=random.uniform(0,1)
        b=random.uniform(0,1)
        if (a**2+b**2<=1):
            count_pi+=1
        count_all+=1
    return count_pi/count_all*4

#求Buffon问题（随机抛针求圆周率）
def cal_buffon(l,s,x):
    count_buffon=0.0
    count_all=0.0
    pi=math.pi
    l=float(l)
    s=float(s)
    while count_all<x:
        a=random.uniform(0,pi)
        b=random.uniform(0,s/2)
        if (b<=l/2*math.sin(a)):
            count_buffon+=1
        count_all+=1
    return 2*l/s/(count_buffon/count_all)
