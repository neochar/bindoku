import random
from typing import Callable

from game.components.field import Field
from game.puzzleizer import Puzzleizer
from game.validator import Validator


class Generator:
    # TODO move props here
    puzzleizer: Puzzleizer or None = None

    def __init__(
            self,
            validator: Validator,
            render_callback: Callable,  # for debug
            seed: int = 1
    ):
        self.validator = validator
        self.field = None
        self.seed = seed  # TODO make seed generator for non-local env
        self.field_size = None
        self.render_callback = render_callback
        random.seed(self.seed)

    def set_puzzleizer(self, puzzleizer: Puzzleizer):
        self.puzzleizer = puzzleizer

    def generate(self, field_size: int, seed: int = None) -> list[list[int]]:
        if seed is not None:
            self.seed = seed

        self.field_size = field_size

        self._initialize()
        self._randomize()
        self.puzzleize()

        return self.field

    def puzzleize(self):
        if self.puzzleizer is None:
            return

        self.field = self.puzzleizer.puzzleize(self.field)

    def _initialize(self):
        self.field = Field.get_valid_field(self.field_size // 2)

    def _randomize(self):
        for _ in range(random.randint(1, 100)):
            if random.randint(0, 1) == 1:
                self.field = Field.shift_field_right(self.field)
            else:
                self.field = Field.shift_field_down(self.field)

            if random.randint(0, 10) == 1:
                self.field = Field.invert_field(self.field)

            if random.randint(0, 5) == 1:
                self.field = Field.rotate_ccw(self.field)

        while not self.validator.validate(self.field)[0] is True:
            if random.randint(0, 1) == 1:
                self.field = Field.shift_field_right(self.field)
            else:
                self.field = Field.shift_field_down(self.field)
