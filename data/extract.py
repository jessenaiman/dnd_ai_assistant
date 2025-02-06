import json
import os
import logging
from pdf2image import convert_from_path
import pytesseract
import re
from PIL import Image
import tempfile

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def clean_text(text):
    """Clean and normalize text."""
    if not text:
        return ""
    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text)
    # Remove leading/trailing whitespace
    return text.strip()

def extract_glossary_terms(text):
    """
    Extract terms and definitions from text.
    Looks for patterns like "TERM - definition" or "Term - definition"
    """
    # Split by newlines first
    lines = text.split('\n')
    terms = []
    
    for line in lines:
        line = clean_text(line)
        if not line or len(line) < 3:  # Skip empty or very short lines
            continue
            
        # Try to split on " - " or "- " or " -"
        for separator in [" - ", "- ", " -"]:
            if separator in line:
                parts = line.split(separator, 1)
                if len(parts) == 2:
                    term = clean_text(parts[0])
                    definition = clean_text(parts[1])
                    
                    # Only add if both term and definition are non-empty
                    if term and definition and len(term) > 1:
                        terms.append({
                            "term": term,
                            "definition": definition,
                            "original_line": line
                        })
                        logger.info(f"Found term: {term}")
                        break  # Found a valid separator, no need to try others
    
    return terms

def extract_text_from_pdf_to_json(pdf_path, output_json_path):
    """
    Extracts glossary terms from a PDF file using OCR and saves them as a JSON file.

    Args:
        pdf_path (str): The file path to the PDF document from which text will be extracted.
        output_json_path (str): The file path where the extracted text will be saved as a JSON file.

    Returns:
        bool: True if extraction was successful, False otherwise
    """
    try:
        # Convert to absolute paths
        pdf_path = os.path.abspath(pdf_path)
        output_json_path = os.path.abspath(output_json_path)
        
        logger.info(f"Attempting to read PDF from: {pdf_path}")
        
        if not os.path.exists(pdf_path):
            logger.error(f"PDF file not found at: {pdf_path}")
            return False

        all_terms = []
        
        # Create a temporary directory for the images
        with tempfile.TemporaryDirectory() as temp_dir:
            logger.info("Converting PDF to images...")
            # Convert PDF to images with higher DPI for better OCR
            images = convert_from_path(pdf_path, dpi=300)
            logger.info(f"Successfully converted PDF. Number of pages: {len(images)}")
            
            # Process each page
            for i, image in enumerate(images):
                logger.info(f"Processing page {i + 1}...")
                
                # Increase contrast to make text more visible
                image = image.point(lambda x: 0 if x < 128 else 255)
                
                # Perform OCR with specific configuration
                custom_config = r'--oem 3 --psm 6'
                text = pytesseract.image_to_string(image, config=custom_config)
                
                if not text.strip():
                    logger.warning(f"Page {i + 1} appears to be empty")
                    continue
                
                # Extract terms from this page
                page_terms = extract_glossary_terms(text)
                
                # Add page number to each term
                for term in page_terms:
                    term["page_number"] = i + 1
                
                all_terms.extend(page_terms)
        
        # Create the output data structure
        extracted_data = {
            "glossary": all_terms,
            "metadata": {
                "total_terms": len(all_terms),
                "source_file": pdf_path
            }
        }
        
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_json_path), exist_ok=True)
        
        # Write the JSON file with proper formatting
        with open(output_json_path, 'w', encoding='utf-8') as json_file:
            json.dump(extracted_data, json_file, indent=2, ensure_ascii=False)
            logger.info(f"Successfully wrote {len(all_terms)} terms to: {output_json_path}")
        
        # Print some sample terms
        if all_terms:
            logger.info("\nSample of extracted terms:")
            for term in all_terms[:3]:
                logger.info(f"Term: {term['term']}")
                logger.info(f"Definition: {term['definition']}")
                logger.info("---")
        
        return True
        
    except Exception as e:
        logger.error(f"Error during PDF extraction: {str(e)}")
        return False

if __name__ == "__main__":
    # Use absolute paths relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(script_dir, "glossary.pdf")
    output_path = os.path.join(script_dir, "extracted_text.json")
    
    success = extract_text_from_pdf_to_json(pdf_path, output_path)
    if success:
        logger.info("PDF extraction completed successfully")
    else:
        logger.error("PDF extraction failed")
