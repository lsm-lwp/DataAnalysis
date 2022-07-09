
str1 ="abc"
int1 = 123
float1 = 123.123
bool1 = True
# 1. 创建数据容器
list1 = [str1,int1,float1,bool1,str1,int1,float1,bool1]
set1 = {str1,int1,float1,bool1,str1,int1,float1,bool1}
dict1 = {'string': str1, 'int': int1, 'float':float1, 'bool':bool1}

# 2.打印、查看数据类型
print(list1)
print(set1)
print(dict1)

print(type(list1))
print(type(set1))
print(type(dict1))