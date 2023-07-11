import pandas as pd
import numpy as np
from scipy.stats import norm

fName = ["projects\数学建模\GKN.xlsx","projects\数学建模\GKF.xlsx","projects\数学建模\KBN.xlsx","projects\数学建模\KBF.xlsx"]
average = np.zeros((4,16))

for t in range(4):
    A = pd.read_excel(fName[t])
    n, m = A.shape

    for i in range(m):
        temp = np.sort(A.iloc[:, i])
        ave = 0
        sum = 0
        for j in range(n):
            alpha = norm.pdf((j/n-0.5)*3)
            ave = ave + temp[j]*alpha
            sum = sum + alpha
        ave = ave / sum
        average[t, i] = ave

print(average)