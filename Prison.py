### Prison ###
from Case import*

class Prison :

    def __init__(self) :

        self.nombre_de_places = 5
        self.places_libres = 5

        self.prison=[" "]*5

    def affiche_p(self):
        print("Prison :", end=' ')
        print (self.prison)

P = Prison()

P.affiche_p()
