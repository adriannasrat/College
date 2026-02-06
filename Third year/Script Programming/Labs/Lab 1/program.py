import modules

def read_menu_choice():
    """Enkel felhantering för menyval."""
    choice = input("\nVälj ett alternativ (1-4): ").strip()
    if choice not in {"1", "2", "3", "4"}:
        return None
    return choice

def handle_random_tip():
    genres = modules.get_genres()

    while True:
        print("\nVälj genre:")
        for i, g in enumerate(genres, start=1):
            print(f"{i}. {g}")

        pick = input("Skriv numret på genren: ").strip()
        if not pick.isdigit():
            print("Fel: du måste skriva en siffra.")
            return

        idx = int(pick)
        if idx < 1 or idx > len(genres):
            print("Fel: ogiltigt val.")
            continue

        chosen_genre = genres[idx - 1]
        film = modules.random_movie_by_genre(chosen_genre)
        if film is None:
            print("Hittade ingen film i den genren.")
        else:
            print(f"Dagens filmtips ({chosen_genre}): {film['titel']}")
        break

def main():
    while True:
        print("\n=== FILMSPEL (Sprint 1) ===")
        print("1. Få ett slumpmässigt filmförslag")
        print("2. Gissa filmen utifrån handling")
        print("3. Visa alla filmer")
        print("4. Avsluta")

        choice = read_menu_choice()
        if choice is None:
            print("Fel: välj 1-4.")
            continue

        if choice == "1":
            handle_random_tip()
        elif choice == "2":
            modules.guess_movie()
        elif choice == "3":
            modules.list_all_movies()
        elif choice == "4":
            print("Hej då!")
            break

if __name__ == "__main__":
    main()