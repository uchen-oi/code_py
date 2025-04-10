import numpy as np
from scipy.io import loadmat
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 1. 加载数据
# 假设 data_digits.mat 文件中有两个变量：X 和 y
data = loadmat('data_digits.mat')
X = data['X']  # 特征矩阵 (5000 x 400)
y = data['y'].ravel()  # 标签向量 (5000,)，需要展平为一维数组

# 2. 数据集划分
# 将数据集划分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. 创建逻辑回归模型
# 设置 multi_class='multinomial' 表示多分类问题，solver='lbfgs' 是适合多分类的求解器
model = LogisticRegression(solver='lbfgs', max_iter=500)

# 4. 训练模型
model.fit(X_train, y_train)

# 5. 预测
y_pred = model.predict(X_test)

# 6. 评估模型
accuracy = accuracy_score(y_test, y_pred)
print(f"模型准确率: {accuracy * 100:.2f}%")

# 打印分类报告
print("分类报告:")
print(classification_report(y_test, y_pred))