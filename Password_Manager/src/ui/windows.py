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

def showPasswordsWindow(connection, onUpdatePasswordsUi) -> None:
    width, height = 400, 400
    scrollableWindow = getScrollableWindow(width=width, height=height, title='Passwords')
    root = scrollableWindow['root']
    canvas = scrollableWindow['canvas']
    scrollbar = scrollableWindow['scrollbar']

    onUpdatePasswordsUi(connection, root, canvas, scrollbar, width)

    root.mainloop()

def addPasswordsWindowInnerFrame(connection, root, canvas, scrollbar, getPasswordsFrame, width, onAddPassword, onSearch, onBack):
    canvasFrame = tk.Frame(master=canvas)
    canvasFrame.bind('<Configure>', lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=canvasFrame, anchor=tk.NW)

    passwordsFrame = getPasswordsFrame(connection, canvasFrame)
    passwordsFrame.pack(padx=Padding.small.value, pady=Padding.small.value, side=tk.TOP)

    actionButtonsFrame = tk.Frame(master=canvasFrame)
    addSimpleButton(actionButtonsFrame, "New Password", onAddPassword, connection, root, passwordsFrame, canvas, scrollbar, width)
    addSimpleButton(actionButtonsFrame, "Search Password", onSearch, connection)
    actionButtonsFrame.pack(padx=Padding.small.value, pady=Padding.small.value, side=tk.TOP)

    centeredButton = tk.Frame(master=canvasFrame)
    addCenteredButton(centeredButton, "Back", onBack, root)
    centeredButton.pack(padx=Padding.small.value, pady=Padding.small.value, side=tk.TOP)

    fullWidthFrame = tk.Frame(master=canvasFrame, width=width-15, height=1)
    fullWidthFrame.pack(side=tk.TOP, fill=tk.X)
