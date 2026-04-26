import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def sayHello():
    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents="Saludo corto"
    )
    print(response.text)
