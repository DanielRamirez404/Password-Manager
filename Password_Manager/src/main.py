import json
import sqlite3
import tkinter

def getDefaultLoginInfo() -> dict:
    return { 'users': [], 'encrypted-passwords': [] }

def getLoginInfo() -> dict:
    filepath = r"../users/login.json"
    try:
        with open(filepath, 'r') as file:
            loginInfo = json.load(file)
    except IOError:
        print(r"There's no login file")
        loginInfo = getDefaultLoginInfo()
    finally:
        return loginInfo

def loadDatabase():
    return 0
    #return sqlite3.connect("database.db")

def __main__():
    loginInfo = getLoginInfo()
    connection = loadDatabase()
    return 0

__main__()
