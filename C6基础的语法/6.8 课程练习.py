
coffee_max = 10 # 上限，太浓了
coffee_min = 5 # 下限，太淡了
coffee = 20 # 当前浓度

print ("当前咖啡浓度为: ",coffee) #可在输出的结果上每次都加上一句 “当前咖啡浓度为:  ”

if coffee < coffee_max and coffee > coffee_min:
    print ("咖啡浓度正好，继续倒牛奶")
elif coffee > coffee_max:
    print ("咖啡浓度太浓，继续倒水")
else:
    print ("咖啡浓度太淡，继续倒咖啡粉")

######  elif 可以 无限加 很多个，形成 多选1 的情况