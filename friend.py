class Friend:
    def __init__(self, name, borrowed_movie=False, has_a_movie=False):
        self.name = name
        self.borrowed_movie = borrowed_movie
        self.has_a_movie = has_a_movie

    def borrow_movie(self, movie, bibliotheque):
        if self.has_a_movie is True:
            # Un ami ne peut pas m'emprunter un film si il en a déjà un
            print("{} m'a déjà emprunté le film {}, il ne peut pas en emprunter un deuxieme en même temps".format(self.name, self.borrowed_movie))
        else:
            if movie in bibliotheque.liste_movie:
                self.borrowed_movie = movie
                self.has_a_movie = True
                bibliotheque.list_movie = [element for element in bibliotheque.list_movie if element != movie]
            else:
                print("le film {} demandé n'est pas présente dans ma bibliothèque".format(movie.name))
    
    def return_movie(self, bibliotheque):
        if self.has_a_movie is False:
            print("il n'y a aucun film a retourner.")
        else:
            bibliotheque.recover_movie(self.borrowed_movie)
            self.borrowed_movie = False
            self.has_a_movie = False

