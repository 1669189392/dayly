import pandas as pd
import numpy as np

s = pd.Series([1, 3, 6, np.nan, 44, 1])  # np.nan 生成一个空值 Series类似字典操作
print(s)
dates = pd.date_range('20200101', periods=6)  # 生成固定格式的时间序列
print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])  # index 列 coulumns 行
print(df)
df1 = pd.DataFrame(np.arange(12).reshape((3, 4)))
print(df1)
df2 = pd.DataFrame({'A': 1.0,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
print(df2)
print(df2.dtypes)
print(df2.index)  # 列序
print(df2.columns)  # 行序
print(df2.values)  # 其他元素
print(df2.describe())  # 数字统计
print(df2.T)  # 矩阵转置
print(df2.sort_index(axis=1, ascending=False))  # 行/列序排序 ascending 正/逆序
print(df2.sort_values(by='E'))  # 相同项放一起
