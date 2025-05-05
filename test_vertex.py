from vertex_handler import generate_image
from gemini_handler import response

#print("Hangi ürünün geri dönüşümü?")
#urun=input("Seciminiz:")
#prompt = f"{urun}'in geri dönüşüm yolculuğu"
print(generate_image(response.text))
