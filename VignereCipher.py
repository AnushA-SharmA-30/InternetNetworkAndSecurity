 # Vigneere
def vigenere_cipher(text, key):
    key = key.upper()
    result = []
    key_index = 0
    for char in text.upper():
        if char.isalpha():
            shift = (ord(key[key_index]) - ord('A')) * 1
            result.append(chr((ord(char) - ord('A') + shift) % 26 + 
ord('A')))
            key_index = (key_index + 1) % len(key)
        else:
            result.append(char)
    return ''.join(result)
def vigenere_Dcipher(text, key):
    key = key.upper()
    result = []
    key_index = 0
    for char in text.upper():
        if char.isalpha():
            shift = (ord(key[key_index]) - ord('A')) * -1
            result.append(chr((ord(char) - ord('A') + shift) % 26 + 
ord('A')))
            key_index = (key_index + 1) % len(key)
        else:
            result.append(char)
    return ''.join(result)
 # Example usage
plaintext = "HELLO"
key = "KEY" 
encrypted = vigenere_cipher(plaintext, key )
decrypted = vigenere_Dcipher(encrypted, key)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
