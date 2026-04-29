# import tkinter for GUI app

import tkinter as tk
from tkinter import filedialog, messagebox

# Main window code

root = tk.Tk()
root.title("My text editor")
root.geometry("800x600")

# Create text area

text = tk.Text(
    root,
    wrap = tk.WORD,
    font = ("Arial", 18)
)

text.pack(expand=True,fill=tk.BOTH)

# Main Logic

# FUNCTION-01 :- To create a new file

def newFile():
    text.delete(1.0, tk.END)

root.mainloop() # Starts and keeps the window open
