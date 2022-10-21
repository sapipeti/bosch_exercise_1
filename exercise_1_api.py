from fastapi import FastAPI
import exercise_1_func as func

app = FastAPI()


@app.get("/weather/")
def weather(lat, lon):
    return func.get_weather_data(lat, lon)

@app.get("/weather/report/")
def temp(lat, lon):
    pass

@app.get("/weather/report/temp")
def temp(lat, lon):
    return func.calculate_fahrenheit(func.get_weather_data(lat, lon))

@app.get("/weather/report/hours_till")
def temp(lat, lon):
    return func.hours_till(func.get_weather_data(lat, lon))
