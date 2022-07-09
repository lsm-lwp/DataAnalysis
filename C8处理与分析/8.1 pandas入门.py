import numpy as np #NumPy(Numerical Python) 是 Python 语言的一个扩展程序库，支持大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8]) #创建了S：数据容器，含Series：类似带标签的列表；np.nan是一个float类型的数据
print(s)

dates = pd.date_range('20130101', periods=6)#pd是pandas的；date_range类似于单一变量，但可以是数组或电子表形式，且只有pd库能调用它，但本本质也只是一种数据容器/数据类型
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))#index是行标签、columns是列标签
print(df)

