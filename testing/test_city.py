import unittest
from city_function import get_city_country

class CityTestCase(unittest.TestCase):
    """Test for city_function.py"""
    def test_city_country(self):
        formatted_city_country = get_city_country('delhi', 'india')
        self.assertEqual(formatted_city_country, 'Delhi, India')
        
    def test_city_country_population(self):
        """Test for new parameter population"""
        formatted_city_population = get_city_country('delhi', 'india', population=4000000)
        self.assertEqual(formatted_city_population, 'Delhi, India - population 4000000')
        
unittest.main()