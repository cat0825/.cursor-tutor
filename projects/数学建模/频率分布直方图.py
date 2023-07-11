import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import matplotlib.font_manager as fm

# 设置字体为SimHei显示中文
font = fm.FontProperties(fname='C:/Windows/Fonts/simhei.ttf')

fName = ["projects\数学建模\GKN.xlsx","projects\数学建模\GKF.xlsx","projects\数学建模\KBN.xlsx","projects\数学建模\KBF.xlsx"]
yLabels = ["高钾类未风化","高钾类风化","铅钡类未风化","铅钡类风化"]
xLabels = ["二氧化硅(SiO2)","氧化钾(K2O)","氧化钙(CaO)","氧化铝(Al2O3)","氧化铁(Fe2O3)","氧化铜(CuO)","五氧化二磷(P2O5)"]
idx = [1,3,4,6,7,8,11]  # Python的索引从0开始

for t in range(4):
    A = pd.read_excel(fName[t])
    n, m = A.shape

    for k in range(len(idx)):
        x = A.iloc[:, idx[k]]

        picPos = k + t*7
        plt.subplot(4,7,picPos+1)

        h = plt.hist(x, 5, edgecolor='black')
        if t == 1 or t == 3:
            plt.setp(h[2], 'facecolor', [0.1, 0.1, 0.5], 'edgecolor', 'r')

        mu, sigma = norm.fit(x)
        x2 = np.linspace(min(x), max(x), 100)
        y2 = norm.pdf(x2, mu, sigma) * 10
        plt.plot(x2, y2, linewidth=5)

        if picPos == 3:
            plt.title("不同玻璃类型风化前后不同化学成分频率分布直方图", fontproperties=font)
        if t == 3:
            plt.xlabel(xLabels[k], fontproperties=font)
        if k == 0:
            plt.ylabel(yLabels[t], fontproperties=font)

plt.show()