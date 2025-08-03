def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == "encrypt":
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == "decrypt":
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

def main():
    print("=== Caesar Cipher Program ===")
    mode = input("Choose mode: encrypt or decrypt: ").strip().lower()

    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")
        return

    message = input("Enter your message: ")
    
    try:
        shift = int(input("Enter shift value (integer): "))
    except ValueError:
        print("Shift must be an integer.")
        return

    output = caesar_cipher(message, shift, mode)
    print(f"\nResult: {output}")

if __name__ == "__main__":
    main()
