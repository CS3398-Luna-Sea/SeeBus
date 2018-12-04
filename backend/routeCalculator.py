import poll_api as api
import pymongo
import datetime
import time


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["TestBusDatabase"]
mycol = mydb["FridayCollection"]

# for x in mycol.find():
#    print(x)

class StopCalculator:

    # Query's for stops and arrival times of bus 401

    def BobcatStadiumQuery():

        cursor = mydb.mycol.find({"stop": "3"})
        print(cursor)
        # Bobcat Stadium route stop 3(Bobcat Stadium East) departure time

        # Bobcat Stadium route stop 4(Bobcat Stadium West) arrival time
        for x in mycol.find({}, {"buses": "401", "route": "646", "_id": 0}):
            print(x)

if __name__ == '__main__':

    sc = StopCalculator
    sc.BobcatStadiumQuery()