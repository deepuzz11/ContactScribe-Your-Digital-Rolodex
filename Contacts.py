import tkinter as tk
from tkinter import messagebox
import re

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBookApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")
        self.master.geometry("500x400")
        self.master.configure(bg='lightblue')  # Set background color to pale blue

        self.contacts = []

        self.create_widgets()

    def create_widgets(self):
        self.label_name = tk.Label(self.master, text="Name:", bg='lightblue', font=('Helvetica', 14))
        self.label_name.grid(row=0, column=0, sticky="e")
        self.entry_name = tk.Entry(self.master, font=('Helvetica', 14))
        self.entry_name.grid(row=0, column=1)
        self.entry_name.focus()

        self.label_phone = tk.Label(self.master, text="Phone Number:", bg='lightblue', font=('Helvetica', 14))
        self.label_phone.grid(row=1, column=0, sticky="e")
        self.entry_phone = tk.Entry(self.master, font=('Helvetica', 14))
        self.entry_phone.grid(row=1, column=1)

        self.label_email = tk.Label(self.master, text="Email:", bg='lightblue', font=('Helvetica', 14))
        self.label_email.grid(row=2, column=0, sticky="e")
        self.entry_email = tk.Entry(self.master, font=('Helvetica', 14))
        self.entry_email.grid(row=2, column=1)

        self.label_address = tk.Label(self.master, text="Address:", bg='lightblue', font=('Helvetica', 14))
        self.label_address.grid(row=3, column=0, sticky="e")
        self.entry_address = tk.Entry(self.master, font=('Helvetica', 14))
        self.entry_address.grid(row=3, column=1)

        self.button_add = tk.Button(self.master, text="Add Contact", command=self.add_contact, font=('Helvetica', 14))
        self.button_add.grid(row=4, column=0, columnspan=2, pady=10)
        self.button_add.bind("<Enter>", lambda event: self.button_add.config(bg='lightgreen'))
        self.button_add.bind("<Leave>", lambda event: self.button_add.config(bg='SystemButtonFace'))

        self.button_view = tk.Button(self.master, text="View Contacts", command=self.view_contacts, font=('Helvetica', 14))
        self.button_view.grid(row=5, column=0, columnspan=2, pady=10)
        self.button_view.bind("<Enter>", lambda event: self.button_view.config(bg='lightgreen'))
        self.button_view.bind("<Leave>", lambda event: self.button_view.config(bg='SystemButtonFace'))

    def add_contact(self):
        name = self.entry_name.get()
        phone_number = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()

        if not name or not phone_number:
            messagebox.showerror("Error", "Name and phone number are required.")
            return

        # Phone number validation with respective ISD codes
        isd_codes = {
            'US': r'^\+1\d{10}$',  # United States
            'UK': r'^\+44\d{10}$',  # United Kingdom
            'IN': r'^\+91\d{10}$',  # India
            'CA': r'^\+1\d{10}$',   # Canada
            'AU': r'^\+61\d{9}$',   # Australia
            # Add more ISD codes as needed
        }
        country_code = None
        for code, pattern in isd_codes.items():
            if re.match(pattern, phone_number):
                country_code = code
                break

        if not country_code:
            messagebox.showerror("Error", "Invalid phone number format.")
            return

        # Email format validation
        if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Error", "Invalid email format.")
            return

        # Proceed with adding contact
        new_contact = Contact(name, phone_number, email, address)
        self.contacts.append(new_contact)
        messagebox.showinfo("Success", "Contact added successfully.")

        self.clear_entries()
        self.entry_name.focus()

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts to display.")
            return

        contact_list = ""
        for contact in self.contacts:
            contact_list += f"Name: {contact.name}\n"
            contact_list += f"Phone: {contact.phone_number}\n"
            contact_list += f"Email: {contact.email}\n"
            contact_list += f"Address: {contact.address}\n\n"

        messagebox.showinfo("Contact List", contact_list)

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
