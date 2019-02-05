from alejandria.models.book import Book


def test_save_book(category, author):
    book = Book(
        id=1,
        title='Refactoring',
        subtitle='Improving the design of existing code',
        publication_date='2018-11-20',
        publisher='Addison-Wesley Professional',
        description='qweqwe'
    )
    book.save()

    b = Book.get_by_id(1)

    assert b.id == book.id
    assert b.title == book.title
    assert b.subtitle == book.subtitle
