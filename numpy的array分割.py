import numpy as np

a = np.arange(12).reshape((3, 4))
print(a)
print(np.split(a, 3, axis=0))  # 数组分割
print(np.array_split(a, 3, axis=1))  # 数组不等分割
print(np.vsplit(a, 3))  # 纵向分割
print(np.hsplit(a, 2))  # 横向分割
