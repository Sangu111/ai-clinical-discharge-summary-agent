import fitz
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
)

def read_pdf(pdf_path: str) -> str:

    doc = fitz.open(pdf_path)

    full_text = []

    for page_num in range(len(doc)):

        page = doc[page_num]

        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))

        img = Image.frombytes(
            "RGB",
            [pix.width, pix.height],
            pix.samples
        )

        text = pytesseract.image_to_string(img)

        full_text.append(
            f"\n\n--- PAGE {page_num + 1} ---\n{text}"
        )

        print(f"Processed Page {page_num + 1}/{len(doc)}")

    return "\n".join(full_text)