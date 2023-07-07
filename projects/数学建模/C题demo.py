import pandas as pd
from sklearn.preprocessing import LabelEncoder
import chardet
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 检测文件编码
with open(r"C:\Users\17591\Desktop\file.csv", 'rb') as f:
    result = chardet.detect(f.read())
    
# 设置字体为SimHei显示中文
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False 
# 使用检测到的编码读取文件
data = pd.read_csv(r"C:\Users\17591\Desktop\file.csv", encoding=result['encoding'])
data.hist(bins=50, figsize=(20,15))
plt.show()


print(data.head())