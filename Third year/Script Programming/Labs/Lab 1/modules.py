import random

filmer = [
    {"titel": "The Matrix", "genre": "Sci-Fi", "beskrivning": "En hacker upptäcker att verkligheten är en simulering."},
    {"titel": "Interstellar", "genre": "Sci-Fi", "beskrivning": "En resa genom rymden för att rädda mänskligheten."},
    {"titel": "Titanic", "genre": "Drama", "beskrivning": "En kärlekshistoria ombord på ett sjunkande skepp."},
    {"titel": "The Pursuit of Happyness", "genre": "Drama", "beskrivning": "En pappa kämpar för ett bättre liv för sin son."},
    {"titel": "The Hangover", "genre": "Comedy", "beskrivning": "En vild utekväll får oväntade konsekvenser."},
    {"titel": "Superbad", "genre": "Comedy", "beskrivning": "Två vänner försöker göra sin sista skoltid minnesvärd."},
]

def get_genres():
    """Returnerar en sorterad lista av unika genrer."""
    return sorted({film["genre"] for film in filmer})

def random_movie_by_genre(chosen_genre):
    """Slumpar en film från vald genre. Returnerar film-dict eller None om ingen finns."""
    matches = [film for film in filmer if film["genre"].lower() == chosen_genre.lower()]
    if not matches:
        return None
    return random.choice(matches)

def guess_movie():
    """Spel: gissa filmen baserat på beskrivning."""
    film = random.choice(filmer)
    print("\nLedtråd:")
    print(f"\"{film['beskrivning']}\"")
    guess = input("Vilken film är det? ").strip()

    if guess.lower() == film["titel"].lower():
        print("Rätt!")
    else:
        print(f"Fel! Rätt svar var: {film['titel']}")

def list_all_movies():
    """Skriver ut alla filmer."""
    print("\nAlla filmer:")
    for i, film in enumerate(filmer, start=1):
        print(f"{i}. {film['titel']} ({film['genre']}) - {film['beskrivning']}")