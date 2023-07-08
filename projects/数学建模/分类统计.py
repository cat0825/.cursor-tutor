import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# 从数据中读取并预处理
data = pd.read_excel('C:\\Users\\17591\\Desktop\\demo.xlsx', sheet_name='表单1+2合并后')
data.fillna(0, inplace=True)  # 填充缺失值为0

# 提取高钾玻璃和铅钡玻璃数据
high_potassium = data[data['类型'] == '高钾']
lead_barium = data[data['类型'] == '铅钡']

# 按化学成分绘制箱线图比较
chemical_compositions = ['二氧化硅(SiO2)', '氧化钠(Na2O)', '氧化钾(K2O)', '氧化钙(CaO)', '氧化镁(MgO)',
                         '氧化铝(Al2O3)', '氧化铁(Fe2O3)', '氧化铜(CuO)', '氧化铅(PbO)', '氧化钡(BaO)']
plt.figure(figsize=(12, 8))
for composition in chemical_compositions:
    plt.subplot(2, 5, chemical_compositions.index(composition) + 1)
    sns.boxplot(x='类型', y=composition, data=data)
    plt.title(composition)
    plt.ylabel('')
plt.tight_layout()
plt.show()
