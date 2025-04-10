from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

iris = datasets.load_iris()
x=iris.data
y=iris.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

cls=GaussianNB(priors=None)
cls.fit(x_train,y_train)
pred=cls.predict(x_test)

print("鸢尾花数据集分类")
print("预测标签：",pred)
print("真实标签：",y_test)
print("准确率:", accuracy_score(y_test, pred))
