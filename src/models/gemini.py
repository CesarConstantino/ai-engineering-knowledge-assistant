from google import genai
from config import GOOGLE_API_KEY


client = genai.Client(
    api_key=GOOGLE_API_KEY
)


MODEL = "gemini-3.1-flash-lite"


def ask_gemini(history):

    response = client.models.generate_content(
        model=MODEL,
        contents=history
    )

    return response.text