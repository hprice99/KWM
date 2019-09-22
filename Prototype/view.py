from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fileName = "None"

root = Tk()

def create_window():
    mainFrame = ttk.Frame(root)

    mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    fileString = StringVar()

    ttk.Label(mainFrame, text="File name").grid(row = 1, column = 1, sticky=W)
    file_label = ttk.Label(mainFrame, width=50, textvariable=fileString).grid(row = 1, column = 2)
    ttk.Button(mainFrame, text="Select file", command=select_file).grid(row = 1, column = 3, sticky=W)
    ttk.Button(mainFrame, text="Open file", command=create_dataframe).grid(row = 2, column = 3, sticky = W)


    create_menu()

    root.mainloop()

def quit_app():
    root.quit()

def show_about(event=None):
    messagebox.showwarning("About", "This program was made in TKinter")

def create_menu():
    # Generate a menu for the program
    the_menu = Menu(root)

    # ---- File menu ----
    file_menu = Menu(the_menu, tearoff=0)

    file_menu.add_command(label="Open")
    file_menu.add_separator()
    file_menu.add_command(label="Quit", command=quit_app)

    the_menu.add_cascade(label="File", menu=file_menu)

    # Generate keyboard shortcuts
    root.bind("<Command-Q>", quit_app)

    # ---- Help menu ----
    help_menu = Menu(the_menu, tearoff=0)
    help_menu.add_command(label="About", accelerator="Command-A", command=show_about)

    the_menu.add_cascade(label="Help", menu=help_menu)

    # Generate keyboard shortcuts
    root.bind("<Command-A>", show_about)
    root.bind("<Command-a>", show_about)

    # Add the menu to the root
    root.configure(menu=the_menu)

def create_dataframe():
    if fileName != "None":
        df = pd.read_csv(fileName)
        print(df)


def select_file(*args):
    fileName = filedialog.askopenfilename(title="Select file",
                                          filetypes=(("CSV files", "*.csv"), ("Excel files", "*.xlsx")))

    print(fileName)

    return fileName
