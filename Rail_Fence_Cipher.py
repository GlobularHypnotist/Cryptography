def encrypt(plaintext, key):
    # Remove spaces from plaintext
    plaintext = plaintext.replace(" ", "")
    # Filling the rail matrix
    rail = [['\n' for i in range(len(plaintext))]
                for j in range(key)]

    # To find the direction
    dir_down = False
    row, col = 0, 0

    for i in range(len(plaintext)):

        # Reverse the direction if we've just filled the top or bottom rail
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down

        # Fill the corresponding alphabet
        rail[row][col] = plaintext[i]
        col += 1

        # Find the next row using direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    # Construct the ciphertext using the rail matrix
    result = []
    for i in range(key):
        for j in range(len(plaintext)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return "".join(result)

def decrypt(ciphertext, key):
    # Filling the rail matrix
    rail = [['\n' for i in range(len(ciphertext))]
                for j in range(key)]

    # To find the direction
    dir_down = None
    row, col = 0, 0

    # Mark the places with '*'
    for i in range(len(ciphertext)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        # Place the marker
        rail[row][col] = '*'
        col += 1

        # Find the next row using direction flag
        if dir_down:
            row += 1
        else:
            row -= 1

    # Construct the rail matrix
    index = 0
    for i in range(key):
        for j in range(len(ciphertext)):
            if ((rail[i][j] == '*') and
            (index < len(ciphertext))):
                rail[i][j] = ciphertext[index]
                index += 1

    # Read the matrix in zig-zag manner to construct plaintext
    result = []
    row, col = 0, 0
    for i in range(len(ciphertext)):

        # Check the direction of flow
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False

        # Place the marker
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1

        # Find the next row using direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    return "".join(result)

# Prompt the user to enter the text to be encrypted or decrypted
plaintext_org = input("\nEnter the plaintext: ")
# Prompt the user to enter the number of rails
key = int(input("Enter the number of rails: "))

ciphertext = encrypt(plaintext_org, key)
print("\nCipher Text is: " + ciphertext)
plaintext = decrypt(ciphertext, key)
print("\nPlain Text is: " + plaintext, "\n")
