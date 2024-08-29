import tkinter as tk
from ui.variables import *

def getTitledEntry(master, title: str):
    frame = tk.Frame(master=master)
    label = tk.Label(master=frame, text=title, anchor='w')
    entry = tk.Entry(master=frame)
    label.pack(fill=tk.X)
    entry.pack(fill=tk.X)
    frame.pack(fill=tk.X, padx=Padding.small.value, pady=Padding.small.value)
    return entry

def addSimpleButton(master, text: str, onClick, *args) -> None:
    button = tk.Button(master=master, text=text)
    button.bind("<Button-1>", lambda event: onClick(*args))
    button.pack(side=tk.LEFT, padx=Padding.small.value)

def addCenteredButton(master, text: str, onClick, *args) -> None:
    button = tk.Button(master=master, text=text, width=Padding.medium.value)
    button.bind("<Button-1>", lambda event: onClick(*args))
    button.pack(padx=Padding.small.value, pady=Padding.small.value)

def addPasswordFrame(master, connection, identifier: str, password: str, onEdit, onDelete, onView) -> None:
    frame = tk.Frame(master=master)
    titleLabel = tk.Label(master=frame, text=identifier, anchor='w')
    passwordLabel = tk.Label(master=frame, text=password, anchor='w')
    titleLabel.pack(side=tk.LEFT, padx=Padding.small.value)
    passwordLabel.pack(side=tk.LEFT, padx=Padding.small.value)
    addSimpleButton(frame, 'edit', onEdit)
    addSimpleButton(frame, 'erase', onDelete, connection, identifier, frame)
    addSimpleButton(frame, 'view', onView)
    frame.pack(padx=Padding.small.value, pady=Padding.small.value)
