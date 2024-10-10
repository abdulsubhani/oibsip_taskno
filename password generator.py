import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_symbols=True):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    symbols = string.punctuation if use_symbols else ''
    
    # Combine all selected characters
    all_characters = lowercase + uppercase + numbers + symbols
    
    if not all_characters:
        raise ValueError("At least one character set must be selected.")

    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

# Example usage
if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    
    password = generate_password(length, use_uppercase, use_numbers, use_symbols)
    print(f"Generated password: {password}")
