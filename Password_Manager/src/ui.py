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

def showSignUpWindow()-> None:
    root = tk.TK()
    root.title('Sign Up')
