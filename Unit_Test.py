
import unittest
from Journal_Practice import city_country

class NameTester(unittest.TestCase):
    def test_city_country(self):
        formatted_string = city_country("karachi", "Pakistan")
        self.assertEqual(formatted_string, "Karachi, Pakistan")
    def test_city_country_population(self):
        formatted_string = city_country("karachi", "Pakistan", "22 crore")
        self.assertEqual(formatted_string, "Karachi, Pakistan - population 22 crore")


if __name__ == "__main":
    unittest.main()





