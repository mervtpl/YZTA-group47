import os
import json
from dotenv import load_dotenv
import vertexai
from vertexai.preview.vision_models import ImageGenerationModel
import google.generativeai as genai

# Ortam değişkenlerini yükle
load_dotenv()

# Gemini API anahtarını JSON dosyasından al
key_file_path = os.getenv("GENAI_CREDENTIALS")
with open(key_file_path) as f:
    config = json.load(f)

api_key = config["GENAI_API_KEY"]
genai.configure(api_key=api_key)

def translate_prompt_to_english(turkish_prompt: str) -> str:
    model = genai.GenerativeModel("gemini-2.0-flash")
    translation_prompt = f'Aşağıdaki cümleyi sadece İngilizce\'ye çevir: "{turkish_prompt}"'
    response = model.generate_content(translation_prompt)

    if not response.text:
        return "An object being recycled into something new."

    return response.text.strip()


def extract_visual_description(turkish_story: str) -> str:
    model = genai.GenerativeModel("gemini-2.0-flash")
    prompt = (
        f"Aşağıdaki hikayeyi oku ve sadece görselle ilgili olan betimleyici cümleleri ayır:\n\n"
        f"{turkish_story}\n\n"
        f"Sadece görselle ilgili kısmı kısa bir paragraf olarak yaz. Yazı, metin, yazılı içerik gibi öğeleri dahil etme."
    )
    response = model.generate_content(prompt)
    return response.text.strip() if response.text else turkish_story



def generate_image(prompt: str, output_path="output.png") -> str:
    project_id = os.getenv("PROJECT_ID")
    location = "us-central1"
    credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

    # Vertex AI'ı başlat
    vertexai.init(project=project_id, location=location)

    visual_desc = extract_visual_description(prompt)
    prompt_en = translate_prompt_to_english(visual_desc)
    prompt_en += " No text, no letters, no writing, only visual description."

    # Görsel üretimi
    model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-002")
    images = model.generate_images(prompt=prompt_en, number_of_images=1)

    if not images:
        return "❌ Görsel üretilemedi."

    image_data = images[0]._image_bytes  # ❗ Gizli alan, Google tarafından desteklenmeyebilir

    with open(output_path, "wb") as f:
        f.write(image_data)

    return f"✅ Görsel başarıyla kaydedildi: {output_path}"
