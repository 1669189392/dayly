import numpy as np

a = np.array([1, 1, 1])
b = np.array([2, 2, 2])
print(np.vstack((a, b)))  # a,b纵向合并
print(np.hstack((a, b)))  # a,b横向合并
# vstack和hstack处理完后不再是数组而是序列
