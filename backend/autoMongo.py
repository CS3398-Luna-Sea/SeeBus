import poll_api as api
import pymongo
import datetime
import time



class AutoMongo:
    def currentDay(self):
        today = datetime.datetime.today().weekday()
        if today == 0:
            return "Monday"
        if today == 1:
            return "Tuesday"
        if today == 2:
            return "Wednesday"
        if today == 3:
            return "Thursday"
        if today == 4:
            return "Friday"
        if today == 5:
            return "Saturday"
        if today == 6:
            return "Sunday"

    def insert_Buses(self):

        while True:
            bus_dict = api.get_buses()
            x = mycol.insert_many(bus_dict)
            time.sleep(5)

if __name__ == '__main__':

    am = AutoMongo()
    print("Today is: " + am.currentDay())


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient[am.currentDay() + "BusDatabase"]
mycol = mydb[am.currentDay() + "BusCollection"]
am.insert_Buses()
print (myclient.list_database_names())








