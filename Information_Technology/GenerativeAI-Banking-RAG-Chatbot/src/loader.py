import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

def ocr_pdf_to_text_chunks(pdf_path, chunk_size=500, overlap=50):
    doc = fitz.open(pdf_path)
    all_text = []

    for page in doc:
        pix = page.get_pixmap(dpi=300)
        img = Image.open(io.BytesIO(pix.tobytes()))
        text = pytesseract.image_to_string(img)
        all_text.append(text)

    full_text = " ".join(all_text)
    
    # Dividir en chunks
    chunks = []
    for i in range(0, len(full_text), chunk_size - overlap):
        chunk = full_text[i:i+chunk_size]
        chunks.append(chunk)

    print(f"✅ OCR extraído y dividido en {len(chunks)} chunks")
    return chunks
