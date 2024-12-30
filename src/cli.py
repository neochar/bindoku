from game.configurator import Configurator
from game.game import Game
from game.generator import Generator
from cli.app import App
from game.solver import Solver
from game.validator import Validator


def run_game():
    cli = App()
    validator = Validator()
    solver = Solver(validator=validator)
    generator = Generator(
        validator=validator,
        render_callback=cli.render,
    )
    game = Game(
        cli.render,
        cli.quit,
        cli.grab_input,
        generator,
        validator,
        configurator=Configurator.dev(),
        solver=solver
    )
    game.run()


if __name__ == '__main__':
    run_game()
