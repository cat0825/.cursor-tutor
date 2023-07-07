import matplotlib.pyplot as plt

# 假设你想要对'类型'列生成频率分布直方图
plt.hist(data['类型'], bins=10, alpha=0.5)
plt.xlabel('类型')
plt.ylabel('频率')
plt.title('类型的频率分布直方图')
plt.show()