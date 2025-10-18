import random
import string
def generate_password(lenght, use_uppercase=True, use_numbers=True, use_symbols=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(lenght))
    return password
        
# Ask the user for password settings. Pyton ignores it.
length = int(input("Enter password length: "))
use_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
use_numbers = input("Include numbers? (y/n): ").lower() == "y"
use_symbols = input("Include Symbols? (y/n): ").lower() == "y"

# Generatr and show the password
password = generate_password(length, use_uppercase, use_numbers, use_symbols)
print("Your generated password is:", password)