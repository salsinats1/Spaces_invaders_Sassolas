"""
27/02/2023
SASSOLAS Stanislas
Ce fichier contient la classe Projectile qui permet de créer un projectile
Cette classe possède les attributs suivants :
    - x : position en x du projectile
    - y : position en y du projectile
    - hauteur : hauteur du projectile
    - largeur : largeur du projectile
    - vitesse : vitesse du projectile
    - direction : direction du projectile
Cette classe possède les méthodes suivantes :
    - __init__ : constructeur de la classe
    - getPx : retourne la position en x du projectile
    - getPy : retourne la position en y du projectile
    - getlargeur : retourne la largeur du projectile
    - gethauteur : retourne la hauteur du projectile
    - speed : permet au projectile de se déplacer
Cette classe est utilisée dans le fichier main1.py  
"""





#Classe Projectile
class Projectile:
    def __init__(self,positionPx,positionPy,Largeur,Hauteur,speed=5,direction=1):
        self.__x = positionPx
        self.__y = positionPy
        self.__Largeur = Largeur 
        self.__Hauteur = Hauteur
        self.__vitesse = speed
        self.__direction = direction

    #Fonction qui retourne la position en x du projectile
    def getPx(self):
        return self.__x

    #Fonction qui retourne la position en y du projectile
    def getPy(self):
        return self.__y
    
    #Fonction qui retourne la largeur du projectile
    def getlargeur(self):
        return self.__Largeur

    #Fonction qui retourne la hauteur du projectile
    def gethauteur(self):
        return self.__Hauteur
    
    #Fonction qui permet au projectile de se déplacer
    def speed(self):
        self.__x+= self.__vitesse*self.__direction