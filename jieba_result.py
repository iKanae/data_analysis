#-*- coding: utf-8 -*-
import jieba

fin=open('123.txt','r')
fou=open('123_result.txt','w')

line=fin.readline()
while line:
    newline=jieba.cut(line,cut_all=False)
    str_out=' '.join(newline).encode('utf-8').replace('，','').replace('。','')\
    .replace('(','').replace(')','').replace('!','').replace('-','').replace('？','')\
    .replace('”','').replace('：','').replace('“','').replace('、','').replace('！','')\
    .replace('…','').replace('《','').replace('》','').replace('.','')
    print str_out,
    print >> fou,str_out,
    line=fin.readline()
fin.close()
fou.close()
