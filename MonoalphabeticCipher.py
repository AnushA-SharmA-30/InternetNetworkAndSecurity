 # Monoalphabetic Cipher
import string
alphabet = list(string.ascii_lowercase)
key = alphabet[::-1]  # Reverse the alphabet for the key
def cipher(text):
    return ''.join(key[alphabet.index(char)] if char in alphabet else 
char for char in text)
def decipher(text):
    return ''.join(alphabet[key.index(char)] if char in key else char 
for char in text)
msg = input("Enter your message: ")
cypher_text = cipher(msg)
print("Cipher:", cypher_text)
plain_text = decipher(cypher_text)
print("Plaintext:", plain_text)