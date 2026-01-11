from encrypt import encrypt_text
from decrypt import decrypt_text


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
