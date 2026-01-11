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
