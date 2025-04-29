import numpy as np
def mod_inverse_matrix(matrix, mod=26):
    """Compute the modular inverse of a matrix under modulo 26."""
    det = int(round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, mod)
    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int) % mod
    return (det_inv * adjugate) % mod
def hill_cipher_encrypt(plaintext, key_matrix):
    n = len(key_matrix)
    plaintext = plaintext.upper().replace(" ", "")
    if len(plaintext) % n != 0:
        plaintext += "X"  # Padding with 'X' if necessary
    plaintext_vector = [ord(char) - ord('A') for char in plaintext]
    ciphertext = ""
    for i in range(0, len(plaintext_vector), n):
        block = plaintext_vector[i:i + n]
        result = np.dot(key_matrix, block) % 26
        ciphertext += "".join(chr(num + ord('A')) for num in result)
    return ciphertext
def hill_cipher_decrypt(ciphertext, key_matrix):
    n = len(key_matrix)
    key_matrix_inv = mod_inverse_matrix(key_matrix, 26)
    ciphertext_vector = [ord(char) - ord('A') for char in ciphertext]
    plaintext = ""
    for i in range(0, len(ciphertext_vector), n):
        block = ciphertext_vector[i:i + n]
        result = np.dot(key_matrix_inv, block) % 26
        plaintext += "".join(chr(num + ord('A')) for num in result)
    return plaintext
 # Example 2x2 key matrix
key_matrix = np.array([[3, 3], [2, 5]])
plaintext = "HELLO"
ciphertext = hill_cipher_encrypt(plaintext, key_matrix)
print("Encrypted:", ciphertext)
decrypted_text = hill_cipher_decrypt(ciphertext, key_matrix)
print("Decrypted:", decrypted_text)