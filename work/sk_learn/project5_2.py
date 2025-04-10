from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score

# 1. 加载手写字体数据集
digits = load_digits()
X = digits.data
y = digits.target

# 2. 划分训练集和测试集（测试集占20%）
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. 对手写字体进行二值化处理（像素值>8设为1，否则设为0）
threshold = 8
X_train_binary = (X_train > threshold).astype(int)
X_test_binary = (X_test > threshold).astype(int)

# 4. 创建并训练朴素贝叶斯分类器（使用伯努利分布，适用于二值特征）
nb_classifier = BernoulliNB()
nb_classifier.fit(X_train_binary, y_train)

# 5. 在测试集上进行预测
y_pred = nb_classifier.predict(X_test_binary)

# 6. 计算并输出分类准确率
accuracy = accuracy_score(y_test, y_pred)
print(f"分类准确率: {accuracy:.4f}")