import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# 从数据中读取并预处理
data = pd.read_excel('C:\\Users\\17591\\Desktop\\demo.xlsx', sheet_name='表单1+2合并后')
data.fillna(0, inplace=True)  # 填充缺失值为0

# 提取特征和标签
features = data.drop(['类型'], axis=1)  # 假设类型列为标签列
labels = data['类型']

# 特征编码
label_encoder = LabelEncoder()
labels_encoded = label_encoder.fit_transform(labels)

# 将特征进行0/1编码
encoder_dict = {}

for feature_name in features.columns:
    encoder = LabelEncoder()
    features[feature_name] = encoder.fit_transform(features[feature_name].astype(str))
    encoder_dict[feature_name] = encoder

# 创建并训练分类模型（以决策树为例）
model = DecisionTreeClassifier()
model.fit(features, labels_encoded)

# 计算基准精确度（使用完整数据集）
baseline_accuracy = accuracy_score(labels_encoded, model.predict(features))
print("Baseline Accuracy:", baseline_accuracy)

# 逐个化学成分进行敏感性分析
chemical_features = ['二氧化硅(SiO2)', '氧化钠(Na2O)', '氧化钾(K2O)', '氧化钙(CaO)', '氧化镁(MgO)',
                     '氧化铝(Al2O3)', '氧化铁(Fe2O3)', '氧化铜(CuO)', '氧化铅(PbO)', '氧化钡(BaO)',
                     '五氧化二磷(P2O5)', '氧化锶(SrO)', '氧化锡(SnO2)', '二氧化硫(SO2)']

sensitivity_values = []

for feature_name in chemical_features:
    modified_features = features.copy()
    modified_features[feature_name] = 0  # 将当前化学成分特征的值设置为0

    modified_accuracy = accuracy_score(labels_encoded, model.predict(modified_features))
    sensitivity = baseline_accuracy - modified_accuracy
    sensitivity_values.append(sensitivity)

    print("Feature:", feature_name)
    print("Modified Accuracy:", modified_accuracy)
    print("Sensitivity:", sensitivity)
    print()

# 数据可视化
plt.figure(figsize=(10, 6))
plt.bar(chemical_features, sensitivity_values)
plt.xlabel('Chemical Features')
plt.ylabel('Sensitivity')
plt.title('Sensitivity Analysis of Chemical Features')
plt.xticks(rotation=45)
plt.show()
