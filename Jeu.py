### Jeu ###

from Prison import *
from Plateau import *
from Joueur import *
from Inspecteur import *



class Jeu :

    def __init__ (self) :## ajouter des attributs si besoin
        self.plateau = Plateau(43)
        self.joueur = Joueur()
        self.prison = Prison()
        self.inspecteur = Inspecteur()

## début de partie
    def start (self) :
        self.plateau.remplir_plateau()
        self.plateau.random_plateau()
        self.plateau.afficher()
        self.inspecteur.deplacement(self)
        self.plateau.afficher(self.inspecteur.position)
        self.inspecteur.deplacement(self)

##fin de partie si prison pleine
    def end (self) :
        if self.prison.places_libres() == 0 :
            Quit()

J = Jeu()
J.start()
