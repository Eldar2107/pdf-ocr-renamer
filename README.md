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
# Smart PDF Barcode & Date Organizer 📂🤖

Bu Python skripti skan olunmuş (şəkil formatındakı) PDF sənədlərini süni intellekt əsaslı **OCR (Optical Character Recognition)** vasitəsilə oxuyur, içindən **barkod** və **tarix** məlumatlarını `regex` ilə aşkarlayır, ardından faylları avtomatik olaraq müvafiq barkod adlarına uyğun qovluqlara çeşidləyib köçürür.

---

## 🚀 Əsas Özəlliklər

* **Yüksək Keyfiyyətli Skan:** `PyMuPDF` vasitəsilə səhifələri 300 DPI keyfiyyətində şəkilə çevirir.
* **Süni İntellektlə Oxuma:** `EasyOCR` istifadə edərək şəkillərdəki mətnləri tanıyır (CPU rejimində işləyir).
* **Ağıllı Barkod Axtarışı:** Standart barkodları (`3 hərf + 6 rəqəm`) tapır və OCR xətalarını (`O` -> `0`, `I/L` -> `1`, `Z` -> `2`) avtomatik düzəldir.
* **Tarix Standartlaşdırması:** Müxtəlif tarix formatlarını (`DD.MM.YYYY`, `DD/MM/YYYY`) tapıb `DD-MM-YYYY` formatına çevrir.
* **Avtomatik Qovruqlama (Yeni!):** Faylları sadəcə adlandırmır, həm də təyinat qovluğunda (`destination_root`) hər barkod üçün ayrıca qovluq açıb ora daşıyır (`shutil.move`).
* **Dublikat Qoruması:** Eyni adla fayl mövcud olduqda silinmənin qarşısını almaq üçün sonuna sıra nömrəsi əlavə edir (`_(1)`, `_(2)`).

---

## 📦 Tələb Olunan Kitabxanalar

Proqramı işlətmək üçün aşağıdakı kitabxanaları quraşdırmalısınız:

```bash
pip install pymupdf easyocr
