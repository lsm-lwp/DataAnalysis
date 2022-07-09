import pandas
import requests
from bs4 import BeautifulSoup
import pandas as pd  #pandas是著名的数据处理分析的库，as表示重命名

headers = {'user-agent': 'my-app/0.0.1'}
movie_links = []
movie_names = []

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



# 1.访问主页面，并且完成页面跳转
def get_page(page_link):
    page = 0
    max_page = 225
    while page <= max_page:
        url = page_link + "?start=" + page.__str__() + "&filter="
        response = requests.get(url=url, headers=headers)
        # 获取电影链接
        get_links(response)
        # 修改staet参数
        page = page + 25
        # 验证数据正确性
        print(url)

# 2.抓取每个页面所有的电影链接,info=information
def get_links(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    for hhh in soup.find_all(class_="hd"):
        movie_names.append(hhh.find(class_="title").string)
        movie_links.append(hhh.find('a', href=True).attrs['href'])

    # 3.根据电影链接，获取基本信息、评分信息
def get_infos(url):
    response = requests.get(url=url, headers=headers)
    # 获取目标信息=解析网页
    soup = BeautifulSoup(response.text, 'html.parser')
    # 存储容器，电影信息一览（info = infomation)
    movie_info = {}
    # 容错处理（在跑数据过程中，遇到报错，即某部电影信息被隐藏了无法再继续爬取等类似的原因）
    try:
        # 电影名称
        movie_info['title'] = soup.find(property="v:itemreviewed").string
        # 简介部分 (与【电影名称】的操作一样)
        movie_info['director '] = soup.find(rel="v:directedBy").string  # 导演
        writer = soup.find_all(class_="attrs")
        movie_info['writer'] = soup.find_all(class_="attrs")[1].string if len(writer) > 1 else "" # 有编剧
        movie_info['actors'] = get_list(soup.find_all(rel="v:starring"))  # 演员表                                                       # 演员表)
        movie_info['gener'] = get_list(soup.find_all(property="v:genre"))  # 电影类型
        movie_info['language'] = soup.find(text="语言:").next_element            # 语言
        movie_info['runtime'] = soup.find(property="v:initialReleaseDate").string  # 上映日期
        # 评分部分
        movie_info['average'] = soup.find(property="v:average").string
        movie_info['votes'] = soup.find(property="v:votes").string
        # 打印电影信息
        for key in movie_info:  # key是指['']里面的内容
            print(key, ":", movie_info.get(key))
    except AttributeError:
        print ("电影已下架")

    # 输入一个命函数，让整个文档的函数从下面这行开始运行
if __name__ == '__main__':
    # 调用功能1，实现页面的访问
    get_page(page_link="https://movie.douban.com/top250")
    # 获取所有链接
    for name, link in zip(movie_names, movie_links):
        print(name, ":", link)
        get_infos(link)  # 调用功能3，根据url爬取电影信息
