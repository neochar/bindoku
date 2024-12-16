import os
import sys
import typing

from field import Field
from generator import Generator
from validator import Validator


class Game:

    def __init__(
            self,
            render_callback: typing.Callable,
            input_resolver: typing.Callable,
            generator: Generator,
            validator: Validator,
    ):
        self.seed = 1
        self.render_callback = render_callback
        self.input_resolver = input_resolver
        self.generator = generator
        self.validator = validator

        self.field_size = 3 * 2
        self.field = []

    def run(self):
        if len(self.field) < 1:
            self.generate_field()

        self.render_field()

        while 1:
            self.process_input()
            self.render_field()

    def process_input(self):
        c = self.input_resolver()

        if c == ord('q'):
            exit()

        if c == ord('0'):
            os.execl(sys.executable, sys.executable, *sys.argv)

        if c == ord('i'):
            self.field = Field.invert_field(self.field)
        if c == ord('r'):
            self.field = Field.rotate_field(self.field)

        if c == ord('l'):
            self.field = Field.shift_field_right(self.field)
        if c == ord('h'):
            self.field = Field.shift_field_left(self.field)
        if c == ord('k'):
            self.field = Field.shift_field_up(self.field)
        if c == ord('j'):
            self.field = Field.shift_field_down(self.field)

        if c == ord('s'):
            self.seed += 1
            self.generate_field()

        if c == ord('1'):
            self.field_size = 2*2
            self.generate_field()
        if c == ord('2'):
            self.field_size = 3*2
            self.generate_field()
        if c == ord('3'):
            self.field_size = 4*2
            self.generate_field()

    def generate_field(self):
        self.field = self.generator.generate(self.field_size, self.seed)

    def render_field(self):
        result, errors = self.validator.validate(self.field)
        if result is True:
            messages = ['Field is valid!']
        else:
            messages = errors

        self.render_callback(self.field, messages)

