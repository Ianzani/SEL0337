import json
from requests import get
from pprint import pprint

stations="https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations"
weather="https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements966583"

#all_stations = get(stations).json()['items']


my_weather=get(weather).json()['items']

pprint(my_weather)