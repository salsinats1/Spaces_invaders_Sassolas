"""
27/02/2023
SASSOLAS Stanislas
Ce fichier contient la classe Spaceship qui permet de créer un vaisseau
Cette classe possède les attributs suivants :
    - x : position en x du vaisseau
    - y : position en y du vaisseau
    - hauteur : hauteur du vaisseau
    - largeur : largeur du vaisseau
Cette classe possède les méthodes suivantes :
    - __init__ : constructeur de la classe
    - move : permet au vaisseau de se déplacer
    - getposition : retourne la position du vaisseau   
Cette classe est utilisée dans le fichier main1.py
"""


# class Spaceship
class Spaceship:
    def __init__(self, x, y, H , L):
        self.__x=x
        self.__y=y
        self.__Hauteur = H
        self.__Largeur = L

    #fonction qui retourne la position en x du vaisseau
    def getx(self):
        return self.__x

    #fonction qui retourne la position en y du vaisseau
    def gety(self):
        return self.__y
    
    #fonction qui retourne la largeur du vaisseau
    def getLargeur(self):
        return self.__Largeur
    
    #fonction qui retourne la hauteur du vaisseau
    def getHauteur(self):
        return self.__Hauteur

    

    #fonction qui permet au vaisseau de se déplacer suivant direction 
    def move(self,direction):
        speed=10
        if self.__x>=self.__Largeur and direction==-1:
            self.__x+=speed*direction #vitesse de déplacement du vaisseau
        elif self.__x<=1280-self.__Largeur and direction==1:
            self.__x+=speed*direction #vitesse de déplacement du vaisseau
