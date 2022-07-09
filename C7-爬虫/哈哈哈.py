



import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'user-agent': 'my-app/0.0.1'}
movie_links = []
movie_names = []
all_infos = [] #all表示这个是一个容纳了全部数据的列表容器，把每次输出的movie_info都放进去，这样方便导出到excel
movie_lists = []


def get_list(soup_list):
    """
    清洗解析后的网页信息，并以列表形式返回
    :param soup_list: bs_list
    :return: list
    """
    list = []
    for hh in soup_list:
        list.append(hh.string)
    return list


def get_page(page_link, tag, genre):
    page = 0
    max_page = 100
    while page <= max_page:
        url = page_link + "tags=" + tag + "&start=" + page.__str__() + "&genres=" + genre
        response = requests.get(url=url, headers=headers)
        print(response.text)
        movie_info = response.text
        movie_info = eval(movie_info)
        # m是字典类型的数据，存放了data里所有的数据，如director编剧等
        for m in movie_info['data']:
            movie_lists.append(m)
            # 提取 m 里面对应电影链接的那些值: 通过get key来达到
            # 但url直接爬取下来的链接都是有问题的，有几个错误符号/\，所有要统一去除
            # 原写法：movie_links.append(m.get('url'))，但要处理错误符合，因此

            # 处理错误符合的python方法：百度搜python replace
            # 原写法：url_str.replace('\/','/')

        # 修改staet参数
        page = page + 20
        # 验证数据正确性
        print(url)
##因为第一段代码，爬取到的信息都是基于api最基本的一个data 键值对的数据，
##并不是完整的电影信息，所以需要进行第二段代码，已取得完整的信息


  # 2.根据电影链接，获取基本信息、评分信息,info=information
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
        movie_info['writer'] = get_list(soup.find_all(class_="attrs")[1].find_all('a')) if len(writer) > 1 else "" # 有编剧
        movie_info['actors'] = get_list(soup.find_all(rel="v:starring"))  # 演员表                                                       # 演员表)
        movie_info['gener'] = get_list(soup.find_all(property="v:genre"))  # 电影类型
        movie_info['language'] = soup.find(text="语言:").next_element            # 语言
        movie_info['runtime'] = soup.find(property="v:initialReleaseDate").string  # 上映日期
        # 评分部分
        movie_info['average'] = soup.find(property="v:average").string
        movie_info['votes'] = soup.find(property="v:votes").string
        # 每部电影对应的链接
        movie_info['link'] = url
        # 打印电影信息
        for key in movie_info:  # key是指['']里面的内容
            print(key, ":", movie_info.get(key))
    except AttributeError:
        print("电影已下架")
    all_infos.append(movie_info)


# 输入一个main函数，让整个文档的函数从下面这行开始运行
if __name__ == '__main__':
    # 调用功能1，实现页面的访问
    get_page(page_link="https://movie.douban.com/j/new_search_subjects?"
             "sort=U&range=0,10&", tag="电影", genre="爱情")
    for h in movie_links:
        print("正在抓取电影：", h)
    get_infos(url=h)  # 原本不用谢for和print那两句，但因为get infos里的url需要通过movielinks拿，所以必须写，并把所有url存在【l】
        # 通过get_infos(url=l)，就可以进行第二段代码的循环: 即爬取每个url里的信息
    data = pd.DataFrame(all_infos)
    data.to_excel("API参数爬豆瓣爱情电影数据.xlsx")


    url_str = m.get('url')
    movie_lists.append(url_str.replace('\/', '/'))