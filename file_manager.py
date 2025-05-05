# file_manager.py

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import os
from datetime import datetime

class FileManager:
    def __init__(self, output_dir="output"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def save_pdf(self, story_text, image_path=None, filename=None):
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"story_{timestamp}.pdf"

        output_path = os.path.join(self.output_dir, filename)

        c = canvas.Canvas(output_path, pagesize=A4)
        width, height = A4

        # Hikaye metni
        text_object = c.beginText(50, height - 50)
        text_object.setFont("Helvetica", 12)
        for line in story_text.split('\n'):
            text_object.textLine(line)
        c.drawText(text_object)

        # Resmi ekle (varsa)
        if image_path and os.path.exists(image_path):
            try:
                image = ImageReader(image_path)
                img_width, img_height = image.getSize()
                aspect = img_height / float(img_width)

                max_width = width - 100
                max_height = height / 2

                if img_width > max_width:
                    img_width = max_width
                    img_height = img_width * aspect

                if img_height > max_height:
                    img_height = max_height
                    img_width = img_height / aspect

                x = (width - img_width) / 2
                y = 100
                c.drawImage(image, x, y, width=img_width, height=img_height)
            except Exception as e:
                print(f"Resim yüklenemedi: {e}")

        c.showPage()
        c.save()

        return output_path  # PDF dosya yolunu döndürür

    def save_txt(self, story_text, image_path=None, filename=None):
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"story_{timestamp}.txt"

        output_path = os.path.join(self.output_dir, filename)

        try:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(story_text)
                if image_path:
                    f.write("\n\n---\nİlgili görsel: " + image_path)
            return output_path  # TXT dosya yolunu döndürür
        except Exception as e:
            print(f"TXT dosyası kaydedilemedi: {e}")
            return None
