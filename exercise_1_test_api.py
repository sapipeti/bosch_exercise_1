import json
import exercise_1_api
from unittest.mock import patch
import unittest

import exercise_1_func


def get_mock_response():
    with open('mock_weather.json', 'r') as f:
        return json.loads(f.read())


class MyTestCase(unittest.TestCase):
    @patch('exercise_1_func.get_weather_data')
    def test_weather(self, mock_get_weather):
        mock_get_weather.return_value = get_mock_response()
        assert exercise_1_api.get_weather(11, 11) == get_mock_response()

    @patch('exercise_1_func.get_weather_data')
    def test_get_temp(self, mock_get_weather):
        mock_get_weather.return_value = get_mock_response()
        assert exercise_1_api.get_temp(11, 11) == {"Temperature": {"°C": 20.43, "°F": 68.774}}

    @patch('exercise_1_func.get_weather_data')
    def test_get_hours_till(self, mock_get_weather):
        mock_get_weather.return_value = get_mock_response()
        assert exercise_1_api.get_hours_till(11, 11) == {"Hours till": "We are closer to sunset(02:53)"}

    @patch('exercise_1_func.get_weather_data')
    def test_get_mood(self, mock_get_weather):
        mock_get_weather.return_value = get_mock_response()
        assert exercise_1_api.get_mood(11, 11) == {"Mood": "Uncertain"}

    def test_get_cities(self):
        expected = [exercise_1_func.City("Warsaw", "52.2319581", "21.0067249"),
                    exercise_1_func.City("Budapest", "47.4979937", "19.0403594"),
                    exercise_1_func.City("Prague", "50.0874654", "14.4212535"),
                    exercise_1_func.City("Wien", "48.2083537", "16.3725042")]
        self.assertListEqual(exercise_1_api.get_cities(), expected)
