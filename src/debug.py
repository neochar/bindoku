import logging

from game.components.row import Row
from game.solver import Solver
from game.validator import Validator

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

CASE_FIELD = 2
CASE_EXCLUSION = 1


def get_field_cases():
    return [
        {
            'puzzle': [[1, 0, 0, 2, 2, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1],
                       [2, 0, 0, 0, 0, 2, 2, 0],
                       [0, 0, 1, 0, 2, 0, 0, 0],
                       [0, 1, 1, 0, 0, 1, 0, 0],
                       [1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 2, 0, 0, 0, 2],
                       [1, 0, 0, 0, 0, 1, 0, 2]],
        }
    ]


def get_exclusion_cases():
    return [
        {
            'enable': True,
            'puzzle': [1, 0, 2, 0, 1, 0, 0, 1],
            'expect': [1, 0, 2, 0, 1, 2, 2, 1]
        },
        {
            'enable': True,
            'puzzle': [0, 2, 0, 0, 1, 2, 2, 1],
            'expect': [1, 2, 0, 0, 1, 2, 2, 1]
        },
        {
            'puzzle': [0, 0, 2, 0, 1, 2, 1, 2, 1, 1],
            'expect': [2, 0, 2, 2, 1, 2, 1, 2, 1, 1],
        },
        {
            'enable': True,
            'puzzle': [2, 2, 1, 2, 0, 1, 0, 2, 0, 0],
            'expect': [2, 2, 1, 2, 0, 1, 0, 2, 1, 1],
        }
    ]


def get_solution(solver: Solver, puzzle, case):
    if case & CASE_FIELD:
        solution = solver.solve(puzzle)[1]
        return solution, solver.validator.validate(solution), solver.is_solvable(puzzle)

    if case & CASE_EXCLUSION:
        return solver.exclusion_checker.try_row_exclusion(
            Row.from_row(
                solver.exclusion_checker.try_row_exclusion(
                    Row.from_row(puzzle)
                )
            )
        )


def log(case, solution):
    logging.debug('== Puzzle: ')
    logging.debug(case['puzzle'])
    if 'expect' in case:
        logging.debug('== Expected: ')
        logging.debug(case['expect'])
    logging.debug('== Solution: ')
    logging.debug(solution)
    if 'expect' in case:
        logging.debug('== Solution is as expected: ')
        logging.debug(solution == case['expect'])
    for _ in range(3):
        logging.debug('-' * 32)


def debug(solver: Solver, cases):
    if cases & CASE_FIELD:
        for case in get_field_cases():
            log(
                case,
                get_solution(
                    solver,
                    case['puzzle'],
                    CASE_FIELD
                )
            )

    if cases & CASE_EXCLUSION:
        for case in get_exclusion_cases():
            if 'enable' in case and case['enable'] is False:
                continue

            log(
                case,
                get_solution(
                    solver,
                    case['puzzle'],
                    CASE_EXCLUSION
                )
            )


if __name__ == '__main__':
    debug(
        Solver(Validator()),
        CASE_FIELD
        |
        ~CASE_EXCLUSION
    )
