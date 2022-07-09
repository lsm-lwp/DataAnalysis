import requests
from bs4 import BeautifulSoup

def get_list(soup_list):
    """
    清洗解析后的网页信息，并以列表形式返回
    :param soup_list: bs_list
    :return: list
    """
    list = []
    for hhh in soup_list:
        list.append(hhh.string)
    return list

# 访问网页、获取信息
url1= "https://movie.douban.com/subject/26419637"
headers = {'user-agent':'my-app/0.0.1'}
response1 = requests.get(url=url1,headers=headers)
#print(response1.text)


# 获取目标信息=解析网页
soup = BeautifulSoup(response1.text,'html.parser') #该行代码的格式来源于官方文档
#print(soup.prettify())

# 为了不用给每个函数改成“print"那么麻烦，借助字典(一种数据容器)存储，把所有的title=XXX等代码都存储在一个字典里即movie_info = { }，通过一次的print就可打印全部，然后用for循环，依次对齐输出所有内容
movie_info = { }
# 电影名称（在网页的开发者工具，找到电影名称的数据标签)
print(soup.find(property="v:itemreviewed").text)
# 给【电影名称】一个定义/赋值
movie_info['title'] = soup.find(property="v:itemreviewed").string

# 简介部分 (与【电影名称】的操作一样)
movie_info['director '] = soup.find(rel="v:directedBy").string      # 导演
movie_info['writer'] = soup.find_all(class_="attrs")[1].string      # 编剧
movie_info['actors'] = get_list(soup.find_all(rel="v:starring"))    # 演员表 （有多个人，所以加一个get_list)                                                                        # 演员表)
movie_info['gener'] = get_list(soup.find_all(property="v:genre"))   # 电影类型（有多个类型，所以加一个get_list)
movie_info['language'] = soup.find(text="语言:").next_element       # 语言 (.next_element通过官方文档查找到的功能)
movie_info['runtime'] = soup.find(property="v:initialReleaseDate").string #上映日期

# for遍历数据项，.string获取目标信息。通过该行代码，能直接获取所有演员的名字！！！就不用那么麻烦
# 注意for的循环格式

# 评分部分
movie_info['average'] = soup.find(property="v:average").string
movie_info['votes'] = soup.find(property="v:votes").string

for key in movie_info:        #key是指['']里面的内容
    print(key,":",movie_info.get(key)) #get(key)是为了让print可以通过key去找movie.info里面的值，因为movie.info里面既有导演 编剧等等，需要让key去带领print精准查找
