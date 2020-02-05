import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class App():
    def __init__(self, root):
        self.root = root
        
    def setMainWindow(self, title, dimensions, resizable):
        self.root.title(title)
        self.root.geometry(dimensions)
        self.root.resizable(*resizable)
    
    def createButton(self, window, name, bWidth, bCommand, coordinates):
        ttk.Button(window, text=name, width=bWidth, command=bCommand).place(x=coordinates[0], y=coordinates[1])
        
    def createEntry(self, window, txtVariable, eWidth, coordinates):
        ttk.Entry(window, textvariable=txtVariable, width=eWidth).place(x=coordinates[0], y=coordinates[1])
        
    def show_error_message(self, message_content):
        tk.messagebox.showerror("Error", message_content)
        

root = tk.Tk()
app = App(root)
app.regEx = ""
app.setMainWindow("sd", "500x500", (False, False))
app.createButton(app.root, "Create Automata", 20, app.show_error_message, (300, 250))
app.createEntry(app.root, app.regEx, 50, (300, 200))
app.root.mainloop()