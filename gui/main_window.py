import tkinter as tk
from tkinter import messagebox

from gui.add_book_form import AddBookForm
from models.book import Book

from database.book_database import BookDatabase

# db = BookDatabase()
# db.add_book("1984", "George Orwell")
# print(db.get_all_books())
# db.close()


class MainWindow: 
    def __init__(self, root):
       
        self.root = root
        self.db = BookDatabase()
        self.books = [] #Lista local de objetos Book
        self.root.title("Book Manager")
        self.books_ids = []

        self.books = []

        self.create_widgets()
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def create_widgets(self):

        self.load_books()

        self.label = tk.Label(self.root, text="Bienvenido a Book Manager")
        self.label.pack(padx=20, pady=20)

        #Crear una lista de libros (ejemplo)
        self.books_listbox = tk.Listbox(self.root)
        self.books_listbox.pack(padx=10, pady=10)

        #Botones para las acciones
        self.add_button = tk.Button(self.root, text="Add Book", command=self.add_book)
        self.add_button.pack(pady=5)

        self.edit_button = tk.Button(self.root, text="Edit Book", command=self.edit_book)
        self.edit_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Book", command=self.delete_book)
        self.delete_button.pack(pady=5)

    def load_books(self):
        self.books_listbox.delete(0, tk.END) #Limpiar la lista
        self.books_ids.clear()

        books = self.db.get_all_books()

        for book in books:
            book_id, title, author = book
            display_text = f"{title} by {author}"
            self.books_listbox.insert(tk.END, display_text)
            self.books_ids.append(book_id)

    def add_book(self):
        #Aquí podemos abrir un formulario para agregar un libro
        form = AddBookForm(self.root)

        if form.result:
            title = form.result["title"]
            author = form.result["author"]
            
            #Guarda en la base de datos
            self.db.add_book(title, author)

            #Recargar en la lista
            self.load_books()

    def edit_book(self):
        selection = self.books_listbox.curselection()

        if not selection:
            messagebox.showwarning("Edit Book", "No book selected")
            return 
        
        index = selection[0]
        book_id = self.book_ids[index]
        book_data = self.db.get_book(book_id)

        if book_data:
            _, title, author = book_data
            form = AddBookForm(self.root, book_data=(title, author))

            if form.result:
                new_title = form.result["title"]
                new_author = form.result["author"]
                self.db.update_book(book_id, new_title, new_author)
                self.load_books()

    def delete_book(self):

        selection = self.books_listbox.curselection()

        if not selection:
            messagebox.showwarning("Delete Book", "No book selected")
            return
        
        index = selection[0]
        book_id = self.book_ids[index]

        confirm = messagebox.askyesno("Delete Book", "Are you sure you want to delete this book?")
        if confirm:
            self.db.delete_book(book_id)
            self.load_books()       
    
    def on_close(self):
        self.db.close()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()



