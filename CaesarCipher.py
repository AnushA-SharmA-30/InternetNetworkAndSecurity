# Ceaser
input_text = "string"
encoded = ''
k = 3
def encyp():
    global encoded
    print("------Encrypted----------")
    for ch in input_text:
        encrypted_char = chr((ord(ch) + k) % 256)
        encoded += encrypted_char
    print(encoded)
def decyp():
    print("------Decrypted----------")
    decoded_text = ""
    for ch in encoded:
        decrypted_char = chr((ord(ch) - k) % 256)
        decoded_text += decrypted_char
    print(decoded_text)
print("Original:", input_text)
encyp()
decyp()