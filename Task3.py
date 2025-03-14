import random
import string

def generate_password(length):
    # Define the character sets for password complexity
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets based on complexity
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure the password includes at least one character from each set
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length with random choices from all characters
    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    # Convert the list to a string
    return ''.join(password)

def main():
    # Prompt the user for the desired password length
    try:
        length = int(input("Enter the desired length of the password (minimum 4): "))
        if length < 4:
            print("Password length must be at least 4 characters.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Generate and display the password
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()