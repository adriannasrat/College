import os
import requests
from requests.exceptions import RequestException, Timeout
import env_utils
import json  # needed for history handling

API_KEY = env_utils.env_util()

HISTORY_FILE = "search_history.json"
OMDB_URL = "https://www.omdbapi.com/"

# ---------- History (endast för exakt titel-sökning, t) ----------
def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        return []


def save_history(history):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4, ensure_ascii=False)


def add_to_history(history, movie_obj, limit=5):
    """
    Extra: spara bara senaste 'limit' sökningar.
    Vi sparar bara exakt titel-sökningar (t).
    """
    history.append(movie_obj)
    if len(history) > limit:
        history = history[-limit:]
    save_history(history)
    return history


# ---------- OMDb API calls ----------
def _get(params, api_key):
    params = dict(params)
    params["apikey"] = api_key

    try:
        r = requests.get(OMDB_URL, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
    except Timeout:
        raise Timeout("Timeout: OMDb svarade inte i tid.")
    except RequestException:
        raise RequestException("Nätverksfel: kunde inte kontakta OMDb.")
    except ValueError:
        raise ValueError("Kunde inte tolka svaret från OMDb (ogiltig JSON).")

    if data.get("Response") == "False":
        raise ValueError(data.get("Error", "Okänt fel från OMDb."))
    return data


def search_by_exact_title(title, api_key):
    """
    Sök via exakt titel (t). Returnerar ett 'fullare' filmobjekt (svenska keys).
    """
    data = _get({"t": title, "plot": "short"}, api_key)

    return {
        "titel": data.get("Title", ""),
        "år": data.get("Year", ""),
        "genre": data.get("Genre", ""),
        "beskrivning": data.get("Plot", ""),
        "imdbID": data.get("imdbID", ""),
        "typ": data.get("Type", "")
    }


def search_by_partial_title(keyword, api_key):
    """
    Sök via del av titel (s). Returnerar en lista av träffar (kort info).
    """
    data = _get({"s": keyword}, api_key)
    results = data.get("Search", [])
    hits = []
    for item in results:
        hits.append({
            "titel": item.get("Title", ""),
            "år": item.get("Year", ""),
            "imdbID": item.get("imdbID", ""),
            "typ": item.get("Type", "")
        })
    return hits


def get_details_by_imdb_id(imdb_id, api_key):
    """
    Extra: Hämta mer info om en vald träff via imdbID (i).
    """
    data = _get({"i": imdb_id, "plot": "full"}, api_key)
    return {
        "titel": data.get("Title", ""),
        "år": data.get("Year", ""),
        "genre": data.get("Genre", ""),
        "beskrivning": data.get("Plot", ""),
        "imdbID": data.get("imdbID", ""),
        "typ": data.get("Type", ""),
        "regissör": data.get("Director", ""),
        "skådespelare": data.get("Actors", ""),
        "imdbRating": data.get("imdbRating", "")
    }