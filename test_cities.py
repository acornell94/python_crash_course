import unittest
from city_functions import location


class CityTestCase(unittest.TestCase):
    """Test functionality of city_functions.py"""
    
    def test_location(self):
        """Test whether a city, country format works."""
        tested_location = location("montreal", "canada")
        self.assertEqual(tested_location, 'Montreal, Canada')

unittest.main()