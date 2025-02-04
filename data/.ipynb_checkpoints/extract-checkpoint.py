import PyPDF2

# Open the PDF file
with open("players_handbook.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    
    # Initialize an empty string to store the text
    full_text = ""
    
    # Loop through each page and extract text
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        full_text += page.extract_text()

# Print the extracted text
print(full_text[:500])  # Print the first 500 characters to check
