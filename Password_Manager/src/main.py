from accounts import LoginInfo
import ui
import sqlite3

def loadDatabase():
    pass
    #return sqlite3.connect("database.db")

def __main__() -> int:

    LoginInfo.load()
    ui.showLoginWindow()

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
