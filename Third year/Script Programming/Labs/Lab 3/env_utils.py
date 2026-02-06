from dotenv import load_dotenv
import os

def env_util():
    load_dotenv()
    api_key = os.getenv("API_KEY")

    if not api_key:
        raise ValueError(
            "API-nyckel saknas. Skapa en .env-fil och lägg till:\n"
            "API_KEY=din_api_nyckel"
        )

    return api_key