def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine the character's case (uppercase or lowercase)
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')
            # Apply the shift, wrapping around the alphabet
            shifted = (ord(char) - start + shift) % 26 + start
            result += chr(shifted)
        else:
            # If the character is not alphabetic, leave it unchanged
            result += char
    return result

# Prompt the user to enter the text to be encrypted or decrypted
plaintext = input("Enter the text: ")
# Prompt the user to enter the shift number
shift = int(input("Enter the shift number: "))

encrypted_text = caesar_cipher(plaintext, shift)
print("Encrypted:", encrypted_text)

decrypted_text = caesar_cipher(encrypted_text, -shift)
print("Decrypted:", decrypted_text)