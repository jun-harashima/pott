import os


class File:

    def set_file_name(self, file_name):
        if not os.path.isdir(self.dir_name()):
            os.makedirs(self.dir_name())
        self.file_name = file_name

    def dir_name(self):
        raise RuntimeError("dir_name should be implemented in child classes!")
