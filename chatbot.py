import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

import database

load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

CONFIG = types.GenerateContentConfig(
    system_instruction="You're a friendly assistant focused on programming questions.",
    temperature=1,
    max_output_tokens=750,
    top_p=0.8,
)

def sayHello():
    response = client.models.generate_content(
        model = "gemini-3-flash-preview", 
        contents = "Short greeting",
        config = CONFIG
    )
    return response.text

def conversation(prompt):
    database.save_message(
        "usuario",  #Sender
        prompt,     #Prompt
        database.get_next_number() #Number of the message
    )

    #Brings up the last 3 messages, including the last one
    history = database.get_last_messages(limit=6)

    #Convert the history into the format required by Gemini
    contents = []
    for msg in history:
        role = "user" if msg["remitente"] == "usuario" else "model"
        contents.append(
            types.Content(
                role=role,
                parts=[types.Part(text=msg["mensaje"])]
            )
        )


    #Call the model 
    response = client.models.generate_content(
        model = "gemini-3-flash-preview", 
        contents = contents,
        config = CONFIG
    )
    answer = response.text

    #Save response in the database
    database.save_message("modelo", answer, database.get_next_number() + 1)

    return answer