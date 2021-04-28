### Inspecteur ###
from Joueur import *

class Inspecteur :

    def __init__ (self) :    ## mettre des attributs
        self.position = 0

    def deplacement (self, J) :
        jeu = J
        self.position = self.position + jeu.joueur.mouvement()          ## en fonction du choix du joueur
        print(self.position)
