import numpy as np

a = np.array([1, 1, 1])
b = np.array([2, 2, 2])
print(np.vstack((a, b)))  # a,b纵向合并
print(np.hstack((a, b)))  # a,b横向合并
# vstack和hstack处理完后不再是数组而是序列
print(a[:, np.newaxis])  # np.newaxis 新增一个维度（这一句增加的是列竖向维度）
c = np.concatenate((a, b, a, b, a, b), axis=0)  # 多个矩阵进行合并，自选方向
print(c)
# 以下是矩阵纵置合并
A = np.array([1, 1, 1])[:, np.newaxis]
B = np.array([2, 2, 2])[:, np.newaxis]
C = np.concatenate((A, B, A, B), axis=1)
print(C)
