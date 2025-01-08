import os
import sys
import typing

from game.configurator import Configurator
from game.const import MAX_MOVES
from game.errors import FieldNotSolvableException
from game.components.field import Field
from game.generator import Generator
from game.puzzler import Puzzler
from game.solver import Solver
from game.validator import Validator


class Game:
    config: dict
    validator: Validator
    generator: Generator
    solver: Solver

    def __init__(
            self,
            render_callback: typing.Callable,
            quit_callback: typing.Callable,
            input_resolver: typing.Callable,
            generator: Generator,
            validator: Validator,
            configurator: Configurator,
            solver: Solver,
    ):
        self.messages = []
        self.seed = 1
        self.quit_callback = quit_callback
        self.render_callback = render_callback
        self.input_resolver = input_resolver
        self.generator = generator
        self.validator = validator
        self.solver = solver

        self.config = configurator.config

        self.field_size = 3 * 2
        self.field = []

    def run(self):
        if len(self.field) < 1:
            self.generate_field()

        self.render_field()

        while 1:
            self.process_input()
            self.render_field()

    def generate_field(self):
        self.messages = []
        self.field = self.generator.generate(self.field_size, self.seed)

    def render_field(self):
        result, errors = self.validator.validate(self.field)
        if result is True:
            messages = ['Field is valid!']
        else:
            messages = errors

        self.render_callback(self.field, list(set(messages)) + self.messages)

    def process_input(self):
        c = self.input_resolver()

        self.handle_input_system(c)
        self.handle_input_field(c)
        self.handle_input_generate(c)
        self.handle_input_game(c)

    def handle_input_system(self, c):
        if c == ord('q'):
            self.quit()

        if c == ord('0'):
            os.execl(sys.executable, sys.executable, *sys.argv)

    def handle_input_field(self, c):
        if c == ord('i'):
            self.field = Field.invert_field(self.field)
        if c == ord('r'):
            self.field = Field.rotate_ccw(self.field)

        if c == ord('l'):
            self.field = Field.shift_field_right(self.field)
        if c == ord('h'):
            self.field = Field.shift_field_left(self.field)
        if c == ord('k'):
            self.field = Field.shift_field_up(self.field)
        if c == ord('j'):
            self.field = Field.shift_field_down(self.field)

    def handle_input_generate(self, c):
        if c == ord('2'):
            self.field_size = 2 * 2
            self.generate_field()
        if c == ord('3'):
            self.field_size = 3 * 2
            self.generate_field()
        if c == ord('4'):
            self.field_size = 4 * 2
            self.generate_field()

    def handle_input_game(self, c):
        if c == ord('p'):
            if self.generator.puzzleizer is not None:
                self.generator.puzzleizer = None
                self.generate_field()
            else:
                self.generator.set_puzzleizer(Puzzler(Solver(self.validator)))
                self.field = self.generator.puzzleize()

        if c == ord('s'):
            self.messages = []
            try:
                moves, self.field = self.solver.solve(
                    self.field,
                    max_moves=MAX_MOVES
                )
                self.messages.append(f'Solved in {moves} moves')
            except FieldNotSolvableException as e:
                self.messages.append('Field is not solvable')

    def quit(self):
        self.quit_callback()
