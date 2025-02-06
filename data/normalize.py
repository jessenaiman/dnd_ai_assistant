import re

def normalize_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s+\-]', '', text)  # Keep numbers, spaces, plus, and minus
    return text

# Example usage
print(normalize_text("The Wand of +2 Magic Missiles!"))