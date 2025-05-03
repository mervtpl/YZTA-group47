from vertex_handler import generate_image

print("Hangi ürünün geri dönüşümü?")
urun=input("Seciminiz:")
prompt = f"{urun}'in geri dönüşüm yolculuğu"
print(generate_image(prompt))
