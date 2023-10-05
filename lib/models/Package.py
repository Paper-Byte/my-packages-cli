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

    @property
    def command(self):
        return self._command

    @command.setter
    def command(self, command):
        command_list = command.split()
        if ((command_list[0] == 'npm') and (command_list[1] == 'install')):
            if isinstance(command, str) and len(command):
                self._command = command
            else:
                raise ValueError(
                    "command must be a non-empty string"
                )
        else:
            raise ValueError(
                "command must be a valid npm install command"
            )

    @property
    def language_id(self):
        return self._language_id

    @language_id.setter
    def language_id(self, language_id):
        if type(language_id) is int and Language.find_by_id(language_id):
            self._language_id = language_id
        else:
            raise ValueError(
                "language_id must reference a language in the database")

    @classmethod
    def create_table(cls):

        sql = """
            CREATE TABLE IF NOT EXISTS packages (
            id INTEGER PRIMARY KEY,
            name TEXT,
            command TEXT,
            language_id INTEGER,
            FOREIGN KEY (language_id) REFERENCES languages(id))
        """
        CURSOR.execute(sql)
        CONN.commit()
