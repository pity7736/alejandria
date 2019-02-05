
class Book:

    _instances = {}

    def __init__(self, id, title, subtitle, publication_date, publisher, description):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.publication_date = publication_date
        self.publisher = publisher
        self.description = description

    def save(self):
        self._instances[self.id] = self
        return True

    @classmethod
    def get_by_id(cls, id):
        return cls._instances.get(id)

