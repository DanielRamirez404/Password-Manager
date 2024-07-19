import tkinter as tk

def getTitledEntry(master, title: str):
    frame = tk.Frame(master=master)
    label = tk.Label(master=frame, text=title, anchor='w')
    entry = tk.Entry(master=frame)
    label.pack(fill=tk.X)
    entry.pack(fill=tk.X)
    frame.pack(fill=tk.X, padx=5, pady=5)
    return entry

def addSimpleButton(master, text: str, onClick, *args):
    button = tk.Button(master=master, text=text)
    button.bind("<Button-1>", lambda event: onClick(*args))
    button.pack(side=tk.LEFT, padx=5, pady=5)

def showLoginWindow(onLogIn, onSignUp) -> None:
    root = tk.Tk()
    root.title('Login')
    userEntry = getTitledEntry(root, "Username: ")
    passwordEntry = getTitledEntry(root, "Password: ")
    buttonsFrame = tk.Frame(master=root)
    addSimpleButton(buttonsFrame, "Log in", onLogIn, root, userEntry, passwordEntry)
    addSimpleButton(buttonsFrame, "Sign up", onSignUp)
    buttonsFrame.pack(padx=5, pady=5)
    root.mainloop()
