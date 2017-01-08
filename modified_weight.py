#-*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

def plot_decision_function(classifier, sample_weight, axis, title):
    # plot the decision function
    xx, yy = np.meshgrid(np.linspace(-4, 5, 500), np.linspace(-4, 5, 500))

    Z = classifier.decision_function(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # plot the line, the points, and the nearest vectors to the plane
    axis.contourf(xx, yy, Z, alpha=0.75, cmap=plt.cm.bone)
    axis.scatter(X[:, 0], X[:, 1], c=y, s=100 * sample_weight, alpha=0.9,
                 cmap=plt.cm.bone)

    axis.axis('off')
    axis.set_title(title)

X=np.r_[np.random.rand(10,2)+[1,1],np.random.rand(10,2)]
y=[1]*10+[0]*10
sample_weight_1=abs(np.random.randn(20))
sample_weight_1[14:]+=5
sample_weight_2=np.ones(20)

clf_weights=svm.SVC()
clf_weights.fit(X,y,sample_weight=sample_weight_1)

clf_no_weights=svm.SVC()
clf_no_weights.fit(X,y)


fig,axes = plt.subplots(1, 2, figsize=(10, 6))
plot_decision_function(clf_no_weights,sample_weight_2,axes[0],'no weights')
plot_decision_function(clf_weights,sample_weight_1,axes[1],'weights')
plt.show()