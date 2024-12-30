from unittest import TestCase

from game.solver import RowChecker


class TestRowChecker(TestCase):

    def test_try_count(self):
        row = [1, 1, 0, 1, 0, 0]
        self.assertEqual(
            RowChecker.from_row(row).try_count(),
            [1, 1, 2, 1, 2, 2]
        )

    def test_try_101(self):
        self.assertEqual(
            [1, 2, 1, 0, 0, 0],
            RowChecker.from_row([1, 0, 1, 0, 0, 0]).try_101(1)
        )

        self.assertEqual(
            [1, 0, 0, 2, 1, 2],
            RowChecker.from_row([1, 0, 0, 2, 0, 2]).try_101(4)
        )

    def test_try_110(self):
        self.assertEqual(
            [1, 1, 2, 0, 0, 0],
            RowChecker.from_row([1, 1, 0, 0, 0, 0]).try_110(2)
        )
        self.assertEqual(
            [1, 2, 1, 2, 2, 1],
            RowChecker.from_row([1, 2, 1, 2, 2, 0]).try_110(5)
        )

    def test_try_011(self):
        self.assertEqual(
            [2, 1, 1, 0, 0, 0],
            RowChecker.from_row([0, 1, 1, 0, 0, 0]).try_011(0)
        )
        self.assertEqual(
            [0, 0, 0, 1, 2, 2],
            RowChecker.from_row([0, 0, 0, 0, 2, 2]).try_011(3)
        )
