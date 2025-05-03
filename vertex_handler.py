import os
from dotenv import load_dotenv
from vertexai.preview.vision_models import ImageGenerationModel
import vertexai

# Ortam değişkenlerini yükle
load_dotenv()

def generate_image(prompt: str, output_path="output.png") -> str:
    project_id = os.getenv("PROJECT_ID")
    location = "us-central1"
    credentials = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials
    vertexai.init(project=project_id, location=location)

    # Kararlı sürümü kullan
    model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-002")
    images = model.generate_images(prompt=prompt, number_of_images=1)

    # ✅ GİZLİ ALAN: _image_bytes
    image_data = images[0]._image_bytes

    # Görseli kaydet
    with open(output_path, "wb") as f:
        f.write(image_data)

    return f"Görsel başarıyla kaydedildi: {output_path}"