from ui.windows import *
from accounts import LoginInfo
from tkinter import messagebox
from tkinter.simpledialog import askstring
import tkinter as tk
from database import DatabaseConnection

def onLogIn(window, usernameEntry, passwordEntry) -> None:
    if LoginInfo.validateCredentials(usernameEntry.get(), passwordEntry.get()):
        messagebox.showinfo(title="Login Successful", message="Welcome back! Thanks for trusting us! :)")
        username = usernameEntry.get()
        password = passwordEntry.get()
        window.destroy()
        connection = DatabaseConnection(username, password)
        showPasswordsWindow(connection, onAddPassword, onSearchPassword, onBackToLogin, onLoadPasswords)
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

def onLoadPasswords(connection: DatabaseConnection, frame) -> None:

    for widget in frame.winfo_children():
        widget.destroy()

    data = connection.getSavedPasswords()

    for identifier, password in data:
        addPasswordFrame(frame, connection, identifier, password, onEditPassword, onDeletePassword, onViewPassword)


def onSignUp(parent) -> None:
    parent.destroy()
    messagebox.showinfo(title = "Warning", message="Make sure to save your password, since you won't be able to recover it, and that could lead to data loss")
    showSignUpWindow(onSave=onSaveNewUser, onBack=onBackToLogin)  

def onBackToLogin(currentWindow) -> None:
    currentWindow.destroy()
    showLoginWindow(onLogIn=onLogIn, onSignUp=onSignUp, onExit=onExit)

def onDeletePassword(connection: DatabaseConnection, identifier: str, frame: tk.Frame) -> None:
    
    if messagebox.askquestion(title="Delete?", message="Are you sure you want to delete the current password? This cannot be undone.") == 'yes':
        connection.deletePassword(identifier)
        frame.pack_forget()
        frame.destroy()
        messagebox.showinfo(title = "Done!", message = "Your password has been successfully erased!")

def onEditPassword(connection: DatabaseConnection, identifierLabel, passwordLabel):
    password = askstring('Edit Password', "Add the corresponding password: ")
    
    if password is None:
        return

    passwordLabel["text"] = password

    connection.updatePassword(identifier, password)

    messagebox.showinfo(title = "Done!", message = "Your password has been successfully updated")

def onAddPassword(connection: DatabaseConnection, passwordsFrame):
    identifier = askstring('Identifier', r"Enter the password's identifier")

    if identifier is None:
        return
    if connection.doesIdentifierExist(identifier):
        messagebox.showerror(title="Error", message = "You cannot create a new entry with an existing identifier")
        return

    password = askstring('Password', "Enter the password")

    if password is None:
        return

    connection.savePassword(identifier, password)
    messagebox.showinfo(title = "Done!", message = "Your password has been successfully saved!")
    onLoadPasswords(connection, passwordsFrame)

def onViewPassword(identifierLabel, passwordLabel):
    showPassword('View', identifierLabel["text"], passwordLabel["text"])

def onSearchPassword(connection: DatabaseConnection):
    identifier = askstring('Search', r"Enter the identifier you want to look for")

    if identifier is None:
        return
    if not connection.doesIdentifierExist(identifier):
        messagebox.showerror(title="Error", message = "That identifier does not belong to any existing password")
        return

    showPassword('Search', identifier, connection.getPassword(identifier))

def showPassword(title: str, identifier: str, password: str) -> None:
    messagebox.showinfo(title = title, message = f"Title: {identifier}\nPassword: {password}")

'''
label for future use: label = tk.Label(master=passwordFrame, text="Oh-Oh!\nNo saved passwords\nfor this profile!", anchor='w')
'''
