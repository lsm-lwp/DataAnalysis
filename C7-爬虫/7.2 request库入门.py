## 第六周1.2

# 导入模块
import requests
# 定义url=网址
url1= "https://movie.douban.com/"
# headers 告诉网站你是谁,即浏览器的身份
headers = {'user-agent':'my-app/0.0.1'}
# 访问、并获取网页信息
# response是响应，与requset请求，相互对应
response1 = requests.get(url=url1,headers=headers)
# print(response1.text)

# 将上述代码实际应用一遍，即以下三行。首先避免出现太多代码，先把上面的print加#，注释掉，不运行
# 某电影在豆瓣电影中的主页
url2 = "https://movie.douban.com/subject/26419637" #删除网址后面的部分，即/?from=showing，因为该部分仅代表网址的出处，没用的
response2 = requests.get(url=url2,headers=headers) #浏览器身份不用变
# print(response2.text)

# 将上述代码实际应用一遍，即以下三行。先把上面的print加#，注释掉，不运行
# 百度百科
url3 = "https://baike.baidu.com/"
response3 = requests.get(url=url3,headers=headers)
print(response3.text)