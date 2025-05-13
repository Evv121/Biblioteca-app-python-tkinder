import sqlite3

class BookDatabase:
    def __init__(self, db_name ="books.db"):
        self.connection = sqlite3.connect(db_name)
        self.create_table()
        
    def create_table(self):
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS books (
                                    id INTEGER PRIMERY KEY AUTOINCREMENT,
                                    title TEXT NOT NULL,
                                    author TEXT NOT NULL
                                    )
                """)
    
    def add_book(self, title, author):
        with self.connection:
            self.connection.execute(
                "INSERT INTO books (title, author) VALUES (?, ? )", (title, author)
            )
    
    def get_all_books(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, title, author FROM books")
        return cursor.fetchall()
    
    def delete_book(self, book_id, title, author):
        with self.connection:
            self.connection.execute(
                "UPDATE books SET title = ?, author = ? WHERE id = ?",
                (title, author, book_id)
            )
    
    def get_book(self, book_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, title, author FROM books WHERE id = ?", (book_id,))
        return cursor.fetchone()
    
    def update_book(self, book_id, title, author):
        with self.connection:
            self.connection.execute(
                "UPDATE books SET title = ?, author = ?, WHERE id = ?", (title, author, book_id)
            )
    
    def close(self):
        self.connection.close()

