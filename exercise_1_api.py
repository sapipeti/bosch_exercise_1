import requests
from fastapi import FastAPI
import exercise_1_func as func
from starlette.responses import FileResponse

app = FastAPI()


@app.get("/weather/")
def weather(lat, lon):
    return func.get_weather_data(lat, lon)


@app.get("/weather/report/")
def temp(lat, lon):
    response_json = func.get_weather_data(lat, lon)
    report = {"City": response_json["name"], "Hours till": func.hours_till(response_json),
              "Temperature": {"°C": response_json["main"]["temp"],
                              "°F": func.calculate_fahrenheit(float(response_json["main"]["temp"]))},
              "Mood": func.calculate_mood(response_json)}
    return report


@app.get("/weather/report/temp")
def temp(lat, lon):
    response_json = func.get_weather_data(lat, lon)
    return {"Temperature": {"°C": response_json["main"]["temp"],
                            "°F": func.calculate_fahrenheit(float(response_json["main"]["temp"]))}}


@app.get("/weather/report/hours_till")
def temp(lat, lon):
    return {"Hours till": func.hours_till(func.get_weather_data(lat, lon))}


@app.get("/weather/report/mood")
def temp(lat, lon):
    return {"Mood": func.calculate_mood(func.get_weather_data(lat, lon))}


@app.get("/weather/plot/")
def temp():
    func.get_plot()
    return FileResponse(path="report.png", filename="report.png", media_type='text/png')


@app.get('/city_coordinates/')
def fetch_users():
    locations = {"PL": "Warsaw", "HU": "Budapest", "CZ": "Prague", "AT": "Wien"}
    return func.get_city_coordinates(locations)
