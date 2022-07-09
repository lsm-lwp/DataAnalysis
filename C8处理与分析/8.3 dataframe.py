import numpy as np
import pandas as pd

# 创建Series
s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e']) #通过np库的random函数生成了5个数字，索引是abcde，如果不写index=这行代码，默认索引是01234
print(s)

# 利用上面生成的s，生成一个dataframe（确定一个数据容器即二维表的行 列数据）
d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two': s,
     '自定义':'自定义'} #用''或者“”都可以，而因为没规定自定义的值和行数，所以会用自定义填充所有行数
print(d)
df = pd.DataFrame(d)
print(df)

# 选取：

# 按行的索引：行号（即按01234行，第一行是从0开始），索引值（相当于自定义行标签，a行b行等)
# 行号打印法：
print("==============1")
print(df.iloc[2]) #表打印第3行的值(第一行是从0开始)。loc是loaction定位的缩写，iloc通过坐标定位，如打印第三行的值。
# 索引值打印法：
print("==============2")
print(df.loc['e']) #表打印e所在的那行的值(注意不是iloc，是loc)，或者理解为打印e那行的值，e是自定义行标签

# 按列的名称
# 单列(只打一列)
print("==============3")
print(df['two']) #表打印two这列的值，two是自定义的列标签
# 多列(打多列)
print("===============4")
print(df[['two','one']]) #双重的[[]]，相当于把two one放到列表里，因为这样才能告诉它这是两个列标签

# 行列同时筛选（如：只想打印出位于one列b行的那个值）
print("===============5")
print(df['one'].loc['b'])
# 打印出位于two、one列b行的那些值
print("==============6")
print(df[['two','one']].loc['b'])

# 模糊查询
# 查询出符合one列中>0这个条件的所有值，打印出来，注意one=Nan(无)的都没显示
print("===============7")
print(df [df['one'] > 0] )
# 查询出符合one、two这两列中>0这个条件的所有值
print("===============8")
print(df[(df['one']>0)&(df['two']<0)]) #格式是两个(df[]>0)被df[ & ]包着

# 精准查询
# 查询one列=3的所有值,要用双等号==
print("===============9")
print(df[df['one'] == 3])
# 查询one列不等于≠3的所有值，要用!=, 例如！=3
print("===============10")
print(df[(df['one'] != 3) & (df['two'] <= 0)])



