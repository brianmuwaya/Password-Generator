import random
import string

def generate_password(length):
    # Define the possible characters: letters (lowercase & uppercase), digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly select characters from the pool to form the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Set the length of the password
password_length = 12
# Generate and print the password
generated_password = generate_password(password_length)
print(f"Generated Password: {generated_password}")