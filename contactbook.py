import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import pickle
import os

# File to store contacts
CONTACTS_FILE = 'contacts.pkl'

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'rb') as file:
            return pickle.load(file)
    return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'wb') as file:
        pickle.dump(contacts, file)

# GUI Functions
def add_contact():
    name = simpledialog.askstring("Add Contact", "Enter contact name:")
    if name in contacts:
        messagebox.showwarning("Warning", "Contact already exists!")
        return
    phone = simpledialog.askstring("Add Contact", "Enter phone number:")
    email = simpledialog.askstring("Add Contact", "Enter email address:")
    if name and phone and email:
        contacts[name] = {'phone': phone, 'email': email}
        save_contacts(contacts)
        messagebox.showinfo("Info", "Contact added!")
    else:
        messagebox.showwarning("Warning", "All fields are required!")

def update_contact():
    name = simpledialog.askstring("Update Contact", "Enter contact name to update:")
    if name in contacts:
        phone = simpledialog.askstring("Update Contact", "Enter new phone number:")
        email = simpledialog.askstring("Update Contact", "Enter new email address:")
        if phone and email:
            contacts[name] = {'phone': phone, 'email': email}
            save_contacts(contacts)
            messagebox.showinfo("Info", "Contact updated!")
        else:
            messagebox.showwarning("Warning", "All fields are required!")
    else:
        messagebox.showerror("Error", "Contact not found!")

def view_contacts():
    if contacts:
        contact_list = "\n".join(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}" for name, info in contacts.items())
        messagebox.showinfo("Contacts", contact_list)
    else:
        messagebox.showinfo("Info", "No contacts found!")

def search_contact():
    name = simpledialog.askstring("Search Contact", "Enter contact name to search:")
    if name in contacts:
        info = contacts[name]
        messagebox.showinfo("Contact Info", f"Name: {name}\nPhone: {info['phone']}\nEmail: {info['email']}")
    else:
        messagebox.showerror("Error", "Contact not found!")

def delete_contact():
    name = simpledialog.askstring("Delete Contact", "Enter contact name to delete:")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        messagebox.showinfo("Info", "Contact deleted!")
    else:
        messagebox.showerror("Error", "Contact not found!")

# Setting up the main window
app = tk.Tk()
app.title("Contact Book")

contacts = load_contacts()

# Adding buttons to the main window
tk.Button(app, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(app, text="Update Contact", command=update_contact).pack(pady=5)
tk.Button(app, text="View Contacts", command=view_contacts).pack(pady=5)
tk.Button(app, text="Search Contact", command=search_contact).pack(pady=5)
tk.Button(app, text="Delete Contact", command=delete_contact).pack(pady=5)

app.mainloop()



