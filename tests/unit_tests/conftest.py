from pytest import fixture

from alejandria.models import Category, Author


@fixture
def category():
    cat = Category(id=1, name='test')
    cat.save()
    return cat


@fixture
def author():
    author = Author(id=1, name='test author')
    author.save()
    return author
