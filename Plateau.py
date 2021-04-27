### Plateau ###
from Case import*
from Prison import*

class Plateau():

    def __init__(self,cases):

        self.nombre_cases=cases

        self.plateau=[' ']*self.nombre_cases

        for i in range (self.nombre_cases):

            self.plateau[i]=Case()




    def afficher(self):

        print("Plateau :", end=' ')

        for i in range(self.nombre_cases):

            self.plateau[i].affichage()



## remplir le plateau de manière aléatoire

    def remplir_plateau(self):

        tableau_personnages=["Argent", "1Gangster", "2Gangster", "2Gangster", "3Gangster", "Boss"]

        tableau_couleur=["R", "Ve", "J", "B", "V", "M", "Ro"]


        for i in range (len(tableau_personnages)):

            for j in range (len(tableau_couleur)):

                    self.plateau[i*7+j].remplir_case(tableau_personnages [i],tableau_couleur[j])
        print("\nPlateau rempli")
        self.afficher()






P=Plateau(43)
P.afficher()
P.remplir_plateau()
