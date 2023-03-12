"""
27/02/2023
SASSOLAS Stanislas
Ce fichier contient la classe Alien qui permet de créer un alien
Cette classe possède les attributs suivants :
    - positionX : position en x de l'alien
    - positionY : position en y de l'alien
    - hauteur : hauteur de l'alien
    - largeur : largeur de l'alien
    - vitesse : vitesse de déplacement de l'alien
    - direction : sens de déplacement de l'alien
Cette classe possède les méthodes suivantes :
    - __init__ : constructeur de la classe
    - getpositionX : retourne la position en x de l'alien
    - getpositionY : retourne la position en y de l'alien
    - gethauteur : retourne la hauteur de l'alien
    - getlargeur : retourne la largeur de l'alien
    - getvitesse : retourne la vitesse de l'alien
    - getsensdedeplacement : retourne le sens de déplacement de l'alien
    - getvivant : retourne si l'alien est vivant ou non
    - deplacement : permet à l'alien de se déplacer
Cette classe est utilisée dans le fichier main1.py
"""
#Classe Alien
class alien:
    def __init__(self,positionX,positionY,hauteur,largeur,vitesse=3,direction=1):
        self.__positionX = positionX #position de l'alien axe X 
        self.__positionY = positionY # position de l'alien axe Y
        self.__hauteur = hauteur # hauteur de l'alien
        self.__largeur = largeur # largeur de l'alien
        self.__vitesse = vitesse # vitesse de deplacement de l'alien fixé a 5 
        self.__direction = direction # sens de deplacement à droite ou à gauche 

    # les fonctions get permettent de retourner les objets de la classe Alien demandé
    def getpositionX(self): # permet d'obtenir la position X
        return self.__positionX 

    def getpositionY(self): # permet d'obtenir la position Y
        return self.__positionY

    def getlargeur(self): # permet d'obtenir la largeur 
        return self.__largeur

    def gethauteur(self): # permet d'obtenir la hauteur
        return self.__hauteur

    def getvitesse(self):
        return self.__vitesse

    def getsensdedeplacement(self): # permet de connaitre la direction de l'alien
        return self.__direction

    def getvivant(self): # permet de savoir si l'alien est vivant ou non
        return self.__vivant


    #méthode de déplacement de l'alien renvoie aucunes sorties et aucunes entrées
    def deplacement(self):
        # variation de la position sur l'axe X selon le sens et la vitesse
        self.__positionX += self.__vitesse*self.__direction
       
    #méthode qui permet à l'alien de descendre et de changer de sens de deplacement : renvoie un booléen
    def descendre(self):
        # descend de 60 lorsque la fonction est appelée 
        self.__positionY += 50
        self.__sensdedeplacement *= -1 # le sens de deplacement de l'alien change lorsque la fonction est appelée 
        # si l'alien est en bas de l'écran , la fonction renvoie False
        if self.__positionY >= 450 : 
            return False
        return True
    #méthode qui permet de tuer l'alien
    def setvivant(self): 
        self.__vivant = False
    #méthode qui permet d'ajouter de la vitesse à l'alien : renvoie aucunes sorties et une entrée vitesse
    def ajoutvitesse(self, vitesse):
        self.__vitesse = vitesse 
        