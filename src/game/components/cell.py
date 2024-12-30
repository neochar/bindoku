class Cell:

    @staticmethod
    def invert(value: int):
        if value == 0:
            raise ValueError("Cell cannot be inverted")

        return 2 if value == 1 else 1
