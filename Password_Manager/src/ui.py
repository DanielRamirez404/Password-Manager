import tkinter as tk
from ui_variables import *
from ui_reusables import *

def showLoginWindow(onLogIn, onSignUp) -> None:
    root = tk.Tk()
    root.title('Login')
    userEntry = getTitledEntry(root, "Username: ")
    passwordEntry = getTitledEntry(root, "Password: ")
    buttonsFrame = tk.Frame(master=root)
    simpleButtonsFrame = tk.Frame(master=buttonsFrame)
    addSimpleButton(simpleButtonsFrame, "Log in", onLogIn, root, userEntry, passwordEntry)
    addSimpleButton(simpleButtonsFrame, "Sign up", onSignUp, root)
    simpleButtonsFrame.pack(padx=Padding.small.value)
    addCenteredButton(buttonsFrame, "Exit", lambda: root.destroy())
    buttonsFrame.pack(padx=Padding.small.value, pady=Padding.small.value)
    root.mainloop()

def showSignUpWindow(onSave, onBack)-> None:
    root = tk.Tk()
    root.title('Sign Up')
    label = tk.Label(master=root, text="Make sure to save your password,\nsince you won't be able to recover it,\nand that could lead to data loss")
    label.pack(padx=Padding.small.value, pady=Padding.small.value)
    userEntry = getTitledEntry(root, "Username: ")
    passwordEntry = getTitledEntry(root, "Password: ")
    confirmPasswordEntry = getTitledEntry(root, "Confirm Passsword: ")
    buttonsFrame = tk.Frame(master=root)
    addSimpleButton(buttonsFrame, "Save", onSave)
    addSimpleButton(buttonsFrame, "Back", onBack)
    buttonsFrame.pack(padx=Padding.small.value, pady=Padding.small.value)
    root.mainloop()
