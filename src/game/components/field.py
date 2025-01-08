from game.components.cell import Cell
from game.utils.path import get_path


class Field:
    @staticmethod
    def rotate_ccw(field: list[list[int]]) -> list[list[int]]:
        return [list(row) for row in list(zip(*field))[::-1]]

    @staticmethod
    def rotate_cw(field: list[list[int]]) -> list[list[int]]:
        for _ in range(3):
            field = Field.rotate_ccw(field)

        return field

    @staticmethod
    def invert_field(field: list[list[int]]) -> list[list[int]]:
        return [[Cell.invert(cell) for cell in line] for line in field]

    @staticmethod
    def shift_field_up(field: list[list[int]]) -> list[list[int]]:
        return field[1:] + [field[0]]

    @staticmethod
    def shift_field_down(field: list[list[int]]) -> list[list[int]]:
        return [field[-1]] + field[:-1]

    @staticmethod
    def shift_field_left(field: list[list[int]]) -> list[list[int]]:
        field_size = Field.get_field_size(field)
        return [field[y][1:] + [field[y][0]] for y in range(field_size)]

    @staticmethod
    def shift_field_right(field: list[list[int]]) -> list[list[int]]:
        field_size = Field.get_field_size(field)
        return [[field[y][-1]] + field[y][:-1] for y in range(field_size)]

    @staticmethod
    def get_field_size(field: list[list[int]]) -> int:
        return len(field[0])

    @staticmethod
    def get_valid_field(field_size: int):
        with open(
                get_path('../data/fields/' + f'{field_size}x{field_size}.dat'),
                'r'
        ) as f:
            lines = f.readlines()

        return [
            [int(cell) for cell in line.split(' ')]
            for line in lines
        ]

    @staticmethod
    def is_incomplete(field: list[list[int]]) -> bool:
        for row in field:
            if 0 in row:
                return True

        return False

    @staticmethod
    def get_row_empty_cells(row: list[int]) -> list:
        empty = []
        for x, cell in enumerate(row):
            if cell == 0:
                empty.append(x)

        return empty

    @staticmethod
    def get_filled_rows(field: list[list[int]]) -> list[list[int]]:
        rows = []
        for y, row in enumerate(field):
            has_empty = False
            for x, cell in enumerate(row):
                if cell == 0:
                    has_empty = True
                    break

            if not has_empty:
                rows.append(row)

        return rows

    @classmethod
    def get_field_empty_cells(cls, field):
        empty_cells = []
        for y, row in enumerate(field):
            empty_cells.append((y, Field.get_row_empty_cells(row)))

        return empty_cells
