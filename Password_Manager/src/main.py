from accounts import LoginInfo
import sqlite3
import tkinter

def loadDatabase():
    pass
    #return sqlite3.connect("database.db")

def __main__() -> int:
    LoginInfo.load()

    if LoginInfo.isEmpty():
        #create user example
        LoginInfo.createUser('coolUser777', 'password123')
    else:
        pass
        #login
        #connection = loadDatabase()       

    LoginInfo.save()

    return 0

__main__()
