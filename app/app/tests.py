"""
Sample test
"""
from django.test import SimpleTestCase

from app import testCalc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        res = testCalc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_number(self):
        res = testCalc.subtract(10,15)
        self.assertEqual(res, 5)
