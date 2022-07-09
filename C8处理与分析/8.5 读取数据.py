import pandas as pd
import numpy as np

# 基于API爬取的豆瓣爱情电影数据，创建3个series
d = {'title': pd.Series(['泰坦尼克号', '阿甘正传', '怦然心动', '霸王别姬']),
     'director': pd.Series(['詹姆斯·卡梅隆', '罗伯特·泽米吉斯', '罗伯·莱纳', '陈凯歌']),
     'runtime': pd.Series(['1998-04-03', '1994-06-23', '2010-07-26', '1993-07-26'])}
print(d)
# 基于上面3个series，创建1个dataframe，可以让3个series合并起来成为二维表
print("===============2")
df = pd.DataFrame(d)
print(df)

# 选取第2行且列标签为title的数据，是因为我在创建series时并未自定义index列标签，所以注意系统从0行数起，我搞了三行数据，因此为2
# 组成电影数据表
print("===============3")
print(df['title'].iloc[2])

#存储：格式： dataframe.to_csv("文件名")，其中dataframe缩写成df，csv也可换成excel
df.to_csv("file_name.csv")
df.to_excel("D:\pycharm-\DataAnalysis\C6基础的语法\\file2.xlsx") #注意这行代如果出现报错，增加或减少斜杠试试//
#如果继续输入字符串，即csv的命名，就会继续自动保存在c8文件夹里；而现在不输入字符串，输入绝对路径D:\pycharm-\DataAnalysis\C7-爬虫 + 命名file2.xlsx,就可以改变保存的位置

#读取
#读取本文档（8.5读取数据）所在文件夹下（C8）的文件，就只需要写（“文件名”）
#读取非本文档文件夹下的文件，如在C6的file2.xlsx，就需要写（“文件路径+文件名”）如：D:\pycharm-\DataAnalysis\C6基础的语法\\file2.xlsx
# pd.read_csv("file_name.csv") 用pandas库读取上面的那个保存在C8文件夹里的csv文件,也就是把csv文件里的内容跑出来
print("===============4")
print(pd.read_csv("file_name.csv"))
# 同样的方法，读取excel文件
print("===============5")
print(pd.read_excel("D:\pycharm-\DataAnalysis\C6基础的语法\\file2.xlsx"))