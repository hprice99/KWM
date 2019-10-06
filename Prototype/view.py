from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

from sklearn import linear_model
from sklearn import datasets


# File name to load the DataFrame
fileName = "None"

# Empty DataFrame to store the loaded data
data = pd.DataFrame()

# TKinter frame
root = Tk()
mainFrame = ttk.Frame(root)

# String to store the path of the selected file
fileString = StringVar()

columnCount = 8
rowCount = 8

# Variables to store variables from DataFrame
existingClient = IntVar()
estateValue = IntVar()
beneficiaries = IntVar()
juristictions = IntVar()
testementaryTrust  = IntVar()
claimsExpected = IntVar()
cost = IntVar()

# Linear model variables
lm = linear_model.LinearRegression()
coefficients = np.zeros(shape=(6))
intercept = 0

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
        global data
        data = data.append(excelDoc["USE THIS"], ignore_index = True)
        data.set_index("Client", inplace=True)

        data["Existing client"] = data["Existing client"].astype("int")
        data["Value of Estate"] = round(data["Value of Estate"], 2)
        data["Beneficiaries"] = data["Beneficiaries"].astype("int")
        data["Multiple national jurisdictions"] = data["Multiple national jurisdictions"].astype("int")
        data["Testementary Trust"] = data["Testementary Trust"].astype("int")
        data["Claims expected against estate"] = data["Claims expected against estate"].astype("int")
        data["Cost"] = round(data["Cost"], 2)

        show_dataframe()
        generate_model()


def show_dataframe():
    table = ttk.Treeview(mainFrame)
    table.grid(column = 0, row = 3, rowspan = data.shape[1], columnspan = 6, ipadx=5, ipady=5)
    print(tuple(data.columns.to_list()))
    columnNames = data.columns.to_list()
    table["columns"] = tuple(columnNames)

    # Do not show the 'index' column
    table['show'] = 'headings'

    # TKinter variable to store column headings
    i = 0

    # Set the column headings
    for column in columnNames:
        table.column(column, width=100)
        table.heading(column, text=column)

    # Insert the rows into the table
    for row in range(len(data.index)):
        table.insert("", row, text="", values=tuple(data.iloc[row].to_list()))

    # Create a list of the variables involved
    Label(mainFrame, text="Variables", font = 'Arial 14 bold').grid(column=6, row = 3, sticky = W, padx=5, pady=5)

    i = 0
    for column in columnNames:
        if(column == "Cost"):
            Label(mainFrame, text=column).grid(column=6, row=4 + i + 1, sticky=W, padx=5, pady=5)
        else:
            Label(mainFrame, text = column).grid(column=6, row = 4 + i, sticky = W, padx = 5, pady = 5)
        i = i + 1

    existingClientField = Entry(mainFrame, textvariable = existingClient).grid(column=7, row = 4, sticky = W, padx = 5, pady = 5)
    estateValueField = Entry(mainFrame, textvariable = estateValue).grid(column=7, row = 5, sticky = W, padx = 5, pady = 5)
    beneficiariesField = Entry(mainFrame, textvariable = beneficiaries).grid(column=7, row = 6, sticky = W, padx = 5, pady = 5)
    juristictionsField = Entry(mainFrame, textvariable = juristictions).grid(column=7, row = 7, sticky = W, padx = 5, pady = 5)
    testementaryTrustField = Entry(mainFrame, textvariable = testementaryTrust).grid(column=7, row = 8, sticky = W, padx = 5, pady = 5)
    claimsExpectedField = Entry(mainFrame, textvariable = claimsExpected).grid(column=7, row = 9, sticky = W, padx = 5, pady = 5)

    ttk.Button(mainFrame, text="Estimate cost", command=estimate_cost).grid(row=10, column=7, sticky=W)

    costField = Label(mainFrame, textvariable = cost).grid(column=7, row = 11, sticky = W, padx = 5, pady = 5)

def generate_model():
    independentVars = data.loc[:, data.columns != 'Cost']
    dependentVar = data["Cost"]

    # Fit a model
    model = lm.fit(independentVars, dependentVar)

    predictions = lm.predict(independentVars)
    print(predictions[0:5])

    # Find the R^2 score of the model
    print("R^2 =", lm.score(independentVars, dependentVar))

    # Output the coefficients of the model
    print("Coefficients are", lm.coef_)

    global coefficients
    coefficients = lm.coef_

    # Output the intercept of the model
    print("Intercept is", lm.intercept_)
    global intercept
    intercept = lm.intercept_


def select_file(*args):
    global fileName
    fileName = filedialog.askopenfilename(title="Select file", filetypes = (("Excel files", "*.xlsx"), ("All files", "*.*")))

    print(fileName)

    try:
        fileString.set(fileName)
    except:
        print("fileString not set")

    return fileName

def estimate_cost(*args):
    estimate = intercept + coefficients[0] * existingClient.get() + coefficients[1] * estateValue.get() + coefficients[2] * beneficiaries.get() + \
        coefficients[3] * juristictions.get() + coefficients[4] * testementaryTrust.get() + coefficients[5] * claimsExpected.get()

    cost.set(round(estimate, 2))