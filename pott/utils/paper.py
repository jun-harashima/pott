class Paper:

    def __init__(self, url='', title='', authors=[], year=''):
        self.url = url
        self.title = title
        self.authors = authors
        self.year = year
        self.id = ''
        if authors != [] and year != 0:
            self.id = authors[0].split(' ')[-1] + year
