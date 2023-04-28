# pdf_encryption.py

from PyPDF2 import PdfReader, PdfWriter
reader = PdfReader("D:/**/**/**/**.PDF")

writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

writer.encrypt("20230428")

with open("D:/**/**/**/**_sec.PDF", "wb") as f:
    writer.write(f)