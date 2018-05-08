class Paper:

    def __init__(self, url=None, title=None, authors=[], year=None):
        self.url = url
        self.title = title
        self.authors = authors
        self.year = year
        self.id = ''
        if authors != [] and year is not None:
            self.id = authors[0].split(' ')[-1] + year
