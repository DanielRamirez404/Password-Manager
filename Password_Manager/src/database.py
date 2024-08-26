import sqlite3

class DatabaseConnection:
    
    _username = None
    _connection = None
    _cursor = None
    _databasePath = None
    _folderPath = r"../users/"

    def load(self, username: str, password: str) -> None:
        self._username = username
        self._connection = sqlite3.connect(self._folderPath + username + ".db")
        self._cursor = self._connection.cursor()
        self.createTable()
        
    def createTable(self) -> None:
        if (self._cursor.execute(r"SELECT name FROM sqlite_master WHERE name='Passwords'").fetchone() is None):
            self._cursor.execute("CREATE TABLE Passwords(Password)")
        else:
            pass

    def save(password: str) -> None:
        pass

        
