import random
import string

def generate_random_password(length=12):
    # Define the pool of characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage: Generate a password of length 16
password = generate_random_password(16)
print("Generated Password:", password)
