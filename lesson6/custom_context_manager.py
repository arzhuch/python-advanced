"""
3) Написать свой контекстный менеджер для работы с файлами.
"""


class Opener(object):

    def __init__(self, filename, mode):
        self.file = open(filename, mode)

    def __enter__(self):
        return self.file

    def __exit__(self, type, value, traceback):
        self.file.close()
