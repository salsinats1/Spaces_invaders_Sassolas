"""
27/02/2023
SASSOLAS Stanislas
Ce fichier contient la classe Main qui permet de lancer le jeu
Cette classe possède les méthodes suivantes :
    - __init__ : constructeur de la classe
    - Menu : permet d'afficher le menu du jeu
    - Jeu : permet d'afficher le jeu
    - Gameloop : permet de lancer le jeu
    - deplacement_alien : permet de faire bouger les aliens
    - deplacement_projectile : permet de faire bouger les projectiles
    - collision : permet de détecter les collisions entre les projectiles et les aliens
    - Shoot : permet de tirer un projectile
    - tir_alien : permet aux aliens de tirer

Cette classe est utilisée dans le fichier main1.py

"""


from tkinter import Tk , Button, Label, Frame , Canvas , StringVar
from Spaceship import  Spaceship
from PIL import ImageTk, Image
import Alien1 as Alien
import Projectiles as Projectile
from time import time 
from random import choices , randint , random , choice
import tkinter.font as tkFont

#classe Main qui permet l'initialisation du jeu
class Main:
    #initialisation de la classe
    def __init__(self):       
        #initialisation de la fenetre
        self.fenetre = Tk()

        #titre de la fenetre
        self.fenetre.title("Space Invaders V2")
        #données sur la taille de la fenetre
        self.__largeur = 1500
        self.__hauteur = 650

        #taille de la fenetre 
        self.fenetre.geometry(f"{self.__largeur}x{self.__hauteur}")
        self.fenetre.minsize(self.__largeur, self.__hauteur)
        self.fenetre.config(background="black")
        self.Menu()
        
    #fonction qui permet l'affichage du canevas, des boutons et de commencer le jeu
    def Jeu(self):

        #création d'un bouton pour quitter proprement le jeu 
        self.__bouton1 = Button(self.fenetre, text = "Quitter", command=self.fenetre.destroy, font=40)  # Création du bouton
        self.__bouton1.pack()

        #Initialisation du score + affichage sur le canvas 
        self.__Nouveauscore =StringVar() 
        self.__Nouveauscore.set("Score : 0 ")
        self.__score_Label = Label(self.fenetre , textvariable= self.__Nouveauscore)
        self.__score_Label.pack(side="right")

        #Initialisation de la vie
        self.__Nouvellevie =StringVar() #Initialisation de la variable
        self.__Nouvellevie.set("Vie : 0 ") #on met le nombre de vie à 0
        self.__vie_Label = Label(self.fenetre , textvariable= self.__Nouvellevie) #création du label
        self.__vie_Label.pack(side="right") #affichage du nombre de vie à droite
        #Initialisation du nombre de vie
        self.__Nouvellevie.set("Vie = 3") #on met le nombre de vie à 3
        #Initialisation du score
        self.__Nouveauscore = 0 
        self.__Nouveauscore.set("Score = 0 ") 

    



    # Creation du canevas
        self.__largeurcanva = 1000
        self.__hauteurcanva = 600
        self.__canvas = Canvas(self.fenetre, height=self.__hauteurcanva, width=self.__largeurcanva) # definition de la taille
        self.__canvas.pack(expand=True, fill="both") 
 

    #Creation de l'alien
        largeur_alien = 50
        hauteur_alien = 50

        #Image de l'alien 
        alien=Image.open("./Images/alien.png")

        #Resized de l'alien 
        resized_alien = alien.resize((largeur_alien,hauteur_alien),Image.Resampling.LANCZOS)
        new_alien = ImageTk.PhotoImage(resized_alien) # Nouvelle image bien definie de l'alien 
        self.__LapparenceA = []

        #Création de nos aliens
        self.__nombreennemis = 10 # nombre d'alien voulu
        self.__Lenemis = [] # liste des objets de classe Alien
        nombre_ligne = 3 # nombre de ligne d'ennemis voulu
        self.__cadencedetir = 4 #cadence de tir de l'alien
        positionAY = 35

        for _ in range(nombre_ligne):
            positionAX = 4
            for _ in range(self.__nombreennemis):
                #Création du canvas de l'alien
                self.__Lenemis.append(Calien.Alien(positionAX,positionAY,hauteur_alien,largeur_alien))
                self.__LapparenceA.append(self.__canvas.create_image(positionAX, positionAY , image = new_alien, anchor="nw"))
                positionAX += 55
            positionAY += 55

    #Creation du missile
        self.__Lmissile = [] # liste contenant les objets de la classe missile 
        self.__LapparenceM = [] # liste contenant l'apparence des missiles 
        self.__rechargement = 0 # definition du temps entre chaque tirs du mage
        self.__tirA = 0 # initialisation du temps de rechargement des aliens
    #Définition des parametres du vaisseau
        largeur_vaisseau = 90
        hauteur_vaisseau = 90
        self.__viejoueur= 3
        self.__cadencedetirvaisseau = 0.5

        #Centrage du vaisseau
        positionX = self.__largeurcanva/2 - largeur_vaisseau/2  #quand il apparai il se trouve au centre en bas 
        positionY = self.__hauteurcanva -50 #se trouve en bas 
        self.__joueur = Spaceship(positionX, positionY,hauteur_vaisseau , largeur_vaisseau)

        #Image vaisseau
        vaisseau = Image.open("./Images/Spaceship.png")

        #Resize l'image grace à la methode resize
        resized_vaisseau = vaisseau.resize((largeur_vaisseau,hauteur_vaisseau),Image.Resampling.LANCZOS)

        #Definition du nouveau vaisseau 
        new_vaisseau = ImageTk.PhotoImage(resized_vaisseau)
        self.__apparence = self.__canvas.create_image(positionX, positionY , image = new_vaisseau, anchor="nw")

        #Bind des touches 
        self.fenetre.bind('<KeyPress-Left>', lambda *args : self.key_down(-1))
        self.fenetre.bind('<KeyPress-Right>', lambda *args : self.key_down(1))
        self.fenetre.bind('<KeyPress-q>', lambda *args : self.key_down(-1))
        self.fenetre.bind('<KeyPress-d>', lambda *args : self.key_down(1))
        self.fenetre.bind('<Escape>', self.game_pause)
        self.fenetre.bind('<space>' , self.shot)
        self.__gameloopactif =True


        self.game_loop()

    #méthode permettant de lancer la boucle de jeu
    def game_loop(self):

        #boucle de jeu principale

        while self.__gameloopactif:
            self.fenetre.after(10,self.deplacement()) #apres 10 ms les aliens bougent
            self.fenetre.update_idletasks() #permet affichage 
            self.fenetre.update() # update de l'image apres ses deplacements 
            self.fenetre.after(10,self.tirAlien()) #apres 10 sec un alien tire



    def deplacement_alien(self):
        sens = self.__Lenemis[0].getsensdedeplacement() #determiner le sens de deplacement 
        alienmax = self.__Lenemis[0]
        if sens == 1: # si il va a droite 
            xlim = 0 # position maximum de l'alien 
            for alien in self.__Lenemis:# on cherche celui le plus a droite donc le x le plus élevé
                if alien.getpositionX() >= xlim: # si l'alien le plus a droite 
                    xlim = alien.getpositionX() # xlim prend la valeur de la position x
                    alienmax = alien # l'alien prend la valeur de l'alien le plus a droite 
            
            if alienmax.getpositionX() >= 1250 : # si l'alien le plus a droite depasse 1280 
                for alien in self.__Lenemis:
                    possible = Alien.descendre() # tous les aliens descendent d'une case 

        else:
            xlim=1000
            for alien in self.__Lenemis: 
                if alien.getpositionX() <= xlim: # si l'alien le plus a gauche
                    xlim = alien.getpositionX() # xlim prend la valeur de la position x
                    alienmax = alien # l'alien prend la valeur de l'alien le plus a gauche

            if alienmax.getpositionX() <= 30 : # si l'alien le plus a gauche arrive a 0 
                for alien in self.__Lenemis:
                    alien.descendre() # tous les aliens descendent d'une case  

        for i,val in enumerate(self.__Lenemis): # parcours des aliens 
            val.deplacement() # deplacement des aliens horizontalement 
            self.__canvas.coords(self.__LapparenceA[i] , val.getpositionX() , val.getpositionY()) # affichage des aliens 

    def deplacement_missile(self):
        for i,missile in enumerate(self.__Lmissile): # parcours des missiles
            missile.deplacement() # deplacement des missiles verticalement 
            self.__canvas.coords(self.__LapparenceM[i] , missile.getpositionMX() , missile.getpositionMY(), missile.getpositionMX() + missile.getlargeur() ,missile.getpositionMY() + missile.gethauteur()) # affichage des missiles

    def collision(self):
        for missile in self.__Lmissile: #on parcourt la liste des projectiles
            missileX = missile.getPx()
            missileY = missile.getPy()
            largeurM = missile.getLargeur()
            hauteurM = missile.getHauteur()
            touche = False

            for alien in self.__Lenemis:
                if missileX >= alien.getposition() and missileX <= (alien.getpositionX() + alien.getlargeur()) and missileY >= alien.getpositionY() and missileY <= ( alien.getpositionY() + alien.gethauteur() ) or (missileX+largeurM >= alien.getpositionX() and missileX+largeurM <= alien.getpositionX() + alien.getlargeur() and missileY +hauteurM >= alien.getpositionY() and missileY + hauteurM <= alien.getpositionY() + alien.gethauteur())  :
                    self.__canvas.delete(self.__LapparenceA[self.__Lenemis.index(alien)]) # on cherche l'index de l'alien touché dans la liste de la class alien et on le supprime du canvas
                    self.__LapparenceA.remove(self.__LapparenceA[self.__Lenemis.index(alien)])# idem qu'au dessus mais on le supp de la liste d'affichage
                    self.__Lenemis.remove(alien) # on le supprime de la liste des aliens 
                    touche = True
                    n = random() 
                    
                    self.__score += 100
                    self.__scoreA.set(f"Score = {self.__score}")

    #méthode qui permet aux aliens de tirer
    def tirAlien(self):
        if time() - self.__tirA > self.__cadencedetir: 
            if self.__nombreennemis <= len(self.__Lenemis):
                ListeAlien =self.__Lenemis[:self.__nombreennemis] #Liste qui va contenir tous les aliens les plus en haut
            
            else:
                ListeAlien = self.__Lenemis[:] #Liste qui contient les aliens les plus haut (dans le cas ou il y a moins d'aliens en vie sur une ligne)
            
            for alien in self.__Lenemis : # parcours la liste contenant tous les aliens 
                for alienbas in ListeAlien : # on parcours les aliens les plus bas 
                    if alien.getpositionX() == alienbas.getpositionX() and alien.getpositionY() > alienbas.getpositionY():
                        ListeAlien.append(alien) # on ajoute a la liste vide l'alien le plus en bas 
                        ListeAlien.remove(alienbas)
            nombremaxtir = len(ListeAlien)
            
            if nombremaxtir >= 6:
                nombremaxtir = 5
            nombrealientir = randint(1,nombremaxtir)#prend un nombre aleatoire entre 1 et le nbr d'alien dans la liste 
            Lalientir = choices(ListeAlien , k  = nombrealientir)#Liste alien qui vont tirer 
            
            for alien in Lalientir :
                positiontirX = alien.getpositionX()  #position de la balle 
                positiontirY = alien.getpositionY() + 75  #position de la balle 
                #apparence du missile des aliens 
                self.__LapparenceM.append(self.__canvas.create_oval(positiontirX,positiontirY ,positiontirX+10 , positiontirY+40,width=1 , fill = 'red'))
                self.__Lmissile.append(Cmissile.Missile(positiontirX,positiontirY,10,40))
                self.__tirA = time() #reinitialisation du temps de rechargement


    # méthode qui permet au vaisseau de tirer
    def shoot(self,event):
        if time() - self.__rechargement > self.__cadencedetirvaisseau : 
            positiontirX , positiontirY = self.__joueur.getposition()
            positiontirX = positiontirX +7  #position de la balle 
            positiontirY = positiontirY -35#position de la balle 
            #apparence du missile du vaisseau 
            self.__LapparenceM.append(self.__canvas.create_oval(positiontirX,positiontirY ,positiontirX+10 , positiontirY+40,width=1 , fill = 'blue'))
            self.__Lmissile.append(Projectile.Projectile(positiontirX,positiontirY,10,40,-1))
            self.__rechargement = time() #reinitialisation du temps de rechargement

    """Méthode qui permet l'affichage du menu: ne marche pas donc laissé en commentaire"""
    """
    def Menu(self): 
        #création du menu
        self.__frame = Frame(self.fenetre, bg="black")
        self.__frame.pack(expand=True)

        #création boutton Commencer qui aura comme commande d'appeler la fonction affichage = début du jeu
        self.__bouttonjouer = Button(self.__frame, text = "Commencer", command=self.affichage, font=30)
        self.__bouttonjouer.pack(pady=1)

        while True:
            self.fenetre.update_idletasks() #permet affichage 
            self.fenetre.update()
    """




#On lance le programme
game=Main()