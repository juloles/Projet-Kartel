### Cases ###
from Argent import *
from Boss import *
from Gangster import *

class Case:

    def __init__(self):
        self.case=[" "]

    def affichage(self):
        print (self.case, end=' ')

    def remplir_case(self, personnage=None, couleur=None):

        if personnage=="Argent":
            self.case=["€ " + couleur]

        if personnage=="Boss":
            self.case=["B " + couleur]

        if personnage=="1Gangster":
            self.case=["1G " + couleur]

        if personnage=="2Gangster":
            self.case=["2G " + couleur]

        if personnage=="3Gangster":
            self.case=["3G " + couleur]

        if personnage=="Inspecteur" :
            self.case= ["I"]
