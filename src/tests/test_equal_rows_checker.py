import unittest

from game.solver import EqualRowsChecker


class TestEqualRowsChecker(unittest.TestCase):

    def test__try_equal_rows(self):
        field = [
            [1, 2, 1, 2, 0, 0],
            [1, 2, 1, 1, 2, 2],
            [2, 1, 2, 2, 1, 1],
            [1, 2, 1, 2, 2, 1],
            [2, 1, 2, 1, 1, 2],
            [2, 1, 2, 1, 2, 1],
        ]

        equal_rows_checker = EqualRowsChecker.from_field(field)
        equal_rows_checker.try_equal_rows()
        self.assertEqual(
            [1, 2, 1, 2, 1, 2],
            equal_rows_checker.field[0]
        )

    def test__real_cases(self):
        cases = [
            {
                'field': [
                    [1, 2, 1, 2, 2, 1, 1, 2],
                    [2, 1, 2, 0, 1, 0, 0, 1],
                    [2, 1, 2, 1, 1, 2, 2, 1],
                    [1, 2, 1, 0, 2, 0, 1, 2],
                    [2, 1, 1, 2, 2, 1, 2, 1],
                    [1, 2, 2, 1, 1, 2, 2, 1],
                    [2, 1, 1, 2, 1, 2, 1, 2],
                    [1, 2, 2, 1, 2, 1, 1, 2],
                ],
                'expect': [
                    [1, 2, 1, 2, 2, 1, 1, 2],
                    [2, 1, 2, 0, 1, 0, 0, 1],
                    [2, 1, 2, 1, 1, 2, 2, 1],
                    [1, 2, 1, 1, 2, 2, 1, 2],
                    [2, 1, 1, 2, 2, 1, 2, 1],
                    [1, 2, 2, 1, 1, 2, 2, 1],
                    [2, 1, 1, 2, 1, 2, 1, 2],
                    [1, 2, 2, 1, 2, 1, 1, 2],
                ]
            }
        ]

        equal_rows_checker = EqualRowsChecker()

        for i, case in enumerate(cases):
            self.assertEqual(
                case['expect'],
                equal_rows_checker.solve(case['field'])
            )

    def test__find_equalities_number(self):
        pass

    def test__fill_empty(self):
        pass
