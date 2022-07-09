# 视频：第二阶段：第五周：2.7计算销售额
#基础销售数据,第一行是品牌名称，第二行是销量，第三行是单价
sales = [
    ["雅诗兰黛","OLAY","相宜本草","keith"],  #第一行是品牌名称
    [8731, 4209, 10239, 422],             #第二行是销量
    [1099, 675, 516, 1349]]               #第三行是单价
# 通过
print(sales[1])
# 可确定 sales[1] 是 [8731, 4209, 10239, 422]，且可推出sales[2]同理。因此可输出如下
# 1.提取列表中的元素
sales_amount = sales[1]
sales_price = sales[2]
# 2.将列表中第2和第3个元素的数据项分别相乘
sb = []
for (a,b) in zip(sales_amount, sales_price): ##需要zip将两个列表打包即：sales_amount, sales_price；否则for将不知道怎么匹配
    multiple = a * b
    sb.append(multiple)
print(sb)
# 3.并打印对应商品名称的销售总额数据(即销量乘单价)
# sales[0]是指第一行品牌名称
for (s, l) in zip(sales[0], sb):##需要zip将两个列表打包即：sales[0], sb；否则for将不知道怎么匹配
    print(s,"销售总额: ",l)