from alejandria.models import Book, Category, Author
from .command import Command


class AddBookCommand(Command):

    def __init__(self, title='Agregar libro'):
        super().__init__(title=title)

    def execute(self):
        categories = Category.get_all()
        if not categories:
            print('No hay categorías aún. Debe agregar una primero.')
            return
        authors = Category.get_all()
        if not authors:
            print('No hay autores aún. Debe agregar una primero.')
            return

        print('Categories:')
        for category in categories:
            print(category)

        category_id = input('ingrese id de la categoría: ')

        print('Autores:')
        for author in authors:
            print(author)

        author_id = input('ingrese id del author: ')

        id = input('Ingrese id del libro: ')
        title = input('Ingrese título: ')
        subtitle = input('Ingrese subtítulo: ')
        publication_date = input('Ingrese fecha de publicación: ')
        publisher = input('Ingrese editorial: ')
        description = input('Ingrese descripción: ')
        book = Book(
            id=id,
            title=title,
            subtitle=subtitle,
            publication_date=publication_date,
            publisher=publisher,
            description=description
        )
        book.save()
        book.add_author(Author.get_by_id(author_id))
        book.add_category(Category.get_by_id(category_id))
