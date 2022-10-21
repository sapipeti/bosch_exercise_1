from fastapi import FastAPI
import exercise_1_func as func

app = FastAPI()


@app.get("/weather/")
def weather():
    return {"Hello": "World"}
