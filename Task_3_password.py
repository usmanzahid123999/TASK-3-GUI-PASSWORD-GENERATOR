import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())

    char_set = ""
    if include_letters.get():
        char_set += string.ascii_letters
    if include_digits.get():
        char_set += string.digits
    if include_special.get():
        char_set += string.punctuation

    if char_set:
        password = ''.join(random.choice(char_set) for _ in range(password_length))
        password_var.set(password)
    else:
        password_var.set("Select at least one character type")

def reset_options():
    length_entry.delete(0, tk.END)
    include_letters.set(False)
    include_digits.set(False)
    include_special.set(False)
    password_var.set("")

root = tk.Tk()
root.title("Password Generator")

root.geometry("400x300")  # Set window size

length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root, font=("Helvetica", 16))
length_entry.pack(pady=10)

include_letters = tk.BooleanVar()
letters_checkbox = tk.Checkbutton(root, text="Include Letters", variable=include_letters, font=("Helvetica", 14))
letters_checkbox.pack()

include_digits = tk.BooleanVar()
digits_checkbox = tk.Checkbutton(root, text="Include Digits", variable=include_digits, font=("Helvetica", 14))
digits_checkbox.pack()

include_special = tk.BooleanVar()
special_checkbox = tk.Checkbutton(root, text="Include Special Characters", variable=include_special, font=("Helvetica", 14))
special_checkbox.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=("Helvetica", 16))
generate_button.pack(pady=10)

password_var = tk.StringVar()
password_label = tk.Label(root, textvariable=password_var, font=("Helvetica", 16))
password_label.pack()

reset_button = tk.Button(root, text="Reset", command=reset_options, font=("Helvetica", 16))
reset_button.pack()

exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Helvetica", 16))
exit_button.pack()

root.mainloop()
