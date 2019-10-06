from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fileName = "None"

root = Tk()
mainFrame = ttk.Frame(root)

# String to store the path of the selected file
fileString = StringVar()

columnCount = 7
rowCount = 7

independentColumn = StringVar(root)
dependentColumn = StringVar(root)

def create_window():
    root.geometry("1200x500")
    root.resizable(True, True)

    Grid.rowconfigure(root, 0, weight=1)
    Grid.columnconfigure(root, 0, weight=1)

    mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))

    # Make grid resizable
    for row_index in range(rowCount):
        Grid.rowconfigure(mainFrame, row_index, weight=1)
        for column_index in range(columnCount):
            Grid.columnconfigure(mainFrame, column_index, weight=1)

    ttk.Label(mainFrame, text="File name").grid(row = 0, column = 0, sticky = W)
    file_label = ttk.Label(mainFrame, width=50, textvariable=fileString).grid(row = 0, column = 1, columnspan = 5)
    ttk.Button(mainFrame, text="Select file", command=select_file).grid(row = 0, column = 6, columnspan = 2, sticky=E)
    ttk.Button(mainFrame, text="Open file", command=create_dataframe).grid(row = 1, column = 6, columnspan = 2,sticky = E)

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
        # df = pd.read_csv(fileName)
        excelDoc = pd.read_excel(fileName, sheet_name=["USE THIS"])
        data = excelDoc["USE THIS"]
        data.set_index("Client", inplace=True)
        print(data)
        show_dataframe(data)


def show_dataframe(df):
    table = ttk.Treeview(mainFrame)
    table.grid(column = 0, row = 3, rowspan = 6, columnspan = 5, ipadx=5, ipady=5)
    print(tuple(df.columns.to_list()))
    columnNames = df.columns.to_list()
    table["columns"] = tuple(columnNames)

    # Do not show the 'index' column
    table['show'] = 'headings'

    # TKinter variable to store column headings
    i = 0

    # Set the column headings
    for column in columnNames:
        table.column(column, width=200)
        table.heading(column, text=column)

    # Insert the rows into the table
    for row in range(len(df.index)):
        table.insert("", row, text="", values=tuple(df.iloc[row].to_list()))

    # Create a drop-down menu for the column names
    Label(mainFrame, text="Choose the independent variable").grid(column=6, row = 3, sticky = W, padx=5, pady=5)

    independentColumn.set(columnNames[0])
    independentMenu = OptionMenu(mainFrame, independentColumn, *columnNames)
    independentMenu.grid(column = 7, row = 3, sticky = W)

    Label(mainFrame, text="Choose the dependent variable").grid(column=6, row=4, sticky = W, padx=5, pady=5)

    dependentColumn.set(columnNames[1])
    dependentMenu = OptionMenu(mainFrame, dependentColumn, *columnNames)
    dependentMenu.grid(column=7, row=4, sticky = W)

    columnSelectButton = Button(mainFrame, text="Select columns", command=select_columns)
    columnSelectButton.grid(column = 7, row = 5, sticky = W)

def select_columns(*args):
    print("The independent variable is " + independentColumn.get() + " and the dependent variable is " + dependentColumn.get())


def select_file(*args):
    global fileName
    fileName = filedialog.askopenfilename(title="Select file", filetypes = (("Excel files", "*.xlsx"), ("All files", "*.*")))

    print(fileName)

    try:
        fileString.set(fileName)
    except:
        print("fileString not set")

    return fileName
