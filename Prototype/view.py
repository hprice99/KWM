from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog

class MainWindow():
    def __init__(self):
        self.root = Tk()

        self.mainFrame = ttk.Frame(self.root)

        self.mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.fileString = StringVar()
        self.fileString.set("Select a file")

        ttk.Label(self.mainFrame, text="File name").grid(row = 1, column = 1, sticky=W)
        file_label = ttk.Label(self.mainFrame, width=50, textvariable=self.fileString).grid(row = 1, column = 2)
        ttk.Button(self.mainFrame, text="Select file", command=self.select_file).grid(row = 1, column = 3, sticky=W)

        self.create_menu()

        self.root.mainloop()

    def quit_app(self):
        self.root.quit()

    def show_about(event=None):
        messagebox.showwarning("About", "This program was made in TKinter")

    def create_menu(self):
        # Generate a menu for the program
        the_menu = Menu(self.root)

        # ---- File menu ----
        file_menu = Menu(the_menu, tearoff=0)

        file_menu.add_command(label="Open")
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=self.quit_app)

        the_menu.add_cascade(label="File", menu=file_menu)

        # Generate keyboard shortcuts
        self.root.bind("<Command-Q>", self.quit_app)

        # ---- Help menu ----
        help_menu = Menu(the_menu, tearoff=0)
        help_menu.add_command(label="About", accelerator="Command-A", command=self.show_about)

        the_menu.add_cascade(label="Help", menu=help_menu)

        # Generate keyboard shortcuts
        self.root.bind("<Command-A>", self.show_about)
        self.root.bind("<Command-a>", self.show_about)

        # Add the menu to the root
        self.root.configure(menu=the_menu)

    def select_file(self, *args):
        filename = filedialog.askopenfilename(title="Select file",
                                              filetypes=(("CSV files", "*.csv"), ("Excel files", "*.xlsx")))

        print(filename)
        self.fileString.set(filename)

        try:
            self.fileString.set(filename)
        except:
            print("fileString not set")

        return filename
