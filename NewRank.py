#from reddit algorithm
from datetime import datetime
from math import log

def getTimespan(dt):
    startDatetime=datetime.strptime("2016-03-22 00:00:00","%Y-%m-%d %H:%M:%S")
    timespan=(datetime.strptime(dt,"%Y-%m-%d %H:%M:%S")-startDatetime).total_seconds()
    return timespan

def getDownloads(NativeDownloads,ManualDownloads,isCheating):
    downloads=NativeDownloads*0.7+ManualDownloads*0.2-10000*isCheating
    return downloads

def getRankScore(NativeDownloads,ManualDownloads,isCheating,dt,isTop):
    if isTop<=2:
        isToprank=1
    else:
        isToprank=isTop+1
    rankScore=log(getDownloads(NativeDownloads,ManualDownloads,isCheating),10)+(getTimespan(dt)/100000)*(1/isToprank)^2
    return rankScore