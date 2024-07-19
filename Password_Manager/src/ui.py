import tkinter as tk

def addTitledTextbox(window, title: str):
    frame = tk.Frame(master=window)
    label = tk.Label(master=frame, text=title, anchor='w')
    entry = tk.Entry(master=frame)
    label.pack(fill=tk.X)
    entry.pack(fill=tk.X)
    frame.pack(fill=tk.X, padx=5, pady=5)
    

def showLoginWindow() -> None:
    root = tk.Tk()
    root.title('Login')
    addTitledTextbox(root, "Username: ")
    addTitledTextbox(root, "Password: ")
    button = tk.Button(text="Log in")
    button.pack(padx=5, pady=5)
    root.mainloop()
