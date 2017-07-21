from requests import get
import json
import matplotlib.pyplot as plt
from dateutil import parser
from pprint import pprint

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/4653201'
stations = get(url).json()['items']
pprint(stations)
