# PDF to DOCX Converter

Convert PDF files to DOCX format easily using the pdf2docx library.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

To install the pdf2docx library, use pip:

```
pip install pdf2docx
```

## Usage

To convert a PDF file to a DOCX file, follow these steps:

1. Import the Converter class from pdf2docx library:

    ```python
    from pdf2docx import Converter
    ```

2. Create a Converter object by specifying the name of the input PDF file:

    ```python
    cv = Converter("input_file.pdf")
    ```

3. Convert the PDF file to a DOCX file by specifying the name of the output DOCX file:

    ```python
    cv.convert("output_file.docx", start=0, end=None)
    ```

4. Close the Converter object:

    ```python
    cv.close()
    ```
