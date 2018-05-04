import os


class Text:

    DIR_NAME = os.environ['HOME'] + '/.pott/txt'

    def __init__(self, file_name):
        if not os.path.isdir(self.DIR_NAME):
            os.makedirs(self.DIR_NAME)
        self.file_name = file_name

    def save(self, content):
        with open(self.DIR_NAME + '/' + self.file_name, 'w') as file:
            file.write(content)
