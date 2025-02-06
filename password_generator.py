import random
import string

def generate_password(length=random.randint(8, 10)):
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    
    # Ensure at least one special character
    password = [random.choice(special_chars)]
    
    # Fill the rest with letters and digits
    for _ in range(length - 1):
        character_set = random.choice([letters, digits])
        password.append(random.choice(character_set))
    
    # Shuffle to ensure randomness in character placement
    random.shuffle(password)
    
    return ''.join(password)

# Generate and print one password
print(generate_password())