### Plateau ###
from Case import*
from Prison import*
from random import*
from Inspecteur import*

class Plateau():

    def __init__(self,cases):

        self.nombre_cases=cases
        self.plateau=[0]*self.nombre_cases
        for i in range (self.nombre_cases):
            self.plateau[i] = Case()


    def afficher(self, posInspecteur = 0):
        print(posInspecteur)
        print(self.plateau[0].affichage())
        print("Plateau :", end=' ')
        if posInspecteur == 0 :
            print (["I"],end=' ')
        else :
            for i in range(posInspecteur - 1):
                self.plateau[i].affichage()



            print(["I"], end=' ')
        '''
        for i in range (len(self.plateau)) :
            if self.plateau[i] == ["I"] :
                self.plateau[i].affichage()
        '''
        for i in range (posInspecteur + 1,len(self.plateau)) :
            self.plateau[i].affichage()


## remplir le plateau de manière aléatoire

    def remplir_plateau(self):

        tableau_personnages=["Argent", "1Gangster", "2Gangster", "2Gangster", "3Gangster", "Boss"]
        tableau_couleur=["Rouge", "Vert", "Jaune", "Bleu", "Violet", "Marron", "Rose"]


        for i in range (len(tableau_personnages)):
            for j in range (len(tableau_couleur)):
                    self.plateau[i*7+j].remplir_case(tableau_personnages [i],tableau_couleur[j])



    def random_plateau(self):
        x = Case()
        c = Case()

        for i in range (0,10000) :
            r1 = randint(0,41)
            r2 = randint(0,41)
            c = self.plateau[r1]
            self.plateau[r1] = self.plateau[r2]
            self.plateau[r2] = c

        self.plateau[42] = x
        self.plateau[42] = self.plateau[0]
        self.plateau[0] = x

        for i in range (len(self.plateau)) :
            if self.plateau[i].case == [' '] :
                self.plateau[i].remplir_case("Inspecteur")

        print("\nPlateau rempli random :")
