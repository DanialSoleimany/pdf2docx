from pdf2docx import Converter

cv = Converter("input_file.pdf")
cv.convert("output_file.docx", start=0, end=None)
cv.close()
