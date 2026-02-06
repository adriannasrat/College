import modules


def read_choice():
    choice = input("\nVälj ett alternativ (1-6): ").strip()
    if choice not in {"1", "2", "3", "4", "5", "6"}:
        return None
    return choice


def prompt_nonempty(prompt_text):
    while True:
        value = input(prompt_text).strip()
        if value:
            return value
        print("Får inte vara tomt. Försök igen.")


def main():
    # Läs CSV -> spara JSON (initial import om JSON saknas)
    try:
        modules.ensure_json_initialized_from_csv()
    except FileNotFoundError:
        print("Hittar ingen fil. Kontrollera att filen finns i projektmappen.")
        return
    except Exception as e:
        print(f"Ett fel uppstod vid initiering: {e}")
        return

    while True:
        # 2) Ladda alltid senaste JSON-status vid varje menyvarv (så 'Visa alla' alltid är aktuell)
        movies = modules.load_movies_from_json()

        print("\n=== FILMSPEL (Sprint 2) ===")
        print("1. Visa alla filmer (från JSON)")
        print("2. Lägg till ny film (i JSON)")
        print("3. Ta bort film (i JSON)")
        print("4. Spara JSON till CSV (uppdatera CSV)")
        print("5. Läs in filmer från CSV och spara i JSON (import/återställ)")
        print("6. Avsluta")

        choice = read_choice()
        if choice is None:
            print("Fel: välj 1-6.")
            continue

        if choice == "1":
            modules.list_movies(movies)

        elif choice == "2":
            titel = prompt_nonempty("Titel: ")
            genre = prompt_nonempty("Genre: ")
            beskrivning = prompt_nonempty("Beskrivning: ")
            modules.add_movie(movies, titel, genre, beskrivning)
            modules.save_movies_to_json(movies)
            print("Film tillagd i JSON.")

        elif choice == "3":
            modules.list_movies(movies)
            if not movies:
                continue

            while True:
                pick = input("Skriv numret på filmen du vill ta bort: ").strip()
                if not pick.isdigit():
                    print("Fel: du måste skriva en siffra. Försök igen.")
                    continue
                try:
                    idx = int(pick)
                    modules.remove_movie_by_index(movies, idx)
                    modules.save_movies_to_json(movies)
                    print("Film borttagen från JSON.")
                    break
                except ValueError:
                    print("Fel: numret finns inte i listan. Försök igen.")

        elif choice == "4":
            # spara JSON -> CSV
            try:
                modules.save_movies_to_csv(movies)
                print("CSV uppdaterad från JSON.")
            except Exception as e:
                print(f"Kunde inte skriva till CSV: {e}")

        elif choice == "5":
            try:
                csv_movies = modules.load_movies_from_csv()
                modules.save_movies_to_json(csv_movies)
                print("Import klar: CSV läst och JSON uppdaterad.")
            except FileNotFoundError:
                print("Hittar inte movies.csv.")
            except Exception as e:
                print(f"Ett fel uppstod: {e}")

        elif choice == "6":
            print("Hej då!")
            break


if __name__ == "__main__":
    main()