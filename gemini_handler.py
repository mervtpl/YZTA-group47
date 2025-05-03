from google import genai

# API anahtarınızı buraya girin
client = genai.Client(api_key="AIzaSyAmRwflPB5WVKmSKYaj7ZBZ_7o1wCE3h1M")

print("Hangi geri dönüşüm nesnesi ile ilgili hikaye yazılacak ?:")
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

    
