import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为中文显示

# 从Excel文件读取数据
data = pd.read_excel(r"C:\Users\17591\Desktop\file.xlsx")

# 提取相关列数据
surface_wind = data['表面风化']
glass_type = data['类型']
pattern = data['纹饰']
color = data['颜色']

# 执行卡方检验并打印结果
def perform_chi2_test(variable1, variable2):
    observed = pd.crosstab(variable1, variable2)
    chi2, p_val, _, _ = chi2_contingency(observed)
    print("变量关系:", variable1.name, "与", variable2.name)
    print("卡方统计量: ", chi2)
    print("P值: ", p_val)
    print()

# 对类型、纹饰和颜色与表面风化分别进行卡方检验
perform_chi2_test(glass_type, surface_wind)
perform_chi2_test(pattern, surface_wind)
perform_chi2_test(color, surface_wind)

# 可视化卡方检验结果
def visualize_chi2_test(variable1, variable2):
    observed = pd.crosstab(variable1, variable2)
    chi2, p_val, _, _ = chi2_contingency(observed)

    # 创建柱状图
    plt.figure(figsize=(8, 6))
    sns.countplot(x=variable1, hue=variable2)
    plt.title("变量关系: {} vs {}，P值: {:.5f}".format(variable1.name, variable2.name, p_val))
    plt.xlabel(variable1.name)
    plt.ylabel("Count")
    plt.legend(title=variable2.name)
    plt.show()

    # 创建热力图
    plt.figure(figsize=(8, 6))
    sns.heatmap(observed, annot=True, cmap="YlGnBu")
    plt.title("变量关系: {} vs {}，P值: {:.5f}".format(variable1.name, variable2.name, p_val))
    plt.xlabel(variable2.name)
    plt.ylabel(variable1.name)
    plt.show()

# 对类型、纹饰和颜色与表面风化分别进行卡方检验和可视化
visualize_chi2_test(glass_type, surface_wind)
visualize_chi2_test(pattern, surface_wind)
visualize_chi2_test(color, surface_wind)