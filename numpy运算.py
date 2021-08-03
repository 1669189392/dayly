import numpy as np

a = np.array([[10, 20], [30, 40]])
b = np.arange(4).reshape((2, 2))
print(b)
print(b < 3)
print(a - b)  # 两数组相减 相加相乘都相同
c = b ** 2  # 算平方
print(c)
c = np.sin(b)  # 三角函数通用
print(c)
print(np.dot(a, b))  # 矩阵相乘
print(a.dot(b))  # 矩阵相乘
d = np.random.random((3, 3))  # random随机生成数字
print(d)
print(np.max(d))  # .sum .max .min
print(np.sum(d, axis=1))  # axis ‘0’为列（纵向）‘1’为行（横向）
# 第0轴沿着行的垂直往下，第1轴沿着列的方向水平延伸
print(np.argmin(d))  # 最小值索引 max同理
print(np.mean(d))  # 计算平均值
print(d.mean())  # 计算平均值
print(np.median(d))  # 计算中位数
print(np.cumsum(d))  # 计算累加值 即前N位相加
print(np.diff(d))  # 计算累差
print(np.nonzero(d))  # 输出非零值坐标位置
print(np.transpose(np.nonzero(a)))  # transpose矩阵转置为坐标格式
print(np.sort(d))  # sort数组排序 默认按行排序
print(np.transpose(a))  # 矩阵转置
print(a.T)  # 矩阵转置
print(np.clip(a, 15, 35))  # 限幅：将一个数组内小于或大于特定范围的值改为最大或最小值边界
