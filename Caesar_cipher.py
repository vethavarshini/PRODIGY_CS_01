import tkinter as tk
from tkinter import messagebox


def encrypt():
    plaintext = entry.get("1.0", tk.END).strip()  # Get text from Text widget
    ciphertext = caesar_cipher(plaintext, shift_value.get(), 1)
    show_custom_message("Encryption", f"Encrypted text: {ciphertext}")


def decrypt():
    ciphertext = entry.get("1.0", tk.END).strip()  # Get text from Text widget
    plaintext = caesar_cipher(ciphertext, shift_value.get(), -1)
    show_custom_message("Decryption", f"Decrypted text: {plaintext}")


def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shifted = (ord(char) - base + shift * mode) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result


def show_custom_message(title, message):
    popup = tk.Toplevel()
    popup.title(title)

    # Calculate the position to center the popup
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    popup_width = 300
    popup_height = 150
    x = (screen_width - popup_width) // 2
    y = (screen_height - popup_height) // 2
    popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

    popup.resizable(False, False)

    label = tk.Label(popup, text=message, font=("Helvetica", 12))
    label.pack(pady=10)

    ok_button = tk.Button(popup, text="OK", command=popup.destroy)
    ok_button.pack(pady=5)


root = tk.Tk()
root.title("Caesar Cipher")

# Calculate the position to center the main window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 800
window_height = 500
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

frame = tk.Frame(root, bg="white")  # Default background color
frame.place(relx=0.5, rely=0.5, anchor="center")

# Label at the top with "Caesar Cipher"
label_caesar_cipher = tk.Label(frame, text="Caesar Cipher", font=("Helvetica", 18, "bold"), bg="white", fg="black")
label_caesar_cipher.grid(row=0, column=0, columnspan=2, pady=5)

label = tk.Label(frame, text="Enter text:", font=("Helvetica", 14), bg="white", fg="black")
label.grid(row=1, column=0, padx=10, pady=10)

entry = tk.Text(frame, font=("Helvetica", 12), height=8, width=50, borderwidth=2, relief="groove")  # Larger text area
entry.grid(row=1, column=1, padx=10, pady=10)

shift_label = tk.Label(frame, text="Shift value:", font=("Helvetica", 14), bg="white", fg="black")
shift_label.grid(row=2, column=0, padx=10, pady=10)

shift_value = tk.IntVar()
shift_entry = tk.Entry(frame, textvariable=shift_value, font=("Helvetica", 12))
shift_entry.grid(row=2, column=1, padx=10, pady=10)


def show_encryption_info(event=None):
    label_status.config(
        text="Encryption involves shifting each letter in the plaintext by a fixed number of positions down or up the alphabet.",
        bg="black", fg="white")


def show_decryption_info(event=None):
    label_status.config(
        text="Decryption reverses this process by shifting the letters back by the same number of positions.",
        bg="black", fg="white")


def clear_info(event=None):
    label_status.config(text="", bg=root.cget("bg"), fg="black")


encrypt_button = tk.Button(frame, text="Encrypt", command=encrypt, bg="#4CAF50", fg="white", font=("Helvetica", 14))
encrypt_button.grid(row=3, column=0, padx=10, pady=10)
encrypt_button.bind("<Enter>", show_encryption_info)
encrypt_button.bind("<Leave>", clear_info)

decrypt_button = tk.Button(frame, text="Decrypt", command=decrypt, bg="#f44336", fg="white", font=("Helvetica", 14))
decrypt_button.grid(row=3, column=1, padx=10, pady=10)
decrypt_button.bind("<Enter>", show_decryption_info)
decrypt_button.bind("<Leave>", clear_info)

# Center align buttons
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

label_status = tk.Label(root, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
label_status.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()