import tkinter as tk
from tkinter import simpledialog

class AddBookForm(simpledialog.Dialog):

    def __init__(self, parent, book_data=None):
        self.book_data = book_data 
        super().__init__(parent)

    def body(self, master):
        self.title("Edit Book" if self.book_data else "Add Book")

        tk.Label(master, text="Title").grid(row=0, column=0)
        self.title_entry = tk.Entry(master)
        self.title_entry.grid(row=0, column=1)

        tk.Label(master, text="Author:").grid(row=1, column=0)
        self.author_entry = tk.Entry(master)
        self.author_entry.grid(row=1, column=1)

        #Si es edicion rellenar campos
        if self.book_data:
            self.title_entry.insert(0, self.book_data[0])
            self.author_entry.insert(0, self.book_data[1])
        
        return self.title_entry #el cursor empieza aquí
    
    def apply(self):
        self.book_title = self.title_entry.get().strip()
        self.bool_author = self.author_entry.get().strip()
        self.result = {
            "title": self.book_title,
            "author": self.bool_author
        }

