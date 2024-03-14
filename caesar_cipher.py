def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    choice = input("Enter 'e' to encrypt or 'd' to decrypt: ")
    if choice.lower() == 'e':
        plaintext = input("Enter the text to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_text = encrypt(plaintext, shift)
        print("Encrypted text:", encrypted_text)
    elif choice.lower() == 'd':
        ciphertext = input("Enter the text to decrypt: ")
        shift = int(input("Enter the shift value: "))
        decrypted_text = decrypt(ciphertext, shift)
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
   

