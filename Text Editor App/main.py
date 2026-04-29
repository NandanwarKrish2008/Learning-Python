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

# FUNCTION-02 :- To open a new file

def openFile():
    filePath = filedialog.askopenfilename(
        defaultextension=".txt"
        filetypes=[("Text Files", "*.txt")]
    )

    if filePath:
        with open(filePath, "r") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read)

root.mainloop() # Starts and keeps the window open
