import curses
from pott.index import Index
from pott.yaml import Yaml
from pott.utils.output_utils import show_results


class Assistant:

    def __init__(self):
        self.yaml = Yaml()
        self.index = Index()

    def search(self, keywords, year_low, year_high, start):
        curses.wrapper(self._show_papers, keywords, year_low, year_high,
                       start)

    def _show_papers(self, stdscr, keywords, year_low, year_high, start):
        papers = self._get_papers(keywords, year_low, year_high, start)
        stdscr.clear()
        show_results(stdscr, papers, start)
        while True:
            ch = stdscr.getch()
            y, x = stdscr.getyx()
            if ch == curses.KEY_DOWN:
                if y <= 10:
                    stdscr.move(y + 1, 0)
            elif ch == curses.KEY_UP:
                if y >= 3:
                    stdscr.move(y - 1, 0)
            elif ch == ord('n'):
                papers, start = self._get_next_papers(keywords, year_low,
                                                      year_high, start)
                show_results(stdscr, papers, start)
            elif ch == ord('p'):
                papers, start = self._get_previous_papers(keywords, year_low,
                                                          year_high, start)
                show_results(stdscr, papers, start)
            elif ch == ord('q'):
                break
