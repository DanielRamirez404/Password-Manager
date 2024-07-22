from behavior import *
import sqlite3

def loadDatabase():
    pass #return sqlite3.connect("database.db")

def __main__() -> int:

    LoginInfo.load()

    showLoginWindow(onLogIn=onLogIn, onSignUp=onSignUp, onExit=onExit)
    #connection = loadDatabase()

    return 0

__main__()
