import time
import requests
from constants import exercise_1_constants as con
import matplotlib.pyplot as plt

api_key = con.API_KEY_OPENWEATHER


def make_api_call(operation, url, params):
    response = requests.request(operation, url, params=params)
    return response.json()


def get_weather_data(lat, lon, units="metric"):
    params = {"lon": lon, "lat": lat, "appid": api_key, "units": units}
    url = "https://api.openweathermap.org/data/2.5/weather"
    response_json = make_api_call("GET", url, params)
    return response_json


def calculate_fahrenheit(temp_c):
    temp_f = (temp_c * 1.8) + 32
    return temp_f


def hours_till(input_json):
    sunrise = int(input_json["sys"]["sunrise"])
    sunset = int(input_json["sys"]["sunset"])
    date = int(input_json["dt"])

    if abs(date - sunrise) < abs(sunset - date):
        return "We are closer to sunrise(" + time.strftime("%H:%M", time.gmtime(abs(date - sunrise))) + ")"
    elif abs(date - sunrise) > abs(sunset - date):
        return "We are closer to sunset(" + time.strftime("%H:%M", time.gmtime(abs(sunset - date))) + ")"
    else:
        return "We are equally away from sunrise and sunset."


def calculate_mood(input_json):
    temp_c = float(input_json["main"]["temp"])
    cloudiness = float(input_json["clouds"]["all"])

    if cloudiness < 30:
        if temp_c < 29:
            return "Happy"
        return "Exhausted"
    elif cloudiness < 70:
        if temp_c < 29:
            return "Uncertain"
        return "Grateful"
    else:
        if temp_c < 10:
            return "Depressed"
        elif temp_c < 20:
            return "Annoyed"
        elif temp_c < 30:
            return "Uncertain"
        return "Doomsday"


class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = str(lat)
        self.lon = str(lon)

    def __str__(self):
        return "Name: " + self.name + " Lat: " + self.lat + " Lon: " + self.lon

    def __eq__(self, other):
        return vars(self) == vars(other)


def get_city_lat_lon(locations):
    city_coordinates = []
    url = "http://api.openweathermap.org/geo/1.0/direct"

    for country, city in locations.items():
        params = {"q": city + "," + country, "limit": 1, "appid": api_key}
        response_json = make_api_call("GET", url, params)
        city_coordinates.append(City(city, response_json[0]["lat"], response_json[0]["lon"]))
    return city_coordinates


def get_city_temp_c(city_coordinates):
    city_temp_c = {}
    url = "https://api.openweathermap.org/data/2.5/weather"

    for city in city_coordinates:
        params = {"lat": city.lat, "lon": city.lon, "appid": api_key, "units": "metric"}
        response_json = make_api_call("GET", url, params)
        city_temp_c[city.name] = response_json["main"]["temp"]
    return city_temp_c


def convert_city_temp(city_temp_c):
    city_temp_f = {}

    for city, celsius in city_temp_c.items():
        city_temp_f[city] = calculate_fahrenheit(celsius)
    return city_temp_f


def get_plot():
    locations = {"PL": "Warsaw", "HU": "Budapest", "CZ": "Prague", "AT": "Wien"}

    city_coordinates = get_city_lat_lon(locations)
    city_temp_c = get_city_temp_c(city_coordinates)
    city_temp_f = convert_city_temp(city_temp_c)

    fig = plt.figure()
    fig.set_figheight(5)
    fig.set_figwidth(10)

    plt.suptitle('Cities Temperatures')
    plt.subplot(121)
    plt.bar(list(city_temp_c.keys()), list(city_temp_c.values()))
    plt.ylabel('Temperature (°C)')
    plt.subplot(122)
    plt.bar(list(city_temp_f.keys()), list(city_temp_f.values()))
    plt.ylabel('Temperature (°F)')
    plt.savefig("../pictures/report"+time.strftime("%Y%m%d-%H%M%S")+".png")
