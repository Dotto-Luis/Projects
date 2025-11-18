from io import BytesIO

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from backend.utils import extract_text_from_pdf


def generate_pdf_bytes():
    # Create a BytesIO object to hold the PDF data
    pdf_buffer = BytesIO()

    # Create a canvas object
    c = canvas.Canvas(pdf_buffer, pagesize=letter)

    # Define the text to draw
    text = "Hello, World!"

    # Set the font and size
    c.setFont("Helvetica", 12)

    # Draw the text at coordinates (100, 100)
    c.drawString(100, 100, text)

    # Save the PDF content to the BytesIO buffer
    c.save()

    # Get the PDF content from the buffer
    pdf_buffer.seek(0)

    return pdf_buffer


# Call the function to generate PDF bytes
pdf_bytes = generate_pdf_bytes()

# Now you can use pdf_bytes as needed, for example, save it to a file, send it over the network, etc.


def test_extract_text_from_pdf():
    pdf_bytes = generate_pdf_bytes()
    assert extract_text_from_pdf(pdf_bytes).strip() == "Hello, World!"
