import copy
import unittest

from game.components.row import Row
from game.solver import ExclusionChecker


class TestExclusionChecker(unittest.TestCase):
    @staticmethod
    def _get_checker():
        return ExclusionChecker()

    @staticmethod
    def _get_row(_row: list[int] | None = None) -> Row:
        row = Row()
        row.set_row(_row or [0, 1, 0, 0, 2, 1])

        return row

    def test__try_row_by_exclusion(self):
        _rows = [
        ]
        for _row in _rows:
            row = Row.from_row(_row)
            expected = copy.deepcopy(row)
            expected.row[0] = 1
            self.assertNotEqual(expected.row, row)

            exclusion_checker = ExclusionChecker()
            self.assertEqual(
                expected.row,
                exclusion_checker.try_row_exclusion(row)
            )

    def test__some_cases(self):
        cases = [
            {
                'puzzle': [0, 2, 0, 0, 1, 2, 2, 1],
                'expect': [1, 2, 0, 0, 1, 2, 2, 1]
            },
            {
                'puzzle': [2, 2, 1, 2, 0, 1, 0, 2, 0, 0],
                'expect': [2, 2, 1, 2, 0, 1, 0, 2, 1, 1],
            },
            {
                'puzzle': [0, 0, 2, 0, 1, 2, 1, 2, 1, 1],
                'expect': [2, 0, 2, 2, 1, 2, 1, 2, 1, 1],
            },
        ]

        for case in cases:
            self.assertEqual(
                case['expect'],
                self._get_checker().try_row_exclusion(
                    Row.from_row(case['puzzle'])
                )
            )
