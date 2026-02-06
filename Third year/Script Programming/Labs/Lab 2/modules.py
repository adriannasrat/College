import csv
import json
import os

CSV_FILE = "movies_labb2.csv"
JSON_FILE = "movies_labb2.json"


def load_movies_from_csv():
    movies = []
    with open(CSV_FILE, newline="", encoding="utf-8-sig") as f:  # utf-8-sig tar bort BOM
        reader = csv.DictReader(f, delimiter=";")

        for row in reader:
            # Normalisera keys (tar bort spaces runt headers)
            row = { (k or "").strip(): (v or "").strip() for k, v in row.items() }

            titel = row.get("titel", "")
            genre = row.get("genre", "")
            beskrivning = row.get("beskrivning", "")

            if titel:
                movies.append({
                    "titel": titel,
                    "genre": genre,
                    "beskrivning": beskrivning
                })
    return movies

def load_movies_from_json():
    if not os.path.exists(JSON_FILE):
        return []
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        return []

def save_movies_to_json(movies):
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(movies, f, indent=4, ensure_ascii=False)


def save_movies_to_csv(movies):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["titel", "genre", "beskrivning"]
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        for m in movies:
            writer.writerow({
                "titel": m.get("titel", ""),
                "genre": m.get("genre", ""),
                "beskrivning": m.get("beskrivning", "")
            })


def ensure_json_initialized_from_csv():
    if os.path.exists(JSON_FILE):
        return
    movies = load_movies_from_csv()
    save_movies_to_json(movies)


def list_movies(movies):
    if not movies:
        print("\n(Inga filmer i JSON-filen ännu.)")
        return
    print("\nFilmer i JSON:")
    for i, m in enumerate(movies, start=1):
        print(f"{i}. {m.get('titel','')} ({m.get('genre','')}) - {m.get('beskrivning','')}")

def add_movie(movies, titel, genre, beskrivning):
    movies.append({
        "titel": titel.strip(),
        "genre": genre.strip(),
        "beskrivning": beskrivning.strip()
    })

def remove_movie_by_index(movies, index_1_based):
    if index_1_based < 1 or index_1_based > len(movies):
        raise ValueError("Index utanför listan.")
    movies.pop(index_1_based - 1)