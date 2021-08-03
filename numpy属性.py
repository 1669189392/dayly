import numpy as np

array = np.array([[123], [123]])  # np.array方法：转化为array数组格式
print(array)
print(array.ndim)  # np.ndim输出数组维数
print(array.shape)  # np.shape 输出数组形状
print(array.size)  # np.size输出数组长度
print(array.dtype)  # .detype 数据类型
a = np.array([[1, 2, 3], [1, 2, 3]], dtype=np.int64)  # 数据类型设置  #可以选择int32 or 64 #可选其它数据类型
print(a.dtype)  # dtype属性
"""
zeros属性：
生成一个指定规模的零数组
ones属性：
生成一个指定规模的'1'数组
empty属性：
生成一个指定规模的接近于零的数组
arange属性：
生成一个指定范围的随机的数组
arange.reshape：重新生成指定规模的一个指定范围的随机的数组
linspace属性：
按顺序将范围分成指定的小范围，并将端点指定为数组
"""
b = np.zeros((3, 4))
print(b)
