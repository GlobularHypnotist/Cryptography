def generate_key(plain_text, key):
    key = list(key)
    if len(plain_text) == len(key):
        return key
    else:
        for i in range(len(plain_text) - len(key)):
            key.append(key[i % len(key)])
    return ''.join(key)

def encrypt(plain_text, key):
    cipher_text = ""
    for i in range(len(plain_text)):
        if plain_text[i].isalpha():
            shift = ord(key[i].upper()) - 65
            cipher_text += chr(((ord(plain_text[i].upper()) + shift - 65) % 26) + 65)
        else:
            cipher_text += plain_text[i]
    return cipher_text

def decrypt(cipher_text, key):
    plain_text = ""
    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            shift = ord(key[i].upper()) - 65
            plain_text += chr(((ord(cipher_text[i].upper()) - shift - 65) % 26) + 65)
        else:
            plain_text += cipher_text[i]
    return plain_text

# Example usage:
plain_text = "Hello World"
key = "KEY"
key = generate_key(plain_text, key)
cipher_text = encrypt(plain_text, key)
print("Cipher text:", cipher_text)
decrypted_text = decrypt(cipher_text, key)
print("Decrypted text:", decrypted_text)
