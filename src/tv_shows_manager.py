import json


class TVShowsManager:
    def __init__(self):
        self.tv_shows = []
        self.db_path = ""

    def load_db(self, db_path: str):
        with open(db_path, "r", encoding="utf-8") as f:
            self.tv_shows = json.load(f)
            self.db_path = db_path

    def find_by_rating(self, rating: int) -> list[dict]:
        shows_by_rating = []
        for show in self.tv_shows:
            if show["rating"] == rating:
                shows_by_rating.append(show)
        return shows_by_rating

    def find_by_genre(self, genre: str) -> list[dict]:
        shows_by_genre = []
        for show in self.tv_shows:
            if show["genre"] == genre:
                shows_by_genre.append(show)
        return shows_by_genre

    def add_show(self, title: str, genre: str, seasons: int, rating: int) -> bool:
        show = {
            "title": title,
            "genre": genre,
            "seasons": seasons,
            "rating": rating
        }
        if show not in self.tv_shows:
            self.tv_shows.append(show)
            return True
        else:
            return False

    def delete_show(self, title: str) -> bool:
        for i in range(len(self.tv_shows)):
            if self.tv_shows[i]["title"] == title:
                del self.tv_shows[i]
                return True
        return False

    def save_db(self, path: str) -> None:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.tv_shows, f, ensure_ascii=False)

    def __str__(self):
        shows = []
        for i in range(len(self.tv_shows)):
            show = (f'{i + 1}. Title: {self.tv_shows[i]["title"]}, '
                    f'Genre: {self.tv_shows[i]["genre"]}, '
                    f'Seasons: {self.tv_shows[i]["seasons"]}, '
                    f'Rating: {self.tv_shows[i]["rating"]}.'
                    )
            shows.append(f"{show}")

        return "\n".join(shows)

    def manage(self):
        while True:
            print("1.display all tv shows  2. find by rating, 3. find by genre, 4. add show,"
                  " 5. delete show, Q. Exit")

            user_choice = input("Select an action:").upper()

            if user_choice not in {"1", "2", "3", "4", "5", "Q"}:
                print("action is not valid, try again")
                continue

            if user_choice == "Q":
                print("manager closing")
                self.save_db(self.db_path)
                break

            if user_choice == "1":
                print(self)

            elif user_choice == "2":
                try:
                    rating = int(input("enter rating: "))
                except ValueError:
                    print("Rating should be integer")
                    continue
                shows_by_rating = self.find_by_rating(rating)
                print(shows_by_rating)

            elif user_choice == "3":
                genre = input("entr genre: ").strip()
                shows_by_genre = self.find_by_genre(genre)
                if not shows_by_genre:
                    print(f"No tv shows with genre: {genre}")
                else:
                    for i, show in enumerate(shows_by_genre):
                        print(f"{i+1}. {show['title']}")

            elif user_choice == "4":
                title = input("enter title: ").strip()
                genre = input("enter genre: ").strip()
                try:
                    season = int(input("enter season: "))
                except ValueError:
                    print("Season should be integer")
                    continue
                try:
                    rating = int(input("enter rating: "))
                except ValueError:
                    print("Rating should be integer")
                    continue
                self.add_show(title, genre, season, rating)
                print(f"Show {title} is added")

            elif user_choice == "5":
                title = input("entr title: ").strip()
                if self.delete_show(title):
                    print(f"Show {title} is deleted")
                else:
                    print(f"Deletion impossible! Show is not found.")
