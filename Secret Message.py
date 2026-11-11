def cipher(text, shift, mode):
    result = ""
    if mode == "decrypt":
        shift = -shift
        
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around the alphabet
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            result += char
    return result

msg = input("Enter your secret message: ")
key = int(input("Enter shift key (1-25): "))
action = input("Type 'encrypt' or 'decrypt': ").lower()

output = cipher(msg, key, action)
print(f"\nProcessed Message: {output}")
