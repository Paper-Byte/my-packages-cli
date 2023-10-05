from models.__init__ import CURSOR, CONN


class Language:

    all = {}

    def __init__(self, name, id=None):
        self.id = id
        self.name = name
