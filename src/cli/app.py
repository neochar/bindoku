import curses

from game.components.field import Field


class App:

    def __init__(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        pass

    def __exit__(self):
        self.stdscr.erase()
        curses.endwin()

    def render(self, data: list[list[int]], texts: list[str] = None):
        self.stdscr.erase()
        field_size = Field.get_field_size(data)

        for y in range(field_size):
            string = ' '.join([str(val) for val in data[y]])
            self.stdscr.addstr(y, 0, string)

        if texts is not None:
            self.stdscr.addstr(field_size + 1, 0, f'Messages ({len(texts)}):')
            for y, text in enumerate(texts):
                self.stdscr.addstr(y + field_size + 2, 0, text)

        self.stdscr.refresh()

    def grab_input(self):
        return self.stdscr.getch()

    def quit(self):
        self.stdscr.erase()
        curses.endwin()
        exit(0)
