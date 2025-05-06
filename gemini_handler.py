from google import genai
from dotenv import load_dotenv 
import os
import json


load_dotenv()


key_file_path = os.getenv("GENAI_CREDENTIALS")


with open(key_file_path) as f:
    config = json.load(f)

api_key = config["GENAI_API_KEY"]


client = genai.Client(api_key=api_key)

def generate_story(secim):

    prompt = f"""
    Sen bir çocuk hikayesi anlatıcısısın. {secim} nesnesi bir geri dönüşüm kutusuna atıldıktan sonra başına gelenleri anlatan,
    çocuklara sürdürülebilirlik kavramını öğreten kısa ve eğlenceli bir hikaye yaz.
    Hikaye sade bir dille yazılmış olsun (5-8 yaş arası çocuklara uygun).
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text

