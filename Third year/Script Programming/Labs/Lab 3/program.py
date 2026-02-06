import modules
from requests.exceptions import RequestException, Timeout


def print_menu():
    print("\n=== OMDb Filmsök (Sprint 3) ===")
    print("1. Sök film via exakt titel (t)")
    print("2. Sök film via del av titel (s)")
    print("3. Visa sökhistorik (endast t-sökningar, senaste 5)")
    print("4. Avsluta")


def read_choice():
    c = input("Välj (1-4): ").strip()
    return c if c in {"1", "2", "3", "4"} else None


def show_movie_brief(m):
    # kortfattad info för exakt titel-sökning
    print("\n--- Resultat ---")
    print(f"Titel: {m.get('titel','')}")
    print(f"År: {m.get('år','')}")
    print(f"Genre: {m.get('genre','')}")
    print(f"Beskrivning: {m.get('beskrivning','')}")
    print(f"imdbID: {m.get('imdbID','')}")


def show_movie_full(m):
    print("\n--- Mer info ---")
    print(f"Titel: {m.get('titel','')}")
    print(f"År: {m.get('år','')}")
    print(f"Genre: {m.get('genre','')}")
    print(f"IMDb rating: {m.get('imdbRating','')}")
    print(f"Regissör: {m.get('regissör','')}")
    print(f"Skådespelare: {m.get('skådespelare','')}")
    print(f"Beskrivning: {m.get('beskrivning','')}")
    print(f"imdbID: {m.get('imdbID','')}")


def main():
    try:
        api_key = modules.API_KEY
    except Exception as e:
        print(f"Konfig-fel: {e}")
        return

    while True:
        print_menu()
        choice = read_choice()
        if choice is None:
            print("Fel: välj 1-4.")
            continue

        if choice == "1":
            title = input("Ange exakt filmtitel: ").strip()
            if not title:
                print("Titel får inte vara tom.")
                continue

            try:
                movie = modules.search_by_exact_title(title, api_key)
                show_movie_brief(movie)

                history = modules.load_history()
                modules.add_to_history(history, movie, limit=5)
                print("(Sparad i sökhistoriken.)")

            except (ValueError, Timeout, RequestException) as e:
                print(f"Fel: {e}")

        elif choice == "2":
            keyword = input("Ange sökord (del av titel): ").strip()
            if not keyword:
                print("Sökord får inte vara tomt.")
                continue

            try:
                hits = modules.search_by_partial_title(keyword, api_key)
                if not hits:
                    print("Inga träffar.")
                    continue

                print("\n--- Träffar ---")
                for i, h in enumerate(hits, start=1):
                    print(f"{i}. {h['titel']} ({h['år']}) [{h['typ']}] - {h['imdbID']}")

                pick = input("Välj nummer för mer info (eller Enter för att gå tillbaka): ").strip()
                if pick == "":
                    continue
                if not pick.isdigit():
                    print("Fel: måste vara en siffra.")
                    continue

                idx = int(pick)
                if idx < 1 or idx > len(hits):
                    print("Fel: numret finns inte i listan.")
                    continue

                imdb_id = hits[idx - 1]["imdbID"]
                details = modules.get_details_by_imdb_id(imdb_id, api_key)
                show_movie_full(details)

            except (ValueError, Timeout, RequestException) as e:
                print(f"Fel: {e}")

        elif choice == "3":
            history = modules.load_history()
            if not history:
                print("\n(Ingen sökhistorik ännu.)")
                continue

            print("\n--- Sökhistorik (senaste 5 t-sökningar) ---")
            for i, m in enumerate(history, start=1):
                print(f"{i}. {m.get('titel','')} ({m.get('år','')}) - {m.get('imdbID','')}")

        elif choice == "4":
            print("Hej då!")
            break


if __name__ == "__main__":
    main()