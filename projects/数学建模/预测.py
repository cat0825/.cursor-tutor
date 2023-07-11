import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_excel(r"C:\Users\17591\Desktop\demo.xlsx")  # 替换为你的数据文件路径

# 提取特征和目标变量
features = data[['文物采样点']]
target = data[['二氧化硅(SiO2)', '氧化钠(Na2O)', '氧化钾(K2O)', '氧化钙(CaO)', '氧化镁(MgO)', '氧化铝(Al2O3)',
                '氧化铁(Fe2O3)', '氧化铜(CuO)', '氧化铅(PbO)', '氧化钡(BaO)', '五氧化二磷(P2O5)', '氧化锶(SrO)', '氧化锡(SnO2)',
                '二氧化硫(SO2)']]


# 将风化点特征转换为数值型
features['文物采样点'] = features['文物采样点'].str.extract('(\d+)').astype(int)

# 拟合线性回归模型
regression_model = LinearRegression()
regression_model.fit(features, target)

# 预测风化前的化学成分含量
predicted_target = regression_model.predict(features)

# 可视化预测结果
plt.figure(figsize=(10, 6))
for i, column in enumerate(target.columns):
    plt.subplot(4, 4, i + 1)
    plt.scatter(features, target[column], color='blue', label='Actual')
    plt.scatter(features, predicted_target[:, i], color='red', label='Predicted')
    plt.xlabel('文物采样点')
    plt.ylabel(column)
    plt.legend()

plt.tight_layout()
plt.show()
