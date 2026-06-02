import fitz
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

doc = fitz.open("data/Patient 2.pdf")

page = doc[0]

pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))

img = Image.frombytes(
    "RGB",
    [pix.width, pix.height],
    pix.samples
)

text = pytesseract.image_to_string(img)

print("OCR Text Length:", len(text))
print(text[:2000])