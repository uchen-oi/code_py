from sklearn import datasets
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

iris = datasets.load_iris()
X = iris.data
y = iris.target


scaler = StandardScaler()
x_scaled = scaler.fit_transform(X)
knn = KNeighborsClassifier(n_neighbors=9)
knn.fit(x_scaled,y)


scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')
acc=scores.mean()
print(f'模型预测准确率：{acc*100}%')
predict_data=[[1.5 , 3 , 5.8 , 2.2], [6.2 , 2.9 , 4.3 ,1.3]]
predict_data_scaled=scaler.transform(predict_data)
pre=knn.predict(predict_data_scaled)
print(f'预测值：{pre}')



