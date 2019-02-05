from alejandria.models import Author


def test_get_author_by_id(author):
    cat = Author.get_by_id(id=author.id)

    assert author.id == cat.id
    assert author.name == cat.name


def test_save_author():
    author = Author(id=1, name='Martin Fowler')
    author.save()
    cat = author.get_by_id(1)

    assert author.id == cat.id
    assert author.name == cat.name
