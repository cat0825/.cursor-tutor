import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
from scipy.optimize import minimize

# 加载数据
data = pd.read_csv('data.csv')

# 分析数据，选择重点关注的物料
top_materials = data.groupby('material')['quantity'].sum().sort_values(ascending=False).head(6)

# 建立ARIMA模型
model = ARIMA(data['quantity'], order=(1,1,1))
model_fit = model.fit(disp=0)

# 定义优化目标函数和约束条件
def objective(x):
    return x[0]**2 + x[1]**2

def constraint(x):
    return x[0] + x[1] - 100

# 求解优化问题
x0 = [0, 0]
result = minimize(objective, x0, constraints={'type': 'eq', 'fun': constraint})