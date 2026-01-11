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
