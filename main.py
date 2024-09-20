# main.py
import tkinter as tk
from tkinter import filedialog, messagebox
from vigenere import vigenere_encrypt, vigenere_decrypt
from playfair import playfair_encrypt, playfair_decrypt
from hillcipher import hill_encrypt, hill_decrypt
import numpy as np  # Untuk Hill Cipher

def open_file():
    file_path = filedialog.askopenfilename()  # Dialog untuk memilih file
    if file_path:  # Jika pengguna memilih file, lanjutkan
        try:
            with open(file_path, 'r') as file:
                data = file.read()
            input_text.delete("1.0", tk.END)  # Hapus teks yang ada
            input_text.insert(tk.END, data)   # Masukkan data dari file ke dalam text area
        except Exception as e:
            messagebox.showerror("Error", f"Gagal membuka file: {e}")
    else:
        messagebox.showwarning("Warning", "Tidak ada file yang dipilih!")


def save_file(data):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    with open(file_path, 'w') as file:
        file.write(data)

def encrypt_message():
    plaintext = input_text.get("1.0", tk.END).rstrip()
    key = key_entry.get().strip()
    if not plaintext:
        messagebox.showwarning("Warning", "Input pesan tidak boleh kosong!")
        return

    if len(key) < 12:
        messagebox.showerror("Error", "Kunci harus minimal 12 karakter")
        return

    if cipher_var.get() == "Vigenere":
        result = vigenere_encrypt(plaintext, key)
    elif cipher_var.get() == "Playfair":
        result = playfair_encrypt(plaintext, key)
    elif cipher_var.get() == "Hill":
        key_matrix = np.array([[2, 4, 5], [9, 2, 1], [3, 17, 7]])  # Ganti dengan kunci yang valid
        result = hill_encrypt(plaintext, key_matrix)
       # Debugging - Print hasil enkripsi ke konsol untuk memastikan fungsi berfungsi
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

    print(f"Encrypted result: {result}")
    
    # Periksa apakah result kosong
    if result:
        output_text.delete("1.0", tk.END)  # Kosongkan area output
        output_text.insert(tk.END, result)  # Masukkan hasil enkripsi ke output
    else:
        messagebox.showerror("Error", "Enkripsi gagal, tidak ada hasil yang dihasilkan.")

def decrypt_message():
    ciphertext = input_text.get("1.0", tk.END).strip()
    key = key_entry.get().strip()

    if len(key) < 12:
        messagebox.showerror("Error", "Kunci harus minimal 12 karakter")
        return

    if cipher_var.get() == "Vigenere":
        result = vigenere_decrypt(ciphertext, key)
    elif cipher_var.get() == "Playfair":
        result = playfair_decrypt(ciphertext, key)
    elif cipher_var.get() == "Hill":
        key_matrix = np.array([[2, 4, 5], [9, 2, 1], [3, 17, 7]])  # Ganti dengan kunci yang valid
        result = hill_decrypt(ciphertext, key_matrix)

   # Debugging - Print hasil dekripsi ke konsol
    print(f"Decrypted result: {result}")
    
    if result:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)
    else:
        messagebox.showerror("Error", "Dekripsi gagal, tidak ada hasil yang dihasilkan.")

# Setup GUI
window = tk.Tk()
window.title("Kriptografi")

# Input pesan
tk.Label(window, text="Input Pesan:").pack()
input_text = tk.Text(window, height=10, width=50)
input_text.pack()

# Input kunci
tk.Label(window, text="Input Kunci (min 12 karakter):").pack()
key_entry = tk.Entry(window)
key_entry.pack()

# Pilih cipher
cipher_var = tk.StringVar(value="Vigenere")
tk.Radiobutton(window, text="Vigenere", variable=cipher_var, value="Vigenere").pack()
tk.Radiobutton(window, text="Playfair", variable=cipher_var, value="Playfair").pack()
tk.Radiobutton(window, text="Hill", variable=cipher_var, value="Hill").pack()

# Tombol enkripsi dan dekripsi
tk.Button(window, text="Encrypt", command=encrypt_message).pack()
tk.Button(window, text="Decrypt", command=decrypt_message).pack()

# Output pesan
tk.Label(window, text="Output Pesan:").pack()
output_text = tk.Text(window, height=10, width=50)
output_text.pack()

# Tombol buka dan simpan file
tk.Button(window, text="Buka File", command=open_file).pack()
tk.Button(window, text="Simpan File", command=lambda: save_file(output_text.get("1.0", tk.END))).pack()

window.mainloop()