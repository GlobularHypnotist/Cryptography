def generate_playfair_matrix(key):
    # Remove duplicate characters from the key
    key = "".join(dict.fromkeys(key))
    # Remove 'J' from the key and replace with 'I'
    key = key.replace("J", "I")
    # Create the alphabet without 'J'
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    # Generate the playfair matrix
    matrix = []
    for char in key + alphabet:
        if char not in matrix:
            matrix.append(char)
    playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    return playfair_matrix

def find_positions(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return (i, j)

def playfair_encrypt(plaintext, key):
    # Generate the playfair matrix
    matrix = generate_playfair_matrix(key.upper())
    # Preprocess plaintext
    plaintext = plaintext.upper().replace("J", "I")
    plaintext = plaintext.replace(" ", "")
    # Add padding if necessary
    if len(plaintext) % 2 != 0:
        plaintext += "X"
    # Encrypt pairs of characters
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        char1, char2 = plaintext[i], plaintext[i+1]
        row1, col1 = find_positions(matrix, char1)
        row2, col2 = find_positions(matrix, char2)
        if row1 == row2:  # Same row
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
        else:  # Different row and column
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]
    return ciphertext

def playfair_decrypt(ciphertext, key):
    # Generate the playfair matrix
    matrix = generate_playfair_matrix(key.upper())
    # Decrypt pairs of characters
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i+1]
        row1, col1 = find_positions(matrix, char1)
        row2, col2 = find_positions(matrix, char2)
        if row1 == row2:  # Same row
            plaintext += matrix[row1][(col1 - 1) % 5]
            plaintext += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column
            plaintext += matrix[(row1 - 1) % 5][col1]
            plaintext += matrix[(row2 - 1) % 5][col2]
        else:  # Different row and column
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]
    return plaintext

# Prompt the user to enter the key
key = input("Enter the key: ")
# Prompt the user to enter the text to be encrypted or decrypted
plaintext = input("Enter the text: ")
encrypted_text = playfair_encrypt(plaintext, key)
print("Encrypted:", encrypted_text)
decrypted_text = playfair_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)
