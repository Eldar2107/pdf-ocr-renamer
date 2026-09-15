import os
import re
import shutil
import warnings
import pymupdf  # PyMuPDF
import easyocr

# Lazımsız warning-ləri gizlədirik
warnings.filterwarnings("ignore")

print("OCR Modeli yüklənir (CPU Rejimi)...")
reader = easyocr.Reader(['en'], gpu=False)


def extract_text_from_scanned_pdf(pdf_path):
    """Skan olunmuş PDF səhifələrini şəkilə çevirib EasyOCR ilə oxuyur."""
    full_text = ""
    try:
        doc = pymupdf.open(pdf_path)
        for page in doc:
            # 300 DPI keyfiyyətdə şəkilə çeviririk
            pix = page.get_pixmap(dpi=300)
            img_bytes = pix.tobytes("png")

            # EasyOCR ilə mətni oxuyuruq
            results = reader.readtext(img_bytes, detail=0)
            full_text += " ".join(results) + "\n"

        doc.close()
    except Exception as e:
        print(f"OCR xətası ({os.path.basename(pdf_path)}): {e}")

    return full_text


def parse_barcode_and_date(text):
    barcode = None
    date_str = None

    clean_text = text.upper()

    # 1. BARKOD REGEX (Örnək: COR107710, AIL102012, AIP108836, COR112773)
    barcode_match = re.search(r'\b([A-Z]{3}\d{6})\b', clean_text)
    if barcode_match:
        barcode = barcode_match.group(1)
    else:
        # OCR xətalarını (O -> 0, I/L -> 1, Z -> 2) təmizləyən alternativ regex
        alt_barcode = re.search(r'\b((?:COR|AIL|AIP|XXX)[0-9OILZ]{6})\b', clean_text)
        if alt_barcode:
            raw_bc = alt_barcode.group(1)
            digits = raw_bc[3:].replace('O', '0').replace('I', '1').replace('L', '1').replace('Z', '2')
            barcode = raw_bc[:3] + digits

    # 2. TARİX REGEX (DD.MM.YYYY, DD/MM/YYYY, DD-MM-YYYY)
    date_match = re.search(r'\b(\d{2}[\.\/-]\d{2}[\.\/-]\d{3,4})\b', text)
    if date_match:
        raw_date = date_match.group(1)
        formatted_date = raw_date.replace('.', '-').replace('/', '-')
        parts = formatted_date.split('-')

        if len(parts) == 3:
            day, month, year = parts
            if len(year) == 3:  # Nümunə: 202 -> 2026
                year = year
            date_str = f"{day.zfill(2)}-{month.zfill(2)}-{year}"

    final_barcode = barcode if barcode else "UNKNOWN"
    final_date = date_str if date_str else "xx-xx-xxxx"

    return final_barcode, final_date


def process_and_sort_pdfs(source_folder, destination_root):
    if not os.path.exists(source_folder):
        print(f"Mənbə qovluq tapılmadı: {source_folder}")
        return

    os.makedirs(destination_root, exist_ok=True)

    files = [f for f in os.listdir(source_folder) if f.lower().endswith('.pdf')]
    print(f"\nToplam {len(files)} skan olunmuş PDF faylı emal edilir...\n")

    for file_name in files:
        old_path = os.path.join(source_folder, file_name)

        if not os.path.isfile(old_path):
            continue

        text = extract_text_from_scanned_pdf(old_path)
        barcode, date_str = parse_barcode_and_date(text)

        # test2 daxilində barkod adına uyğun qovluq yaradırıq
        barcode_folder = os.path.join(destination_root, barcode)
        os.makedirs(barcode_folder, exist_ok=True)

        new_file_name = f"{barcode} {date_str}.pdf"
        new_path = os.path.join(barcode_folder, new_file_name)

        # Eyni adlı fayl olduqda sıranı qorumaq
        counter = 1
        base_name = f"{barcode} {date_str}"
        while os.path.exists(new_path):
            new_file_name = f"{base_name}_({counter}).pdf"
            new_path = os.path.join(barcode_folder, new_file_name)
            counter += 1

        try:
            shutil.move(old_path, new_path)
            print(f"Uğurlu: '{file_name}' -> 'test2/{barcode}/{new_file_name}'")
        except Exception as e:
            print(f"Xəta ({file_name}): {e}")


if __name__ == "__main__":
    source_folder = r"C:\Users\user\Desktop\test1"
    destination_root = r"C:\Users\user\Desktop\test2"
    process_and_sort_pdfs(source_folder, destination_root)  
