import tkinter as tk
from tkinter import simpledialog

class AddBookForm(simpledialog.Dialog):
    def body(self, master):
        self.title("Add Book")

        tk.Label(master, text="Title").grid(row=0, column=0)
        self.title_entry = tk.Entry(master)
        self.title_entry.grid(row=0, column=1)

        tk.Label(master, text="Author:").grid(row=0, column=0)
        self.author_entry = tk.Entry(master)
        self.author_entry.grid(row=1, column=1)
        
        return self.title_entry #el cursor empieza aquí
    
    def apply(self):
        self.book_title = self.title_entry.get()
        self.bool_author = self.author_entry.get()
        self.result = {
            "title": self.book_title,
            "author": self.bool_author
        }

