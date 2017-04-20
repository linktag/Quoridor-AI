from random import randint
from IaLevel1 import IaLevel1

class IaLevel2:
    """
    Ia de niveau 2 : elle est capable de plus au moins anticiper la r�action de l'adversaire
    Caract�ristiques :
    - Niveau moyen
    - Temps de jeu moyen : d�pend du coup : si le meilleur coup est un d�placement, environ 5s
    Si le meilleur coup est une barri�re il peut prendre longtemps
    Temps maximum dans le pire des cas : 4 mins 42 secondes
    """

    #Constructeur
    def __init__ (self, numero):
        self.numero = numero;

    #Methodes
    #Fonction Jouer qui fait jouer l'IA
    #Le fonctionnement de cette fonction est tres proche de celle pour IALevel1
    #Sauf qu'au lieu d'�valuer les coups directement a partir de la fonction d'evaluation, on passe par la fonction Anticpation
    def Jouer(self, fenetre, canvas, proportion, plateau):
        #Pour jouer, nous allons dans un premier temps g�n�rer tous les coups que nous pouvons jouer
        tousLesCoups = plateau.TousLesCoups(self.numero);

        #On les notes tous et on joue le meilleur
        meilleurNote = -1000;
        for i in range(len(tousLesCoups)):
            note = IaLevel2.Anticipation(tousLesCoups[i].nouveauPlateau, self.numero);
            print(str(i) + " done | note  : " + str(note));
            if (note > meilleurNote):
                meilleurNote = note;
                indexMeilleursCoups = i;


        print("Meilleur coup : " + str(indexMeilleursCoups) + " with " + str(meilleurNote));
        
        #On joue le coup
        return tousLesCoups[indexMeilleursCoups];

    #Methode permettant d'anticiper les coups adverses pour un plateau donn�
    def Anticipation(plateau, numero):
        #Pour anticiper le coup adverse, il nous faut deja tous les simul�s pour ce coup ci
        tousLesCoups = plateau.TousLesCoups(3-numero);

        #A present, on va supposer que l'adversaire fasse toujours le meilleur coup possible
        #On va donc chercher le meilleur coup parmis tous les coups simul�s
        pireNote = 1000;
        for coup in tousLesCoups:
            note = IaLevel2.Evaluer(coup.nouveauPlateau, numero);
            if (note < pireNote):
                pireNote = note;

        #On a donc la note la plus basse pour tout ce que l'adversaire peut r�pondre
        return pireNote;


    #Methode evaluant un plateau de jeu, lui donnant une note en fonction de la situation
    def Evaluer(plateau, nbJoueur):
        #On releve l'avantage en barriere
        avantageBarriere = plateau.nbBarriere[0] - plateau.nbBarriere[1];

        #On releve le nombre de case d'avance que l'on a:
        distanceJ1 = plateau.BreadthFirstSearch(plateau.CoordonneeJoueur(1), 0);
        distanceJ2 = plateau.BreadthFirstSearch(plateau.CoordonneeJoueur(2), 8);
        avantageDistance = distanceJ2 - distanceJ1;

        #Si un des joueurs a gagner, on donne une tres grosse note
        if (distanceJ1 == 0):
            avantageDistance = 200;
        if (distanceJ2 == 0):
            avantageDistance = -200;

        #On fait la somme pour avoir l'avantage
        avantage = avantageBarriere + avantageDistance;

        #Si un des joueurs s'approche de l'arriv�e, on augmente l'importance de l'avantage distance
        if (distanceJ1 == 1 or distanceJ2 == 1):
            avantage = avantage*1.5;

        #On inverse si on veut l'avantage du joueur 2
        if (nbJoueur == 2):
            avantage = -1 * avantage;
        return avantage;

class IaLevel2Acceleree:
    """
    Ia de niveau 2 : elle est capable de plus au moins anticiper la r�action de l'adversaire
    Caract�ristiques :
    - Niveau moyen
    - Temps de jeu moyen : d�pend du coup : si le meilleur coup est un d�placement, environ 5s
    Si le meilleur coup est une barri�re il peut prendre longtemps
    Temps maximum dans le pire des cas : 4 mins 42 secondes
    """

    #Constructeur
    def __init__ (self, numero):
        self.numero = numero;

    #Methodes
    #Fonction Jouer qui fait jouer l'IA
    #Le fonctionnement de cette fonction est tres proche de celle pour IALevel1
    #Sauf qu'au lieu d'evaluer les coups directement a partir de la fonction d'evaluation, on passe par la fonction Anticpation
    def Jouer(self, fenetre, canvas, proportion, plateau):
        #Pour jouer, nous allons dans un premier temps g�n�rer tous les coups que nous pouvons jouer
        if (plateau.nbBarriere[self.numero-1] > 0):
            tousLesCoups = plateau.TousLesCoups(self.numero);
        else:
            tousLesCoups = plateau.TousLesCoupsSansBarrieres(self.numero);

        #On les notes tous et on joue le meilleur
        meilleurNote = -100000;
        alpha = 100000;
        for i in range(len(tousLesCoups)):
            if i == 0:
                note = IaLevel2Acceleree.Anticipation(tousLesCoups[i].nouveauPlateau, self.numero, -100000);
            else:
                note = IaLevel2Acceleree.Anticipation(tousLesCoups[i].nouveauPlateau, self.numero, alpha);
            print(str(i) + " done | note  : " + str(note));
            if (note > alpha):
                alpha = note;
            if (note > meilleurNote):
                meilleurNote = note;
                indexMeilleursCoups = i;


        print("Meilleur coup : " + str(indexMeilleursCoups) + " with " + str(meilleurNote));
        
        #On joue le coup
        return tousLesCoups[indexMeilleursCoups];

    #Methode permettant d'anticiper les coups adverses pour un plateau donn�
    def Anticipation(plateau, numero, limite):
        #Pour anticiper le coup adverse, il nous faut deja tous les simul�s pour ce coup ci
        tousLesCoups = plateau.TousLesCoups(3-numero);

        #A present, on va supposer que l'adversaire fasse toujours le meilleur coup possible
        #On va donc chercher le meilleur coup parmis tous les coups simul�s
        pireNote = 1000;
        for coup in tousLesCoups:
            note = IaLevel1.Evaluer(coup.nouveauPlateau, numero);
            if (note <= limite):
                return note;
            if (note < pireNote):
                pireNote = note;

        #On a donc la note la plus basse pour tout ce que l'adversaire peut r�pondre
        return pireNote;


    #Methode evaluant un plateau de jeu, lui donnant une note en fonction de la situation
    def Evaluer(plateau, nbJoueur):
        #On releve l'avantage en barriere
        avantageBarriere = plateau.nbBarriere[0] - plateau.nbBarriere[1];

        #On releve le nombre de case d'avance que l'on a:
        distanceJ1 = plateau.BreadthFirstSearch(plateau.CoordonneeJoueur(1), 0);
        distanceJ2 = plateau.BreadthFirstSearch(plateau.CoordonneeJoueur(2), 8);
        avantageDistance = distanceJ2 - distanceJ1;

        #Si un des joueurs a gagner, on donne une tres grosse note
        if (distanceJ1 == 0):
            avantageDistance = 200;
        if (distanceJ2 == 0):
            avantageDistance = -200;

        #On fait la somme pour avoir l'avantage
        avantage = avantageBarriere + avantageDistance;

        #Si un des joueurs s'approche de l'arriv�e, on augmente l'importance de l'avantage distance
        if (distanceJ1 == 1 or distanceJ2 == 1):
            avantage = avantage*1.5;

        #On inverse si on veut l'avantage du joueur 2
        if (nbJoueur == 2):
            avantage = -1 * avantage;
        return avantage;