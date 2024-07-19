from accounts import LoginInfo
import ui
import sqlite3

def loadDatabase():
    pass #return sqlite3.connect("database.db")

def onLogIn(window, usernameEntry, passwordEntry) -> None:
    if LoginInfo.validateCredentials(usernameEntry.get(), passwordEntry.get()):
        print("Logged!")
    else:
        print("Try again!")

def __main__() -> int:

    LoginInfo.load()

    if LoginInfo.isEmpty():
        #create user example
        LoginInfo.createUser('coolUser777', 'password123')
    else:
        ui.showLoginWindow(onLogIn=onLogIn, onSignUp=lambda: print("clicked!"))
        #connection = loadDatabase()

    return 0

__main__()
