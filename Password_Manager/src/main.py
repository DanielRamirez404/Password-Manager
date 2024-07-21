from accounts import LoginInfo
from ui import *
import sqlite3

def loadDatabase():
    pass #return sqlite3.connect("database.db")

def onLogIn(window, usernameEntry, passwordEntry) -> None:
    if LoginInfo.validateCredentials(usernameEntry.get(), passwordEntry.get()):
        print("Logged!")
    else:
        print("Try again!")

def onSignUp(parent) -> None:
    parent.destroy()
    showSignUpWindow(onSave=lambda: print('save'), onBack=lambda: print('back'))

def __main__() -> int:

    LoginInfo.load()

    if LoginInfo.isEmpty():
        #create user example
        LoginInfo.createUser('coolUser777', 'password123')
    else:
        showLoginWindow(onLogIn=onLogIn, onSignUp=onSignUp)
        #connection = loadDatabase()

    return 0

__main__()
