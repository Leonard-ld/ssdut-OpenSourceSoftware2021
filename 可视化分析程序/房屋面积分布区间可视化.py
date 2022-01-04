import pandas
import matplotlib.pyplot
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase = myclient["crawl_beike"]
mycollection = mydatabase["AllCitysData"]
l = list()
for x in mycollection.find({},{ "_id":0, "area": 1}):
    l.extend(x.values())
matplotlib.pyplot.style.use('ggplot')
area = pandas.DataFrame(l)
area.hist(bins=60, alpha=1, range=[20,320])
matplotlib.pyplot.show()