import unittest

from game.components.row import Row
from game.solver import EqualRowsChecker


class TestEqualRowsChecker(unittest.TestCase):
    @staticmethod
    def _get_field() -> list[list[int]]:
        return [
            [0, 1, 0, 0, 2, 1],
            [0, 2, 0, 0, 1, 2],
            [2, 1, 2, 2, 1, 1],
            [1, 2, 1, 1, 2, 2],
            [2, 2, 1, 2, 1, 1],
            [1, 1, 2, 1, 2, 2],
        ]

    def test_try_equal_rows(self):
        pass

    def test__find_equalities_number(self):
        pass

    def test__fill_empty(self):
        pass

    def test__try_semiequal_rows(self):
        expected = self._get_field()
        expected[0][0] = 2
        expected[1][0] = 1

        self.assertNotEqual(self._get_field(), expected)

        equal_rows_checker = EqualRowsChecker.from_field(self._get_field())
        self.assertEqual(
            equal_rows_checker.try_semiequal_rows(),
            expected
        )

    def test__try_semiequal_row(self):
        equal_rows_checker = EqualRowsChecker()
        row = Row.from_row([0, 1, 0, 0, 2, 1])
        expected = [2, 1, 0, 0, 2, 1]
        self.assertEqual(
            expected,
            equal_rows_checker._try_semiequal_row(row)
        )
