import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))


def sayHello():
    response = client.models.generate_content(
        model = "gemini-3-flash-preview", 
        contents = "Short greeting",
        config = types.GenerateContentConfig(
            system_instruction = "You´re a friendly assistant, who might be asked about proggramming questions.",
            temperature = 1,
            max_output_tokens = 100,
            top_p = 0.8,
        )
    )
    return response.text

def conversation(prompt):
    response = client.models.generate_content(
        model = "gemini-3-flash-preview", 
        contents = "Make sure to give a short and direct answer(less than 750 tokens). This is the prompt: " + prompt,
        config = types.GenerateContentConfig(
            system_instruction = "You´re a friendly assistant, who might be asked about proggramming questions.",
            temperature = 1,
            max_output_tokens = 750,
            top_p = 0.8,
        )
    )
    return response.text
