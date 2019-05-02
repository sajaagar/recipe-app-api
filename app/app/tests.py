from django.test import TestCase

from app.calc import add, sub


class CalcTests (TestCase):

    def test_add_numbers(self):
        """Add numbers"""
        self.assertEqual(add(3, 5), 8)

    def test_sub_numbers(self):
        """Sub numbers"""
        self.assertEqual(sub(5, 10), 5)
