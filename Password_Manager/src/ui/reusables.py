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
    addSimpleButton(frame, 'edit', onEdit, connection, titleLabel, passwordLabel)
    addSimpleButton(frame, 'erase', onDelete, connection, identifier, frame)
    addSimpleButton(frame, 'view', onView, titleLabel, passwordLabel)
    frame.pack(padx=Padding.small.value, pady=Padding.small.value)

def getScrollableWindow(width: int, height: int, title: str) -> dict:
    root = tk.Tk()
    root.title(title)
    root.geometry(str(width) + 'x' + str(height))
    root.resizable(False, False)

    windowFrame = tk.Frame(master=root)
    windowFrame.pack(fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(master=windowFrame, width=width-15)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

    scrollbar = tk.Scrollbar(windowFrame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(bg='blue')
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

    canvasFrame = tk.Frame(master=canvas,bg='black', height=height, width=width-15)
    canvasFrame.pack_propagate(False)
    canvas.create_window((0, 0), window=canvasFrame, anchor=tk.N)

    innerFrame = tk.Frame(master=canvasFrame)
    innerFrame.pack(anchor=tk.N)

    return {'root': root, 'canvasFrame': canvasFrame, 'innerFrame': innerFrame}

