from google import genai
from dotenv import load_dotenv
import os

# .env dosyasını yükle
load_dotenv()

# Ortam değişkeninden API anahtarını al
api_key = os.getenv("GENAI_API_KEY")

# Google Generative AI istemcisini başlat
client = genai.Client(api_key=api_key)

print("Hangi geri dönüşüm nesnesi ile ilgili hikaye yazılacak?:")
print(" ")
secim = input("Seçiminiz: ")

prompt = f"""
Sen bir çocuk hikayesi anlatıcısısın. {secim} nesnesi bir geri dönüşüm kutusuna atıldıktan sonra başına gelenleri anlatan,
çocuklara sürdürülebilirlik kavramını öğreten kısa ve eğlenceli bir hikaye yaz.
Hikaye sade bir dille yazılmış olsun (5-8 yaş arası çocuklara uygun).
"""

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt
)

print("\n📖 Hikayen:\n")
print(response.text)
