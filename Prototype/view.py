from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fileName = "None"

root = Tk()

fileString = StringVar()

columnCount = 3
rowCount = 3

def create_window():
    root.geometry("1200x500")
    root.resizable(True, True)

    Grid.rowconfigure(root, 0, weight=1)
    Grid.columnconfigure(root, 0, weight=1)

    mainFrame = ttk.Frame(root)
    mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))

    # Make grid resizable
    for row_index in range(rowCount):
        if row_index == 2:
            Grid.rowconfigure(mainFrame, row_index, weight=2)
        else:
            Grid.rowconfigure(mainFrame, row_index, weight=1)
        for column_index in range(columnCount):
            Grid.columnconfigure(mainFrame, column_index, weight=1)

    ttk.Label(mainFrame, text="File name").grid(row = 1, column = 1, sticky = W)
    file_label = ttk.Label(mainFrame, width=50, textvariable=fileString).grid(row = 1, column = 2)
    ttk.Button(mainFrame, text="Select file", command=select_file).grid(row = 1, column = 3, sticky=W)
    ttk.Button(mainFrame, text="Open file", command=create_dataframe).grid(row = 2, column = 3, sticky = W)

    create_menu()

    root.mainloop()

def quit_app():
    root.quit()
    root.destroy()
    exit()

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
    print("Open button pressed")
    print(fileName)
    if fileName != "None":
        df = pd.read_csv(fileName)
        print(df)
        show_dataframe(df)


def show_dataframe(df):
    # Frame for dataframe
    dataframeFrame = ttk.Frame(root)
    dataframeFrame.grid(column=0, row=4, sticky=(N, W, E, S))

    table = ttk.Treeview(dataframeFrame)
    table.grid(column = 1, row = 5)
    print(tuple(df.columns.to_list()))
    table["columns"] = tuple(df.columns.to_list())

    # Do not show the 'index' column
    table['show'] = 'headings'

    row = 1

    for column in df.columns.to_list():
        table.column(column, width=100)
        table.heading(column, text=column)

def select_file(*args):
    global fileName
    fileName = filedialog.askopenfilename(title="Select file",
                                          filetypes=(("CSV files", "*.csv"), ("Excel files", "*.xlsx")))

    print(fileName)

    try:
        fileString.set(fileName)
    except:
        print("fileString not set")

    return fileName
