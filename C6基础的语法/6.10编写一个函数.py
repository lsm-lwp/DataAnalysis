# 视频：第二阶段：第五周：2.6定义函数

import numpy as np #导入数据分析库 ##必须放在前面

list1 = [1,2,3,4]
# sum (此处是为了演示sum的函数结果）方便自己去编写一个与SUM运算功能一样的函数（取名为get_sum)
print(sum(list1))
#编写一个与SUM运算功能一样的函数（取名为get_sum)
def get_sum(list):
    sum = 0
    for num in list: #循环list里面的number
        print("num:", num)
        sum = sum + num
    return sum   # return的位置必须与For对齐
print("get_sum计算结果:",get_sum(list1))


# average
print(np.average(list1)) #千万别写少1，如果只是输average，会报错，因为使用该函数需要导入数据库numpy
#编写一个与average运算功能一样的函数（取名为get_average)
def get_average(list):
    sum = 0
    for num in list:
        print("num:",num) #这一行必须写，因为这样才能一次次输出num
        sum = sum + num
    # 数据项个数
    count = len(list1)   #数出有多少个字符
    # 数据项平均值
    average = sum / count #总和÷总个数=平均值
    return average
print ("get_average计算结果:", get_average(list1))


## 编写一段制作牛奶咖啡的函数
# 定义相关变量
coffee = 10  #当前咖啡浓度
milk = 20    #当前牛奶浓度
stand_cof = 15  #咖啡标准浓度
stand_milk = 25  #牛奶标准浓度
# 定义函数，命名为make_milkcoffee
def make_milkcoffee(stand_cof, stand_milk, coffee, milk):
    # 判断咖啡浓度
    while coffee < stand_cof:
        # 咖啡如果不够，继续加咖啡粉
        coffee = coffee + 3
        print("当前咖啡浓度:", coffee)
    # 咖啡如果够，加牛奶
    print("咖啡浓度达到标准,准备加牛奶")
    #判断牛奶浓度
    while milk < stand_milk:
        # 牛奶如果不够，继续加牛奶
        milk = milk + 3
        print("当前牛奶浓度:", milk)
    # 牛奶如果够，制作完成
    print("制作完成")

coffee = 10
milk = 20
stand_cof = 15
stand_milk = 25
make_milkcoffee(stand_cof, stand_milk, coffee, milk)