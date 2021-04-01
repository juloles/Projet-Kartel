### Joueur ###
from Inspecteur import*
from De import*

class Joueur :

    def __init__(self):
        self.points=0
        self.de=De()



    def mouvement(self):

        for i in range (self.de.resultats_de()):
            print (self.de.resultats_de())
            nb_cases=int(input("de combien de cases voulez vous avancer ?"))
            if nb_cases>self.de.resultats_de():
                print ("veuillez choisir un autre plus petit que le résultat du dé")
