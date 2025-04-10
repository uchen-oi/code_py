import numpy as np
from sklearn.neighbors import KNeighborsClassifier

learning_dataset = {
    "宝贝当家": [45, 2, 9, "喜剧片"],
    "美人鱼": [21, 17, 5, "喜剧片"],
    "澳门风云3": [54, 9, 11, "喜剧片"],
    "功夫熊猫3": [39, 0, 31, "喜剧片"],
    "谋影重重": [5, 2, 57, "动作片"],
    "叶问3": [3, 2, 65, "动作片"],
    "伦敦陷落": [2, 3, 55, "动作片"],
    "我的特工爷爷": [6, 4, 21, "动作片"],
    "奔爱": [7, 46, 4, "爱情片"],
    "夜孔雀": [9, 39, 8, "爱情片"],
    "代理情人": [9, 38, 2, "爱情片"],
    "新步步惊心": [8, 34, 17, "爱情片"]
}
testData={"老友记": [29, 10, 2, "？片"]}

X_data = []
Y_data = []

for movie, data in learning_dataset.items():
    X_data.append(data[:3])
    Y_data.append(data[3])

neigh=KNeighborsClassifier(n_neighbors=3)
neigh.fit(X_data, Y_data)

test_data = testData['老友记'][:-1]
predict_data=np.array(test_data).reshape(1,-1)
print(neigh.predict(predict_data))