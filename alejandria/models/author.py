
class Author:

    _instances = {}

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def save(self):
        self._instances[self.id] = self
        return True

    @classmethod
    def get_by_id(cls, id):
        return cls._instances.get(id)
