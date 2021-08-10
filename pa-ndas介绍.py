import pandas as pd
import numpy as np

s = pd.Series([1, 3, 6, np.nan, 44, 1])  # np.nan 生成一个空值 Series类似字典操作
print(s)
dates = pd.date_range('20200101', periods=6)  # 生成固定格式的时间序列
print(dates)
