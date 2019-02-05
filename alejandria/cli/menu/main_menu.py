from alejandria.cli.commands import AddCategoryCommand, AddAuthorCommand, AddBookCommand
from .menu import Menu
from ..commands import ExitCommand


class MainMenu(Menu):

    name = 'Menú principal'

    def _get_options(self):
        self._exit_command = ExitCommand()
        return self._exit_command, AddCategoryCommand(), AddAuthorCommand(), AddBookCommand()

    def run(self):
        while self._exit_command.is_closed() is False:
            super().run()
