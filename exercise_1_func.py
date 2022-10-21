import time
import requests
import constants

api_key = constants.API_KEY_OPENWEATHER


def get_weather_data(lat, lon, units="metric"):
    url = "https://api.openweathermap.org/data/2.5/weather?lat="+str(lat)+"&lon="+str(lon)+"&appid="+api_key+"&units="+units
    response = requests.request("GET", url)
    return response.json()


def calculate_fahrenheit(input_json):
    temp_c = float(input_json["main"]["temp"])
    temp_f = (temp_c * 1.8) + 32
    return temp_f


def hours_till(input_json):
    sunrise = int(input_json["sys"]["sunrise"])
    sunset = int(input_json["sys"]["sunset"])
    date = int(input_json["dt"])

    if abs(date - sunrise) < abs(sunset - date):
        return "We are closer to sunrise(" + time.strftime("%H:%M", time.gmtime(abs(date - sunrise)))+")"
    elif abs(date - sunrise) > abs(sunset - date):
        return "We are closer to sunset(" + time.strftime("%H:%M", time.gmtime(abs(sunset - date)))+")"
    else:
        return "We are equally away from sunrise and sunset."