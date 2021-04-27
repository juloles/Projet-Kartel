### Cases ###
from Argent import *
from Boss import *
from Gangster import *

class Case:
    def __init__(self):

        self.case=[" "]


    def affichage(self):

        print (self.case, end=' ')

    def remplir_case(self, personnage, couleur):

        if personnage=="Argent":

            self.case=["€"]

        if personnage=="Boss":

            self.case=["B"]

        if personnage=="1Gangster":

            self.case=["1G"]

        if personnage=="2Gangster":

            self.case=["2G"]

        if personnage=="3Gangster":

            self.case=["3G"]



