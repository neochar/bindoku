from game import Game
from generator import Generator
from interface import Interface
from validator import Validator


def run_game():
    interface = Interface()
    validator = Validator()
    generator = Generator(validator, interface.render)

    game = Game(
        interface.render,
        interface.grab_input,
        generator,
        validator
    )
    game.run()


if __name__ == '__main__':
    run_game()
