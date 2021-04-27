### Plateau ###
from Case import*
from Prison import*

class Plateau():

    def __init__(self,cases):
        self.nombre_cases=cases
        self.plateau=[0]*self.nombre_cases
        for i in range (self.nombre_cases):
            self.plateau[i]=Case()


    def afficher(self):
        print("Plateau :", end=' ')
        for i in range(self.nombre_cases):

            self.plateau[i].affichage()

## remplir le plateau de manière aléatoire




P=Plateau(43)
P.afficher()
