import hashlib

from field import Field


class Validator:
    def __init__(self):
        self.errors = None
        self.do_asserts()

    def validate(self, field: list[list[int]]):
        self.errors = []

        rotated = Field.rotate_field(field)

        self._validate_no_two_equal_lines(field)
        self._validate_no_two_equal_lines(rotated)
        self._validate_no_more_than_two(field)
        self._validate_no_more_than_two(rotated)

        return len(self.errors) == 0, self.errors

    def _validate_no_two_equal_lines(self, field: list[list[int]]):
        hashes = [
            hashlib.md5(
                ''.join([str(elem) for elem in line]).encode('utf-8')
            ).hexdigest()
            for line in field
        ]

        if len(hashes) != len(set(hashes)):
            self.errors.append(
                'There cannot be two equal rows and columns'
            )

    def _validate_no_more_than_two(self, field: list[list[int]]):
        field_size = Field.get_field_size(field)
        for y in range(field_size):
            if not self.validate_line(field[y]):
                self.errors.append(
                    'There cannot be more than two elements of the same color in a row'
                )
                return

    @staticmethod
    def validate_line(line: list[int]):
        cnt = 0
        cur = None
        for x in line:
            if x == cur:
                cnt += 1
            else:
                cnt = 1

            cur = x

            if cnt > 2:
                return False

        return True

    def do_asserts(self):
        for i in range(2, 4):
            field = Field.get_valid_field(i)
            assert self.validate(field)[0] is True
