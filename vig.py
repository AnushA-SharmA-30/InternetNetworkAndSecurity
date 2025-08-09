def encrypt_vigenere(plaintext, key): 
    ciphertext = "" 
    key_index = 0  
    for char in plaintext: 
        if char.isalpha():   
            shift = ord(key[key_index]) - ord('A') 
            encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A')) 
            ciphertext += encrypted_char 
            key_index = (key_index + 1) % len(key)  
        else: 
            ciphertext += char  
    return ciphertext 
 
def decrypt_vigenere(ciphertext, key): 
    plaintext = "" 
    key_index = 0  
    for char in ciphertext: 
        if char.isalpha():   
            shift = ord(key[key_index]) - ord('A') 
            decrypted_char = chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A')) 
            plaintext += decrypted_char 
            key_index = (key_index + 1) % len(key)   
        else: 
            plaintext += char   
    return plaintext 
 

plaintext = input("Enter the plaintext: ").upper() 
key = input("Enter the key: ").upper()


ciphertext = encrypt_vigenere(plaintext, key) 
print("\nEncrypted Text:", ciphertext) 
decrypted_text = decrypt_vigenere(ciphertext, key) 
print("Decrypted Text:", decrypted_text)