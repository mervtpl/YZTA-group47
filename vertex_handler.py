import os
from dotenv import load_dotenv
import vertexai
from vertexai.preview.vision_models import ImageGenerationModel
import google.generativeai as genai

# Ortam değişkenlerini yükle
load_dotenv()

# Gemini API anahtarını yükle
genai.configure(api_key="AIzaSyAmRwflPB5WVKmSKYaj7ZBZ_7o1wCE3h1M")


def translate_prompt_to_english(turkish_prompt: str) -> str:
    model = genai.GenerativeModel("gemini-2.0-flash")
    translation_prompt = f'Aşağıdaki cümleyi sadece İngilizce\'ye çevir: "{turkish_prompt}"'
    response = model.generate_content(translation_prompt)

    if not response.text:
        return "An object being recycled into something new."

    return response.text.strip()


def generate_image(prompt: str, output_path="output.png") -> str:
    project_id = os.getenv("PROJECT_ID")
    location = "us-central1"
    credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

    # Vertex AI'ı başlat
    vertexai.init(project=project_id, location=location)

    # Prompt'u İngilizce'ye çevir
    prompt_en = translate_prompt_to_english(prompt)


    # Görsel üretimi
    model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-002")
    images = model.generate_images(prompt=prompt_en, number_of_images=1)

    if not images:
        return "❌ Görsel üretilemedi."

    image_data = images[0]._image_bytes  # ❗ Gizli alan, Google tarafından desteklenmeyebilir

    with open(output_path, "wb") as f:
        f.write(image_data)

    return f"✅ Görsel başarıyla kaydedildi: {output_path}"
