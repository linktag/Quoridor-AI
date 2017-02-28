# coding: latin-1

"""

Projet Quoridor par Romain
Debut� le 23/01/2017 � 16h58

Objectif : R�aliser un jeu de Quoridor parfaitement fonctionel et jouable � deux joueurs.
R�aliser une IA a plusieurs niveau de difficult�.
L'IA utilisera pour r�fl�chir un algorithme MinMax am�lior� (Negamax) ansi qu'une am�lioration Alpha Beta
Afin d'optimiser le temps que mettra l'IA a jouer, la selection des coups est jou�s est effectuer dans un ordre pr�cis afin de limiter 
les calculs inutiles.


Ce projet sera effectu� en POO afin de grandement simplifier et la comprehension du code, la lisibilit� et la simplicit�

"""

#IMPORTATION
import tkinter as tk
from math import floor
from copy import deepcopy



#CLASSES UTILISEES

class Plateau:
    """
    Classe contenant le plateau de jeu. C'est lui qui poss�de les diff�rentts tableau avec les positions des barri�res, ainsi que les
    coordonn�es de la position de chaque joueur

    Les coordonn�es des jouers sont contenues dans une variables c_joueurs, d'index 0 pour celle du joueur 1 ett d'index 1 pour celle du joueur 2

    Les barri�res verticales et horizontales sont contenues dans un tableau de dimension en fonction de sa direction
    """

    #CONSTRUCTEUR
    def __init__(self):
        #On creer les joueurs et leurs coordonn�es
        self.c_joueurs = [[4,8],[4,0]]

        #Leur barri�res
        self.nbBarriere = [10,10]

        #Creation du tableau contenant les barri�res verticales et les barri�res horizontales
        #On creer aussi les tableau contenant les barri�res interdites
        self.barrieresHorizontales = []
        self.barrieresHorizontalesInterdites = []
        self.barrieresVerticales = []
        self.barrieresVerticalesInterdites = []
        for k in range(8):
            self.barrieresVerticales.append([0]*8)
            self.barrieresVerticalesInterdites.append([0]*8)
            self.barrieresHorizontales.append([0]*8)
            self.barrieresHorizontalesInterdites.append([0]*8)


    #METHODES

    #Methode renvoyant les coordon�es du joueur demand�
    def CoordonneeJoueur(self, numeroJoueur):
        return self.c_joueurs[numeroJoueur-1]


class Joueur:

    """
    Classe de base d'un joueur jouant au jeu. Elle contient toutes les fonctions communes � tous les joueurs.
    Le joueur par d�faut exprimer par cettte classe est humain
    Elle contient toutes les actions que peut effectuer le joueur, notament la fonction jouer, qui atttend une interaction de l'utilisateur
    """

    #Constructeur
    def __init__ (self, numero):
        self.numero = numero

    #Methodes
    #Fonction Jouer qui fait jouer un joueur
    def Jouer(self, fenetre, canvas, proportion, plateau):
        while True:
            #On le fait cliquer, et pour cela on declenche la boucle pour attendre l'interaction
            canvas.bind('<Button-1>', lambda event, arg=fenetre: self.Clique(event, arg))
            fenetre.mainloop()

            #On unbin
            canvas.unbind('<Button-1>')
        
            #On interprete l'emplacement du clique
            #On d�tecte si le clique est sur une case ou sur un vide pour mettre une barri�re
            print("Clique au coordonn�e ", self.x, self.y)

            #On creer le nouveau coup
            newPlateau = deepcopy(plateau) #On effectue un deepcopy pour ne pas juste copier la reference et vraimetn creer un nouveau coup

            cliquerSurUneCase = False;
            for i in range(9):
                for j in range(9):
                    if (i*100+15 <= self.x and self.x <= (i+1)*100-15 and j*100+15 <= self.y and self.y <= (j+1)*100-15):
                        cliquerSurUneCase = True
         
            #Si on a cliqu� sur une case, on envoie le coup
            if cliquerSurUneCase:
                newPlateau.c_joueurs[self.numero-1] = [floor(self.x/100), floor(self.y/100)]
                coup = Coup(plateau, newPlateau, 1)
                return coup #On renvoie le coup jou�

            #Si on a cliqu� pas sur une case -> On a du cliquer sur une barri�re
            #On va detecter de quelle barri�re il sagit
            else:
                #On v�rifie que la bordure ne se trouve pas hors map
                pasDerreur = True
                if (self.x<=15 or self.x>=885 or self.y<=15 or self.y>=885):
                    print("Bordure en dehors du plateau de jeu !")
                    pasDerreur = False


                #On v�rifie que la bordure ne soit pas indecise
                if pasDerreur:
                    for i in range(9):
                        for j in range(9):
                            if (i*100-15 <= self.x and self.x <= i*100+15 and j*100-15 <= self.y and self.y <= j*100+15):
                                print("Imprecision : 2 bordures possibles -> Impossible de choisir")
                                pasDerreur = False

                #Si aucune erreur n'a �t� d�tect� avant, le coup est correct et on peut l'envoyer
                if pasDerreur:
                    #On detecte sur qu'elle barri�re le clique a �t� fait
                    for i in range(8):
                        for j in range(8):
                            #Si le clique est sur une barri�re verticale :
                            if (i*100-15 <= self.x and self.x <= i*100+15 and 100*j <= self.y and self.y <= 100*(j+1)):
                                #Ses coordonn�es sont donc i et j : on creer un nouveau coup avec ca
                                newPlateau.barrieresVerticales[i][j] = 1
                                coup = Coup(plateau, newPlateau, 2)
                                return coup;

                            #SI le clique est sur une barri�re horizontale
                            if (j*100-15 <= self.y and self.y <= j*100+15 and 100*i <= self.x and self.x <= 100*(i+1)):
                                #Ses coordonn�es sont donc i et j : on creer un nouveau coup avec ca
                                newPlateau.barrieresHorizontales[i][j] = 1
                                coup = Coup(plateau, newPlateau, 2)
                                return coup;
                               

    #Fonction appeller quand un clique est detect�
    def Clique(self, event, fenetre):
        self.x = event.x
        self.y = event.y
        fenetre.quit()
           

class Coup:

    """Classe contenant un coup, c'est � dire :
    - Un ancien plateau
    - Un nouveau Plateau
    - L'information de ce qui a �t� jou�. C'est la variable type de coup qui prend 1 si le coup est un d�placement, 2 si c'est une barri�re
    """

    #CONSTRUCTEUR
    def __init__(self, ancienPlateau, nouveauPlateau, typeDeCoup):
        #Ancien plateau et nouveau plateau sont enregistr�s
        self.ancienPlateau = ancienPlateau
        self.nouveauPlateau = nouveauPlateau
        self.typeDeCoup = typeDeCoup

    #Methodes

    #Methode envoyant le nouveau plateau
    def EnvoyerNouveauPlateau(self):
        return self.nouveauPlateau

class Game:

    """
    Classe principale du jeu de Quoridor.
    Elle contient la partit m�me et tous les �l�ments du jeu en cours
    C'est en quelque sorte le cerveau de la partie, qui veille au bon d�roulement du jeu et au respectt des r�gles
    Elle contient �galement le moteur graphique du jeu
    """

    #CONSTRUCTEUR
    def __init__(self, joueur1, joueur2, proportionFenetre):
        #On sauvegarde les joueurs dans la partie
        self.joueur = [joueur1, joueur2] 

        #On cr�er un plateau de jeu
        self.plateau = Plateau()

        #On creer la fenetre
        self.proportion = proportionFenetre/100
        self.fenetre = tk.Tk()
        self.fenetre.wm_title("Quoridor")
        self.canvas = tk.Canvas(self.fenetre, width =900*self.proportion, height = 900*self.proportion, bg ='#d9d9d9')
        self.canvas.pack()

        #On actualise l'affichage une premiere fois
        self.ActualiserAffichage()



    #METHODES

    #Methode qui v�rifie si un joueur a gagn�
    #Retourne 0 si personne n'a gagn�, 1 si le J1 a gagn� ou 2 si le j2 a gagn�
    def VerifierSiUnJoueurAGagne(self):

        #Si le joueur 1 se trouve sur une case avec comme coordonn�e en x 8, il a gagn�
        if (self.plateau.CoordonneeJoueur(1)[1] == 0):
            return 1

        #De meme pour le joueur 2 : si il se trouve a une coordonn�e en x de 0, il a gagn�
        if (self.plateau.CoordonneeJoueur(2)[1] == 8):
            return 2

        #Sinon, perosnne n'a gagn�
        return 0

    

    #Methode ABSTRAITE v�rifiant si un coup est autoris�e
    def VerifierSiCoupValide(self, coupATester):

        #On verifie si le coup est un coup de deplacement ou non
        if coupATester.typeDeCoup == 1:
            #On v�rifie si la variation de case est de 1
            if (coupATester.ancienPlateau.CoordonneeJoueur(1)[0] == coupATester.nouveauPlateau.CoordonneeJoueur(1)[0]+1):
                return True
        return False




    #Methode actualisant l'affichage de la partie a l'ecran
    def ActualiserAffichage(self):
        
        #On efface tout ce qu'il y a:
        self.canvas.delete("all")

        #On creer le plateau
        for i in range(9):
            for j in range(9):
                self.canvas.create_rectangle(self.proportion*100*i+self.proportion*15, self.proportion*100*j+self.proportion*15,self.proportion*100*(i+1)-self.proportion*15, self.proportion*100*(j+1)-self.proportion*15,fill="#621817")

        #On ajoute des cercles pour les joueurs
        self.canvas.create_oval(self.proportion*100*self.plateau.CoordonneeJoueur(1)[0]+self.proportion*15, self.proportion*100*self.plateau.CoordonneeJoueur(1)[1]+self.proportion*15,self.proportion*100*(self.plateau.CoordonneeJoueur(1)[0]+1)-self.proportion*15, self.proportion*100*(self.plateau.CoordonneeJoueur(1)[1]+1)-self.proportion*15,fill="#ffd849")
        self.canvas.create_oval(self.proportion*100*self.plateau.CoordonneeJoueur(2)[0]+self.proportion*15, self.proportion*100*self.plateau.CoordonneeJoueur(2)[1]+self.proportion*15,self.proportion*100*(self.plateau.CoordonneeJoueur(2)[0]+1)-self.proportion*15, self.proportion*100*(self.plateau.CoordonneeJoueur(2)[1]+1)-self.proportion*15,fill="#3673a6")

        #Affichage des barri�res
        for i in range(8):
            for j in range(8):
                if self.plateau.barrieresVerticales[i][j] == 1:
                    self.canvas.create_rectangle(i*100-15, j*100-7 ,i*100+15, (j+2)*100-7, fill="#f3e2bd")

        #On actualise l'affichage
        self.canvas.update()




    #Methode que l'on appelle pour commencer la partie
    def CommencerPartie(self):

        #Variable contenant le tour actuel
        tour = 1

        #Tant que aucun joueur n'a gagn�e
        while self.VerifierSiUnJoueurAGagne() == 0:

            coupValide = False

            #Tant que le joueur n'a pas jou� un coup autorisee
            while coupValide == False:
                #On fait jouer le joueur dont c'est le tour de jouer
                coupDuJoueur = self.joueur[tour-1].Jouer(self.fenetre, self.canvas, self.proportion, self.plateau)

                #On v�rifie si son coup est valide
                print(self.VerifierSiCoupValide(coupDuJoueur))
                coupValide = self.VerifierSiCoupValide(coupDuJoueur)

            #La boucle est fini -> Le coup � �t� valid� et peut donc etre jouer
            #On fait donc jouer le coup au plateau
            self.plateau = coupDuJoueur.nouveauPlateau

            #On actualise l'affichage
            self.ActualiserAffichage()

            #On change de tour
            tour = 3 - tour #Technique pour alternr entre 1 et 2 comme valeure pour tour
            print("C'est au tour du joueur ", tour)

        #La boucle est finie -> Un joueur a gagn�
        #On regarde qui a gagn� :
        gagnant = self.VerifierSiUnJoueurAGagne()

        #On affiche
        print("Victoire du Joueur " + str(gagnant))







#TOUT DEBUT DU PRGRAMME

#Premi�re fonction appell�e dans le programme
def main():

    #On lance le jeu
    j1 = Joueur(1)
    j2 = Joueur(2)
    game = Game(j1,j2,100)
    game.CommencerPartie()


#Definition de la fonction main
if __name__ == "__main__":
    main()