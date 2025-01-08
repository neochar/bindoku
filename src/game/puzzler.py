import copy
import random

from game.components.field import Field
from game.const import PUZZLE_MIN_ROW_LEN, PUZZLE_MAX_ROW_LEN
from game.solver import Solver


class Puzzler:
    original: list[list[int]]
    field: list[list[int]]
    solver: Solver
    seed: int

    def __init__(
            self,
            solver: Solver,
    ):
        self.solver = solver

    def puzzle(self, _field: list[list[int]]) -> list[list[int]]:
        """
        TODO
        Hide cells until unsolvable
        """

        while 1:
            field = self.make_puzzle(copy.deepcopy(_field))

            if self.solver.is_solvable(field) and Field.is_incomplete(field):
                return field

    @staticmethod
    def make_puzzle(_field: list[list[int]]) -> list[list[int]]:
        field_len = len(_field)
        side_len = len(_field[0])
        assert field_len == side_len
        for row in range(field_len):
            n = random.randint(PUZZLE_MIN_ROW_LEN, side_len - PUZZLE_MAX_ROW_LEN)
            for col in random.sample(range(0, side_len), n):
                _field[row][col] = 0

        return _field
