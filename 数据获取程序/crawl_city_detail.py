import requests
import pymongo
from bs4 import BeautifulSoup

# mongodb数据库连接
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase = myclient["crawl_beike"]
mycollection = mydatabase["sz"]

def get_all():
    citys = {
       "dalian":"dl",
       "shenyang":"sy",
       "guangzhou":"gz",
       "beijing":"bj",
       "shanghai":"sh",
       "shenzhen":"sz",
       "xian":"xa",
       "chengdu": "cd"
    }
    # 遍历字典中所有城市爬取二手房信息
    for city in citys.keys():
        get_data(citys[city])

def get_data(city):
    global mycollection, mydatabase
    mycollection = mydatabase[city]
    # 网站共有100页数据
    for i in range(1, 101):  
        print("正在%s的下载第%s页数据" % (city,i))
        # 二手房网站
        target = 'https://%s.ke.com/ershoufang/pg%s/' % (city,i)  
        main_page = requests.get(target).text
        # 解析html
        content = BeautifulSoup(main_page, "html.parser")  
        # 获取单个房源信息
        urls = content.find_all('a', attrs={'class': 'VIEWDATA CLICKDATA maidian-detail'})
        # 提取出房源信息并写入数据库
        for url in iter(urls):
            print(url['href'])
            house_page = requests.get(url['href']).text
            cont = BeautifulSoup(house_page, "html.parser")
            price_str = cont.find('div', attrs={'class': 'price'})
            community_name_str = cont.find('div', attrs={'class': 'communityName'})
            area_name_str = cont.find('div', attrs={'class': 'areaName'})
            price = price_str.find_all('span')[0].text
            price_unit = price_str.find_all('span')[1].find('span').text
            price_perSQM = price_str.find('div', attrs=('class', 'text')).find('span').text
            price_perSQM_unit = price_str.find('div', attrs=('class', 'text')).find('i').text
            community_name = community_name_str.find('a').text
            area_name = area_name_str.find('a').text
            mydict = {
                "price": price,
                "price_unit": price_unit,
                "price_perSQM": price_perSQM,
                "price_perSQM_unit": price_perSQM_unit,
                "community_name": community_name,
                "area_name": area_name
            }
            global mycollection
            mycollection.insert_one(mydict)
    print("数据下载完毕")
 


if __name__ == '__main__':
    get_all()