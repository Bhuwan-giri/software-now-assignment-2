def encrypt_text(shift1, shift2):
    with open("raw_text.txt", "r", encoding="utf-8") as file:
        text = file.read()

    encrypted = ""

    for char in text:
        # Lowercase letters
        if char.islower():
            if 'a' <= char <= 'm':
                shift = shift1 * shift2
                encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif 'n' <= char <= 'z':
                shift = shift1 + shift2
                encrypted += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                encrypted += char

        # Uppercase letters
        elif char.isupper():
            if 'A' <= char <= 'M':
                encrypted += chr((ord(char) - ord('A') - shift1) % 26 + ord('A'))
            elif 'N' <= char <= 'Z':
                shift = shift2 ** 2
                encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted += char

        # Other characters
        else:
            encrypted += char

    with open("encrypted_text.txt", "w", encoding="utf-8") as file:
        file.write(encrypted)
