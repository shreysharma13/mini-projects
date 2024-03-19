import pdfplumber
import os
directory = "/Users/shreysharma/Downloads"
filename = "transactions.pdf"
pdf_path = os.path.join(directory, filename)
with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
print(text)

