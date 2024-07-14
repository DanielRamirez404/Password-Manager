import accounts
import sqlite3
import tkinter

def loadDatabase():
    return 0
    #return sqlite3.connect("database.db")

def __main__():
    loginInfo = accounts.getLoginInfo()
    accounts.saveLoginInfo(loginInfo)
    #connection = loadDatabase()
    return 0

__main__()
