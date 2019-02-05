from alejandria.models import Category


def test_get_category_by_id(category):
    cat = Category.get_by_id(id=category.id)

    assert category.id == cat.id
    assert category.name == cat.name


def test_save_category():
    category = Category(id=1, name='Computers')
    category.save()
    cat = Category.get_by_id(1)

    assert category.id == cat.id
    assert category.name == cat.name
