class Field:
    @staticmethod
    def rotate_field(field: list[list[int]]) -> list[list[int]]:
        return [list(elem) for elem in list(zip(*field))[::-1]]

    @classmethod
    def invert_field(cls, field):
        return [[int(not elem) for elem in line] for line in field]

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
                '../data/fields/' + f'{field_size}x{field_size}.dat',
                'r'
        ) as f:
            lines = f.readlines()

        return [
            [int(elem) for elem in line.split(' ')]
            for line in lines
        ]
