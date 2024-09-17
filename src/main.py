# from matrix_analysis import MatrixAnalysis as ma
from tv_shows_manager import TVShowsManager

matrix = [
    [3, 2, 2],
    [-1, 4, -1, 8],
    [3, 8, 2, -2]
]


# print(ma.min(matrix))
# print(ma.sum(matrix))
# print(ma.mod(matrix))

manager = TVShowsManager()
manager.load_db("src/tv_shows_db.json")

manager.delete_show("Comedy Central")
manager.add_show("Fallout", "action", 1, 8)
manager.add_show("Кухня", "комедия", 5, 7)
manager.save_db("src/tv_shows_db.json")
# print(manager.tv_shows)
# print(manager.find_by_rating(7))
# print(manager.find_by_genre("Fantasy"))
