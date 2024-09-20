# hillcipher.py
import numpy as np

def mod_inv(matrix, mod):
    det = int(np.round(np.linalg.det(matrix)))  # Determinan dari matriks
    det_inv = pow(det, -1, mod)  # Cari invers modulo determinan
    matrix_modulus_inv = (det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % mod) % mod
    return matrix_modulus_inv

def hill_encrypt(plaintext, key_matrix):
    plaintext = plaintext.replace(" ", "").upper()
    if len(plaintext) % 3 != 0:
        while len(plaintext) % 3 != 0:
            plaintext += "X"
    
    plaintext_vector = [ord(char) - 65 for char in plaintext]
    plaintext_matrix = np.array(plaintext_vector).reshape(-1, 3)
    
    encrypted_matrix = (np.dot(plaintext_matrix, key_matrix) % 26)
    encrypted_text = ''.join([chr(num + 65) for row in encrypted_matrix for num in row])
    
    return encrypted_text

def hill_decrypt(ciphertext, key_matrix):
    ciphertext_vector = [ord(char) - 65 for char in ciphertext]
    ciphertext_matrix = np.array(ciphertext_vector).reshape(-1, 3)
    
    inverse_key_matrix = np.linalg.inv(key_matrix).astype(int) % 26
    decrypted_matrix = (np.dot(ciphertext_matrix, inverse_key_matrix) % 26)
    decrypted_text = ''.join([chr(num + 65) for row in decrypted_matrix for num in row])
    
    return decrypted_text