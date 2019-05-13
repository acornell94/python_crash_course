import unittest
from city_functions import location


class CityTestCase(unittest.TestCase):
    """Test functionality of city_functions.py"""
    
    def test_city_country(self):
        """Test whether a city, country format works."""
        tested_location = location("montreal", "canada")
        self.assertEqual(tested_location, 'Montreal, Canada')

    def test_city_state_country(self):
        """Test city, state, country format."""
        tested_location = location("Chicago", "United States of America", "Illinois")
        self.assertEqual(tested_location, "Chicago, Illinois, United States Of America")

unittest.main()