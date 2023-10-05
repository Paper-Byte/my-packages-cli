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
