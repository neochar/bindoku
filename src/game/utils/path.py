from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.parent.absolute()


def get_path(sub: str or None = None) -> str:
    if str is None:
        return ROOT_DIR.__str__()

    return f'{ROOT_DIR}/{sub}'
