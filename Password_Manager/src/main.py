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

def onSaveNewUser(usernameEntry, passwordEntry, confirmPasswordEntry) -> None:
    if LoginInfo.doesUserExist(usernameEntry.get()):
        print('oh-oh, this user already exist!')
    elif passwordEntry.get() != confirmPasswordEntry.get():
        print('oh-oh, the passwords do not match!')
    else:
        LoginInfo.createUser(usernameEntry.get(), passwordEntry.get())
        print('saved!')

def onSignUp(parent) -> None:
    parent.destroy()
    showSignUpWindow(onSave=onSaveNewUser, onBack=onBackToLogin)

def onBackToLogin(currentWindow) -> None:
    currentWindow.destroy()
    showLoginWindow(onLogIn=onLogIn, onSignUp=onSignUp)

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
