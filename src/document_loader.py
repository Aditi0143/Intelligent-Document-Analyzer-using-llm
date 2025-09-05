import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import docx
import os



pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def load_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def load_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join([p.text for p in doc.paragraphs])

def load_image(file_path):
    image = Image.open(file_path)
    return pytesseract.image_to_string(image)

def load_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def load_document(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    ext = os.path.splitext(file_path)[-1].lower()

    if not ext:
        raise ValueError("No file extension found. Please provide a valid file path with an extension.")

    if ext == ".pdf":
        return load_pdf(file_path)
    elif ext == ".docx":
        return load_docx(file_path)
    elif ext == ".txt":
        return load_txt(file_path)
    elif ext in [".png", ".jpg", ".jpeg"]:
        return load_image(file_path)
    else:
        raise ValueError(f"Unsupported file format: '{ext}'")
