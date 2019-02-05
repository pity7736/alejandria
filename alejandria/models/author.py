
class Author:

    _instances = {}

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'{self.id} - {self.name}'

    def save(self):
        self._instances[self.id] = self
        return True

    @classmethod
    def get_by_id(cls, id):
        return cls._instances.get(id)

    @classmethod
    def get_all(cls):
        return cls._instances.values()
