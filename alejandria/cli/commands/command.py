from abc import abstractmethod


class Command:

    def __init__(self, title=''):
        self._title = title

    def get_title(self):
        return self._title

    @abstractmethod
    def execute(self):
        pass
