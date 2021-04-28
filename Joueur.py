### Joueur ###

from De import*
from Prison import*


class Joueur :

    def __init__(self):
        self.points=0
        self.de=De()



    def mouvement(self):

        r=self.de.resultats_de()
        print ("\n",r)

        nb_cases=int(input("de combien de cases voulez vous avancer ?"))

        while nb_cases>self.de.resultats_de():

            print ("Veuillez choisir un nombre plus petit que le résultat du dé")
            nb_cases = int(input("Veuillez entrer votre nouveau choix"))

        return nb_cases
