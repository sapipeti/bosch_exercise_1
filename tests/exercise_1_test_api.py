import json
from src import exercise_1_api, exercise_1_func
from unittest.mock import patch
import unittest


def get_mock_response():
    with open('../data/mock_weather.json', 'r') as f:
        return json.loads(f.read())


class MyTestCase(unittest.TestCase):
    @patch('exercise_1_func.make_api_call')
    def test_get_weather(self, mock_get_api_call):
        mock_get_api_call.return_value = get_mock_response()
        assert exercise_1_api.get_weather(11, 11) == get_mock_response()

    # The get_city_lat_lon is mocked, it's tested bellow in the test_get_cities
    @patch('exercise_1_func.get_city_lat_lon')
    @patch('exercise_1_func.make_api_call')
    def test_get_report_city(self, make_api_call, mock_get_city_lat_lon):
        mock_get_city_lat_lon.return_value = [exercise_1_func.City("Zocca", "47.4979937", "19.0403594")]
        make_api_call.return_value = get_mock_response()
        self.assertEqual(exercise_1_api.get_report_city("IT", "Zocca"),
                         {"City": "Zocca", "Hours till": "We are closer to sunset(02:53)",
                          "Temperature": {"°C": 20.43, "°F": 68.774}, "Mood": "Uncertain"})

    @patch('exercise_1_func.make_api_call')
    def test_get_temp(self, mock_get_api_call):
        mock_get_api_call.return_value = get_mock_response()
        assert exercise_1_api.get_temp(11, 11) == {"Temperature": {"°C": 20.43, "°F": 68.774}}

    @patch('exercise_1_func.make_api_call')
    def test_get_hours_till(self, mock_get_api_call):
        mock_get_api_call.return_value = get_mock_response()
        assert exercise_1_api.get_hours_till(11, 11) == {"Hours till": "We are closer to sunset(02:53)"}

    @patch('exercise_1_func.make_api_call')
    def test_get_mood(self, mock_get_api_call):
        mock_get_api_call.return_value = get_mock_response()
        assert exercise_1_api.get_mood(11, 11) == {"Mood": "Uncertain"}

    @patch('exercise_1_func.make_api_call')
    def test_get_cities(self, mock_get_api_call):
        with open('../data/mock_cities.json', 'r', encoding="utf8") as f:
            mock_get_api_call.side_effect = json.loads(f.read())

        expected = [exercise_1_func.City("Warsaw", "52.2319581", "21.0067249"),
                    exercise_1_func.City("Budapest", "47.4979937", "19.0403594"),
                    exercise_1_func.City("Prague", "50.0874654", "14.4212535"),
                    exercise_1_func.City("Wien", "48.2083537", "16.3725042")]
        self.assertListEqual(exercise_1_api.get_cities(), expected)
