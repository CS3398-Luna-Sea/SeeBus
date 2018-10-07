import pymongo




myclient = pymongo.MongoClient("mongodb://localhost:27017/")
print myclient.list_database_names()

mydb = myclient["PleaseHey"]
mycol = mydb["HeyThere"]


mydict = {"name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)


mydb = myclient["Newdb"]
mycol = mydb["NewCollection"]


mydict = {"name": "Miguel", "address": "im not telling" }

x = mycol.insert_one(mydict)







