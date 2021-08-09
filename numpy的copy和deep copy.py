import numpy as np

a = np.arange(4)
print(a)
b = c = d = a
print(b)
print(c)
print(d)
a[0] = 11
print(a)
print(b is a)
print(c)  # 改变会传导，类似指针的效果
d[1:3] = [22, 33]
print(a)
e = a.copy()  # 数据不会关联，即重新在内存中写入另一个变量     浅复制
print(e)
