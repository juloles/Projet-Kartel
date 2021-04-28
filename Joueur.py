### Joueur ###
from Inspecteur import*
from De import*
from Prison import*


class Joueur :

    def __init__(self):
        self.points=0
        self.de=De()



    def mouvement(self):

        r=self.de.resultats_de()
        print (r)

        nb_cases=int(input("de combien de cases voulez vous avancer ?"))

        if nb_cases>self.de.resultats_de():

            print ("veuillez choisir un nombre plus petit que le résultat du dé")

            int(input("veuillez entrer votre nouveau choix"))
        return nb_cases
