# -*- coding:utf-8 -*-
# 使用逻辑回归对信用卡欺诈进行分类
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import itertools

from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, precision_recall_curve
from sklearn.preprocessing import StandardScaler
import warnings

warnings.filterwarnings('ignore')


# 混淆矩阵可视化
def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion matrix"', cmap=plt.cm.Blues):
    plt.figure()
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=0)
    plt.yticks(tick_marks, classes)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment='center',
                 color='white' if cm[i, j] > thresh else 'black')

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()


# 显示模型评估结果
def show_metrics():
    tp = cm[1, 1]
    fn = cm[1, 0]
    fp = cm[0, 1]
    tn = cm[0, 0]
    print('精确率: {:.3f}'.format(tp / (tp + fp)))
    print('召回率: {:.3f}'.format(tp / (tp + fn)))
    print('F1值: {:.3f}'.format(2 * (((tp / (tp + fp)) * (tp / (tp + fn))) / ((tp / (tp + fp)) + (tp / (tp + fn))))))


# 绘制精确率-召回率曲线
def plot_precision_recall():
    plt.step(recall, precision, color='b', alpha=0.2, where='post')
    plt.fill_between(recall, precision, step='post', alpha=0.2, color='b')
    plt.plot(recall, precision, linewidth=2)
    plt.xlim([0.0, 1])
    plt.ylim([0.0, 1.05])
    plt.xlabel('召回率')
    plt.ylabel('精确率')
    plt.title('精确率-召回率 曲线')
    plt.show();


# 数据加载
data = pd.read_excel(R'E:\WORK\号码诈骗-机器学习\诈骗号码数据集.xlsx')

data.fillna(0,inplace=True)
data.to_excel(R'E:\WORK\号码诈骗-机器学习\诈骗号码数据集.xlsx')
data = pd.read_excel(R'E:\WORK\号码诈骗-机器学习\诈骗号码数据集.xlsx')

# 数据探索
print(data.describe())
# 设置plt正确显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
#设置坐标值单位


# 绘制类别分布
plt.figure()

ax = sns.countplot(x='DB', data=data)
plt.title('类别分布')
plt.show()
# 显示交易笔数，欺诈交易笔数
num = len(data)
num_fraud = len(data[data['DB'] == 1])
print('号码数量: ', num)
print('诈骗笔数：', num_fraud)
print('诈骗交易比例：{:.6f}'.format(num_fraud / num))

# 欺诈和正常交易可视化
f, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(15, 8))
bins = 50
ax1.hist(data.run_time[data.DB == 1], bins=bins, color='deeppink')
ax1.set_title('诈骗号码')
ax2.hist(data.run_time[data.DB == 0], bins=bins, color='deepskyblue')
ax2.set_title('正常号码')
plt.xlabel('时间')
plt.ylabel('次数')
plt.show()
# 对Amount进行数据规范化
data['Amount_Norm'] = StandardScaler().fit_transform(data['age'].values.reshape(-1, 1))

print('输出:')
print(data['Amount_Norm'] )


# 特征选择
y = np.array(data.DB.tolist())

# data = data.drop(['ac_id','run_time', 'age', 'DB','status','AZCODE','AZ','QX','CL','QX1','QX2','MODE'], axis=1)

data= data[['DB','C0','C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13','C14','C15','C16']]

X = np.array(data.values)

# print(X)
# 准备训练集和测试集
train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=0.25, random_state=33,stratify =None)



# train_x.iloc[:,0]=le.fit([train_x.iloc[:,0]])
print("train_X")
print(train_x)
print("train_y")
print(train_y)



# 逻辑回归分类
clf = LogisticRegression()

clf.fit(train_x, train_y)
predict_y = clf.predict(test_x)
print("predict_y")
print(predict_y)

# 预测样本的置信分数
score_y = clf.decision_function(test_x)
# 计算混淆矩阵，并显示
cm = confusion_matrix(test_y, predict_y)
class_names = [0, 1]
# 显示混淆矩阵
plot_confusion_matrix(cm, classes=class_names, title='逻辑回归 混淆矩阵')
# 显示模型评估分数
show_metrics()
# 计算精确率，召回率，阈值用于可视化

print('测试DB')

precision, recall, thresholds = precision_recall_curve(test_y, score_y)


plot_precision_recall()
