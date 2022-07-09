import requests
from bs4 import BeautifulSoup
import pandas as pd
headers = {'user-agent': 'my-app/0.0.1'}
movie_links = []
movie_names = []
movie_info = []
movie_lists = []
all_infos = []

# 1.访问主页面，并且完成页面跳转
def get_page(page_link, genre):
    page = 0
    max_page = 100 # 100是&start=？这个？对应的值，表示第十页的start的值
    while page <= max_page:
        url = page_link + "start=" + page.__str__() + "&genres=" + genre
        response = requests.get(url=url, headers=headers)
        # 验证url的数据有没有错
        print(response.text)
        # 将获取到的string（键值对）转为字典,怎么字典化：eval
        movie_info = eval(movie_info)
        # 在爬取到的一堆信息里提取关键词，以字典形式存放 xx:xx
        # m表示单个的电影信息，即[writer：‘李安’]，通过List.append转储到更大的列表中,给list命名为movielist，并且在文档最上方定义一下
        for m in movie_info['data']:
            movie_lists.append(m)
        # 修改staet参数
        page = page + 20
        # 验证数据正确性
        print(url)

# 整个文档，从下面这行，开始运行
if __name__ == '__main__':
    # 调用功能1，实现页面的访问，page_lin是变量、gener是变量
    get_page("https://movie.douban.com/j/new_search_subjects?"
             "sort=U&range=0,10&tags=&",genre="爱情")

    # 如何存储数据
    # 首先拿到字典形式的{}电影信息，再append到list这个存储容器中，即list.append
    # 再把List转换为二维表dataframe > 再to_excel通过pandas存到excel表里
    data = pd.DataFrame(movie_lists)
    data.to_excel("API参数获取电影数据.xlsx")