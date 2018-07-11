import curses
from texttable import Texttable


class Screen:

    HEADER = ['RANK', 'PDF', 'FIRST AUTHOR', 'YEAR', 'CITED BY', 'TITLE']
    COLS_ALIGN = ['r', 'r', 'l', 'r', 'r', 'l']
    COLS_WIDTH = [4, 3, 12, 4, 8, 79]
    HEADER_HEIGHT = 2

    def __init__(self, assistant):
        self.assistant = assistant
        self.table = self._initialize_table()

    def _initialize_table(self):
        table = Texttable()
        table.set_deco(Texttable.HEADER)
        table.set_cols_align(self.COLS_ALIGN)
        table.set_cols_width(self.COLS_WIDTH)
        table.header(self.HEADER)
        return table

    def show(self, papers):
        selected_papers = curses.wrapper(self._wrap_show, papers)
        return selected_papers

    def _wrap_show(self, stdscr, papers):
        self.stdscr = stdscr  # name of the corresponding C variable
        self.stdscr.clear()
        self._initialize_table()
        self._update_table(papers)
        selected_papers = self._show(papers)
        return selected_papers

    def _show(self, papers):
        selected_papers = []
        while True:
            ch = self.stdscr.getch()
            y, x = self.stdscr.getyx()
            quit, papers = self._act_on_key(ch, y, x, selected_papers, papers)
            if quit:
                break
        return selected_papers

    def _act_on_key(self, ch, y, x, selected_papers, papers):
        if ch == curses.KEY_DOWN and y <= len(papers):
            self._move(y + 1)
        elif ch == curses.KEY_UP and y > self.HEADER_HEIGHT:
            self._move(y - 1)
        elif ch == ord('n') and not self.assistant.option.every:
            papers = self.assistant.search_next(papers)
            self._update_table(papers)
        elif ch == ord('p') and not self.assistant.option.every:
            papers = self.assistant.search_previous(papers)
            self._update_table(papers)
        elif ch == ord('s') and self.assistant.is_global():
            paper = papers[y - self.HEADER_HEIGHT]
            if self.assistant.have_indexed(paper):
                success = self._show_file_path(paper)
            else:
                success = self._save(paper)
            if success:
                selected_papers = \
                    self._append_without_duplication(selected_papers, paper)
            self._move(y)
        elif ch == ord('q'):
            return True, []
        return False, papers

    def _move(self, destination):
        self.stdscr.move(destination, 0)

    def _update_table(self, papers):
        self._delete_rows()
        self._set_rows(papers)
        self._draw_table()

    def _delete_rows(self):
        self.table._rows = []
        for _ in range(self.assistant.PER_PAGE):
            self.stdscr.move(self.HEADER_HEIGHT + 1, 0)
            self.stdscr.deleteln()

    def _set_rows(self, papers):
        for index, paper in enumerate(papers):
            rank = index + self.assistant.option.start + 1
            pdf = '  A' if paper.url is not None else 'N/A'
            first_author = paper.authors[0][:12] if paper.authors else ''
            year = paper.year if paper.year is not None else ''
            cited_by = paper.cited_by if paper.cited_by is not None else ''
            title = paper.title[:79]
            row = [rank, pdf, first_author, year, cited_by, title]
            self.table.add_row(row)

    def _draw_table(self):
        self.stdscr.addstr(0, 0, self.table.draw())
        self.stdscr.move(self.HEADER_HEIGHT, 0)

    def _show_file_path(self, paper):
        self._delete_message()
        file_path = paper.pdf.file_path
        self.stdscr.addstr(13, 0, 'The paper has been saved as ' + file_path)
        return True

    def _recommend_other(self, paper):
        self._delete_message()
        self.stdscr.addstr(13, 0, 'The paper is not available.')

    def _save(self, paper):
        self._delete_message()
        self.stdscr.addstr(13, 0, 'Downloading "' + paper.title + '"')
        self.stdscr.refresh()
        success = self.assistant.save(paper)
        if success:
            self.stdscr.addstr(14, 0, 'Saved as "' + paper.pdf.file_path + '"')
        else:
            self.stdscr.addstr(14, 0, 'The paper could not be downloaded.')
        return success

    def _delete_message(self):
        for _ in range(2):
            self.stdscr.move(13, 0)
            self.stdscr.deleteln()

    def _append_without_duplication(self, selected_papers, paper):
        selected_papers.append(paper)
        selected_papers = list(dict.fromkeys(selected_papers))
        return selected_papers
