import tkinter
from tkinter import messagebox

# Create Screen
secret_screen = tkinter.Tk()
secret_screen.minsize(450, 750)
secret_screen.title("Secret Notes Manager")


# Vigenere Algorithm
def vigenere_algorithm(text, key, decrypt=False):
    result = ""
    key_length = len(key)

    for i in range(len(text)):
        char = text[i]
        key_char = key[i % key_length]

        if char.isalpha():
            shift = ord(key_char.lower()) - ord('a')
            if decrypt:
                shift = -shift
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            decrypted_char = char

        result += decrypted_char

    return result


# File operations
def file_create():
    title = title_entry.get()
    secret_info = secret_Info.get("1.0", tkinter.END)
    key = masterkey_entry.get()

    if not title or not secret_info:
        messagebox.showwarning("Warning", "Title and Secret Note fields cannot be left blank!")
        return

    encrypted_text = vigenere_algorithm(secret_info, key)

    with open("secret_info.txt", "a") as secret_file:
        secret_file.write("Title: " + title + "\n")
        secret_file.write("Encryption Note: " + encrypted_text + "\n\n")

    title_entry.delete(0, tkinter.END)
    secret_Info.delete("1.0", tkinter.END)
    masterkey_entry.delete(0, tkinter.END)


def file_decrypt():
    encrypted_text = secret_Info.get("1.0", tkinter.END)
    key = masterkey_entry.get()

    if not key:
        messagebox.showwarning("Warning", "Enter a key for decryption!")
        return

    decrypted_text = vigenere_algorithm(encrypted_text, key, decrypt=True)

    # Şifre çözülen metni ekranda göster
    secret_Info.delete("1.0", tkinter.END)
    secret_Info.insert("1.0", decrypted_text)


# Interface
# title label
title_label = tkinter.Label(text="Enter your secret info title")
title_label.config(font=("Arial", 10, "bold"), fg="black", pady=10, padx=10)
title_label.pack()

# first Entry
title_entry = tkinter.Entry()
title_entry.pack()

# secret Label
secret_title_label = tkinter.Label(text="Enter your secret note")
secret_title_label.config(font=("Arial", 10, "bold"), fg="black", pady=10, padx=10)
secret_title_label.pack()

# first text
secret_Info = tkinter.Text()
secret_Info.pack()

# Masterkey Label
masterkey_label = tkinter.Label(text="Enter your Encryption Key")
masterkey_label.config(font=("Arial", 10, "bold"), fg="black", pady=10, padx=10)
masterkey_label.pack()

# Masterkey Entry
masterkey_entry = tkinter.Entry()
masterkey_entry.pack()

# Buttons
save_encrypt_button = tkinter.Button(text="Save & Encrypt", command=file_create)
save_encrypt_button.pack()

decrypt_button = tkinter.Button(text="Decrypt", command=file_decrypt)
decrypt_button.pack()

secret_screen.mainloop()
