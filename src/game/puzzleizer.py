import random

from game.const import PUZZLE_MIN_ROW_LEN
from game.solver import Solver


class Puzzleizer:
    field: list[list[int]]
    solver: Solver
    seed: int

    def __init__(
            self,
            solver: Solver,
    ):
        self.solver = solver

    def puzzleize(self, field: list[list[int]]) -> list[list[int]]:
        self.field = field
        return self.make_puzzle(self.field[::])

        # while self.solver.solvable(
        #         self.make_puzzle(self.field[::])
        # ) is False:
        #     continue
        #
        # return field

    @staticmethod
    def make_puzzle(field: list[list[int]]) -> list[list[int]]:
        field_len = len(field)
        for row in range(field_len):
            n = random.randint(PUZZLE_MIN_ROW_LEN, field_len - 1)
            for col in random.sample(range(0, field_len), n):
                field[row][col] = 0

        return field
