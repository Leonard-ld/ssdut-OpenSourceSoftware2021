import pandas
import matplotlib.pyplot
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase = myclient["crawl_beike"]
mycollection = mydatabase["temp"]
l = list()
for x in mycollection.find({},{ "_id":0, "(area * CAST(price_perSQM AS DOUBLE))": 1}):
    l.extend(x.values())
matplotlib.pyplot.style.use('ggplot')
area = pandas.DataFrame(l)
area.hist(bins=52, alpha=1, range=[100000,2700000])
matplotlib.pyplot.show()