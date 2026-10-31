"""Read documents into plain text (FR-1.3, FR-1.4).

Sprint 1: pasted text. PDF reading is included for the evaluation runner;
PDF upload in the app arrives in Sprint 4 (CPA-43).
"""


def read_pdf_bytes(data):
    """Return (text, error). error = 'no_extractable_text' for scanned PDFs."""
    import io
    from pypdf import PdfReader
    reader = PdfReader(io.BytesIO(data))
    text = "\n".join((p.extract_text() or "") for p in reader.pages).strip()
    return (text, None) if text else ("", "no_extractable_text")


def read_file(path):
    """Return (text, error) for a .txt or .pdf file on disk."""
    if path.lower().endswith(".pdf"):
        with open(path, "rb") as f:
            return read_pdf_bytes(f.read())
    with open(path, encoding="utf-8") as f:
        return f.read(), None
