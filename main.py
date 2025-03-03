"""Main file of project"""
from movie import Movie
from bibliotheque import Bibliotheque
from friend import Friend
from network import Network
from utils import clean_data



if __name__ == "__main__":

    films = [
    ("Blade Runner (1982)", "vhf"),
    ("Alien : Le 8ème Passager (1979)", "vhf"),
    ("2001 : L'Odyssée de l'espace (1968)", "VhF"),
    ("Matrix (1999)", "DVD"),
    ("Interstellar (2014)", "dvD"),
    ("L'Empire contre-attaque (1980)", "vhf"),
    ("Retour vers le futur (1985)", "vhf"),
    ("La Guerre des Étoiles (1977)", "vhf"),
    ("L'Armée des 12 singes (1995)", "dVd"),
    ("Terminator 2 : Le Jugement dernier (1991)", "DVD"),
    ]


    friends = [
        ("Paul", "Blade Runner"),
        ("Lucie",),
        ("Zoé", "Terminator 2 : Le Jugement dernier"),
    ]

    clean_data_list = clean_data(films)
    biblio = Bibliotheque()

    # On constitue notre bibliotheque
    for movie_information in clean_data_list:
        movie = Movie(movie_information[0], movie_information[1], movie_information[2])
        biblio.add_movie(movie)

    # On créé notre réseau d'ami
    network=Network()
    for friend_information in friends:
        if len(friend_information)>1:
            (name_friend, borrowed_movie) = friend_information
        else:
            name_friend = friend_information
            borrowed_movie = None


        if borrowed_movie is not None:
            network.add_friend_to_network(Friend(name_friend, borrowed_movie, True))
        else:
            network.add_friend_to_network(Friend(name_friend))

    
    biblio.display_movie_by_type("vhf")




