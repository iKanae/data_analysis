#-*- coding: utf-8 -*-
from sklearn import tree
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.metrics import precision_recall_curve

#提取数据集
def getdoc(url):
    fs = open(url)
    data = []
    labels=[]
    for line in fs.readlines():
        atr=line.strip("\n").split(',')[:-1]
        label=line.strip("\r\n").split(',')[-1:]
        data.append(atr)
        labels.append(label)
    return data,labels

#分拆训练集
data,label=getdoc('transfusion.txt')
label=np.array(label)
labels=label
data=np.array(data)
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size = 0.2)

#训练模型（可用于多类别CART算法）
clf=tree.DecisionTreeClassifier(criterion='entropy')
clf=clf.fit(x_train,y_train)

#预测指定输入的类别
print clf.predict([18,345,12,0])

#每个特征的权重
print clf.feature_importances_

#测试模型效果
answer=clf.predict(x_test)
print (np.mean(answer == y_test))

#准确率&召回率
y_train=np.array(y_train)
x_train=np.array(x_train)
precision, recall, thresholds = precision_recall_curve(y_train, clf.predict(x_train))

#输出决策树图
tree.export_graphviz(clf,out_file='tree.dot')
