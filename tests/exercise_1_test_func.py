import json
import unittest
from unittest.mock import patch

from src import exercise_1_func


class MyTestCase(unittest.TestCase):
    # Unit test of get_city_temp_c
    @patch('src.exercise_1_func.make_api_call')
    def test_get_city_temp_c(self, mock_get_call):
        cities = [exercise_1_func.City("Warsaw", 52.2319581, 21.0067249),
                  exercise_1_func.City("Budapest", 47.4979937, 19.0403594)]
        with open("../data/mock_city_temp.json", "r") as f:
            mock_get_call.side_effect = json.loads(f.read())

        expected = {'Warsaw': 11.91, 'Budapest': 15.63}
        self.assertEqual(expected, exercise_1_func.get_city_temp_c(cities))

    # Testing convert_city_temp & calculate_fahrenheit
    def test_convert_city_temp(self):
        city_temp_c = {'Warsaw': 11.91, 'Budapest': 15.63}

        expected = {'Warsaw': 53.438, 'Budapest': 60.134}
        self.assertEqual(expected, exercise_1_func.convert_city_temp(city_temp_c))


if __name__ == '__main__':
    unittest.main()
