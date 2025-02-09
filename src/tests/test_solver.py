import unittest

from game.solver import Solver
from game.validator import Validator


class TestSolver(unittest.TestCase):
    @staticmethod
    def _get_solver():
        return Solver(Validator())

    def test_is_solvable(self):
        field = [
            [1, 0, 0, 1],
            [0, 0, 0, 1],
            [0, 0, 2, 0],
            [0, 0, 0, 0],
        ]
        solver = Solver(Validator())
        self.assertIs(True, solver.is_solvable(field))

    def test_is_valid(self):
        field = [
            [1, 2, 1, 2, 1, 2],
            [1, 2, 2, 1, 2, 1],
            [2, 1, 1, 2, 1, 2],
            [1, 2, 1, 1, 2, 2],
            [2, 1, 2, 2, 1, 1],
            [2, 1, 2, 1, 2, 1],
        ]

        assert Validator().validate(field)[0] is True

    def test_10x10(self):
        field = [
            [0, 0, 0, 1, 0, 2, 2, 0, 0, 2],
            [0, 1, 0, 0, 0, 2, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 2, 0, 0],
            [0, 1, 0, 2, 0, 2, 0, 2, 1, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 1, 2],
            [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 2, 1, 0, 1, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0, 2, 2, 1],
            [0, 0, 1, 0, 1, 0, 1, 0, 2, 1],
        ]

        solver = Solver(Validator())
        assert solver.is_solvable(field)

    def test_12x12(self):
        field = [
            [0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 2, 0, 0, 2, 0, 1, 2, 0],
            [0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 2, 0],
            [0, 0, 0, 0, 2, 0, 0, 2, 0, 1, 0, 0],
            [0, 1, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0],
            [2, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 2, 1, 0, 1, 0, 0, 1],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0, 2, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        ]

        solver = Solver(Validator())
        assert solver.is_solvable(field)

    def test_puzzles_from_app(self):
        fields = [
            # 4x4
            [[0, 0, 0, 1],
             [0, 0, 0, 0],
             [2, 0, 2, 0],
             [0, 0, 2, 0]],
            [[0, 2, 2, 0],
             [0, 0, 0, 2],
             [1, 0, 1, 0],
             [0, 0, 0, 0]],
            [[1, 0, 1, 0],
             [0, 0, 0, 0],
             [0, 0, 1, 0],
             [0, 2, 0, 0]],

            # 6x6
            [[1, 0, 2, 0, 0, 0],
             [0, 1, 0, 0, 0, 0],
             [1, 0, 2, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [2, 2, 0, 2, 0, 0],
             [0, 1, 0, 2, 0, 0]],
            [[2, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 1, 0],
             [0, 0, 0, 2, 0, 0],
             [0, 0, 1, 0, 1, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 2, 0, 0, 1]],
            [[0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 1, 0],
             [0, 0, 0, 0, 1, 2],
             [0, 0, 0, 0, 0, 2],
             [0, 1, 0, 0, 0, 0],
             [2, 0, 2, 0, 0, 0]],
            [[1, 0, 2, 0, 0, 0],
             [0, 1, 0, 0, 0, 0],
             [1, 0, 2, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [2, 2, 0, 2, 0, 0],
             [0, 1, 0, 2, 0, 0]],

            # 8x8
            [[0, 2, 2, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 2],
             [0, 0, 0, 0, 0, 1, 1, 0],
             [0, 1, 0, 0, 1, 0, 0, 0],
             [2, 0, 2, 0, 1, 0, 0, 0],
             [0, 0, 2, 0, 0, 0, 2, 0],
             [0, 0, 0, 0, 0, 1, 1, 0]],
            [[0, 2, 0, 1, 0, 0, 1, 0],
             [0, 2, 0, 0, 0, 2, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 0, 0, 1],
             [0, 2, 2, 0, 0, 0, 0, 0],
             [0, 2, 0, 1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 2],
             [0, 0, 0, 0, 0, 0, 0, 2]],
            [[1, 0, 0, 2, 2, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1],
             [2, 0, 0, 0, 0, 2, 2, 0],
             [0, 0, 1, 0, 2, 0, 0, 0],
             [0, 1, 1, 0, 0, 1, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 2, 0, 0, 0, 2],
             [1, 0, 0, 0, 0, 1, 0, 2]],

            # 10x10
            [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 1, 0, 2, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 2, 0, 2, 0],
             [2, 0, 0, 0, 0, 1, 0, 0, 2, 0],
             [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
             [0, 2, 2, 0, 0, 0, 2, 0, 0, 0],
             [0, 2, 0, 0, 0, 2, 0, 1, 0, 0],
             [2, 0, 0, 0, 0, 0, 0, 0, 1, 0],
             [0, 0, 0, 2, 0, 1, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 1, 0, 0, 0, 0]],
            [[0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
             [2, 0, 0, 0, 0, 1, 1, 0, 0, 0],
             [0, 0, 1, 0, 0, 2, 0, 0, 0, 1],
             [2, 0, 0, 1, 0, 0, 0, 0, 2, 0],
             [0, 0, 0, 0, 2, 0, 0, 0, 0, 2],
             [0, 2, 0, 0, 0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 2, 2, 0, 2, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
             [2, 0, 0, 1, 0, 0, 0, 0, 2, 0],
             [2, 0, 0, 1, 1, 0, 0, 0, 0, 0]],
            [[0, 0, 2, 0, 0, 0, 1, 1, 0, 0],
             [0, 1, 0, 0, 2, 2, 0, 0, 2, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
             [2, 0, 0, 0, 1, 1, 0, 0, 0, 1],
             [2, 2, 0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
             [0, 0, 0, 2, 0, 0, 1, 0, 0, 0],
             [0, 1, 0, 0, 1, 0, 0, 2, 0, 0]],
        ]

        solver = self._get_solver()
        for i, field in enumerate(fields):
            with self.subTest(label=f'{len(field)}x{len(field)}', i=i):
                self.assertIs(True, solver.is_solvable(field))

    # def test_puzzle_solved(self):
    #     puzzle = [
    #         [0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
    #         [2, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    #         [0, 0, 1, 0, 0, 2, 0, 0, 0, 1],
    #         [2, 0, 0, 1, 0, 0, 0, 0, 2, 0],
    #         [0, 0, 0, 0, 2, 0, 0, 0, 0, 2],
    #         [0, 2, 0, 0, 0, 0, 0, 0, 1, 0],
    #         [0, 0, 0, 0, 2, 2, 0, 2, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    #         [2, 0, 0, 1, 0, 0, 0, 0, 2, 0],
    #         [2, 0, 0, 1, 1, 0, 0, 0, 0, 0]
    #     ]
    #     field = [
    #         [1, 2, 1, 2, 2, 1, 1, 2, 1, 2],
    #         [2, 1, 2, 1, 2, 1, 1, 2, 1, 2],
    #         [1, 2, 1, 2, 1, 2, 2, 1, 2, 1],
    #         [2, 1, 2, 1, 1, 2, 1, 2, 2, 1],
    #         [1, 2, 1, 2, 2, 1, 2, 1, 1, 2],
    #         [2, 2, 1, 2, 1, 1, 2, 1, 1, 2],
    #         [1, 1, 2, 1, 2, 2, 1, 2, 2, 1],
    #         [1, 1, 2, 2, 1, 2, 1, 2, 1, 2],
    #         [2, 2, 1, 1, 2, 1, 2, 1, 2, 1],
    #         [2, 1, 2, 1, 1, 2, 2, 1, 2, 1],
    #     ]
    #
    #     solver = self._get_solver()
    #     solver.solve(puzzle)
