import curses
from pott.index import Index
from pott.yaml import Yaml
from pott.utils.output_utils import show_results


class Assistant:

    PER_PAGE = 10
    HEADER_HEIGHT = 2

    def __init__(self):
        self.yaml = Yaml()
        self.index = Index()

    def search(self, keywords, options):
        selected_papers = curses.wrapper(self._show_papers, keywords, options)
        for paper in selected_papers:
            print(paper.pdf.file_path)

    def _show_papers(self, stdscr, keywords, options):
        selected_papers = []
        papers = self._search(keywords, options)
        stdscr.clear()
        show_results(stdscr, papers, options)
        while True:
            ch = stdscr.getch()
            y, x = stdscr.getyx()
            if ch == curses.KEY_DOWN:
                if y <= len(papers):
                    stdscr.move(y + 1, 0)
            elif ch == curses.KEY_UP:
                if y > self.HEADER_HEIGHT:
                    stdscr.move(y - 1, 0)
            elif ch == ord('n'):
                papers, options = self._search_next(keywords, options)
                show_results(stdscr, papers, options)
            elif ch == ord('p'):
                papers, options = self._search_previous(keywords, options)
                show_results(stdscr, papers, options)
            elif ch == ord('s') and self._is_GlobalAssistant():
                paper = papers[y - self.HEADER_HEIGHT]
                self._save(stdscr, paper)
                selected_papers.append(paper)
                stdscr.move(y, 0)
            elif ch == ord('q'):
                break
        return selected_papers

    def _search_next(self, keywords, options):
        return self._search_other(keywords, options, self.PER_PAGE)

    def _search_previous(self, keywords, options):
        return self._search_other(keywords, options, self.PER_PAGE * -1)

    def _search_other(self, keywords, options, increment):
        original_options = options
        options['start'] += increment
        papers = self._search(keywords, options)
        options = original_options if papers else options
        return papers, options

    def _is_GlobalAssistant(self):
        return self.__class__.__name__ == 'GlobalAssistant'
