import accounts
import sqlite3
import tkinter

def createUser(loginInfo: dict, user: str, password: str) -> None:
    loginInfo['users'].append(user)
    loginInfo['encrypted-passwords'].append(password)   #this has to be encrypted before appending

def loadDatabase():
    pass
    #return sqlite3.connect("database.db")

def __main__() -> int:
    loginInfo = accounts.getLoginInfo()

    if len(loginInfo['users']) == 0:
        #create user example
        createUser(loginInfo, 'coolUser777', 'password123')
    else:
        pass
        #login
        #connection = loadDatabase()       

    accounts.saveLoginInfo(loginInfo)
   
    return 0

__main__()
