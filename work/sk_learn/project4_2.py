import pandas as pd
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier

data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain', 'Sunny',
                'Overcast', 'Overcast', 'Rain'],
    'Temp': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot',
             'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal', 'Normal',
                 'High', 'Normal', 'High'],
    'Windy': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong',
              'Weak', 'Strong'],
    'Play': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}

df = pd.DataFrame(data)

le = LabelEncoder()
y = le.fit_transform(df['Play'])

encoder = OrdinalEncoder()
X = encoder.fit_transform(df[['Outlook', 'Temp', 'Humidity', 'Windy']])

model = DecisionTreeClassifier(criterion='entropy', random_state=42)
model.fit(X, y)

# 预测新样本['Rain', 'Hot', 'High', 'Weak']
# OrdinalEncoder()需要指出特征名
x_new = {'Outlook': ['Rain'],
         'Temp': ['Hot'],
         'Humidity': ['High'],
         'Windy': ['Weak']}
x_pre = pd.DataFrame(x_new)

x_encoded = encoder.transform(x_pre)
pred = le.inverse_transform(model.predict(x_encoded))[0]
print(f"预测结果: {pred}")

