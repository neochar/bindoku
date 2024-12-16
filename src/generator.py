import random
from typing import Callable

from field import Field
from validator import Validator


class Generator:
    def __init__(
            self,
            validator: Validator,
            render_callback: Callable,  # for debug
            seed=1
    ):
        self.validator = validator
        self.field = None
        self.seed = seed  # TODO make seed generator for non-local env
        self.field_size = None
        self.render_callback = render_callback
        random.seed(self.seed)

    def generate(self, field_size: int, seed: int = None) -> list[list[int]]:
        if seed is not None:
            self.seed = seed

        self.field_size = field_size

        self._initialize()
        self._randomize()

        return self.field

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
                self.field = Field.rotate_field(self.field)

        while not self.validator.validate(self.field)[0] is True:
            if random.randint(0, 1) == 1:
                self.field = Field.shift_field_right(self.field)
            else:
                self.field = Field.shift_field_down(self.field)
