#Nomes: Gabriel Domingues       NUSP:11800903
#       Ian Zaniolo Sirbone     NUSP:04735640
#Código Clima

import json
from requests import get
from pprint import pprint

weather="https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/966583"

my_weather=get(weather).json()['items']
pprint(my_weather)