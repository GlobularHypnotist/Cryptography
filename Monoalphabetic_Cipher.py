def generate_key():
    import random
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shuffled_alphabet = list(alphabet)
    random.shuffle(shuffled_alphabet)
    return "".join(shuffled_alphabet)

def encrypt(plaintext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_text = ""
    for char in plaintext:
        if char in alphabet:
            index = alphabet.index(char)
            encrypted_text += key[index]
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(ciphertext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decrypted_text = ""
    for char in ciphertext:
        if char in key:
            index = key.index(char)
            decrypted_text += alphabet[index]
        else:
            decrypted_text += char
    return decrypted_text

# Prompt the user to enter the text to be encrypted or decrypted
plaintext = input("Enter the text: ")
# Randomly generated key
key = generate_key()

print("Original Key:", "abcdefghijklmnopqrstuvwxyz")
print("Generated Key:", key)

encrypted_text = encrypt(plaintext, key)
print("Encrypted Text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, key)
print("Decrypted Text:", decrypted_text)
