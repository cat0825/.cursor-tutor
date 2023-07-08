import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

# 从Excel文件读取数据
data_sheet1 = pd.read_excel(r"C:\Users\17591\Desktop\file.xlsx", sheet_name='Sheet1')
data_sheet2 = pd.read_excel(r"C:\Users\17591\Desktop\file.xlsx", sheet_name='Sheet2')

# 将文物编号作为索引列，并将两个表单按照文物编号进行合并
data_sheet1.set_index('文物编号', inplace=True)
data_sheet2.set_index('文物采样点', inplace=True)
merged_data = pd.concat([data_sheet1, data_sheet2], axis=1)

# 数据预处理
merged_data.dropna(subset=['表面风化'], inplace=True)  # 删除表面风化为空的样本
merged_data.fillna(0, inplace=True)  # 将其他缺失值填充为0

# 数据分组
wind_group = merged_data.groupby('表面风化')

# 数据列筛选
numeric_columns = [column for column in merged_data.columns[2:] if pd.api.types.is_numeric_dtype(merged_data[column])]

# t检验
for i in range(len(numeric_columns) - 1):
    for j in range(i + 1, len(numeric_columns)):
        col1 = numeric_columns[i]
        col2 = numeric_columns[j]
        t_stat, p_val = ttest_ind(merged_data[col1], merged_data[col2])
        print(f"变量 '{col1}' 和 '{col2}' 之间的t检验结果:")
        print("t统计量:", t_stat)
        print("P值:", p_val)
        print()



# t检验
wind_grouped = [group_data[column] for wind, group_data in wind_group for column in merged_data.columns[2:]]
t_stat, p_val = ttest_ind(wind_grouped[0], wind_grouped[1])
print("风化等级间的t检验结果:")
print("t统计量:", t_stat)
print("P值:", p_val)
print()

# 数据可视化
plt.figure(figsize=(10, 6))
sns.boxplot(x='表面风化', y='氧化钡(BaO)', data=merged_data)
plt.xlabel('表面风化等级')
plt.ylabel('氧化钡(BaO)含量')
plt.title('不同表面风化等级下氧化钡含量分布')
plt.show()

# 相关性分析
corr_matrix = merged_data.corr()

# 绘制热力图
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('成分相关性热力图')
plt.show()
