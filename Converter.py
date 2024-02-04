from pdf2docx import Converter

cv = Converter("pdf_name.pdf")
cv.convert("output_docx_name.docx", start=0, end=None)
cv.close()
