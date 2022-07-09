import pandas as pd
import requests
from bs4 import BeautifulSoup
#pandas是著名的数据处理分析的库，as表示重命名

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
    for hhh in soup_list:
        list.append(hhh.string)
    return list

# 1.访问主页面，并且完成页面跳转
# 最终会爬取出120部电影，因为page不代表页数,而是代表当前已爬取有多少部电影，
# 当max_page即100进入循环，会再加一次20，所以最终爬取到第120部电影就会停止循环
def get_page(page_link, tag, genre):
    page = 0
    max_page = 40
    while page <= max_page:
        url = page_link + "tags=" + tag + "&start=" + page.__str__() + "&genres=" + genre
        response = requests.get(url=url, headers=headers)
        print('get_page response.text ---- ')
        print(response.text)
        print('get_page url---- ')
        print(url)
        movie_info = response.text
        movie_info = eval(movie_info)
        print('movie_info ---')
        print(movie_info)

        # m是字典类型的数据，存放了data里所有的数据，如director编剧等
        for m in movie_info['data']:
            movie_lists.append(m)
            # 提取 m 里面对应电影链接的那些值: 通过get key来达到
            # 但url直接爬取下来的链接都是有问题的，有几个错误符号/\，所有要统一去除
            # 原写法：movie_links.append(m.get('url'))，但要处理错误符合，因此

            # 处理错误符合的python方法：百度搜python replace
            # 原写法：url_str.replace('\/','/')

            # 验证数据正确性
            print('for m in movie_info[\'data\'] m --- ')
            print(m)
            print('m.get(\'url\')')
            print(m.get('url'))
            print('m.get(\'url\').replace(\'\/\',\'/\')')
            print(m.get('url').replace('\/', '/'))
            movie_links.append(m.get('url').replace('\/', '/'))

        # 修改start参数
        page = page + 20


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
        # 电影名称    movie_info是一个json对象， movie_info['title']是键值对，装进了 movie_info这个对象里
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
        print ("电影已下架")
    # 电影信息存到列表中，调用.append 对列表进行追加内容,即把每次的movie_info存进去，250个电影就有250个movie_info
    all_infos.append(movie_info)
    print('all_infos --- ')
    print (all_infos)



if __name__ == '__main__':
    get_page("https://movie.douban.com/j/new_search_subjects?"
             "sort=U&range=0,10&", tag="电影" , genre = "爱情")

    # 调用获取详细信息的方法 = 调用 get_infos通过movie links用以获取全部电影信息 ，用【l】遍历links链接里的信息：即每部电影的url
    for l in movie_links:  #
        print("正在抓取电影：",l)
        # 原本不用谢for和print那两句，
        # 但因为get infos里的url需要通过movielinks拿，
        # 所以必须写，并把所有url存在【l】
        get_infos(url=l)

    # 通过get_infos(url=l)，就可以进行第二段代码的循环: 即爬取每个url里的信息
    data = pd.DataFrame(all_infos)
    data.to_excel("API参数获取豆瓣爱情电影数据.xlsx")