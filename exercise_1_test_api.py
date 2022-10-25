import json
import exercise_1_api
from unittest.mock import patch
import unittest

import exercise_1_func


def get_mock_response():
    with open('mock_response.json', 'r') as f:
        return json.loads(f.read())


class MyTestCase(unittest.TestCase):
    @patch('exercise_1_func.get_weather_data')
    def test_weather(self, mock_get_weather):
        mock_get_weather.return_value = get_mock_response()
        assert exercise_1_api.get_weather(11, 11) == {"coord":{"lon":10.99, "lat":44.34}, "weather":[{"id":803, "main": "Clouds", "description": "broken clouds", "icon": "04d"}], "base": "stations", "main":{"temp":20.43, "feels_like":20.2, "temp_min":17.19, "temp_max":21.71, "pressure":1019, "humidity":64, "sea_level":1019, "grnd_level":935}, "visibility":10000, "wind":{"speed":0.64, "deg":118, "gust":2.37}, "clouds":{"all":54}, "dt":1666704210, "sys":{"type":2, "id":2004688, "country": "IT", "sunrise":1666676603, "sunset":1666714597}, "timezone":7200, "id":3163858, "name": "Zocca", "cod":200}

    @patch('exercise_1_func.get_weather_data')
    def test_get_temp(self, mock_get_weather):
        mock_get_weather.return_value = get_mock_response()
        assert exercise_1_api.get_temp(11, 11) == {"Temperature":{"°C":20.43, "°F":68.774}}

    @patch('exercise_1_func.get_weather_data')
    def test_get_hours_till(self, mock_get_weather):
        mock_get_weather.return_value = get_mock_response()
        assert exercise_1_api.get_hours_till(11, 11) == {"Hours till": "We are closer to sunset(02:53)"}

    @patch('exercise_1_func.get_weather_data')
    def test_get_mood(self, mock_get_weather):
        mock_get_weather.return_value = get_mock_response()
        assert exercise_1_api.get_mood(11, 11) == {"Mood": "Uncertain"}

    @patch('exercise_1_func.get_weather_data')
    def test_get_cities(self, mock_get_weather):
        mock_get_weather.return_value = get_mock_response()
        expected = [exercise_1_func.City("Warsaw", "52.2319581", "21.0067249"),
                    exercise_1_func.City("Budapest", "47.4979937", "19.0403594"),
                    exercise_1_func.City("Prague", "50.0874654", "14.4212535"),
                    exercise_1_func.City("Wien", "48.2083537", "16.3725042")]
        self.assertListEqual(exercise_1_api.get_cities(), expected)
