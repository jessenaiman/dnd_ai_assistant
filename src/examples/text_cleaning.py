import re

def clean_text(text):
    """
    Example of basic text cleaning for 2e AD&D text:
      - Lowercase conversion
      - Removal of special characters (keeping only alphanumeric, spaces, hyphens)

    Args:
        text (str): The raw text to clean.

    Returns:
        str: The cleaned text.
    """
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s\-]+', '', text)
    return text

# Example usage
raw_text = "The *Wand of +2 Fireballs* is a powerful artifact!"
cleaned_text = clean_text(raw_text) 
print(f"Raw Text: {raw_text}")
print(f"Cleaned Text: {cleaned_text}") 
