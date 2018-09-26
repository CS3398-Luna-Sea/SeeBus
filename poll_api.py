import requests
import json


def get_buses():
    r = requests.get('http://txstate.doublemap.com/map/v2/buses')
    buses = json.loads(r.text)
    return buses


if __name__ == "__main__":
    print(get_buses())