from random import randint

class IaLevel1:
    """
    Classe de l'IA de niveau 1, la plus faible.
    Elle n'est pas capable d'anticiper les actions adverses, elle voit seulement le meilleur coup à faire avec ce qu'elle a sous les yeux.
    Elle n'est pas très difficile à battre, elle tombe naturelement dans tous les pièges puisqu'elle ne réfléchis pas.
    Caractéristiques :
    - Tres faible, presque n'importe qui peut la battre
    - Tres rapide a jouer, elle joue un coup en environ 2.5 secondes
    
    Cette classe, comme toutes les classe IA, reprend la structure d'une classe joueur, comme une IA est un "joueur amélioré"
    Elle dispose donc des mêmes fonctions (bien qu'elle en est en plus), ce qui permet de ne pas avoir a réécrire le code du jeu :
    Le jeu jjoue avec elle comme il le ferrait avec un jouer humain, c'est une sorte d'utilisation de l'héritage en POO
    C'est d'ailleurs la force d'écriture de ce code, qui peut simplement en changeant les réglages s'adapter à tous les scénarios.
    """

    #Constructeur
    def __init__ (self, numero):
        self.numero = numero;

    #Methodes
    #Fonction Jouer qui fait jouer l'IA
    def Jouer(self, fenetre, canvas, proportion, plateau):
        #On a un plateau sous les yeux : il faut trouver le meilleur coup possible
        #Si on n'a plus de barrière, on appelle la variante sans barrières
        if (plateau.nbBarriere[self.numero-1] > 0):
            tousLesCoups = plateau.TousLesCoups(self.numero);
        else:
            tousLesCoups = plateau.TousLesCoupsSansBarrieres(self.numero);

        #On les notes tous et on joue le meilleur
        indexsMeilleursCoups = [];
        meilleurNote = -1000;
        for i in range(len(tousLesCoups)):
            note = IaLevel1.Evaluer(tousLesCoups[i].nouveauPlateau, self.numero);
            if (note > meilleurNote):
                meilleurNote = note;
                indexsMeilleursCoups = [];
                indexsMeilleursCoups.append(i);
            elif (note == meilleurNote):
                indexsMeilleursCoups.append(i);

        #On tire au hasard un des coups parmis les meilleurs
        if (len(indexsMeilleursCoups) == 1):
            index = indexsMeilleursCoups[0];
        else:
            index = indexsMeilleursCoups[randint(0,len(indexsMeilleursCoups)-1)];

        #On joue le coup
        return tousLesCoups[index];


    #Methode evaluant un plateau de jeu, lui donnant une note en fonction de la situation
    def Evaluer(plateau, nbJoueur):

        #On releve l'avantage en barriere
        avantageBarriere = plateau.nbBarriere[0] - plateau.nbBarriere[1];

        #On releve le nombre de case d'avance que l'on a:
        distanceJ1 = plateau.BreadthFirstSearch(plateau.CoordonneeJoueur(1), 0);
        distanceJ2 = plateau.BreadthFirstSearch(plateau.CoordonneeJoueur(2), 8);
        avantageDifferenceDistance = distanceJ2 - distanceJ1;

        #On ajoute également l'inverse des distances dans les calculs, l'avantage étant inversement proportionel à la distance
        #En effet, plus la distance nous spéarant de l'arrivée est petite, plus l'avantage est grand
        if (distanceJ1 > 0):
            avantageD1 = 1 / distanceJ1;
        else:
            avantageD1 = 1000;

        if (distanceJ2 > 0):
            avantageD2 = 1 / distanceJ2;
        else:
            avantageD2 = 1000;

        avantageDistance = avantageD1 - avantageD2;

        #On fait la somme pour avoir l'avantage
        avantage = avantageBarriere + avantageDifferenceDistance + 5*avantageDistance;

        #On inverse si on veut l'avantage du joueur 2
        if (nbJoueur == 2):
            avantage = -1 * avantage;

        return avantage;


class IaLevel1Evolutive:
    """
    Classe de l'IA de niveau 1, la plus faible.
    Cette variante a pour but de trouver les meilleurs coeficients pour la fonction d'évaluation
    """

    #Constructeur
    def __init__ (self, numero, a, b, c):
        self.numero = numero;
        self.a = a;
        self.b = b;
        self.c = c;

    #Methodes
    #Fonction Jouer qui fait jouer l'IA
    def Jouer(self, fenetre, canvas, proportion, plateau):
        #On a un plateau sous les yeux : il faut trouver le meilleur coup possible
        #Si on n'a plus de barrière, on appelle la variante sans barrières
        if (plateau.nbBarriere[self.numero-1] > 0):
            tousLesCoups = plateau.TousLesCoups(self.numero);
        else:
            tousLesCoups = plateau.TousLesCoupsSansBarrieres(self.numero);

        #On les notes tous et on joue le meilleur
        indexsMeilleursCoups = [];
        meilleurNote = -1000;
        for i in range(len(tousLesCoups)):
            note = self.Evaluer(tousLesCoups[i].nouveauPlateau, self.numero);
            if (note > meilleurNote):
                meilleurNote = note;
                indexsMeilleursCoups = [];
                indexsMeilleursCoups.append(i);
            elif (note == meilleurNote):
                indexsMeilleursCoups.append(i);

        #On tire au hasard un des coups parmis les meilleurs
        if (len(indexsMeilleursCoups) == 1):
            index = indexsMeilleursCoups[0];
        else:
            index = indexsMeilleursCoups[randint(0,len(indexsMeilleursCoups)-1)];

        #On joue le coup
        return tousLesCoups[index];


    #Methode evaluant un plateau de jeu, lui donnant une note en fonction de la situation
    def Evaluer(self, plateau, nbJoueur):

        #On releve l'avantage en barriere
        avantageBarriere = plateau.nbBarriere[0] - plateau.nbBarriere[1];

        #On releve le nombre de case d'avance que l'on a:
        distanceJ1 = plateau.BreadthFirstSearch(plateau.CoordonneeJoueur(1), 0);
        distanceJ2 = plateau.BreadthFirstSearch(plateau.CoordonneeJoueur(2), 8);
        avantageDifferenceDistance = distanceJ2 - distanceJ1;

        #On ajoute également l'inverse des distances dans les calculs, l'avantage étant inversement proportionel à la distance
        #En effet, plus la distance nous spéarant de l'arrivée est petite, plus l'avantage est grand
        if (distanceJ1 > 0):
            avantageD1 = 1 / distanceJ1;
        else:
            avantageD1 = 1000;

        if (distanceJ2 > 0):
            avantageD2 = 1 / distanceJ2;
        else:
            avantageD2 = 1000;

        avantageDistance = avantageD1 - avantageD2;

        #On fait la somme pour avoir l'avantage
        avantage = self.a*avantageBarriere + self.b*avantageDifferenceDistance + self.c*avantageDistance;

        #On inverse si on veut l'avantage du joueur 2
        if (nbJoueur == 2):
            avantage = -1 * avantage;

        return avantage;