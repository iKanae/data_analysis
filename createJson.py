#-*- coding: utf-8 -*-
import json

#提取基础数据并转换成json
def getJson(url):
    fs = open(url)
    data ={}
    for line in fs.readlines():
        localid=line.strip("\n").split(',')[0]
        data['localid']=localid
        category=line.strip("\n").split(',')[1]
        data['category'] = category
        url=line.strip("\n").split(',')[2]
        data['url'] = url
        gp = line.strip("\n").split(',')[3]
        data['gp'] = gp
        filesize=line.strip("\n").split(',')[4]
        data['filesize'] = filesize
        with open('testlocal.json', 'a') as f:
            f.write(json.dumps(data))
    return 0