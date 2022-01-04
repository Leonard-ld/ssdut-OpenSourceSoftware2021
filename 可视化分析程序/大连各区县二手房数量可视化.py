from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase = myclient["crawl_beike"]
mycollection = mydatabase["area_house_num"]
list0 = list()
listx = list()
listy = list()
pie = Pie(init_opts=opts.InitOpts())
for x in mycollection.find({},{ "_id":0, "area_name": 1}):
    listx.extend(x.values())
for y in mycollection.find({},{ "_id":0, "count(area_name)": 1}):
    listy.extend(y.values())

pie.add("大连各区县二手房数量",[list(z) for z in zip(listx, listy)])
pie.render("C:/Users/Leonard/Desktop/BigDataCourseDesign/htmls/大连各区县二手房数量.html")