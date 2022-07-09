import requests
from bs4 import BeautifulSoup
# BeautifulSoup是在用requests库爬取数据后，对数据进行解析及提取目标信息

#获取网页全部信息 （requsets库）
url1= "https://movie.douban.com/subject/26419637"
headers = {'user-agent':'my-app/0.0.1'}            #headers不需要变，全部文档使用同一个
response1 = requests.get(url=url1,headers=headers)
print(response1.text)

print("\n-------------------------------\n")       #因为有两个print，为了隔开

#解析网页
soup = BeautifulSoup(response1.text,'html.parser') #该代码句式（包括'html.parser'）来自官方文档。response1.text要与上段代码print()括号里的一致
print(soup.prettify())                             # prettify是为了给后面的代码进行格式化（删空行等）

#提取目标信息
print(soup.title.string) #提取网址的标题，string表示去除<>等符号，只提取纯文字
print(soup.find_all(property="v:summary")[0].text) #注意find_all是下划线
# 提取网址的关于剧情介绍的段落，text表示去除<>等符号，只提取纯文字
# 怎么提取该段落呢？即，在网页中的开发者工具，定位到关于想要的段落的代码标签，离该段落最近的那段
# 在开发者工具中，定位到关于想要的段落，会出现<span class=""property="v:summary">
# 因此，用bs库官方文档中的find_all工具，输入property="v:summary"
# 我们只需要第一个元素，因此输入[0]