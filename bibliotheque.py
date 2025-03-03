from utils import sort_movies_by_date, sort_movies_by_name, sort_movies_by_type

class Bibliotheque:
    def __init__(self, list_movie=[]):
        self.list_movie = list_movie
    
    def add_movie(self, movie):
        self.list_movie.append(movie)

    def recover_movie(self, movie):
        self.list_movie.append(movie)

    def display_movie_by_date(self):
        print(sort_movies_by_date(self.list_movie))

    def display_movie_by_name(self):
        print(sort_movies_by_name(self.list_movie))

    def display_movie_by_type(self, type):
        sorted_list = sort_movies_by_type(self.list_movie, type)
        if len(sorted_list)==0:
            print("type de film non reconnu.")
        else:
            print(sorted_list)