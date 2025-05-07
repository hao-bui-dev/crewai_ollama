import fitz  # PyMuPDF

def extract_page_text(pdf_path, page_number):
    doc = fitz.open(pdf_path)
    if not (1 <= page_number <= len(doc)):
        raise ValueError("Page number out of range.")
    return doc[page_number - 1].get_text()
