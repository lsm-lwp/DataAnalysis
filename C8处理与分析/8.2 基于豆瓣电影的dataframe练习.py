import numpy as np
import pandas as pd

# 基于API爬取的豆瓣爱情电影数据，创建3个series
d = {'title': pd.Series(['泰坦尼克号', '阿甘正传', '怦然心动', '霸王别姬']),
     'director': pd.Series(['詹姆斯·卡梅隆', '罗伯特·泽米吉斯', '罗伯·莱纳', '陈凯歌']),
     'runtime': pd.Series(['1998-04-03', '1994-06-23', '2010-07-26', '1993-07-26'])}
print(d)
# 基于上面3个series，创建1个dataframe，可以让3个series合并起来成为二维表
print("===============2")
df = pd.DataFrame(d)
print(df)

# 选取第2行且列标签为title的数据，由于第2行属于系统自定的顺序，我在创建series时并未自定义index列标签，所以注意系统从0行数起
print("===============3")
print(df['title'].iloc[2])
