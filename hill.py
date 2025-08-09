# Python3 code to implement Hill Cipher Decryption
import numpy as np

def get_key_matrix(key):
    """
    Converts a 4-letter key into a 2×2 matrix.
    """
    return np.array([
        [ord(key[0]) - 65, ord(key[1]) - 65],
        [ord(key[2]) - 65, ord(key[3]) - 65]
    ])

def mod_inverse(key_matrix):
    """
    Computes the modular inverse of a 2×2 key matrix under mod 26.
    """
    determinant = int(round(np.linalg.det(key_matrix))) % 26
    determinant_inv = pow(determinant, -1, 26)  # Modular inverse of determinant

    adj = np.array([
        [key_matrix[1][1], -key_matrix[0][1]],
        [-key_matrix[1][0], key_matrix[0][0]]
    ]) % 26

    return (determinant_inv * adj) % 26

def encrypt(message, key):
    """
    Encrypts the message in 2-letter blocks.
    """
    key_matrix = get_key_matrix(key)
    encrypted_text = ""

    for i in range(0, len(message), 2):
        block = message[i:i+2]


        message_vector = np.array([
            [ord(block[0]) - 65],
            [ord(block[1]) - 65]
        ])

        cipher_vector = np.dot(key_matrix, message_vector) % 26

        for j in range(2):
            encrypted_text += chr(int(cipher_vector[j][0]) + 65)

    return encrypted_text

def decrypt(cipher_text, key):
    """
    Decrypts the encrypted text in 2-letter blocks.
    """
    key_matrix = get_key_matrix(key)
    inv_key_matrix = mod_inverse(key_matrix)
    decrypted_text = ""


    for i in range(0, len(cipher_text), 2):
        block = cipher_text[i:i+2]
        cipher_vector = np.array([
            [ord(block[0]) - 65],
            [ord(block[1]) - 65]
        ])


        decrypted_vector = np.dot(inv_key_matrix, cipher_vector) % 26

        for j in range(2):
            decrypted_text += chr(int(decrypted_vector[j][0]) + 65)

    return decrypted_text


message = "ASTSTKLM"
key = "HILL"

encrypted_message = encrypt(message, key)
decrypted_message = decrypt(encrypted_message, key)

print("Encrypted:", encrypted_message)
print("Decrypted:", decrypted_message)


