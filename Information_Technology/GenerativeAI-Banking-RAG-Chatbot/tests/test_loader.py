from unittest.mock import MagicMock, patch

from src.loader import ocr_pdf_to_text_chunks

PAGE_TEXT = "mortgage terms " * 50  # ~800 chars per page


def _mock_doc(n_pages: int):
    """Fake fitz document: iterable of pages with get_pixmap()."""
    page = MagicMock()
    page.get_pixmap.return_value.tobytes.return_value = b"fake-image-bytes"
    return [page] * n_pages


@patch("src.loader.pytesseract.image_to_string", return_value=PAGE_TEXT)
@patch("src.loader.Image.open", return_value=MagicMock())
@patch("src.loader.fitz.open")
def test_ocr_pdf_to_text_chunks(fitz_open_mock, image_open_mock, ocr_mock):
    """OCR output is chunked with the requested size and overlap."""
    fitz_open_mock.return_value = _mock_doc(n_pages=2)

    chunk_size, overlap = 500, 50
    chunks = ocr_pdf_to_text_chunks("fake.pdf", chunk_size=chunk_size, overlap=overlap)

    # OCR ran once per page
    assert ocr_mock.call_count == 2

    # Chunks respect the max size
    assert all(len(c) <= chunk_size for c in chunks)

    # Consecutive chunks overlap: step is chunk_size - overlap
    full_text = " ".join([PAGE_TEXT, PAGE_TEXT])
    expected_n_chunks = len(range(0, len(full_text), chunk_size - overlap))
    assert len(chunks) == expected_n_chunks

    # No text is lost: chunks reassemble to the full text
    step = chunk_size - overlap
    reassembled = "".join(c[:step] for c in chunks[:-1]) + chunks[-1]
    assert reassembled == full_text


@patch("src.loader.pytesseract.image_to_string", return_value="short")
@patch("src.loader.Image.open", return_value=MagicMock())
@patch("src.loader.fitz.open")
def test_single_short_page_gives_one_chunk(fitz_open_mock, image_open_mock, ocr_mock):
    fitz_open_mock.return_value = _mock_doc(n_pages=1)

    chunks = ocr_pdf_to_text_chunks("fake.pdf", chunk_size=500, overlap=50)

    assert chunks == ["short"]
