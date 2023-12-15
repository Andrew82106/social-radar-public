import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# 读取数据

df = pd.read_csv("./fit.csv")

# 定义特征和目标变量
features = ['Sensitive', 'UserQuota', 'OpinionQuota', 'TimeQuota', 'EmotionQuota']
target = 'HotIndex'

X = df[features]
y = df[target]

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 初始化线性回归模型
model = LinearRegression()

# 拟合模型
model.fit(X_train, y_train)

# 获取模型权重
weights = model.coef_
intercept = model.intercept_

print("模型权重:")
for feature, weight in zip(features, weights):
    print(f"{feature}: {weight}")

# 在测试集上评估模型
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"均方误差 (MSE): {mse}")
