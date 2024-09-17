import json


class TVShowsManager:
    def __init__(self):
        self.tv_shows = []

    def load_db(self, db_path: str):
        with open(db_path, "r") as f:
            self.tv_shows = json.load(f)

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
