from accounts import LoginInfo
from ui import *
from tkinter import messagebox
import sqlite3

def loadDatabase():
    pass #return sqlite3.connect("database.db")

def onLogIn(window, usernameEntry, passwordEntry) -> None:
    if LoginInfo.validateCredentials(usernameEntry.get(), passwordEntry.get()):
        messagebox.showinfo(title="Login Successful", message="Welcome back! Thanks for trusting on us! :)")
    else:
        messagebox.showerror(title="Invalid Credentials", message="Oh-oh, your credentials do not correspond to any existing user. If you please, try again.")

def onExit(window) -> None:
    if messagebox.askquestion(title="Quitting Confirmation", message="Are you sure you want to quit? Your data will not be lost.") == 'yes':
        messagebox.showinfo(title="Goodbye!", message="See you next time!")
        window.destroy()

def onSaveNewUser(usernameEntry, passwordEntry, confirmPasswordEntry) -> None:
    if LoginInfo.doesUserExist(usernameEntry.get()):
        messagebox.showerror(title="Invalid User", message="Oh-oh, this user already exist!")
    elif passwordEntry.get() != confirmPasswordEntry.get():
        messagebox.showerror(title="Mismatched Passwords", message="Oh-oh, the passwords do not match!")
    else:
        LoginInfo.createUser(usernameEntry.get(), passwordEntry.get())
        messagebox.showinfo(title="Saved Successfully", message="Your data has been successfully registered")

def onSignUp(parent) -> None:
    parent.destroy()
    showSignUpWindow(onSave=onSaveNewUser, onBack=onBackToLogin)

def onBackToLogin(currentWindow) -> None:
    currentWindow.destroy()
    showLoginWindow(onLogIn=onLogIn, onSignUp=onSignUp, onExit=onExit)

def __main__() -> int:

    LoginInfo.load()

    showLoginWindow(onLogIn=onLogIn, onSignUp=onSignUp, onExit=onExit)
    #connection = loadDatabase()

    return 0

__main__()
