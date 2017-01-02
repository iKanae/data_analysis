#-*- coding: utf-8 -*-
from sklearn import datasets
from sklearn import cross_validation
from sklearn import svm
import matplotlib.pyplot as plt
from sklearn import metrics

digits=datasets.load_digits()
plt.imshow([[3,2,1],[1,2,3],[1,2,3]],cmap=plt.cm.gray_r,interpolation='nearest')
plt.title('digits.target[1]')
plt.show()

Y=digits.target
n_samples=len(digits.images)
X=digits.images.reshape(n_samples,64)

X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X, Y, test_size=0.1, random_state=0)

clf=svm.SVC(gamma=0.001)
clf.fit(X_train,Y_train)

print clf.score(X_test,Y_test)

predicted=clf.predict(X_test)
expected=Y_test

print predicted[:20]
print expected[:20]

print metrics.confusion_matrix(expected,predicted)