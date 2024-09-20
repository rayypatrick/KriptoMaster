__Program Kriptografi (Vigenere, Playfair, dan Hill Cipher)__

Ini adalah program kriptografi yang mengimplementasikan tiga algoritma enkripsi dan dekripsi:
- Vigenere Cipher
- Playfair Cipher
- Hill Cipher

__Cara Menjalankan Program__

*Persiapan*
1. Pastikan Anda telah menginstal Python 3 di sistem Anda. Jika belum, Anda bisa mengunduh dan menginstalnya dari python.org.
2. Clone repository ini ke direktori lokal Anda:
   ```bash git clone https://github.com/username/repository-name.git ```
3. Masuk ke folder program:
   ```bash cd QuizKriptografi ```

*Instalasi Dependensi*
Program ini membutuhkan pustaka numpy untuk menjalankan Hill Cipher. Untuk menginstal numpy, jalankan perintah berikut di terminal atau command prompt : 

pip install numpy

*Menjalankan Program*
Setelah dependensi terinstal, Anda bisa menjalankan program dengan perintah berikut:

python main.py

atau jika menggunakan python 3 :

python3 main.py

Ini akan membuka antarmuka GUI di mana Anda dapat memasukkan pesan, kunci, dan memilih metode enkripsi/dekripsi.

*Menggunakan Program*
1. Input Pesan: Masukkan pesan teks yang ingin dienkripsi atau didekripsi.
2. Input Kunci: Masukkan kunci dengan panjang minimal 12 karakter.
3. Pilih Cipher: Pilih metode kriptografi (Vigenere, Playfair, atau Hill).
4. Encrypt: Klik tombol Encrypt untuk mengenkripsi pesan.
5. Decrypt: Klik tombol Decrypt untuk mendekripsi pesan terenkripsi.
6. Simpan dan Buka File: Anda juga dapat membuka file teks untuk dienkripsi atau menyimpan hasil enkripsi ke file teks.

*File - File Utama*
- main.py: Program utama yang menjalankan antarmuka GUI dan menggabungkan cipher.
- vigenere.py: Implementasi algoritma Vigenere Cipher.
- playfair.py: Implementasi algoritma Playfair Cipher.
- hillcipher.py: Implementasi algoritma Hill Cipher dengan matriks 3x3.
