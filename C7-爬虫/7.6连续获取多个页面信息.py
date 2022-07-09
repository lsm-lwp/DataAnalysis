import requests
from bs4 import BeautifulSoup

# 访问豆瓣电影top250的主页
# 访问网页、获取信息（基础操作，只留这一个步骤，其他挪到下面的while循环里面）
headers = {'user-agent':'my-app/0.0.1'}

# 实现页面自动跳转 ?start=225&filter= （学会观察跳转页面前后的url网址的变化及内在关系）
# 经过观察，豆瓣top250的网址变化是?start=0&filter=、?start=25&filter=、...50...以此类推
# 解析版本看word
page = 0
max_page = 225
movie_links = []
movie_names = []
while page <= max_page:
    url = "https://movie.douban.com/top250?start=" + page.__str__() + "&filter="
    response = requests.get(url=url, headers=headers)
    #print(response.text)
    #实现每个页面信息的抓取：电影单链（点击电影标题后自动跳转的电影详情页链接）
    soup = BeautifulSoup(response.text,'html.parser')
    #print(soup.find_all(class_="hd")) 停用这种初级的print方法，因为还没上容器

    for hhh in soup.find_all(class_="hd"):
        movie_names.append(hhh.find(class_="title").string)
        movie_links.append(hhh.find('a',href=True).attrs['href']) #该代码句式（）来自百度博客，搜【bs库 href抓取】，截取了有用的部分
    # 修改staet参数，20是要根据所爬取的网页一页有多少部电影而改的，20=一页20部电影，想要获取下一页，就+20
    page = page + 25
    print(url)
    #exit()

# 浏览所有抓取到的信息
for name,link in zip(movie_names,movie_links):
    print(name,":",link)
