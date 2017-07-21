from requests import get
import json
import matplotlib.pyplot as plt
from dateutil import parser
from pprint import pprint
from haversine import haversine

stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

my_lat = 2.971941
my_lon = 101.810586
all_stations = get(stations).json()['items']

def find_closest():
    smallest = 20036
    for station in all_stations:
        station_lon = station['weather_stn_long']
        station_lat = station['weather_stn_lat']
        distance = haversine(my_lon, my_lat, station_lon, station_lat)
        if distance < smallest:
            smallest = distance
            closest_station = station['weather_stn_id']
    return closest_station 
find_closest()
