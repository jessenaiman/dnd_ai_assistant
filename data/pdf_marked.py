import pdfplumber
from markdownify import markdownify
import os

def pdf_to_markdown(pdf_path, md_path):
    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        markdown_content = ""

        # Iterate through each page of the PDF
        for page_num, page in enumerate(pdf.pages, start=1):
            print(f"Processing page {page_num}...")
            
            # Extract text from the page
            text = page.extract_text()

            # If no text was extracted, continue to next page
            if not text:
                print(f"No text found on page {page_num}.")
                continue

            # Optionally, you can add a page break or header for clarity
            markdown_content += f"\n\n# Page {page_num}\n\n"
            
            # Append the extracted text to the markdown content
            markdown_content += text + "\n"

    # Write the markdown content to the output file
    with open(md_path, 'w', encoding='utf-8') as md_file:
        md_file.write(markdown_content)

    print(f"Markdown file saved to {md_path}")

# Example usage
current_dir = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(current_dir, "glossary.pdf")  # Path to your input PDF file
md_path = os.path.join(current_dir, "output.md")     # Path where you want to save the Markdown file

pdf_to_markdown(pdf_path, md_path)