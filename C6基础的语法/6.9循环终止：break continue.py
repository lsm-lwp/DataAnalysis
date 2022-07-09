# while 执行判断咖啡浓度是否达到标准，如果没有达到，就持续倒入咖啡粉

coffee = 10  # 当前咖啡浓度
coffee_standard = 20  # 标准浓度
each_time = 3  # 每次加咖啡粉的量
X = 1 #卖了一杯咖啡（从第一杯开始卖）
guest = 'Joey'
#当客户不是MIKE这个黑名单人士时，进入循环，而Mike是唯一的黑名单用户.因为这里顾客是joey而不是mike所以以下循环能照常进行

# 咖啡的销量: >=25 杯,则正常卖; <25杯,不再卖
while True : #杯数无条件设置了，就算是无条件进入while语句
    if guest == 'Mike': # Mike是唯一的黑名单用户，只要符合if guest =Mike 循环就不会再进行continue以下的语句,即不再做咖啡
        print (guest)
        continue
    print ("目前已经做了多少",X,"杯")
   # 制作咖啡
    while coffee < coffee_standard:
        print("\n------------------------------")
        print("继续加入咖啡粉",each_time,"g")
        print("未加入咖啡粉,当前咖啡粉含量: ", coffee)
        coffee = coffee + each_time
        print("已加入咖啡粉,当前咖啡粉含量: ", coffee)
    # 因为当X=24,就继续+1了,所以不需要X <=25,不然当X=25，再次循环+1,最终会变成26杯
    if X < 25:
        X += 1
    else:
        break;