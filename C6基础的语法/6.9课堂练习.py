# while 执行判断咖啡浓度是否达到标准，如果没有达到，就持续倒入咖啡粉
coffee = 10  # 当前咖啡浓度
coffee_standard = 20  # 标准浓度
each_time = 3  # 每次加咖啡粉的量
while coffee < coffee_standard:
    print("\n------------------------------")
    print("继续加入咖啡粉",each_time,"g")
    print("未加入咖啡粉,当前咖啡粉含量: ", coffee)
    coffee = coffee + each_time
    print("已加入咖啡粉,当前咖啡粉含量: ", coffee)

#首先有一个条件while coffee < coffee_standard去判断它的迭代变量【即咖啡浓度】
##那个迭代变量如果到达了那个条件【即coffee =/> coffee_standard】咖啡浓度达到/大于标准
###他就不会再循环了，当这个表达式while coffee < coffee_standard返回的值是FLASE的时候，就退出这个循环
####相反，当返回值是TRUE，他都会继续循环【coffee = coffee + each_time】，即一直加3，加3，直到浓度达到/大于标准



#for 遍历销售列表中的数据，对sales里地所有数据进行求合【sale1+sale2+...】

sales = [5, 567123.123, 234, 34]
sum_sales = 0.00
#因为单单写sum会默认成公式，而不是一个数据容器，所以加一个后缀sales
print("\n------------------------------")
for sale in sales:
    print("当前数据项:", sale)
    sum_sales = sum_sales + sale
# 如果写sum_sales = sale，则每一次输出的sale都不会得到累加sum-sales= sale1+sale2+...,
# 只会一次次地更新【sum-sales= xxx】定义而已
print(sum_sales)