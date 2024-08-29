import sqlite3
import base64
from cryptography.fernet import Fernet

class DatabaseConnection:
    
    def __init__(self, username: str, password: str) -> None:
        self._initConnection(username)
        self._initFernet(password)
    
    def _initConnection(self, username: str) -> None:
        self._connection = sqlite3.connect(r"../users/" + username + ".db")
        self._cursor = self._connection.cursor()
        if not self._doesPasswordTableExist():
            self._createTable()

    def _initFernet(self, password: str) -> None:
        encryptionKey = password
        encryptionKeyBytes = password.encode().ljust(32)[:32]
        fernetKey = base64.urlsafe_b64encode(encryptionKeyBytes)
        self._fernet = Fernet(fernetKey)

    def _doesPasswordTableExist(self) -> bool:
        return self._cursor.execute(r"SELECT name FROM sqlite_master WHERE name='Passwords'").fetchone() is not None

    def _createTable(self) -> None:
        self._cursor.execute("CREATE TABLE Passwords(identifier, password)")

    def doesIdentifierExist(self, identifier) -> bool:
        return self._cursor.execute(r"SELECT * FROM Passwords WHERE identifier='?'", key).fetchone() is not None

    def savePassword(self, identifier: str, password: str) -> None:
        data = (identifier, self._fernet.encrypt(password.encode()))
        self._cursor.execute("INSERT INTO Passwords VALUES(?, ?)", data)
        self._connection.commit()

    def getSavedPasswords(self) -> list:
        fetchedData = self._cursor.execute("SELECT * FROM Passwords").fetchall()
        decryptedPasswords = []

        for key, password in fetchedData:
            decryptedPasswords.append((key, self._fernet.decrypt(password).decode()))
        
        return decryptedPasswords

    def updatePassword(self, identifier: str, password: str) -> None:
        data = (identifier, self._fernet.encrypt(password.encode()))
        self._cursor.execute(r"UPDATE Passwords SET key='?', password='?'", data)
        self._connection.commit()

    def deletePassword(self, identifier: str) -> None: 
        self._cursor.execute(r"DELETE FROM Passwords WHERE identifier=?", (identifier,))
        self._connection.commit()
