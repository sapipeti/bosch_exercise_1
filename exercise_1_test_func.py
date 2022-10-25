import unittest
from unittest.mock import patch

import exercise_1_func


class MyTestCase(unittest.TestCase):
    @patch('exercise_1_func.get_city_coordinates')
    def test_get_city_coordinates(self, mock_get_locations):
        mock_get_locations.return_value = ""
        expected = [exercise_1_func.City("Warsaw", "52.2319581", "21.0067249"),
                    exercise_1_func.City("Budapest", "47.4979937", "19.0403594"),
                    exercise_1_func.City("Prague", "50.0874654", "14.4212535"),
                    exercise_1_func.City("Wien", "48.2083537", "16.3725042")]
        self.assertListEqual(exercise_1_func.get_city_coordinates(""), expected)


if __name__ == '__main__':
    unittest.main()
