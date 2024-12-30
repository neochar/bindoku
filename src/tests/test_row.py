import unittest

from game.components.row import Row


class TestRow(unittest.TestCase):
    def test_row_try_value(self):
        row = Row.from_row([0, 0, 2, 1, 2, 0])
        self.assertIsNone(row.try_value(-2))
        self.assertIsNone(row.try_value(-1))
        self.assertIsNone(row.try_value(0))
        self.assertIsNone(row.try_value(1))
        self.assertEqual(2, row.try_value(2))
        self.assertEqual(1, row.try_value(3))
        self.assertEqual(2, row.try_value(4))
        self.assertIsNone(row.try_value(5))
        self.assertIsNone(row.try_value(6))
        self.assertIsNone(row.try_value(7))

    def test__get_values(self):
        row = Row.from_row([1, 1, 2, 1, 2, 2])
        self.assertEqual((None, None, None), row.get_values(-2))
        self.assertEqual((None, None, 1), row.get_values(-1))
        self.assertEqual((None, 1, 1), row.get_values(0))
        self.assertEqual((1, 1, 2), row.get_values(1))
        self.assertEqual((1, 2, 1), row.get_values(2))
        self.assertEqual((2, 1, 2), row.get_values(3))
        self.assertEqual((1, 2, 2), row.get_values(4))
        self.assertEqual((2, 2, None), row.get_values(5))
        self.assertEqual((2, None, None), row.get_values(6))
        self.assertEqual((None, None, None), row.get_values(7))

