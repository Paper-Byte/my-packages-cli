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

    @classmethod
    def drop_table(cls):

        sql = """
            DROP TABLE IF EXISTS packages;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):

        sql = """
                INSERT INTO packages (name, command, language_id)
                VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.command, self.language_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):

        sql = """
            UPDATE packages
            SET name = ?, command = ?, language_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.command,
                             self.language_id, self.id))
        CONN.commit()

    def delete(self):

        sql = """
            DELETE FROM packages
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def create(cls, name, command, language_id):

        package = cls(name, command, language_id)
        package.save()
        return package

    @classmethod
    def instance_from_db(cls, row):

        package = cls.all.get(row[0])

        if package:
            package.name = row[1]
            package.command = row[2]
            package.language_id = row[3]
        else:
            package = cls(row[1], row[2], row[3])
            package.id = row[0]
            cls.all[package.id] = package
        return package

    @classmethod
    def get_all(cls):

        sql = """
            SELECT *
            FROM packages
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
