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

def showPasswordsWindow(connection, onAddPassword, onSearch, onBack, onLoadPasswords) -> None:
    root = tk.Tk()
    root.title('Passwords')
    root.geometry('400x300')

    frameContainer = tk.Frame(master=root)
    frameContainer.pack(padx=Padding.small.value, pady=Padding.small.value, fill=tk.BOTH, expand=True)

    canvasContainer = tk.Canvas(master=frameContainer)
    canvasContainer.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frameContainer, orient=tk.VERTICAL, command=canvasContainer.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvasContainer.configure(yscrollcommand=scrollbar.set)
    canvasContainer.bind('<Configure>', lambda event: canvasContainer.configure(scrollregion=canvasContainer.bbox("all")))

    outerFrame = tk.Frame(master=canvasContainer '''bg="black"''', height=300, width=300)
    outerFrame.pack_propagate(False)
    canvasContainer.create_window((0, 0), window=outerFrame, anchor=tk.N)

    innerFrame = tk.Frame(master=outerFrame)
    innerFrame.pack(anchor=tk.N)

    passwordsFrame = tk.Frame(master=innerFrame)
    onLoadPasswords(connection, passwordsFrame)
    passwordsFrame.pack(padx=Padding.small.value, pady=Padding.small.value, anchor=tk.CENTER, fill=tk.BOTH)

    actionButtonsFrame = tk.Frame(master=innerFrame)
    addSimpleButton(actionButtonsFrame, "New Password", onAddPassword, connection, passwordsFrame)
    addSimpleButton(actionButtonsFrame, "Search Password", onSearch, connection)
    actionButtonsFrame.pack(padx=Padding.small.value, pady=Padding.small.value, anchor=tk.CENTER, fill=tk.BOTH)

    centeredButton = tk.Frame(master=innerFrame)
    addCenteredButton(centeredButton, "Back", onBack, root)
    centeredButton.pack(padx=Padding.small.value, pady=Padding.small.value, anchor=tk.CENTER, fill=tk.BOTH)


    #outerFrame.configure(height=1000)

    root.mainloop()
