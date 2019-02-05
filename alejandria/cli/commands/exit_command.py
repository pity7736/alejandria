from .command import Command


class ExitCommand(Command):

    def __init__(self, title='Salir'):
        super().__init__(title=title)
        self._closed = False

    def execute(self):
        self._closed = True

    def is_closed(self):
        return self._closed
