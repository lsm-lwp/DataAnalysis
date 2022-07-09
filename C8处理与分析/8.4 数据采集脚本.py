import pandas as pd
import requests
import time
import os
from bs4 import BeautifulSoup

# pandas是著名的数据处理分析的库，as表示重命名

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
movie_lists = []
x = 0  # 计次
movie_links = []
movie_names = []
all_infos = []  # all表示这个是一个容纳了全部数据的列表容器，把每次输出的movie_info都放进去，这样方便导出到excel


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
# 最终会爬取出120部电影，因为page不代表页数,而是代表当前已爬取有多少部电影，
# 当max_page即100进入循环，会再加一次20，所以最终爬取到第120部电影就会停止循环
def get_page(page_link, tag):
    page = 6220
    max_page = 10000
    while page <= max_page:
        url = page_link + "tags=" + tag + "&start=" + page.__str__() #+ "&genres=" + genre
        print("当前URL：", url)
        response = requests.get(url=url, headers=headers)
        #print(response.text)
        movie_info = response.text
        # 将获取到的string转为字典
        movie_info = eval(movie_info) # eval() = dict()
        # 转出到列表中
        movie_links = []
        for m in movie_info['data']:
            # m是字典类型的数据，存放了data里所有的数据，如director编剧等
            # 提取 m 里面对应电影链接的那些值: 通过get key来达到
            # 但url直接爬取下来的链接都是有问题的，有几个错误符号/\，所有要统一去除
            # 原写法：movie_links.append(m.get('url'))，但要处理错误符合，因此
            # 处理错误符合的python方法：百度搜python replace
            # 原写法：url_str.replace('\/','/')
            movie_lists.append(m) #调用.append 对列表进行追加内容,即把每次m存进去，循环250次就有250个m
            url_str = m.get('url')
            movie_links.append(url_str.replace('\/', '/'))
        # 调用获取详细信息的方法
        movie20_list = []
        for l in movie_links:
            time.sleep(3)

            movie = get_infos(url=l)
            try:
                print("已获取电影：", movie['title'])
            except KeyError:
                print("skip keyerror")
            movie20_list.append(movie)
        # 存CSV
        save_csv(movie20_list)
        # 修改staet参数
        page = page + 20
        # 验证数据正确性
        #print(url)


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
        movie_info['writer'] = get_list(soup.find_all(class_="attrs")[1].find_all('a')) if len(
            writer) > 1 else ""  # 有编剧
        movie_info['actors'] = get_list(
            soup.find_all(rel="v:starring"))  # 演员表                                                       # 演员表)
        movie_info['gener'] = get_list(soup.find_all(property="v:genre"))  # 电影类型
        movie_info['language'] = soup.find(text="语言:").next_element  # 语言
        movie_info['runtime'] = soup.find(property="v:initialReleaseDate").string  # 上映日期
        # 评分部分
        movie_info['average'] = soup.find(property="v:average").string
        movie_info['votes'] = soup.find(property="v:votes").string
        # 每部电影对应的链接
        movie_info['link'] = url
        # 打印电影信息
        #for key in movie_info:  # key是指['']里面的内容
        #    print(key, ":", movie_info.get(key))
    except AttributeError:
        print("电影已下架")

    # 返回电影信息
    return movie_info
    # 电影信息存到列表中，调用.append 对列表进行追加内容,即把每次的movie_info存进去，250个电影就有250个movie_info
    #all_infos.append(movie_info)

def save_csv(movies):
    """
    :param movies: list
    :return: nan
    """
    data = pd.DataFrame(movies)
    file = "movie_data.csv" #给file赋值一个字符串movie_data.csv，字符串就是一串英文或符号。赋值：把=右边的赋给左边
    if os.path.exists(file): #os库需要在开头导入，os库是python标准库，包含几百个函数，常用路径操作、进程管理、环境参数等
                             #os.path字库以path为入口，用于操作和处理文件路径
        data.to_csv(file, mode='a', header=False)
    else:
        data.to_csv(file)
    print("\n==========================存储成功：", data.tail(1)['title'])
    #上面一行是pandas:DataFrame对行和列的操作，可通过.head()、.tail()，也可以data[]单独使用
    #data.tail(1)表示返回data的后1行数据

# 输入一个main函数，让整个文档的函数从下面这行开始运行
if __name__ == '__main__':
    get_page("https://movie.douban.com/j/new_search_subjects?", tag="电影")
