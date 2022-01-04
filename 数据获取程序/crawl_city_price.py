import requests
import pymongo
from bs4 import BeautifulSoup
import bson
import re

# mongodb数据库连接
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# 数据库名称
mydatabase = myclient["crawl_beike"]
# 数据集合名称
mycollection = mydatabase["AllCitysData"]

def get_all():
    # 用于暂时存储数据的字典
    citys = {
       "dalian":"dl",
       "shenyang":"sy",
       "guangzhou":"gz",
       "beijing":"bj",
       "shanghai":"sh",
       "shenzhen":"sz",
       "xian": "xa",
       "chengdu": "cd"
    }
    # 遍历字典中所有城市爬取二手房信息
    for city in citys.keys():
        get_data(citys[city])

def get_data(city):
    # 网站共有100页数据
    for i in range(1, 101):  
        print("正在下载%s第%s页数据" % (city, i))
        # 贝壳大连二手房信息
        target = 'https://%s.ke.com/ershoufang/pg%s/' % (city, i)  
        main_page = requests.get(target).text
        # 解析html
        content = BeautifulSoup(main_page, "html.parser")  
        # 获取单个房源信息
        urls = content.find_all('a', attrs={'class': 'VIEWDATA CLICKDATA maidian-detail'})
        # 提取出房源信息并写入数据库
        for url in iter(urls):
            house_page = requests.get(url['href']).text
            cont = BeautifulSoup(house_page, "html.parser")
            price_str = cont.find('div', attrs={'class': 'price'})
            area_str = cont.find('div', attrs={'class': 'area'})
            price_perSQM = price_str.find('div', attrs=('class', 'text')).find('span').text
            area = area_str.find('div', attrs=('class', 'mainInfo')).text

            area_digit = float(re.findall(r"\d+\.?\d*",area)[0])
            price_digit = int(price_perSQM)
            mydict = {
                "city": city,
                "area": area_digit,
                "price_perSQM": price_digit
            }
            global mycollection
            mycollection.insert_one(mydict)
    print("数据下载完毕")

if __name__ == '__main__':
    get_all()