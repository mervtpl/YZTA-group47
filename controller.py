
from fpdf import FPDF
from PIL import Image
import os
import interface  

def kaydet_pdf():
    story_text = interface.story_box.get("1.0", "end").strip()
    image_path = "output.png"
    output_pdf_path = "output/story_output.pdf"

    if not story_text:
        print("Hikaye metni boş.")
        return
    if not os.path.exists(image_path):
        print(f"Görsel bulunamadı: {image_path}")
        return

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, story_text)

    pdf.ln(10)
    try:
        pdf.image(image_path, x=10, y=pdf.get_y(), w=150)
    except RuntimeError as e:
        print(f"Görsel eklenemedi: {e}")

    os.makedirs(os.path.dirname(output_pdf_path), exist_ok=True)
    pdf.output(output_pdf_path)
    print(f"PDF başarıyla kaydedildi: {output_pdf_path}")
