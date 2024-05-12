import numpy as np

def generate_key_matrix(n):
    print(f"Enter the elements of the {n}x{n} key matrix (row-wise):")
    key_matrix = []
    for i in range(n):
        row = input().split()
        row = [int(num) for num in row]
        key_matrix.append(row)
    key_matrix = np.array(key_matrix)
    return key_matrix

def encrypt(message, key_matrix):
    n = len(key_matrix)
    message = message.lower().replace(" ", "")
    message = ''.join(char for char in message if char.isalpha())  # Remove non-alphabetic characters
    while len(message) % n != 0:
        message += 'x'  # Pad with 'x'
    
    encrypted_text = ""
    for i in range(0, len(message), n):
        vector = np.array([ord(char) - ord('a') for char in message[i:i+n]])
        vector = vector.reshape(n, 1)
        encrypted_vector = np.dot(key_matrix, vector) % 26
        encrypted_text += ''.join(chr(num[0] + ord('a')) for num in encrypted_vector)
    return encrypted_text

def decrypt(encrypted_text, key_matrix):
    n = len(key_matrix)
    det = int(round(np.linalg.det(key_matrix)))
    det_inv = pow(det, -1, 26)
    inverse_key_matrix = np.linalg.inv(key_matrix)
    adjugate = (det * inverse_key_matrix) % 26
    key_matrix_inv = (det_inv * adjugate) % 26
    
    decrypted_text = ""
    for i in range(0, len(encrypted_text), n):
        vector = np.array([ord(char) - ord('a') for char in encrypted_text[i:i+n]])
        vector = vector.reshape(n, 1)
        decrypted_vector = np.dot(key_matrix_inv, vector) % 26
        decrypted_text += ''.join(chr(int(num[0]) + ord('a')) for num in decrypted_vector)
    return decrypted_text

def main():
    #Size of key matrix: 2, Key = 5 8 Enter 17 3
    n = int(input("Enter the size of the key matrix (2 or 3): "))
    if n != 2 and n != 3:
        print("Invalid matrix size. Exiting.")
        return
    
    key_matrix = generate_key_matrix(n)
    message = input("Enter the message to encrypt: ")

    encrypted_text = encrypt(message, key_matrix)
    print("Encrypted text:", encrypted_text)
    
    decrypted_text = decrypt(encrypted_text, key_matrix)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
