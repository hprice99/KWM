from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog

def quit_app():
    root.quit()

def show_about(event = None):
    messagebox.showwarning("About", "This program was made in TKinter")

def  start_main_window():
    root = Tk()

    frame = Frame(root)

    add_buttons(frame)

    print(file)

    frame.pack()

    root.mainloop()

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

def add_buttons(frame):
    # Select file button
    fileButton = ttk.Button(frame, text="Important button", command=select_file)

    fileButton['state'] = 'disabled'
    fileButton['state'] = 'normal'
    fileButton.pack()

def select_file():
    filename = filedialog.askopenfilename(title="Select file",
                                               filetypes=(("csv files", "*.csv"), ("Excel files", "*.xlsx")))
    return filename
