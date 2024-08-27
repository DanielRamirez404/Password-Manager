import sqlite3
from cryptography.fernet import Fernet

class DatabaseConnection:
    
    _username = None
    _encryptionKey = None
    _fernet = None
    _connection = None
    _cursor = None
    _databasePath = None
    _folderPath = r"../users/"

    def load(self, username: str, password: str) -> None:
        self._username = username
        self._connection = sqlite3.connect(self._folderPath + username + ".db")
        self._cursor = self._connection.cursor()
        self._encryptionKey = password
        encryptionKeyBytes = password.encode().ljust(32)[:32]
        fernetKey = base64.urlsafe_b64encode(encryptionKeyBytes)
        self._fernet = Fernet(fernetKey)
        if not self._doesPasswordTableExist():
            self._createTable()
    
    def _doesPasswordTableExist(self) -> bool:
        return self._cursor.execute(r"SELECT name FROM sqlite_master WHERE name='Passwords'").fetchone() is not None

    def _createTable(self) -> None:
        self._cursor.execute("CREATE TABLE Passwords(Key, Password)")

    def doesKeyExist(self, key) -> bool:
        return self._cursor.execute(r"SELECT * FROM Passwords WHERE key='?'", key).fetchone() is not None

    def savePassword(self, key: str, password: str) -> None:
        data = (key, self._fernet.encrypt(password.encode()))
        self._cursor.execute("INSERT INTO Passwords VALUES(?, ?)", data)
        self._connection.commit()

    def getSavedPasswords(self) -> list:
        passwords = self._cursor.execute("SELECT * FROM Passwords").fetchall()
        for key, password in passwords:
            password = self._fernet.decrypt(password.encode())
        return passwords

