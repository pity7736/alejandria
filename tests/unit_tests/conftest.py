from pytest import fixture

from alejandria.models import Category


@fixture
def category():
    cat = Category(id=1, name='test')
    cat.save()
    return cat
