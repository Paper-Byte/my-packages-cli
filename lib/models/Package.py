from models.__init__ import CURSOR, CONN
from models.language import Language


class Package:

    all = {}

    def __init__(self, name, command, language_id, id=None):
        self.id = id
        self.name = name
        self.command = command
        self.language_id = language_id

    def __repr__(self):
        return (
            f"<Package {self.id}: {self.name}, {self.command}, " +
            f"Language ID: {self.language_id}>"
        )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )
