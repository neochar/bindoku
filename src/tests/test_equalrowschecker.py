import unittest

from game.components.row import Row
from game.solver.equalrowschecker import EqualRowsChecker
from game.solver.exclusionchecker import ExclusionChecker


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

    def test__try_equal_rows(self):
        # TODO implement equal rows checker
        EqualRowsChecker()
        pass

    def test__find_equalities_number(self):
        pass

    def test__fill_empty(self):
        pass

    def test__try_row_by_exclusion(self):
        expected = self._get_field()
        expected[0][0] = 2
        expected[1][0] = 1

        self.assertNotEqual(self._get_field(), expected)

        exclusion_checker = ExclusionChecker.from_field(self._get_field())
        self.assertEqual(
            exclusion_checker.try_by_exclusion(),
            expected
        )

    def test__try_by_exclusion(self):
        exclusion_checker = ExclusionChecker()
        row = Row.from_row([0, 1, 0, 0, 2, 1])
        expected = [2, 1, 0, 0, 2, 1]
        self.assertEqual(
            expected,
            exclusion_checker._try_by_exclusion(row)
        )
