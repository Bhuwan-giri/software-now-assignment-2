def decrypt_text(shift1, shift2):
    with open("encrypted_text.txt", "r", encoding="utf-8") as file:
        text = file.read()

    decrypted = ""

    for char in text:
        # Lowercase letters
        if char.islower():
            if 'a' <= char <= 'm':
                shift = shift1 * shift2
                decrypted += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            elif 'n' <= char <= 'z':
                shift = shift1 + shift2
                decrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                decrypted += char

        # Uppercase letters
        elif char.isupper():
            if 'A' <= char <= 'M':
                decrypted += chr((ord(char) - ord('A') + shift1) % 26 + ord('A'))
            elif 'N' <= char <= 'Z':
                shift = shift2 ** 2
                decrypted += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted += char

        # Other characters
        else:
            decrypted += char

    with open("decrypted_text.txt", "w", encoding="utf-8") as file:
        file.write(decrypted)
