import tkinter as tk
from tkinter import messagebox

class MainWindow: 
    def __init__(self, root):
        self.root = root
        self.root.title("Book Manager")

        self.create_widgets()

    def create_widgets(self):

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


    def add_book(self):
        #Aquí podemos abrir un formulario para agregar un libro
        messagebox.showinfo("Add Book", "Form to add a book")

    def edit_book(self):
        # Aquí podrías abrir un formulario para editar un libro seleccionado
        messagebox.showinfo("Edit Book", "Form to edit a book")

    def delete_book(self):
        # Aquí podrías abrir un formulario para borrar un libro seleccionado
        messagebox.showinfo("Delete Book", "Confirm deletion of a book")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()