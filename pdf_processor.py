import pdfplumber
import pytesseract
from PIL import Image
import os

def load_pdf(file_path):
    """Load PDF file and return page texts."""
    texts = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            texts.append(page.extract_text())
    return texts

def perform_ocr(image_path):
    """Perform OCR on the given image and return extracted text."""
    text = pytesseract.image_to_string(Image.open(image_path))
    return text

def process_images_from_pdf(file_path):
    """Extract images from PDF, perform OCR and return extracted texts."""
    texts = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            images = page.images
            for img in images:
                img_path = os.path.join('temp_images', f'image_{img[0]}.png')
                with Image.open(img_path) as img_obj:
                    ocr_text = perform_ocr(img_path)
                    texts.append(ocr_text)
    return texts

# Example usage
# pdf_texts = load_pdf('example.pdf')
# ocr_result = process_images_from_pdf('example.pdf')
