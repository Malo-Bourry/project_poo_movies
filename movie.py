class Movie:
    def __init__(self, name, date, type, location="bibliotheque", is_borrowed=False):
        self.name = name
        self.date = date
        self.location = location
        self.type = type
        self.is_borrowed = is_borrowed

    def display_type(self):
        print("Le film {} est un film {}".format(self.name, self.type))

    def display_location(self):
        if self.location == "bibliotheque":
            print("Le livre est rangé dans ma bibliothèque")
        else:
            print("le film est chez {}".format(self.location))