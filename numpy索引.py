import numpy as np

a = np.arange(3, 15)
print(a)
print(a[3])
b = a.reshape(3, 4)
print(b[2, 1])  # ‘:’切片操作 头：尾：步长
for column in b:  # row行 field列 column矩阵转置 flat()需要提取维数的深度，1,2,3.......(即前n行/列）
    print(column)
print(b.flatten())  # 多维数组压缩到一维
for item in b.flat:  # flat数组每个元素迭代
    print(item)