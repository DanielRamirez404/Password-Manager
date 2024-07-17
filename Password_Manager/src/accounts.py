import json

class LoginInfo:
    _path = r"../users/login.json"
    _info = _getDefaultLoginInfo()

    def _getDefaultLoginInfo() -> dict:
        return { 'users': [], 'encrypted-passwords': [] }

    def load() -> None:
        try:
            with open(_path, 'r') as file:
                 _info = json.load(file)
        except IOError:
            _info = _getDefaultLoginInfo()

    def save() -> None:
        try:
            with open(_path, 'w') as file:
                json.dump(_info, file, indent = 4)
        except FileNotFoundError:
            file = open(_path, 'x')
            file.close()
            save()
