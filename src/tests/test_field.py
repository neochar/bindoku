import unittest

from game.components.field import Field


class TestField(unittest.TestCase):
    @staticmethod
    def _get_field() -> list[list[int]]:
        return [
            [1, 2, 0, 0, 0, 0],
            [1, 2, 0, 0, 2, 0],
            [0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [2, 1, 2, 1, 1, 2],
            [2, 1, 2, 1, 2, 1],
        ]

    def test_rotate_ccw(self):
        expected = [
            [0, 0, 0, 0, 2, 1],
            [0, 2, 0, 0, 1, 2],
            [0, 0, 0, 0, 1, 1],
            [0, 0, 1, 0, 2, 2],
            [2, 2, 0, 0, 1, 1],
            [1, 1, 0, 1, 2, 2],
        ]
        self.assertEqual(
            expected,
            Field.rotate_ccw(self._get_field()),
        )

    def test_rotate_cw(self):
        expected = [
            [2, 2, 1, 0, 1, 1],
            [1, 1, 0, 0, 2, 2],
            [2, 2, 0, 1, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [2, 1, 0, 0, 2, 0],
            [1, 2, 0, 0, 0, 0],
        ]
        self.assertEqual(
            expected,
            Field.rotate_cw(self._get_field()),
        )

    def test_invert_field(self):
        pass

    def test_is_incomplete(self):
        pass
