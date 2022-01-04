from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase = myclient["crawl_beike"]
mycollection = mydatabase["avg_city"]
list0 = list()
listx = list()
listy = list()
bar = Bar(init_opts=opts.InitOpts(width="1000px", height="800px", theme=ThemeType.LIGHT))
for x in mycollection.find({},{ "_id":0, "city": 1}):
    listx.extend(x.values())
for y in mycollection.find({},{ "_id":0, "(sum((CAST(price_perSQM AS DOUBLE) * area)) / sum(area))": 1}):
    list0.extend(y.values())
listy = [int(i) for i in list0]

bar.add_xaxis(listx)
bar.add_yaxis("均价", listy)
bar.set_global_opts(title_opts=opts.TitleOpts(title="国内部分城市二手房均价", subtitle="单位：元/平方米"))
bar.render("C:/Users/Leonard/Desktop/BigDataCourseDesign/htmls/国内部分城市均价.html")