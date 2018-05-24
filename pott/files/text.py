import os
from pott.files.file import File


class Text(File):

    DIR_NAME = os.environ['HOME'] + '/.pott/txt'

    def __init__(self, file_name):
        self.set_file_name_and_path(file_name)

    def dir_name(self):
        return self.DIR_NAME

    def save(self, content):
        with open(self.DIR_NAME + '/' + self.file_name, 'w') as file:
            file.write(content)
