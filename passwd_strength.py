password = input("Enter a password to test: ")

upper = lower = digit = special = 0

for char in password:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
    elif char.isdigit():
        digit += 1
    else:
        special += 1

print("\n--- Password Analysis ---")
print(f"Length: {len(password)} | Uppercase: {upper} | Lowercase: {lower} | Digits: {digit} | Special: {special}")

if len(password) >= 8 and upper > 0 and lower > 0 and digit > 0 and special > 0:
    print("Result: STRONG Password!")
elif len(password) >= 6 and (upper > 0 or lower > 0) and digit > 0:
    print("Result: MODERATE Password. Add special characters for better security.")
else:
    print("Result: WEAK Password. Make it longer and mix character types.")
