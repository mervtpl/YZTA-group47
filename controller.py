from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        pass
    def footer(self):
        pass


def kaydet_pdf(story_text):
    image_path = "output.png"
    output_pdf_path = "output/story_output.pdf"
    font_path = "fonts/DejaVuSans.ttf"

    if not story_text:
        print("Hikaye metni boş.")
        return False
    if not os.path.exists(image_path):
        print(f"Görsel bulunamadı: {image_path}")
        return False
    if not os.path.exists(font_path):
        print(f"Yazı tipi bulunamadı: {font_path}")
        return False

    try:
        pdf = PDF()
        pdf.add_page()
        pdf.add_font("DejaVu", "", font_path, uni=True)
        pdf.set_font("DejaVu", size=12)
        pdf.multi_cell(0, 10, story_text)

        # Sayfada resim için yeterli yer yoksa yeni sayfa ekle
        remaining_height = pdf.h - pdf.get_y() - 10
        if remaining_height < 100:
            pdf.add_page()

        pdf.image(image_path, x=10, y=pdf.get_y(), w=150)

        os.makedirs(os.path.dirname(output_pdf_path), exist_ok=True)
        pdf.output(output_pdf_path)
        print(f"PDF başarıyla kaydedildi: {output_pdf_path}")
        return True
    except Exception as e:
        print(f"PDF kaydedilirken hata oluştu: {e}")
        return False
