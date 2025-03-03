"""Méthodes utiles au projet de bibliothèque de film."""

import numpy as np

def sort_movies_by_date(list_of_movies):
    array_movies = np.array([[movie.name, movie.date] for movie in list_of_movies])
    array_sorted = array_movies[array_movies[:, 1].astype(int).argsort()]
    return list(array_sorted)

    pass

def sort_movies_by_name(list_of_movies):
    list_movie_names = [movie.name for movie in list_of_movies]
    return sorted(list_movie_names)

def sort_movies_by_type(list_of_movies, type_of_movie):
    if type_of_movie not in ["vhf", "dvd"]:
        return []
    else:
        list_movies = np.array([movie.name for movie in list_of_movies if movie.type == type_of_movie])
        return list_movies

def clean_data(unclean_list_of_movies):
    clean_list_of_film = []
    for element in unclean_list_of_movies:
        name_date_of_movie = element[0]
        type_of_movie= element[1]
        
        # On extrait les données utiles
        name_of_movie = name_date_of_movie.split(" (")[0]
        date_of_movie = name_date_of_movie.split(" (")[1][:-1]
        date_of_movie = int(date_of_movie)
        type_of_movie = type_of_movie.lower()
        clean_list_of_film.append([name_of_movie, date_of_movie, type_of_movie])
    
    return clean_list_of_film