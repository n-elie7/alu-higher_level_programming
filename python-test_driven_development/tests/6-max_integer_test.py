import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 2, 4]), 4)

    def test_max_at_start(self):
        self.assertEqual(max_integer([9, 2, 3, 1]), 9)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-5, -1, -7]), -1)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)
