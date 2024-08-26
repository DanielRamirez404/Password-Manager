from ui.windows import *
from accounts import LoginInfo
from tkinter import messagebox
from database import DatabaseConnection

def onLogIn(window, usernameEntry, passwordEntry) -> None:
    if LoginInfo.validateCredentials(usernameEntry.get(), passwordEntry.get()):
        messagebox.showinfo(title="Login Successful", message="Welcome back! Thanks for trusting on us! :)")
        test = DatabaseConnection()
        test.load(usernameEntry.get(), passwordEntry.get())
        window.destroy()
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
    elif usernameEntry.get() == "" or usernameEntry.get() == "":
        messagebox.showerror(title="Empty Entries", message="Youc can\'t leave any empty entries before saving your new user")
    else:
        LoginInfo.createUser(usernameEntry.get(), passwordEntry.get())
        messagebox.showinfo(title="Saved Successfully", message="Your data has been successfully registered")

def onSignUp(parent) -> None:
    parent.destroy()
    messagebox.showinfo(title = "Warning", message="Make sure to save your password, since you won't be able to recover it, and that could lead to data loss")
    showSignUpWindow(onSave=onSaveNewUser, onBack=onBackToLogin)  

def onBackToLogin(currentWindow) -> None:
    currentWindow.destroy()
    showLoginWindow(onLogIn=onLogIn, onSignUp=onSignUp, onExit=onExit)
