# PDF Barcode and Date Renamer

This Python script automatically extracts text from scanned PDF documents using **PyMuPDF** and **EasyOCR**, parses specific barcodes and dates using Regular Expressions (RegEx), and renames the files accordingly.

## Features
- **OCR Processing:** Converts PDF pages to 300 DPI images and extracts text using EasyOCR (runs on CPU).
- **Smart Barcode Extraction:** Searches for specific barcode patterns and corrects common OCR reading errors (e.g., `O` to `0`, `I` to `1`).
- **Date Parsing:** Detects and standardizes dates in formats like `DD.MM.YYYY`, `DD/MM/YYYY`, and `DD-MM-YYYY`.
- **Safe Renaming:** Renames files to `BARCODE DATE.pdf` and handles duplicates automatically with a counter (`_(1)`, `_(2)`).

## Requirements
- Python 3.8+
- PyMuPDF
- EasyOCR

## Installation & Usage
1. Clone the repository:
   ```bash
   git clone [https://github.com/Eldar2107/pdf-ocr-renamer.git](https://github.com/Eldar2107/pdf-ocr-renamer.git)
   cd pdf-ocr-renamer
