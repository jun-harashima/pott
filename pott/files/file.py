import os


class File:

    def set_file_name_and_path(self, file_name):
        if not os.path.isdir(self.dir_name()):
            os.makedirs(self.dir_name())
        self.file_name = file_name
        self.file_path = self.dir_name() + '/' + file_name

    def dir_name(self):
        raise RuntimeError("dir_name should be implemented in child classes!")
