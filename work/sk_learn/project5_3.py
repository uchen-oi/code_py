from sklearn import datasets
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.preprocessing import MinMaxScaler

wine=datasets.load_wine()
iris=datasets.load_iris()
cancer=datasets.load_breast_cancer()

x1=wine['data']
y1=wine['target']
x2=iris['data']
y2=iris['target']
x3=cancer['data']
y3=cancer['target']

x_train1,x_test1,y_train1,y_test1=train_test_split(x1,y1,test_size=0.2)
x_train2,x_test2,y_train2,y_test2=train_test_split(x2,y2,test_size=0.2)
x_train3,x_test3,y_train3,y_test3=train_test_split(x3,y3,test_size=0.2)

cls=GaussianNB(priors=None)
cls.fit(x_train1,y_train1)
pred1=cls.predict(x_test1)
print("-------------------高斯朴素贝叶斯-------------------")
print("葡萄酒分类准确率：",accuracy_score(y_test1,pred1))
print("葡萄酒混淆矩阵：\n",confusion_matrix(y_test1,pred1))
cls.fit(x_train2,y_train2)
pred2=cls.predict(x_test2)
print("鸢尾花分类准确率：",accuracy_score(y_test2,pred2))
print("鸢尾花混淆矩阵：\n",confusion_matrix(y_test2,pred2))
cls.fit(x_train3,y_train3)
pred3=cls.predict(x_test3)
print("乳腺癌分类准确率：",accuracy_score(y_test3,pred3))
print("乳腺癌混淆矩阵：\n",confusion_matrix(y_test3,pred3))

cls=MultinomialNB()
cls.fit(x_train1,y_train1)
pred1=cls.predict(x_test1)
print("-------------------多项式贝叶斯-------------------")
print("葡萄酒分类准确率：",accuracy_score(y_test1,pred1))
print("葡萄酒混淆矩阵：\n",confusion_matrix(y_test1,pred1))
cls.fit(x_train2,y_train2)
pred2=cls.predict(x_test2)
print("鸢尾花分类准确率：",accuracy_score(y_test2,pred2))
print("鸢尾花混淆矩阵：\n",confusion_matrix(y_test2,pred2))
cls.fit(x_train3,y_train3)
pred3=cls.predict(x_test3)
print("乳腺癌分类准确率：",accuracy_score(y_test3,pred3))
print("乳腺癌混淆矩阵：\n",confusion_matrix(y_test3,pred3))

cls=BernoulliNB(binarize=0.5)
cls.fit(x_train1,y_train1)
pred1=cls.predict(x_test1)
print("-------------------伯努利贝叶斯-------------------")
print("葡萄酒分类准确率：",accuracy_score(y_test1,pred1))
print("葡萄酒混淆矩阵：\n",confusion_matrix(y_test1,pred1))
cls.fit(x_train2,y_train2)
pred2=cls.predict(x_test2)
print("鸢尾花分类准确率：",accuracy_score(y_test2,pred2))
print("鸢尾花混淆矩阵：\n",confusion_matrix(y_test2,pred2))
cls.fit(x_train3,y_train3)
pred3=cls.predict(x_test3)
print("乳腺癌分类准确率：",accuracy_score(y_test3,pred3))
print("乳腺癌混淆矩阵：\n",confusion_matrix(y_test3,pred3))