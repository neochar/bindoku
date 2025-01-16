import unittest

from game.validator import Validator


class TestValidator(unittest.TestCase):
    def test_solution_is_valid(self):
        fields = [
            [[1, 2, 2, 1, 1, 2, 2, 1, 1, 2],
             [2, 1, 2, 1, 1, 2, 2, 1, 2, 1],
             [1, 2, 1, 2, 2, 1, 1, 2, 2, 1],
             [1, 1, 2, 2, 1, 2, 1, 2, 1, 2],
             [2, 1, 2, 1, 2, 1, 2, 1, 1, 2],
             [2, 2, 1, 1, 2, 1, 1, 2, 2, 1],
             [1, 2, 1, 2, 1, 2, 2, 1, 1, 2],
             [1, 1, 2, 1, 2, 1, 2, 2, 1, 2],
             [2, 1, 1, 2, 2, 1, 1, 2, 2, 1],
             [2, 2, 1, 2, 1, 2, 1, 1, 2, 1]],
        ]
        validator = Validator()
        for i, field in enumerate(fields):
            with self.subTest(i=i, label=len(field)):
                self.assertIs(True, validator.validate(field)[0])
