import tkinter as tk
from tkinter import messagebox
import random
import string

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("450x350")
root.configure(bg="#e3f2fd")  # Light ice blue background

# Center window on screen
root.update_idletasks()
x = (root.winfo_screenwidth() // 2) - (450 // 2)
y = (root.winfo_screenheight() // 2) - (350 // 2)
root.geometry(f"450x350+{x}+{y}")

# Main frame to organize layout
frame = tk.Frame(root, bg="#e3f2fd")
frame.pack(pady=20)

# Title label
title_label = tk.Label(frame, text="Password Generator", font=("Arial", 18, "bold"), bg="#e3f2fd", fg="#0d47a1")
title_label.pack(pady=10)


# Password length input
length_label = tk.Label(frame, text="Password Length:", font=("Arial", 12), bg="#e3f2fd")
length_label.pack(anchor="w", pady=(10,0))

length_entry = tk.Entry(frame, font=("Arial", 12), width=10)
length_entry.pack(anchor="w", pady=(0,10))

# Checkboxes
use_uppercase_var = tk.BooleanVar(value=True)
uppercase_check = tk.Checkbutton(frame, text="Include Uppercase Letters", variable=use_uppercase_var, bg="#e3f2fd", font=("Arial", 12))
uppercase_check.pack(anchor="w")

use_numbers_var = tk.BooleanVar(value=True)
numbers_check = tk.Checkbutton(frame, text="Include Numbers", variable=use_numbers_var, bg="#e3f2fd", font=("Arial", 12))
numbers_check.pack(anchor="w")

use_symbols_var = tk.BooleanVar(value=True)
symbols_check = tk.Checkbutton(frame, text="Include Symbols", variable=use_symbols_var, bg="#e3f2fd", font=("Arial", 12))
symbols_check.pack(anchor="w")


def generate_password():
    length = length_entry.get()

    if not length.isdigit():
        messagebox.showerror("Error", "Password length must be a number.")
        return

    length = int(length)
    characters = string.ascii_lowercase

    if use_uppercase_var.get():
        characters += string.ascii_uppercase
    if use_numbers_var.get():
        characters += string.digits
    if use_symbols_var.get():
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text="Generated Password: " + password)

# Generate Password Button
generate_button = tk.Button(frame, text="Generate Password", command=generate_password,
                            font=("Arial", 12, "bold"), bg="#0d47a1", fg="white", width=20)
generate_button.pack(pady=15)

# Result Label
result_label = tk.Label(frame, text="Generated Password: ", font=("Arial", 12), bg="#e3f2fd", fg="#0d47a1")
result_label.pack(pady=5)


root.mainloop()
