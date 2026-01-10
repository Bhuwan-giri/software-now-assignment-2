def encrypt_text(shift1, shift2):
    with open("raw_text.txt", "r") as f:
        text = f.read()

    encrypted = ""
    key_map = ""

    for ch in text:
        if ch.islower():
            if 'a' <= ch <= 'm':
                shift = shift1 * shift2
                encrypted += chr((ord(ch) - 97 + shift) % 26 + 97)
                key_map += "l1"
            else:
                shift = shift1 + shift2
                encrypted += chr((ord(ch) - 97 - shift) % 26 + 97)
                key_map += "l2"

        elif ch.isupper():
            if 'A' <= ch <= 'M':
                encrypted += chr((ord(ch) - 65 - shift1) % 26 + 65)
                key_map += "u1"
            else:
                shift = shift2 ** 2
                encrypted += chr((ord(ch) - 65 + shift) % 26 + 65)
                key_map += "u2"

        else:
            encrypted += ch
            key_map += "__"

    with open("encrypted_text.txt", "w") as f:
        f.write(encrypted)

    with open("key_map.txt", "w") as f:
        f.write(key_map)


def decrypt_text(shift1, shift2):
    with open("encrypted_text.txt", "r") as f:
        text = f.read()

    with open("key_map.txt", "r") as f:
        key_map = f.read()

    decrypted = ""
    i = 0

    while i < len(text):
        ch = text[i]
        rule = key_map[i*2:i*2+2]

        if rule == "l1":
            shift = shift1 * shift2
            decrypted += chr((ord(ch) - 97 - shift) % 26 + 97)

        elif rule == "l2":
            shift = shift1 + shift2
            decrypted += chr((ord(ch) - 97 + shift) % 26 + 97)

        elif rule == "u1":
            decrypted += chr((ord(ch) - 65 + shift1) % 26 + 65)

        elif rule == "u2":
            shift = shift2 ** 2
            decrypted += chr((ord(ch) - 65 - shift) % 26 + 65)

        else:
            decrypted += ch

        i += 1

    with open("decrypted_text.txt", "w") as f:
        f.write(decrypted)


def verify():
    with open("raw_text.txt", "r") as f1, open("decrypted_text.txt", "r") as f2:
        return f1.read() == f2.read()


def main():
    shift1 = int(input("Enter shift1 value: "))
    shift2 = int(input("Enter shift2 value: "))

    encrypt_text(shift1, shift2)
    decrypt_text(shift1, shift2)

    if verify():
        print("✅ Decryption successful. Files match.")
    else:
        print("❌ Decryption failed. Files do not match.")


main()
