from alejandria.models.book import Book


def test_add_book():
    book = Book(
        id=1,
        title='Refactoring',
        subtitle='Improving the design of existing code',
        publication_date='2018-11-20',
        publisher='Addison-Wesley Professional',
    )
