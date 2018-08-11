import curses


class KwicScreen:

    def __init(self):
        pass

    def show(self):
        curses.wrapper(self._wrap_show)

    def _wrap_show(self, stdscr):
        self.stdscr = stdscr  # name of the corresponding C variable
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, 'TBI')
        self.stdscr.refresh()
