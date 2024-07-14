import json

loginInfoPath = r"../users/login.json"

def getDefaultLoginInfo() -> dict:
    return { 'users': [], 'encrypted-passwords': [] }

def getLoginInfo() -> dict:
    global loginInfoPath 
    try:
        with open(loginInfoPath, 'r') as file:
            return json.load(file)
    except IOError:
        return getDefaultLoginInfo()

def saveLoginInfo(loginDictionary: dict) -> None:
    global loginInfoPath
    try:
        with open(loginInfoPath, 'w') as file:
            json.dump(loginDictionary, file, indent = 4)
    except FileNotFoundError:
        with open(loginInfoPath, 'x') as file:
            pass
        saveLoginInfo(loginDictionary)
