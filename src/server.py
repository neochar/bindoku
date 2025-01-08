from typing import Union

from fastapi import FastAPI

from game.generator import Generator
from game.puzzler import Puzzler
from game.solver import Solver
from game.validator import Validator

app = FastAPI()


@app.get("/api/get-board/{sidelen}")
def get_board(sidelen: int, seed: Union[int, None] = None):
    validator = Validator()
    solver = Solver(validator=validator)
    generator = Generator(validator=validator)
    field = generator.generate(sidelen, seed)
    generator.set_puzzleizer(Puzzler(solver=solver))
    puzzle = generator.puzzleize()
    return {
        'field': _prepare_for_app(field),
        'puzzle': _prepare_for_app(puzzle),
    }


def _prepare_for_app(field: list[list[int]]) -> list[list[int or None]]:
    for y, row in enumerate(field):
        for x, col in enumerate(row):
            if col == 0:
                field[y][x] = None
            else:
                field[y][x] = col - 1

    return field
