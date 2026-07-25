import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# API Key de Google Gemini
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError(
        "No se encontró GOOGLE_API_KEY. "
        "Verifica tu archivo .env"
    )