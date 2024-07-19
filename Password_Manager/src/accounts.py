import json
import hashlib

class LoginInfo:

    def _getDefaultLoginInfo() -> dict:
        return { 'users': [], 'encrypted-passwords': [] }

    def _generateHash(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    _path = r"../users/login.json"
    _info = _getDefaultLoginInfo()

    @classmethod
    def load(cls) -> None:
        try:
            with open(cls._path, 'r') as file:
                 cls._info = json.load(file)
        except IOError:
            cls._info = cls._getDefaultLoginInfo()

    @classmethod
    def save(cls) -> None:
        try:
            with open(cls._path, 'w') as file:
                json.dump(cls._info, file, indent = 4)
        except FileNotFoundError:
            file = open(cls._path, 'x')
            file.close()
            cls.save()

    @classmethod
    def isEmpty(cls) -> bool:
        return len(cls._info['users']) == 0

    @classmethod
    def createUser(cls, username: str, password: str) -> None:
        cls._info['users'].append(username)
        cls._info['encrypted-passwords'].append(cls._generateHash(password))
        cls.save()

    @classmethod
    def deleteUser(cls, username: str) -> None:
        index = cls._info['users'].index(username)
        cls._info['users'].remove(index)
        cls._info['encrypted-passwords'].remove(index)
        cls.save()

    @classmethod
    def doesUserExist(cls, username: str) -> bool:
        return cls._info['users'].count(username) > 0

    @classmethod
    def _validateUser(cls, username: str, password: str) -> bool:
        index = cls._info['users'].index(username)
        return cls._info['encrypted-passwords'][index] == cls._generateHash(password)

    @classmethod
    def validateCredentials(cls, username: str, password: str) -> bool:
        return cls.doesUserExist(username) and cls._validateUser(username, password)
