from alejandria.models import Category
from .command import Command


class AddCategoryCommand(Command):

    def __init__(self, title='Agregar categoría'):
        super().__init__(title=title)

    def execute(self):
        id = input('Ingrese id: ')
        name = input('Ingrese nombre: ')
        category = Category(id=id, name=name)
        category.save()
