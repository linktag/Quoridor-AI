# coding: latin-1

"""

Projet Quoridor par Romain
Debuté le 23/01/2017 à 16h58

Objectif : Réaliser un jeu de Quoridor parfaitement fonctionel et jouable à deux joueurs.
Réaliser une IA a plusieurs niveau de difficulté.
L'IA utilisera pour réfléchir un algorithme MinMax amélioré (Negamax) ansi qu'une amélioration Alpha Beta
Afin d'optimiser le temps que mettra l'IA a jouer, la selection des coups est joués est effectuer dans un ordre précis afin de limiter 
les calculs inutiles.


Ce projet sera effectué en POO afin de grandement simplifier la comprehension du code, la lisibilité et la simplicité

"""

#IMPORTATION
import tkinter as tk
from math import floor
from random import randint
import queue
import time
import _pickle as cPickle

#Add Files
from IaLevel1 import IaLevel1
from IaLevel1 import IaLevel1Evolutive

from IaLevel2 import IaLevel2
from IaLevel2 import IaLevel2Acceleree



#CLASSES UTILISEES

class Plateau:
    """
    Classe contenant le plateau de jeu. C'est lui qui possède les différentts tableau avec les positions des barrières, ainsi que les
    coordonnées de la position de chaque joueur

    Les coordonnées des jouers sont contenues dans une variables c_joueurs, d'index 0 pour celle du joueur 1 ett d'index 1 pour celle du joueur 2

    Les barrières verticales et horizontales sont contenues dans un tableau de dimension en fonction de sa direction
    """

    #CONSTRUCTEUR
    def __init__(self):
        #On creer les joueurs et leurs coordonnées
        self.c_joueurs = [(4,8),(4,0)];

        #Leur barrières
        self.nbBarriere = [10,10];

        #Creation du tableau contenant les barrières verticales et les barrières horizontales
        #On creer aussi les tableau contenant les barrières interdites
        self.barrieresHorizontales = [];
        self.barrieresHorizontalesInterdites = [];
        self.barrieresVerticales = [];
        self.barrieresVerticalesInterdites = [];
        for k in range(8):
            self.barrieresVerticales.append([0]*8);
            self.barrieresVerticalesInterdites.append([0]*8);
            self.barrieresHorizontales.append([0]*8);
            self.barrieresHorizontalesInterdites.append([0]*8);


    #METHODES

    #Methode renvoyant les coordonées du joueur demandé
    def CoordonneeJoueur(self, numeroJoueur):
        return self.c_joueurs[numeroJoueur-1];

    #Methode renvoyant si oui ou non un joueur a gagnee
    def GameOver(self):
        if self.CoordonneeJoueur(1)[1] == 0 or self.CoordonneeJoueur(2)[1] == 8:
            return True;
        return False;



    #Methode qui renvoie tous les coups possible pour un joueur a partir du plateau actuel
    def TousLesCoups(self, numeroJoueur):
        listeCoups = [];

        #On commence par ajouter tous les coups qui sont liés au déplacement
        #Coup vers le haut
        if (self.CoordonneeJoueur(numeroJoueur)[1] > 0):
            #On vérifie si une barrière se trouve au dessus
            if (self.CoordonneeJoueur(numeroJoueur)[0] == 0 and self.barrieresHorizontales[self.CoordonneeJoueur(numeroJoueur)[0]][self.CoordonneeJoueur(numeroJoueur)[1]-1] == 0) or (self.CoordonneeJoueur(numeroJoueur)[0] == 8 and self.barrieresHorizontales[self.CoordonneeJoueur(numeroJoueur)[0]-1][self.CoordonneeJoueur(numeroJoueur)[1]-1] == 0) or (self.CoordonneeJoueur(numeroJoueur)[0] != 0 and self.CoordonneeJoueur(numeroJoueur)[0] != 8 and self.barrieresHorizontales[self.CoordonneeJoueur(numeroJoueur)[0]][self.CoordonneeJoueur(numeroJoueur)[1]-1] == 0 and self.barrieresHorizontales[self.CoordonneeJoueur(numeroJoueur)[0]-1][self.CoordonneeJoueur(numeroJoueur)[1]-1] == 0):
                newPlateau = cPickle.loads(cPickle.dumps(self, -1));
                newPlateau.c_joueurs[numeroJoueur-1] = (self.c_joueurs[numeroJoueur-1][0], self.c_joueurs[numeroJoueur-1][1]-1);
                listeCoups.append(Coup(self, newPlateau, 1));

        #Coup vers le bas
        if (self.CoordonneeJoueur(numeroJoueur)[1] < 8):
            if (self.CoordonneeJoueur(numeroJoueur)[0] == 0 and self.barrieresHorizontales[self.CoordonneeJoueur(numeroJoueur)[0]][self.CoordonneeJoueur(numeroJoueur)[1]] == 0) or (self.CoordonneeJoueur(numeroJoueur)[0] == 8 and self.barrieresHorizontales[self.CoordonneeJoueur(numeroJoueur)[0]-1][self.CoordonneeJoueur(numeroJoueur)[1]] == 0) or (self.CoordonneeJoueur(numeroJoueur)[0] != 0 and self.CoordonneeJoueur(numeroJoueur)[0] != 8 and self.barrieresHorizontales[self.CoordonneeJoueur(numeroJoueur)[0]][self.CoordonneeJoueur(numeroJoueur)[1]] == 0 and self.barrieresHorizontales[self.CoordonneeJoueur(numeroJoueur)[0]-1][self.CoordonneeJoueur(numeroJoueur)[1]] == 0):
                newPlateau = cPickle.loads(cPickle.dumps(self, -1));
                newPlateau.c_joueurs[numeroJoueur-1] = (self.c_joueurs[numeroJoueur-1][0], self.c_joueurs[numeroJoueur-1][1]+1);
                listeCoups.append(Coup(self, newPlateau, 1));

        #Coup vers la gauche
        if (self.CoordonneeJoueur(numeroJoueur)[0] > 0):
            if (self.CoordonneeJoueur(numeroJoueur)[1] == 0 and self.barrieresVerticales[self.CoordonneeJoueur(numeroJoueur)[0]-1][self.CoordonneeJoueur(numeroJoueur)[1]] == 0) or (self.CoordonneeJoueur(numeroJoueur)[1] == 8 and self.barrieresVerticales[self.CoordonneeJoueur(numeroJoueur)[0]-1][self.CoordonneeJoueur(numeroJoueur)[1]-1] == 0) or (self.CoordonneeJoueur(numeroJoueur)[1] != 0 and self.CoordonneeJoueur(numeroJoueur)[1] != 8 and self.barrieresVerticales[self.CoordonneeJoueur(numeroJoueur)[0]-1][self.CoordonneeJoueur(numeroJoueur)[1]] == 0 and self.barrieresVerticales[self.CoordonneeJoueur(numeroJoueur)[0]-1][self.CoordonneeJoueur(numeroJoueur)[1]-1] == 0):
                newPlateau = cPickle.loads(cPickle.dumps(self, -1));
                newPlateau.c_joueurs[numeroJoueur-1] = (self.c_joueurs[numeroJoueur-1][0]-1, self.c_joueurs[numeroJoueur-1][1]);
                listeCoups.append(Coup(self, newPlateau, 1));

        #Coup vers la droite
        if (self.CoordonneeJoueur(numeroJoueur)[0] < 8):
            if (self.CoordonneeJoueur(numeroJoueur)[1] == 0 and self.barrieresVerticales[self.CoordonneeJoueur(numeroJoueur)[0]][self.CoordonneeJoueur(numeroJoueur)[1]] == 0) or (self.CoordonneeJoueur(numeroJoueur)[1] == 8 and self.barrieresVerticales[self.CoordonneeJoueur(numeroJoueur)[0]][self.CoordonneeJoueur(numeroJoueur)[1]-1] == 0) or (self.CoordonneeJoueur(numeroJoueur)[1] != 0 and self.CoordonneeJoueur(numeroJoueur)[1] != 8 and self.barrieresVerticales[self.CoordonneeJoueur(numeroJoueur)[0]][self.CoordonneeJoueur(numeroJoueur)[1]] == 0 and self.barrieresVerticales[self.CoordonneeJoueur(numeroJoueur)[0]][self.CoordonneeJoueur(numeroJoueur)[1]-1] == 0):
                newPlateau = cPickle.loads(cPickle.dumps(self, -1));
                newPlateau.c_joueurs[numeroJoueur-1] = (self.c_joueurs[numeroJoueur-1][0]+1, self.c_joueurs[numeroJoueur-1][1]);
                listeCoups.append(Coup(self, newPlateau, 1));


        #On ajoute maintenant tous les coups liés aux barrières
        for i in range(8):
            for j in range(8):
                if (self.barrieresHorizontalesInterdites[i][j] == 0 and self.barrieresHorizontales[i][j] == 0):
                    newPlateau = cPickle.loads(cPickle.dumps(self, -1));
                    newPlateau.barrieresHorizontales[i][j] = 1;
                    listeCoups.append(Coup(self, newPlateau, 2));
                if (self.barrieresVerticalesInterdites[i][j] == 0 and self.barrieresVerticales[i][j] == 0):
                    newPlateau = cPickle.loads(cPickle.dumps(self, -1));
                    newPlateau.barrieresVerticales[i][j] = 1;
                    listeCoups.append(Coup(self, newPlateau, 2));

        #On retourne le tout
        return listeCoups;

    #Methode alternative qui renvoit les 4 coups de déplacements si possible, sans renvoyer les coups de barrières
    def TousLesCoupsSansBarrieres(self, numeroJoueur):
        listeCoups = [];

        #On commence par ajouter tous les coups qui sont liés au déplacement
        #Coup vers le haut
        if (self.CoordonneeJoueur(numeroJoueur)[1] > 0):
            #On vérifie si une barrière se trouve au dessus
            if (self.CoordonneeJoueur(numeroJoueur)[0] == 0 and self.barrieresHorizontales[self.CoordonneeJoueur(numeroJoueur)[0]][self.CoordonneeJoueur(numeroJoueur)[1]-1] == 0) or (self.CoordonneeJoueur(numeroJoueur)[0] == 8 and self.barrieresHorizontales[self.CoordonneeJoueur(numeroJoueur)[0]-1][self.CoordonneeJoueur(numeroJoueur)[1]-1] == 0) or (self.CoordonneeJoueur(numeroJoueur)[0] != 0 and self.CoordonneeJoueur(numeroJoueur)[0] != 8 and self.barrieresHorizontales[self.CoordonneeJoueur(numeroJoueur)[0]][self.CoordonneeJoueur(numeroJoueur)[1]-1] == 0 and self.barrieresHorizontales[self.CoordonneeJoueur(numeroJoueur)[0]-1][self.CoordonneeJoueur(numeroJoueur)[1]-1] == 0):
                newPlateau = cPickle.loads(cPickle.dumps(self, -1));
                newPlateau.c_joueurs[numeroJoueur-1] = (self.c_joueurs[numeroJoueur-1][0], self.c_joueurs[numeroJoueur-1][1]-1);
                listeCoups.append(Coup(self, newPlateau, 1));

        #Coup vers le bas
        if (self.CoordonneeJoueur(numeroJoueur)[1] < 8):
            if (self.CoordonneeJoueur(numeroJoueur)[0] == 0 and self.barrieresHorizontales[self.CoordonneeJoueur(numeroJoueur)[0]][self.CoordonneeJoueur(numeroJoueur)[1]] == 0) or (self.CoordonneeJoueur(numeroJoueur)[0] == 8 and self.barrieresHorizontales[self.CoordonneeJoueur(numeroJoueur)[0]-1][self.CoordonneeJoueur(numeroJoueur)[1]] == 0) or (self.CoordonneeJoueur(numeroJoueur)[0] != 0 and self.CoordonneeJoueur(numeroJoueur)[0] != 8 and self.barrieresHorizontales[self.CoordonneeJoueur(numeroJoueur)[0]][self.CoordonneeJoueur(numeroJoueur)[1]] == 0 and self.barrieresHorizontales[self.CoordonneeJoueur(numeroJoueur)[0]-1][self.CoordonneeJoueur(numeroJoueur)[1]] == 0):
                newPlateau = cPickle.loads(cPickle.dumps(self, -1));
                newPlateau.c_joueurs[numeroJoueur-1] = (self.c_joueurs[numeroJoueur-1][0], self.c_joueurs[numeroJoueur-1][1]+1);
                listeCoups.append(Coup(self, newPlateau, 1));

        #Coup vers la gauche
        if (self.CoordonneeJoueur(numeroJoueur)[0] > 0):
            if (self.CoordonneeJoueur(numeroJoueur)[1] == 0 and self.barrieresVerticales[self.CoordonneeJoueur(numeroJoueur)[0]-1][self.CoordonneeJoueur(numeroJoueur)[1]] == 0) or (self.CoordonneeJoueur(numeroJoueur)[1] == 8 and self.barrieresVerticales[self.CoordonneeJoueur(numeroJoueur)[0]-1][self.CoordonneeJoueur(numeroJoueur)[1]-1] == 0) or (self.CoordonneeJoueur(numeroJoueur)[1] != 0 and self.CoordonneeJoueur(numeroJoueur)[1] != 8 and self.barrieresVerticales[self.CoordonneeJoueur(numeroJoueur)[0]-1][self.CoordonneeJoueur(numeroJoueur)[1]] == 0 and self.barrieresVerticales[self.CoordonneeJoueur(numeroJoueur)[0]-1][self.CoordonneeJoueur(numeroJoueur)[1]-1] == 0):
                newPlateau = cPickle.loads(cPickle.dumps(self, -1));
                newPlateau.c_joueurs[numeroJoueur-1] = (self.c_joueurs[numeroJoueur-1][0]-1, self.c_joueurs[numeroJoueur-1][1]);
                listeCoups.append(Coup(self, newPlateau, 1));

        #Coup vers la droite
        if (self.CoordonneeJoueur(numeroJoueur)[0] < 8):
            if (self.CoordonneeJoueur(numeroJoueur)[1] == 0 and self.barrieresVerticales[self.CoordonneeJoueur(numeroJoueur)[0]][self.CoordonneeJoueur(numeroJoueur)[1]] == 0) or (self.CoordonneeJoueur(numeroJoueur)[1] == 8 and self.barrieresVerticales[self.CoordonneeJoueur(numeroJoueur)[0]][self.CoordonneeJoueur(numeroJoueur)[1]-1] == 0) or (self.CoordonneeJoueur(numeroJoueur)[1] != 0 and self.CoordonneeJoueur(numeroJoueur)[1] != 8 and self.barrieresVerticales[self.CoordonneeJoueur(numeroJoueur)[0]][self.CoordonneeJoueur(numeroJoueur)[1]] == 0 and self.barrieresVerticales[self.CoordonneeJoueur(numeroJoueur)[0]][self.CoordonneeJoueur(numeroJoueur)[1]-1] == 0):
                newPlateau = cPickle.loads(cPickle.dumps(self, -1));
                newPlateau.c_joueurs[numeroJoueur-1] = (self.c_joueurs[numeroJoueur-1][0]+1, self.c_joueurs[numeroJoueur-1][1]);
                listeCoups.append(Coup(self, newPlateau, 1));

        #On retourne le tout
        return listeCoups;



    #Méthode méttant à jour barrieresHorizontalesInterdites et barrieresVerticalesInterdites en fonction du plateau
    def ActualiserBarrieresInterdites(self):
        listeMap = [];
        for i in range(8):
            for j in range(8):

                #Etape 1 : Il est impossible, comme chaque barrière fait 2 case, de mettre une barrière directement a droite ou a gauche, et vis versa
                 #On élimine donc logiquement les barrières impossible à mettre
                if i > 0:
                    if (self.barrieresHorizontales[i][j] == 1):
                        self.barrieresHorizontalesInterdites[i-1][j] = 1;
                if j > 0:
                    if (self.barrieresVerticales[i][j] == 1):
                        self.barrieresVerticalesInterdites[i][j-1] = 1;

                if i < 7:
                    if (self.barrieresHorizontales[i][j] == 1):
                        self.barrieresHorizontalesInterdites[i+1][j] = 1;
                if j < 7:
                    if (self.barrieresVerticales[i][j] == 1):
                        self.barrieresVerticalesInterdites[i][j+1] = 1;

                #Etape 2 : Il est impossible de mettre une barrière en travers d'une autre
                if (self.barrieresHorizontales[i][j] == 1):
                    self.barrieresVerticalesInterdites[i][j] = 1;

                if (self.barrieresVerticales[i][j] == 1):
                    self.barrieresHorizontalesInterdites[i][j] = 1;

        #Etape 3 : Si une barrière pourrait interdire tout possibilité de gagner à un joueur
        #On va donc dans un premier temps générer toutes les maps possibles en ne rajoutant qu'une barrière
        #Pour cela, si la barrière actuelle (i,j) peut etre posée, on effectue un test pour savoir si les joueurs
        #peuvent toujours passer. Si non, on interdit cette barrière

        for j in range(8):
            for i in range(8):
                if (self.barrieresHorizontalesInterdites[i][j] == 0 and self.barrieresHorizontales[i][j] == 0):
                    self.barrieresHorizontales[i][j] = 1;
                    if (self.LesDeuxJoueursPeuventGagner() == False):
                        self.barrieresHorizontalesInterdites[i][j] = 1;
                    self.barrieresHorizontales[i][j] = 0;


                if (self.barrieresVerticalesInterdites[i][j] == 0 and self.barrieresVerticales[i][j] == 0):
                    self.barrieresVerticales[i][j] = 1;
                    if (self.LesDeuxJoueursPeuventGagner() == False):
                        self.barrieresVerticalesInterdites[i][j] = 1;
                    self.barrieresVerticales[i][j] = 0;  
                    


    #Méthode renvoyant si oui ou non les deux joeurs ont acces aux cases leurs permetant de gagner
    def LesDeuxJoueursPeuventGagner(self):

        #On va commencer par tester avec le joueur 1
        #Pour cela, on doit donc vérifier si il est possible que celui ci atteigne la ligne de rang 0
        #On part donc de ses coordonées et lentement mais surement on explore toutes les possibilités
        graph1 = [];
        graph2 = [];
        for i in range(9):
            graph1.append([False]*9);
            graph2.append([False]*9);
        self.graphe = [graph1, graph2];
        coo1 = (self.CoordonneeJoueur(1)[0], self.CoordonneeJoueur(1)[1]);
        coo2 = (self.CoordonneeJoueur(2)[0], self.CoordonneeJoueur(2)[1]);
        bool1 = self.DepthFirstSearch(coo1, 1 , 0);
        bool2 = self.DepthFirstSearch(coo2, 2 , 8);

        if (bool1 == True and bool2 == True):
            return True;
        return False;




    #Methode renvoyant la distance la plus courte pour un joueur pour parvenir au point d'arrivée
    #Cette algorithme est beacoup plus long que celui de la fonction DepthFirstSearch, mais lui renvoie le chemin le plus court,
    #Alors que la fonction DepthFirstSearch ne fait que dire si oui ou non le chemin est accessible ou pas
    #Bien qu'elles se ressemblent, elles ont donc des fonctions différentes
    #---
    #positionDeDepart est la position de départ du joueur
    #ligneAAtteindre correspond a la ligne d'arrivée en fonction du joueur (Mettre 0 si Joueur 1, 8 si joueur 2)
    def BreadthFirstSearch(self, positionDeDepart, ligneAAtteindre):
        #On creer tout ce qu'il faut pour l'algorithme
        liste = queue.Queue();
        visite = set();

        #On ajoute la position actuelle
        liste.put((positionDeDepart, 0));

        #On marque la position comme déja passée
        visite.add(positionDeDepart);

        #On commence la boucle
        while not liste.empty():
            #On recupère la position la plus lointaine ajoutée et on la supprime
            wallah = liste.get();
            positionActuelle = wallah[0];
            distance = wallah[1];


            #On regarde tous les voisins de cette position, que l'on va explorer :
            #Tentative de mouvement vers le haut
            if (positionActuelle[1] > 0): #Si on n'est pas deja tout en haut
                #On creer la posittion
                newPosition = (positionActuelle[0], positionActuelle[1] - 1);
                if newPosition not in visite: #Si on n'a pas deja visiter cette case
                    #On vérifie si une barrière se trouve au dessus
                    if (positionActuelle[0] == 0 and self.barrieresHorizontales[positionActuelle[0]][positionActuelle[1]-1] == 0) or (positionActuelle[0] == 8 and self.barrieresHorizontales[positionActuelle[0]-1][positionActuelle[1]-1] == 0) or (positionActuelle[0] != 0 and positionActuelle[0] != 8 and self.barrieresHorizontales[positionActuelle[0]][positionActuelle[1]-1] == 0 and self.barrieresHorizontales[positionActuelle[0]-1][positionActuelle[1]-1] == 0):
                        #On peut se rendre sur cette case
                        #Si on a atteint note but :
                        if (newPosition[1] == ligneAAtteindre):
                            #Alors on peut retourner la distance
                            return distance+1;
                        else:
                            #On l'ajoute a la liste
                            liste.put((newPosition, distance+1));
                            visite.add(newPosition);

            #Tentative de mouvement vers le bas
            if (positionActuelle[1] < 8):#Si on est pas tout en bas
                #On creer la posittion
                newPosition = (positionActuelle[0], positionActuelle[1] + 1);
                if newPosition not in visite: #Si on n'a pas deja visiter cette case
                    #On vérifie si une barrière se trouve en dessous
                    if (positionActuelle[0] == 0 and self.barrieresHorizontales[positionActuelle[0]][positionActuelle[1]] == 0) or (positionActuelle[0] == 8 and self.barrieresHorizontales[positionActuelle[0]-1][positionActuelle[1]] == 0) or (positionActuelle[0] != 0 and positionActuelle[0] != 8 and self.barrieresHorizontales[positionActuelle[0]][positionActuelle[1]] == 0 and self.barrieresHorizontales[positionActuelle[0]-1][positionActuelle[1]] == 0):
                        #On peut se rendre sur cette case
                        #Si on a atteint note but :
                        if (newPosition[1] == ligneAAtteindre):
                            #Alors on peut retourner la distance
                            return distance+1;
                        else:
                            #On l'ajoute a la liste
                            liste.put((newPosition, distance+1));
                            visite.add(newPosition);

            #Tentative de mouvement vers la gauche
            if (positionActuelle[0] > 0):#Si on est pas tout a gauche
                #On creer la posittion
                newPosition = (positionActuelle[0] - 1, positionActuelle[1]);
                if newPosition not in visite: #Si on n'a pas deja visiter cette case
                    if (positionActuelle[1] == 0 and self.barrieresVerticales[positionActuelle[0]-1][positionActuelle[1]] == 0) or (positionActuelle[1] == 8 and self.barrieresVerticales[positionActuelle[0]-1][positionActuelle[1]-1] == 0) or (positionActuelle[1] != 0 and positionActuelle[1] != 8 and self.barrieresVerticales[positionActuelle[0]-1][positionActuelle[1]] == 0 and self.barrieresVerticales[positionActuelle[0]-1][positionActuelle[1]-1] == 0):
                        #On peut se rendre sur cette case
                        #On l'ajoute a la liste
                        liste.put((newPosition, distance+1));
                        visite.add(newPosition);

            #Tentative de mouvement vers la droite
            if (positionActuelle[0] < 8):
                #On creer la posittion
                newPosition = (positionActuelle[0] + 1, positionActuelle[1]);
                if newPosition not in visite: #Si on n'a pas deja visiter cette case
                    if (positionActuelle[1] == 0 and self.barrieresVerticales[positionActuelle[0]][positionActuelle[1]] == 0) or (positionActuelle[1] == 8 and self.barrieresVerticales[positionActuelle[0]][positionActuelle[1]-1] == 0) or (positionActuelle[1] != 0 and positionActuelle[1] != 8 and self.barrieresVerticales[positionActuelle[0]][positionActuelle[1]] == 0 and self.barrieresVerticales[positionActuelle[0]][positionActuelle[1]-1] == 0):
                        #On peut se rendre sur cette case
                        #On l'ajoute a la liste
                        liste.put((newPosition, distance+1));
                        visite.add(newPosition);


        #Si la boucle c'est finie sans avoir rien retourner avant, c'est qu'il n'y a rien a re tourner => aucun chemin possible
        #On renvoit donc -1
        return -1;






    #Methode permettant de savoir si il au moins un chemin permettant de faire gagner un joueur
    #Cet algorithme est assez rapide mais ne fait que renvoyer Vrai ou faux et non la distance
    #Pour trouver la distance au chemin le plus court, utiliser la fonction BFS
    #---
    #positionActuelle est la position de départ du joueur
    #k est l'index du joueur (1 ou 2)
    #ligneAAtteindre correspond a la ligne d'arrivée en fonction du joueur (Mettre 0 si Joueur 1, 8 si joueur 2)
    def DepthFirstSearch(self, positionActuelle, k, ligneAAtteindre):
        #On vérifie si l'on est sur une position ou le joueur peut gagner :
        #- Si oui, cela veut dire qu'il existe un chemin permettant de gagner, donc on renvoie vrai
        if (positionActuelle[1] == ligneAAtteindre):
            return True;
        #- Si non, il faut continuer à chercher

        #On marque le sommet sur lequel on se trouve, se serait con de passer deux fois au meme endroit
        self.graphe[k-1][positionActuelle[0]][ positionActuelle[1]] = True;

        #On va donc explorer les 4 cases adjacentes, mais uniquement si :
        #- il n'y a pas de mur entre nous et la case adjacente
        #- on n'est pas déja allez sur cette case

        #De plus, pour optimiser la fonction :
        #- Si on est le joueur 1 : On test les mouvements dans cet ordre : HAUT, GAUCHE, DROITE, BAS
        #Pour le joueur 2, c'est BAS, GAUCHE, DROITE, HAUT

        if (ligneAAtteindre == 0): #Implicitement : Si on est le joueur 1
            #On essaie d'aller sur la case du HAUT
            if (positionActuelle[1] > 0): #Si on n'est pas deja tout en haut
                if (self.graphe[k-1][positionActuelle[0]][positionActuelle[1]-1] == False):#Si on n'a pas deja visiter cette case
                    #On vérifie si une barrière se trouve au dessus
                    if (positionActuelle[0] == 0 and self.barrieresHorizontales[positionActuelle[0]][positionActuelle[1]-1] == 0) or (positionActuelle[0] == 8 and self.barrieresHorizontales[positionActuelle[0]-1][positionActuelle[1]-1] == 0) or (positionActuelle[0] != 0 and positionActuelle[0] != 8 and self.barrieresHorizontales[positionActuelle[0]][positionActuelle[1]-1] == 0 and self.barrieresHorizontales[positionActuelle[0]-1][positionActuelle[1]-1] == 0):
                        #On peut y acceder !
                        newPosition = (positionActuelle[0], positionActuelle[1] - 1);
                        #Au passage, on vérifie si l'exploration des lignes suivantes a permi de trouver le chemin ou non
                        #Et si oui, on renvoit oui a notre tour pour faire remonter la nouvelle
                        if (self.DepthFirstSearch(newPosition, k, ligneAAtteindre) == True):
                            return True; 
        else:
            #On fait la même chose avec les autres directions :
            #BAS
            if (positionActuelle[1] < 8):#Si on est pas tout en bas
                if (self.graphe[k-1][positionActuelle[0]][positionActuelle[1]+1] == False):#Si on n'a pas deja visiter cette case
                    #On vérifie si une barrière se trouve en dessous
                    if (positionActuelle[0] == 0 and self.barrieresHorizontales[positionActuelle[0]][positionActuelle[1]] == 0) or (positionActuelle[0] == 8 and self.barrieresHorizontales[positionActuelle[0]-1][positionActuelle[1]] == 0) or (positionActuelle[0] != 0 and positionActuelle[0] != 8 and self.barrieresHorizontales[positionActuelle[0]][positionActuelle[1]] == 0 and self.barrieresHorizontales[positionActuelle[0]-1][positionActuelle[1]] == 0):
                        #On peut y acceder !
                        newPosition = (positionActuelle[0], positionActuelle[1] + 1);
                        #Au passage, on vérifie si l'exploration des lignes suivantes a permi de trouver le chemin ou non
                        #Et si oui, on renvoit oui a notre tour pour faire remonter la nouvelle
                        if (self.DepthFirstSearch(newPosition, k, ligneAAtteindre) == True):
                            return True; 


        #GAUCHE
        if (positionActuelle[0] > 0):#Si on est pas tout a gauche
            if (self.graphe[k-1][positionActuelle[0]-1][positionActuelle[1]] == False):
                if (positionActuelle[1] == 0 and self.barrieresVerticales[positionActuelle[0]-1][positionActuelle[1]] == 0) or (positionActuelle[1] == 8 and self.barrieresVerticales[positionActuelle[0]-1][positionActuelle[1]-1] == 0) or (positionActuelle[1] != 0 and positionActuelle[1] != 8 and self.barrieresVerticales[positionActuelle[0]-1][positionActuelle[1]] == 0 and self.barrieresVerticales[positionActuelle[0]-1][positionActuelle[1]-1] == 0):
                    #On peut y acceder !
                    newPosition = (positionActuelle[0]-1, positionActuelle[1]);
                    #Au passage, on vérifie si l'exploration des lignes suivantes a permi de trouver le chemin ou non
                    #Et si oui, on renvoit oui a notre tour pour faire remonter la nouvelle
                    if (self.DepthFirstSearch(newPosition, k, ligneAAtteindre) == True):
                        return True; 

        #DROITE
        if (positionActuelle[0] < 8):
            if (self.graphe[k-1][positionActuelle[0]+1][positionActuelle[1]] == False):
                if (positionActuelle[1] == 0 and self.barrieresVerticales[positionActuelle[0]][positionActuelle[1]] == 0) or (positionActuelle[1] == 8 and self.barrieresVerticales[positionActuelle[0]][positionActuelle[1]-1] == 0) or (positionActuelle[1] != 0 and positionActuelle[1] != 8 and self.barrieresVerticales[positionActuelle[0]][positionActuelle[1]] == 0 and self.barrieresVerticales[positionActuelle[0]][positionActuelle[1]-1] == 0):
                    #On peut y acceder !
                    newPosition = (positionActuelle[0]+1, positionActuelle[1]);
                    #Au passage, on vérifie si l'exploration des lignes suivantes a permi de trouver le chemin ou non
                    #Et si oui, on renvoit oui a notre tour pour faire remonter la nouvelle
                    if (self.DepthFirstSearch(newPosition, k, ligneAAtteindre) == True):
                        return True; 

        if (ligneAAtteindre == 0): #Implicitement : Si on est le joueur 1
            #BAS
            if (positionActuelle[1] < 8):#Si on est pas tout en bas
                if (self.graphe[k-1][positionActuelle[0]][positionActuelle[1]+1] == False):#Si on n'a pas deja visiter cette case
                    #On vérifie si une barrière se trouve en dessous
                    if (positionActuelle[0] == 0 and self.barrieresHorizontales[positionActuelle[0]][positionActuelle[1]] == 0) or (positionActuelle[0] == 8 and self.barrieresHorizontales[positionActuelle[0]-1][positionActuelle[1]] == 0) or (positionActuelle[0] != 0 and positionActuelle[0] != 8 and self.barrieresHorizontales[positionActuelle[0]][positionActuelle[1]] == 0 and self.barrieresHorizontales[positionActuelle[0]-1][positionActuelle[1]] == 0):
                        #On peut y acceder !
                        newPosition = (positionActuelle[0], positionActuelle[1] + 1);
                        #Au passage, on vérifie si l'exploration des lignes suivantes a permi de trouver le chemin ou non
                        #Et si oui, on renvoit oui a notre tour pour faire remonter la nouvelle
                        if (self.DepthFirstSearch(newPosition, k, ligneAAtteindre) == True):
                            return True; 
        else:
            #HAUT
            if (positionActuelle[1] > 0): #Si on n'est pas deja tout en haut
                if (self.graphe[k-1][positionActuelle[0]][positionActuelle[1]-1] == False):#Si on n'a pas deja visiter cette case
                    #On vérifie si une barrière se trouve au dessus
                    if (positionActuelle[0] == 0 and self.barrieresHorizontales[positionActuelle[0]][positionActuelle[1]-1] == 0) or (positionActuelle[0] == 8 and self.barrieresHorizontales[positionActuelle[0]-1][positionActuelle[1]-1] == 0) or (positionActuelle[0] != 0 and positionActuelle[0] != 8 and self.barrieresHorizontales[positionActuelle[0]][positionActuelle[1]-1] == 0 and self.barrieresHorizontales[positionActuelle[0]-1][positionActuelle[1]-1] == 0):
                        #On peut y acceder !
                        newPosition = (positionActuelle[0], positionActuelle[1] - 1);
                        #Au passage, on vérifie si l'exploration des lignes suivantes a permi de trouver le chemin ou non
                        #Et si oui, on renvoit oui a notre tour pour faire remonter la nouvelle
                        if (self.DepthFirstSearch(newPosition, k, ligneAAtteindre) == True):
                            return True; 
            

        #Rien n'a été trouvé, on renvoit faux
        return False;




class Joueur:

    """
    Classe de base d'un joueur jouant au jeu. Elle contient toutes les fonctions communes à tous les joueurs.
    Le joueur par défaut exprimer par cettte classe est humain
    Elle contient toutes les actions que peut effectuer le joueur, notament la fonction jouer, qui atttend une interaction de l'utilisateur.
    """

    #Constructeur
    def __init__ (self, numero):
        self.numero = numero;


    #Methodes
    #Fonction Jouer qui fait jouer un joueur
    def Jouer(self, fenetre, canvas, proportion, plateau):
        while True:
            #On le fait cliquer, et pour cela on declenche la boucle pour attendre l'interaction
            canvas.bind('<Button-1>', lambda event, arg=fenetre: self.Clique(event, arg));
            fenetre.mainloop();

            #On unbin
            canvas.unbind('<Button-1>');
        
            #On interprete l'emplacement du clique
            #On détecte si le clique est sur une case ou sur un vide pour mettre une barrière

            #On creer le nouveau coup
            newPlateau = cPickle.loads(cPickle.dumps(plateau, -1)); #On effectue un deepcopy pour ne pas juste copier la reference et vraimetn creer un nouveau coup

            cliquerSurUneCase = False;
            for i in range(9):
                for j in range(9):
                    if (i*100+15 <= self.x and self.x <= (i+1)*100-15 and j*100+15 <= self.y and self.y <= (j+1)*100-15):
                        cliquerSurUneCase = True;
         
            #Si on a cliqué sur une case, on envoie le coup
            if cliquerSurUneCase:
                newPlateau.c_joueurs[self.numero-1] = (floor(self.x/100), floor(self.y/100));
                coup = Coup(plateau, newPlateau, 1);
                return coup; #On renvoie le coup joué

            #Si on a cliqué pas sur une case -> On a du cliquer sur une barrière
            #On va detecter de quelle barrière il sagit
            else:
                #On vérifie que la bordure ne se trouve pas hors map
                pasDerreur = True
                if (self.x<=15 or self.x>=885 or self.y<=15 or self.y>=885):
                    print("Bordure en dehors du plateau de jeu !");
                    pasDerreur = False;


                #On vérifie que la bordure ne soit pas indecise
                if pasDerreur:
                    for i in range(9):
                        for j in range(9):
                            if (i*100-15 <= self.x and self.x <= i*100+15 and j*100-15 <= self.y and self.y <= j*100+15):
                                print("Imprecision : 2 barrières possibles -> Impossible de choisir");
                                pasDerreur = False;

                #Si aucune erreur n'a été détecté avant, le coup est correct et on peut l'envoyer
                if pasDerreur:
                    #On detecte sur qu'elle barrière le clique a été fait
                    for i in range(8):
                        for j in range(8):
                            #Si le clique est sur une barrière verticale :
                            if ((i+1)*100-15 <= self.x and self.x <= (i+1)*100+15 and 100*j <= self.y and self.y <= 100*(j+1)):
                                #Ses coordonnées sont donc i et j : on creer un nouveau coup avec ca
                                newPlateau.barrieresVerticales[i][j] = 1;
                                coup = Coup(plateau, newPlateau, 2);
                                return coup;

                            #SI le clique est sur une barrière horizontale
                            if ((j+1)*100-15 <= self.y and self.y <= (j+1)*100+15 and 100*i <= self.x and self.x <= 100*(i+1)):
                                #Ses coordonnées sont donc i et j : on creer un nouveau coup avec ca
                                newPlateau.barrieresHorizontales[i][j] = 1;
                                coup = Coup(plateau, newPlateau, 2);
                                return coup;
                               

    #Fonction appeller quand un clique est detecté
    def Clique(self, event, fenetre):
        self.x = event.x;
        self.y = event.y;
        fenetre.quit();
           

class Coup:

    """Classe contenant un coup, c'est à dire :
    - Un ancien plateau
    - Un nouveau Plateau
    - L'information de ce qui a été joué. C'est la variable type de coup qui prend 1 si le coup est un déplacement, 2 si c'est une barrière
    """

    #CONSTRUCTEUR
    def __init__(self, ancienPlateau, nouveauPlateau, typeDeCoup):
        #Ancien plateau et nouveau plateau sont enregistrés
        self.ancienPlateau = ancienPlateau;
        self.nouveauPlateau = nouveauPlateau;
        self.typeDeCoup = typeDeCoup;

    #Methodes

    #Methode envoyant le nouveau plateau
    def EnvoyerNouveauPlateau(self):
        return self.nouveauPlateau;

class Game:

    """
    Classe principale du jeu de Quoridor.
    Elle contient la partit même et tous les éléments du jeu en cours
    C'est en quelque sorte le cerveau de la partie, qui veille au bon déroulement du jeu et au respectt des règles
    Elle contient également le moteur graphique du jeu
    """

    #CONSTRUCTEUR
    def __init__(self, joueur1, joueur2, proportionFenetre):
        #On sauvegarde les joueurs dans la partie
        self.joueur = [joueur1, joueur2];

        #On créer un plateau de jeu
        self.plateau = Plateau();

        #On creer la fenetre
        self.proportion = proportionFenetre/100;
        self.fenetre = tk.Tk();
        self.fenetre.wm_title("Quoridor");
        self.canvas = tk.Canvas(self.fenetre, width =900*self.proportion, height = 900*self.proportion, bg ='#d9d9d9');
        self.canvas.pack();

        #On actualise l'affichage une premiere fois
        self.ActualiserAffichage();



    #METHODES
    #Methode pour détruire la partie
    def destroy(self):
       self.fenetre.destroy();

    #Methode qui vérifie si un joueur a gagné
    #Retourne 0 si personne n'a gagné, 1 si le J1 a gagné ou 2 si le j2 a gagné
    def VerifierSiUnJoueurAGagne(self):

        #Si le joueur 1 se trouve sur une case avec comme coordonnée en x 8, il a gagné
        if (self.plateau.CoordonneeJoueur(1)[1] == 0):
            return 1;

        #De meme pour le joueur 2 : si il se trouve a une coordonnée en x de 0, il a gagné
        if (self.plateau.CoordonneeJoueur(2)[1] == 8):
            return 2;

        #Sinon, perosnne n'a gagné
        return 0;

    

    #Methode vérifiant si un coup est autorisée
    def VerifierSiCoupValide(self, coupATester, indexJoueurEnCours):

        #On verifie si le coup est un coup de deplacement ou non
        if coupATester.typeDeCoup == 1:
            #On vérifie si c'est un des 4 coups autorisés

            #Coup ou x reste stable 
            if (coupATester.ancienPlateau.CoordonneeJoueur(indexJoueurEnCours)[0] == coupATester.nouveauPlateau.CoordonneeJoueur(indexJoueurEnCours)[0] ):
                #Coup case HAUT
                if(coupATester.ancienPlateau.CoordonneeJoueur(indexJoueurEnCours)[1] == coupATester.nouveauPlateau.CoordonneeJoueur(indexJoueurEnCours)[1]+1):
                    print("Coup vers le HAUT");

                    #Vérification de l'absence de barrière
                    i = coupATester.ancienPlateau.CoordonneeJoueur(indexJoueurEnCours)[0];
                    j = coupATester.ancienPlateau.CoordonneeJoueur(indexJoueurEnCours)[1];
                    
                    #Si on est dans la colonne 0, c'est a dire tout a gauche
                    if (i == 0):
                        #On vérifie si il y a une barrière au dessus
                        if (coupATester.nouveauPlateau.barrieresHorizontales[i][j-1] == 0):
                            return True;
                        else:
                            print("Barrière détectée");
                    #Si on est dans la colonne 8, c'est à dire tout a droite
                    elif (i == 8):
                        #On vérifie si il y a une barrière au dessus
                        if (coupATester.nouveauPlateau.barrieresHorizontales[i-1][j-1] == 0):
                            return True;
                        else:
                            print("Barrière détectée");
                    #Sinon, on vérifie les deux
                    else:
                        if (coupATester.nouveauPlateau.barrieresHorizontales[i-1][j-1] == 0 and coupATester.nouveauPlateau.barrieresHorizontales[i][j-1] == 0):
                            return True;
                        else:
                            print("Barrière détectée");
                    
                    

                #coup case BAS
                elif (coupATester.ancienPlateau.CoordonneeJoueur(indexJoueurEnCours)[1] == coupATester.nouveauPlateau.CoordonneeJoueur(indexJoueurEnCours)[1]-1):
                    print("Coup vers le BAS");
                    
                    #Vérification de l'absence de barrière
                    i = coupATester.ancienPlateau.CoordonneeJoueur(indexJoueurEnCours)[0];
                    j = coupATester.ancienPlateau.CoordonneeJoueur(indexJoueurEnCours)[1];
                    
                    #Si on est dans la colonne 0, c'est a dire tout a gauche
                    if (i == 0):
                        #On vérifie si il y a une barrière en dessous
                        if (coupATester.nouveauPlateau.barrieresHorizontales[i][j] == 0):
                            return True;
                        else:
                            print("Barrière détectée");
                    #Si on est dans la colonne 8, c'est à dire tout a droite
                    elif (i == 8):
                        #On vérifie si il y a une barrière en dessous
                        if (coupATester.nouveauPlateau.barrieresHorizontales[i-1][j] == 0):
                            return True;
                        else:
                            print("Barrière détectée");
                    #Sinon, on vérifie les deux
                    else:
                        if (coupATester.nouveauPlateau.barrieresHorizontales[i-1][j] == 0 and coupATester.nouveauPlateau.barrieresHorizontales[i][j] == 0):
                            return True;
                        else:
                            print("Barrière détectée");

            #Coup ou y reste stable 
            if (coupATester.ancienPlateau.CoordonneeJoueur(indexJoueurEnCours)[1] == coupATester.nouveauPlateau.CoordonneeJoueur(indexJoueurEnCours)[1] ):
                #Coup case GAUCHE
                if(coupATester.ancienPlateau.CoordonneeJoueur(indexJoueurEnCours)[0] == coupATester.nouveauPlateau.CoordonneeJoueur(indexJoueurEnCours)[0]+1):
                    print("Coup vers la GAUCHE");

                    #Vérification de l'absence de barrière
                    i = coupATester.ancienPlateau.CoordonneeJoueur(indexJoueurEnCours)[0];
                    j = coupATester.ancienPlateau.CoordonneeJoueur(indexJoueurEnCours)[1];
                    
                    #Si on est dans la ligne 0, c'est a dire tout en haut
                    if (j == 0):
                        #On vérifie si il y a une barrière à gauche
                        if (coupATester.nouveauPlateau.barrieresVerticales[i-1][j] == 0):
                            return True;
                        else:
                            print("Barrière détectée");
                    #Si on est dans la ligne 8, c'est à dire tout en bas
                    elif (j == 8):
                        #On vérifie si il y a une barrière à gauche
                        if (coupATester.nouveauPlateau.barrieresVerticales[i-1][j-1] == 0):
                            return True;
                        else:
                            print("Barrière détectée");
                    #Sinon, on vérifie les deux
                    else:
                        if (coupATester.nouveauPlateau.barrieresVerticales[i-1][j] == 0 and coupATester.nouveauPlateau.barrieresVerticales[i-1][j-1] == 0):
                            return True;
                        else:
                            print("Barrière détectée");

                #Coup case DROITE
                elif (coupATester.ancienPlateau.CoordonneeJoueur(indexJoueurEnCours)[0] == coupATester.nouveauPlateau.CoordonneeJoueur(indexJoueurEnCours)[0]-1):
                    print("Coup vers la DROITE");

                    #Vérification de l'absence de barrière
                    i = coupATester.ancienPlateau.CoordonneeJoueur(indexJoueurEnCours)[0];
                    j = coupATester.ancienPlateau.CoordonneeJoueur(indexJoueurEnCours)[1];
                    
                    #Si on est dans la ligne 0, c'est a dire tout en haut
                    if (j == 0):
                        #On vérifie si il y a une barrière à gauche
                        if (coupATester.nouveauPlateau.barrieresVerticales[i][j] == 0):
                            return True;
                        else:
                            print("Barrière détectée");
                    #Si on est dans la ligne 8, c'est à dire tout en bas
                    elif (j == 8):
                        #On vérifie si il y a une barrière à gauche
                        if (coupATester.nouveauPlateau.barrieresVerticales[i][j-1] == 0):
                            return True;
                        else:
                            print("Barrière détectée");
                    #Sinon, on vérifie les deux
                    else:
                        if (coupATester.nouveauPlateau.barrieresVerticales[i][j] == 0 and coupATester.nouveauPlateau.barrieresVerticales[i][j-1] == 0):
                            return True;
                        else:
                            print("Barrière détectée");

        #Si il s'agit d'une barrière
        elif coupATester.typeDeCoup == 2:
        #On vérifie si il reste des barrières au joueur
            if (coupATester.nouveauPlateau.nbBarriere[indexJoueurEnCours-1] != 0):
                #On vérifie si la barrière est autorisé
                for i in range(8):
                    for j in range(8):
                        if (coupATester.nouveauPlateau.barrieresHorizontales[i][j] == 1 and coupATester.nouveauPlateau.barrieresHorizontalesInterdites[i][j] == 1): 
                            print("Erreur : Impossible de placer cette barrière");
                            return False;
                        if (coupATester.nouveauPlateau.barrieresVerticales[i][j] == 1 and coupATester.nouveauPlateau.barrieresVerticalesInterdites[i][j] == 1):
                            print("Erreur : Impossible de placer cette barrière");
                            return False;

                #Sinon, on peut jouer la barrière 
                return True;

            else:
                print("Le joueur " + str(indexJoueurEnCours) + " n'a plus de barrière !");


        print("Coup interdit");
        return False;




    #Methode actualisant l'affichage de la partie a l'ecran
    def ActualiserAffichage(self):
        
        #On efface tout ce qu'il y a:
        self.canvas.delete("all");

        #On creer le plateau
        for i in range(9):
            for j in range(9):
                self.canvas.create_rectangle(self.proportion*100*i+self.proportion*15, self.proportion*100*j+self.proportion*15,self.proportion*100*(i+1)-self.proportion*15, self.proportion*100*(j+1)-self.proportion*15,fill="#621817");

        #On ajoute des cercles pour les joueurs
        self.canvas.create_oval(self.proportion*100*self.plateau.CoordonneeJoueur(1)[0]+self.proportion*15, self.proportion*100*self.plateau.CoordonneeJoueur(1)[1]+self.proportion*15,self.proportion*100*(self.plateau.CoordonneeJoueur(1)[0]+1)-self.proportion*15, self.proportion*100*(self.plateau.CoordonneeJoueur(1)[1]+1)-self.proportion*15,fill="#ffd849");
        self.canvas.create_oval(self.proportion*100*self.plateau.CoordonneeJoueur(2)[0]+self.proportion*15, self.proportion*100*self.plateau.CoordonneeJoueur(2)[1]+self.proportion*15,self.proportion*100*(self.plateau.CoordonneeJoueur(2)[0]+1)-self.proportion*15, self.proportion*100*(self.plateau.CoordonneeJoueur(2)[1]+1)-self.proportion*15,fill="#3673a6");

        #Affichage des barrières
        for i in range(8):
            for j in range(8):
                if self.plateau.barrieresVerticales[i][j] == 1:
                    self.canvas.create_rectangle((i+1)*100-15, j*100-7 ,(i+1)*100+15, (j+2)*100-7, fill="#f3e2bd");
                if self.plateau.barrieresHorizontales[i][j] == 1:
                    self.canvas.create_rectangle(i*100-7, (j+1)*100-15 ,(i+2)*100-7, (j+1)*100+15, fill="#f3e2bd");

        #On actualise l'affichage
        self.canvas.update();




    #Methode que l'on appelle pour commencer la partie
    def CommencerPartie(self):

        #Variable contenant le tour actuel
        tour = 1;

        #Tant que aucun joueur n'a gagnée
        while self.VerifierSiUnJoueurAGagne() == 0:

            print("\nC'est au tour du joueur ", tour);
            coupValide = False;

            #Tant que le joueur n'a pas joué un coup autorisee
            while coupValide == False:
                #On fait jouer le joueur dont c'est le tour de jouer
                depart = time.time();
                coupDuJoueur = self.joueur[tour-1].Jouer(self.fenetre, self.canvas, self.proportion, self.plateau);
                print("Temps pour joueur : " + str(time.time() - depart));

                #On vérifie si son coup est valide
                coupValide = self.VerifierSiCoupValide(coupDuJoueur, tour);

            #La boucle est fini -> Le coup à été validé et peut donc etre jouer
            #On fait donc jouer le coup au plateau
            #On décompte la barrière du joueur si il en a posé une
            if (coupDuJoueur.typeDeCoup == 1):
                print("Le joueur " + str(tour) + " se déplace");
            else:
                coupDuJoueur.nouveauPlateau.nbBarriere[tour-1] -= 1;
                #On appelle la fonction pour trouver les barrières interdites
                coupDuJoueur.nouveauPlateau.ActualiserBarrieresInterdites();
                print("Il reste " + str(coupDuJoueur.nouveauPlateau.nbBarriere[tour-1]) + " barrières au joueur " + str(tour));

            #On actualise le plateau
            self.plateau = coupDuJoueur.nouveauPlateau;

            #On actualise l'affichage
            self.ActualiserAffichage();

            #On change de tour
            tour = 3 - tour; #Technique pour alternr entre 1 et 2 comme valeure pour tour

        #La boucle est finie -> Un joueur a gagné
        #On regarde qui a gagné :
        gagnant = self.VerifierSiUnJoueurAGagne();

        #On affiche
        print("Victoire du Joueur " + str(gagnant));
        return gagnant;







#TOUT DEBUT DU PROGRAMME

#Première fonction appellée dans le programme
def main():

    #On lance le jeu
    j1 = IaLevel1(1)
    j2 = IaLevel2Acceleree(2)
    game = Game(j1,j2,100)
    game.CommencerPartie()

#Fonction pour entrainer le programme
def StartTrain(j, a, b, c):
    #On lance le jeu
    if j == 2:
        j1 = IaLevel1(1)
        j2 = IaLevel1Evolutive(2, a, b, c)
    else:
        j1 = IaLevel1Evolutive(1, a, b, c)
        j2 = IaLevel1(2)
        
    game = Game(j1,j2,100)
    result = game.CommencerPartie();
    game.destroy();
    if (result == j):
        return 1;
    else:
        return 0;


#Fonction pour entrainer le programme
def train():
    print("Train start");

    #On génère une population de 20 individus de manière aléatoires
    listeDIndividus = [];
    for i in range(30):
        listeDIndividus.append((randint(1,20), randint(1,20), randint(0,200)));

    tableauVictoire = [];
    #On fait jouer ses matchs à chaque individus
    for k in range(15):
        victoire = 0;
        for i in range(50):
            if i > 9:
                tour = 1;
            else:
                tour = 2;

            print("\n\nDEBUT DU MATCH " + str(i+1) + " AVEC INDIVIDU N " + str(k+1) + " DE TYPE (" + str(listeDIndividus[k][0]) + ";" + str(listeDIndividus[k][1]) + ";" + str(listeDIndividus[k][2]) + ")");
            victoire += StartTrain(tour, listeDIndividus[k][0], listeDIndividus[k][0], listeDIndividus[k][0]);
        
        #On note ses stats
        tableauVictoire.append(victoire);

    #On affiche le tableau :
    for k in range (30):
        print("Joueur " + str(k+1) + " : " + "(" + str(listeDIndividus[k][0]) + ";" + str(listeDIndividus[k][1]) + ";" + str(listeDIndividus[k][2]) + ") -> " + str(tableauVictoire[k]) + " victoire(s)");
    print("Fin");




#Definition de la fonction main
if __name__ == "__main__":
    main()