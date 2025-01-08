import unittest

from game.solver import Solver
from game.validator import Validator


class TestSolver(unittest.TestCase):
    def test_is_solvable(self):
        field = [
            [1, 0, 0, 1],
            [0, 0, 0, 1],
            [0, 0, 2, 0],
            [0, 0, 0, 0],
        ]
        solver = Solver(Validator())
        assert solver.is_solvable(field)

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
