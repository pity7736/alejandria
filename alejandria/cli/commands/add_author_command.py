from alejandria.models import Author
from .command import Command


class AddAuthorCommand(Command):

    def __init__(self, title='Agregar autor'):
        super().__init__(title=title)

    def execute(self):
        id = input('Ingrese id: ')
        name = input('Ingrese nombre: ')
        category = Author(id=id, name=name)
        category.save()
