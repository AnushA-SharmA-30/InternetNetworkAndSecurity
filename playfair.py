
def create_playfair(key):
    key = key.lower().replace(" ", "").replace("j", "i")
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    seen = set()
    playfair_square = []

    for char in key + alphabet:
        if char not in seen:
            seen.add(char)
            playfair_square.append(char)
    print(playfair_square)
    return playfair_square



def create_digraphs(text):
    Digraphs=[]
    i=0
    while i<len(text):
        if i+1==len(text):
            text+='x'
        if text[i+1]==text[i]:
            st=text[i]+'x'
            i+=1
        else:
            st=text[i:i+2]
            i+=2
        Digraphs.append(st)
    return Digraphs



def playfair_encrypt(plaintext, key):
   
    playfair_square = create_playfair(key)
    digraphs = create_digraphs(plaintext)
    ciphertext = ""

    for digraph in digraphs:
        a, b = playfair_square.index(digraph[0]), playfair_square.index(digraph[1])
        row_a, col_a = a // 5, a % 5
        row_b, col_b = b // 5, b % 5

        if row_a == row_b:  
            col_a = (col_a + 1) % 5
            col_b = (col_b + 1) % 5
        elif col_a == col_b:  
            row_a = (row_a + 1) % 5
            row_b = (row_b + 1) % 5
        else: 
            col_a, col_b = col_b, col_a

        ciphertext += playfair_square[row_a * 5 + col_a] + playfair_square[row_b * 5 + col_b]

    return ciphertext



def playfair_decrypt(ciphertext, key):
    
    playfair_square = create_playfair(key)
    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        a, b = playfair_square.index(ciphertext[i]), playfair_square.index(ciphertext[i + 1])
        row_a, col_a = a // 5, a % 5
        row_b, col_b = b // 5, b % 5

        if row_a == row_b:  
            col_a = (col_a - 1) % 5
            col_b = (col_b - 1) % 5
        elif col_a == col_b: 
            row_a = (row_a - 1) % 5
            row_b = (row_b - 1) % 5
        else: 
            col_a, col_b = col_b, col_a

        plaintext += playfair_square[row_a * 5 + col_a] + playfair_square[row_b * 5 + col_b]

    return plaintext.rstrip('x') 


plaintext = "sathhwiksttt"
key = "Key"

encrypted_text = playfair_encrypt(plaintext, key)
print("Encrypted Text:", encrypted_text)

decrypted_text = playfair_decrypt(encrypted_text, key)
print("Decrypted Text:", decrypted_text)
