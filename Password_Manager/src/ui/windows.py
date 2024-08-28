import tkinter as tk
from ui.variables import *
from ui.reusables import *

def showLoginWindow(onLogIn, onSignUp, onExit) -> None:
    root = tk.Tk()
    root.title('Login')
    userEntry = getTitledEntry(root, "Username: ")
    passwordEntry = getTitledEntry(root, "Password: ")
    buttonsFrame = tk.Frame(master=root)
    simpleButtonsFrame = tk.Frame(master=buttonsFrame)
    addSimpleButton(simpleButtonsFrame, "Log in", onLogIn, root, userEntry, passwordEntry)
    addSimpleButton(simpleButtonsFrame, "Sign up", onSignUp, root)
    simpleButtonsFrame.pack(padx=Padding.small.value)
    addCenteredButton(buttonsFrame, "Exit", onExit, root)
    buttonsFrame.pack(padx=Padding.small.value, pady=Padding.small.value)
    root.mainloop()

def showSignUpWindow(onSave, onBack)-> None:
    root = tk.Tk()
    root.title('Sign Up')
    userEntry = getTitledEntry(root, "Username: ")
    passwordEntry = getTitledEntry(root, "Password: ")
    confirmPasswordEntry = getTitledEntry(root, "Confirm Passsword: ")
    buttonsFrame = tk.Frame(master=root)
    addSimpleButton(buttonsFrame, "Save", onSave, userEntry, passwordEntry, confirmPasswordEntry)
    addSimpleButton(buttonsFrame, "Back", onBack, root)
    buttonsFrame.pack(padx=Padding.small.value, pady=Padding.small.value)
    root.mainloop()

def showPasswordsWindow(connection, onUpdate, onNewPassword, onSearch, onBack) -> None:
    root = tk.Tk()
    root.title('Menu')

    passwordsFrame = tk.Frame(master=root)

    onUpdate(data, passwordsFrame)
    
    buttonsFrame = tk.Frame(master=root)

    actionButtonsFrame = tk.Frame(master=buttonsFrame)

    addSimpleButton(actionButtonsFrame, "New Password", onNewPassword)
    addSimpleButton(actionButtonsFrame, "Search Password", onSearch)
    actionButtonsFrame.pack(padx=Padding.small.value, pady=Padding.small.value)
    addCenteredButton(buttonsFrame, "Back", onBack, root)

    passwordsFrame.pack(padx=Padding.small.value, pady=Padding.small.value)
    buttonsFrame.pack(padx=Padding.small.value, pady=Padding.small.value)
    root.mainloop()
