from PyPDF2 import PdfReader #pip install PyPDF2

reader = PdfReader("zadost_prijeti.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"
print(text)
