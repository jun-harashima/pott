from pott.files.pdf import Pdf
from pott.files.text import Text


class Paper:

    def __init__(self, title, authors=[], year=None, cited_by=None, url=None,
                 snippets=[]):
        self.title = title
        self.authors = authors
        self.year = year
        self.cited_by = cited_by
        self.url = url
        self.snippets = snippets
        self.id = ''
        if authors != [] and year is not None:
            self.id = authors[0].split(' ')[-1] + year
            self.pdf = Pdf(self.id + '.pdf')
            self.text = Text(self.id + '.txt')
