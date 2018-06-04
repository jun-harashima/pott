import curses
import requests
from pyquery import PyQuery
from pott.assistants.assistant import Assistant
from pott.utils.html_utils import extract_papers_from
from pott.utils.output_utils import show_results
from pott.utils.log import logger


class GlobalAssistant(Assistant):

    SCHOLAR_URL = "https://scholar.google.com/scholar"

    def search(self, keywords, year_low, year_high, start):
        saved_papers = curses.wrapper(self._show_papers, keywords, year_low,
                                      year_high, start)
        if not saved_papers:
            return
        print('Saved in the following location:')
        for paper in saved_papers:
            print(paper.pdf.file_path)

    def _show_papers(self, stdscr, keywords, year_low, year_high, start):
        saved_papers = []
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
                if start <= 980:
                    start += 10
                    papers = self._get_papers(keywords, year_low, year_high,
                                              start)
                    show_results(stdscr, papers, start)
            elif ch == ord('p'):
                if start >= 10:
                    start -= 10
                    papers = self._get_papers(keywords, year_low, year_high,
                                              start)
                    show_results(stdscr, papers, start)
            elif ch == ord('s'):
                self._save(stdscr, papers[y - 2])
                saved_papers.append(papers[y - 2])
                stdscr.move(y, 0)
            elif ch == ord('q'):
                break
        return saved_papers

    def _get_papers(self, keywords, year_low, year_high, start):
        url = self._set_url(keywords, year_low, year_high, start)
        pq_html = PyQuery(url)
        papers = extract_papers_from(pq_html)
        return papers

    def _set_url(self, keywords, year_low, year_high, start):
        url = self.SCHOLAR_URL + '?q=' + ' '.join(keywords)
        if year_low is not None:
            url += '&as_ylo=' + year_low
        if year_high is not None:
            url += '&as_yhi=' + year_high
        if start != 0:
            url += '&start=' + str(start)
        return url

    def _save(self, stdscr, paper):
        stdscr.addstr(13, 0, 'Downloading "' + paper.title + '"')
        stdscr.move(14, 0)
        stdscr.deleteln()
        stdscr.refresh()
        response = self._download(paper)
        paper.pdf.save(response.content)
        paper.text.save(paper.pdf.extract_text())
        self.index.save(paper)
        self.yaml.update(paper)
        stdscr.addstr(14, 0, 'Saved as "' + paper.pdf.file_path + '"')

    def _download(self, paper):
        try:
            response = requests.get(paper.url, timeout=10)
            if response.status_code == 200:
                return response
        except requests.ConnectionError as e:
            logger.warn(str(e))
