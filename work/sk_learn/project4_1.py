from sklearn.datasets import load_wine
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

wine=load_wine()
X=wine.data
y=wine.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

cart=DecisionTreeClassifier(criterion='gini',random_state=42)
cart.fit(X_train, y_train)
y_pred = cart.predict(X_test)


print('\n')
print("CART 算法结果：")
print("真实标签:", y_test)
print("预测标签:", y_pred)
print("准确率:", accuracy_score(y_test, y_pred))


id3=DecisionTreeClassifier(criterion='entropy',random_state=42)
id3.fit(X_train, y_train)
y_pred = id3.predict(X_test)

print('\n')
print("ID3 算法结果：")
print("真实标签:", y_test)
print("预测标签:", y_pred)
print("准确率:", accuracy_score(y_test, y_pred))
