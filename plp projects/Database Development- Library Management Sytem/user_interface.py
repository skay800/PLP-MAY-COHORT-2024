# library_management_gui.py

import tkinter as tk
from tkinter import messagebox, simpledialog
from sqlalchemy.orm import Session
from database import SessionLocal, init_db
from library_logic import create_author, create_book, create_member, get_authors, get_books, get_members  # Importing from your logic file
import re  # Regular expression for email validation

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("500x600")
        self.root.configure(bg="#f0f0f0")

        # Initialize the database
        init_db()
        self.db = SessionLocal()

        # Create UI Elements
        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Library Management System", font=("Helvetica", 20, "bold"), bg="#f0f0f0")
        title_label.pack(pady=20)

        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Add Author", command=self.add_author, bg="#4CAF50", fg="white").pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(button_frame, text="Add Book", command=self.add_book, bg="#4CAF50", fg="white").pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(button_frame, text="Add Member", command=self.add_member, bg="#4CAF50", fg="white").pack(pady=5, padx=10, side=tk.LEFT)

        tk.Button(button_frame, text="View Authors", command=self.view_authors, bg="#2196F3", fg="white").pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(button_frame, text="View Books", command=self.view_books, bg="#2196F3", fg="white").pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(button_frame, text="View Members", command=self.view_members, bg="#2196F3", fg="white").pack(pady=5, padx=10, side=tk.LEFT)

       
        
        tk.Button(self.root, text="Exit", command=self.root.quit, bg="#F44336", fg="white").pack(pady=20)

        # Adding some padding to buttons
        for btn in button_frame.winfo_children():
            btn.config(width=15)

    def add_author(self):
        name = simpledialog.askstring("Input", "Enter author name:")
        if name:
            create_author(self.db, name)
            messagebox.showinfo("Success", "Author added successfully!")

    def add_book(self):
        title = simpledialog.askstring("Input", "Enter book title:")
        if title:
            author_id = simpledialog.askinteger("Input", "Enter author ID:")
            if author_id is not None:
                create_book(self.db, title, author_id)
                messagebox.showinfo("Success", "Book added successfully!")

    def add_member(self):
        name = simpledialog.askstring("Input", "Enter member name:")
        if name:
            email = simpledialog.askstring("Input", "Enter member email:")
            if email:
                if self.validate_email(email):
                    create_member(self.db, name, email)
                    messagebox.showinfo("Success", "Member added successfully!")
                else:
                    messagebox.showerror("Error", "Invalid email format.")

    def view_authors(self):
        authors = get_authors(self.db)
        authors_list = "\n".join([f"ID: {author.id}, Name: {author.name}" for author in authors])
        if authors_list:
            messagebox.showinfo("Authors", authors_list)
        else:
            messagebox.showinfo("Authors", "No authors found.")

    def view_books(self):
        books = get_books(self.db)
        books_list = "\n".join([f"ID: {book.id}, Title: {book.title}, Author ID: {book.author_id}" for book in books])
        if books_list:
            messagebox.showinfo("Books", books_list)
        else:
            messagebox.showinfo("Books", "No books found.")

    def view_members(self):
        members = get_members(self.db)
        members_list = "\n".join([f"ID: {member.id}, Name: {member.name}, Email: {member.email}" for member in members])
        if members_list:
            messagebox.showinfo("Members", members_list)
        else:
            messagebox.showinfo("Members", "No members found.")

    
    def validate_email(self, email):
        # Simple regex for validating an email
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagementSystem(root)
    root.mainloop()
