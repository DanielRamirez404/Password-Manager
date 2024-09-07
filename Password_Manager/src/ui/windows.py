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

def showPasswordsWindow(connection, onLoadPasswords) -> None:
    width, height = 400, 400
    scrollableWindow = getScrollableWindow(width=width, height=height, title='Passwords')
    root = scrollableWindow['root']
    canvasFrame = scrollableWindow['canvasFrame']

    onLoadPasswords(connection, root, canvasFrame, height)

    root.mainloop()

def addPasswordsWindowInnerFrame(connection, root, canvasFrame, getPasswordsFrame, height, onAddPassword, onSearch, onBack):
    innerFrame = tk.Frame(master=canvasFrame)
    innerFrame.pack(fill=None, expand=True)

    passwordsFrame = getPasswordsFrame(connection, innerFrame, canvasFrame, height)
    passwordsFrame.pack(padx=Padding.small.value, pady=Padding.small.value, anchor=tk.N, fill=tk.BOTH)

    actionButtonsFrame = tk.Frame(master=innerFrame)
    addSimpleButton(actionButtonsFrame, "New Password", onAddPassword, connection, root, passwordsFrame, canvasFrame, height)
    addSimpleButton(actionButtonsFrame, "Search Password", onSearch, connection)
    actionButtonsFrame.pack(padx=Padding.small.value, pady=Padding.small.value, anchor=tk.CENTER, fill=tk.BOTH)

    centeredButton = tk.Frame(master=innerFrame)
    addCenteredButton(centeredButton, "Back", onBack, root)
    centeredButton.pack(padx=Padding.small.value, pady=Padding.small.value, anchor=tk.CENTER, fill=tk.BOTH)
