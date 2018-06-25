import curses
from texttable import Texttable


class Screen:

    HEADERS = ['RANK', 'PDF', 'FIRST AUTHOR', 'YEAR', 'CITED BY', 'TITLE']
    HEADER_HEIGHT = 2

    def __init__(self, assistant):
        self.assistant = assistant

    def show(self, papers):
        selected_papers = curses.wrapper(self._show, papers)
        return selected_papers

    def _show(self, stdscr, papers):
        selected_papers = []
        stdscr.clear()
        self._update_table(stdscr, papers)
        while True:
            ch = stdscr.getch()
            y, x = stdscr.getyx()
            if ch == curses.KEY_DOWN:
                if y <= len(papers):
                    stdscr.move(y + 1, 0)
            elif ch == curses.KEY_UP:
                if y > self.HEADER_HEIGHT:
                    stdscr.move(y - 1, 0)
            elif ch == ord('n') and not self.assistant.option.every:
                papers = self.assistant.search_next(papers)
                self._update_table(stdscr, papers)
            elif ch == ord('p') and not self.assistant.option.every:
                papers = self.assistant.search_previous(papers)
                self._update_table(stdscr, papers)
            elif ch == ord('s') and self.assistant.is_global():
                paper = papers[y - self.HEADER_HEIGHT]
                if self.assistant.have_indexed(paper):
                    self._show_file_path(stdscr, paper)
                else:
                    self._save(stdscr, paper)
                selected_papers = \
                    self._append_without_duplication(selected_papers, paper)
                stdscr.move(y, 0)
            elif ch == ord('q'):
                break
        return selected_papers

    def _update_table(self, stdscr, papers):
        self._delete_rows(stdscr)
        rows = self._set_rows(papers)
        table = self._set_table(rows)
        self._draw_table(stdscr, table)

    def _delete_rows(self, stdscr):
        for _ in range(self.assistant.PER_PAGE):
            stdscr.move(self.HEADER_HEIGHT + 1, 0)
            stdscr.deleteln()

    def _set_rows(self, papers):
        rows = [self.HEADERS]
        for index, paper in enumerate(papers):
            rank = index + self.assistant.option.start + 1
            pdf = '  A' if paper.url is not None else 'N/A'
            first_author = paper.authors[0][:12] if paper.authors else ''
            year = paper.year if paper.year is not None else ''
            cited_by = paper.cited_by if paper.cited_by is not None else ''
            title = paper.title[:79]
            row = [rank, pdf, first_author, year, cited_by, title]
            rows.append(row)
        return rows

    def _set_table(self, rows):
        table = Texttable()
        table.set_deco(Texttable.HEADER)
        table.set_cols_align(['r', 'r', 'l', 'r', 'r', 'l'])
        table.set_cols_width([4, 3, 12, 4, 8, 79])
        table.add_rows(rows)
        return table

    def _draw_table(self, stdscr, table):
        stdscr.addstr(0, 0, table.draw())
        stdscr.move(self.HEADER_HEIGHT, 0)

    def _show_file_path(self, stdscr, paper):
        file_path = paper.pdf.file_path
        stdscr.addstr(13, 0, 'The paper has been saved as ' + file_path)
        stdscr.move(14, 0)
        stdscr.deleteln()

    def _save(self, stdscr, paper):
        stdscr.addstr(13, 0, 'Downloading "' + paper.title + '"')
        stdscr.move(14, 0)
        stdscr.deleteln()
        stdscr.refresh()
        self.assistant.save(paper)
        stdscr.addstr(14, 0, 'Saved as "' + paper.pdf.file_path + '"')

    def _append_without_duplication(self, selected_papers, paper):
        selected_papers.append(paper)
        selected_papers = list(dict.fromkeys(selected_papers))
        return selected_papers
