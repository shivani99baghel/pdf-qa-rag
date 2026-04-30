import pdfplumber

def load_pdf_with_pages(file_path):
    docs = []

    with pdfplumber.open(file_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text() or ""
            docs.append({
                "text": text,
                "page": i + 1
            })

    return docs