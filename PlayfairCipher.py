# Playfair Cipher
def create_playfair_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # 'J' is replaced with 'I'
    key = "".join(dict.fromkeys(key.upper().replace("J", "I") + 
alphabet))  # Remove duplicates
    return [list(key[i:i+5]) for i in range(0, 25, 5)]
def find_position(matrix, char):
    for row in range(5):
        if char in matrix[row]:
            return row, matrix[row].index(char)
def process_playfair(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    if len(text) % 2 != 0:
        text += "X"
    return text
def playfair(text, key, mode='encrypt'):
    matrix = create_playfair_matrix(key)
    text = process_playfair(text)
    result = []
    shift = 1 if mode == 'encrypt' else -1
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:
            result.append(matrix[row1][(col1 + shift) % 5])
            result.append(matrix[row2][(col2 + shift) % 5])
        elif col1 == col2:
            result.append(matrix[(row1 + shift) % 5][col1])
            result.append(matrix[(row2 + shift) % 5][col2])
        else:
            result.append(matrix[row1][col2])
            result.append(matrix[row2][col1])
    return "".join(result)
 # Example usage
plaintext = "HELLOBrother"
key = "KEYWORD"
encrypted = playfair(plaintext, key, mode='encrypt')
decrypted = playfair(encrypted, key, mode='decrypt')
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)