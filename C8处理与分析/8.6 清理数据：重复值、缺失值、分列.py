import pandas as pd

# 当dataframe有多行、多列；跑出来的数据会显示不全。所以需要写以下几行代码，使其完整显示
# 以下三行代码，来源于百度
# 显示所有列 （参数设置为None代表显示所有列
pd.set_option('display.max_columes',None)
# 显示所有列
pd.set_option('display.max_rows',None)
# 设置数据的显示长度，默认为50
pd.set_option('max_colwidth',200)

# 读取数据
data = pd.read_csv("movie_data.csv")
print(data)

# 查重、去重：根据title来去重


# 缺失值：即出现NAN空值；若，评分/人数的值为空，则取平均值；若，是文本数据为空（如电影类型），则保留NAN即可


# 分列