def load_data(file_path):
    """
    Example of loading text data from a file.

    Args:
        file_path (str): The path to the text file.

    Returns:
        str: The content of the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    return data

# Example usage
file_path = "../data/raw/example_rulebook_section.txt" # Adjust path if needed
text_data = load_data(file_path)
print(text_data)
