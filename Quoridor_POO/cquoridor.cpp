#include <Python.h>
#include <list>         
#include <queue>

using namespace std;

//C++ function
int BreadthFirstSearch(vector<int> positionDeDepart, int ligneAAtteindre, int barrieresHorizontales[8][8], int barrieresVerticales[8][8])
{
	//On creer tout ce qu'il faut pour l'algorithme
	queue<vector<int>> liste;
	queue<int> listeDistance;
	set<vector<int>> visite;

	//On ajoute la position actuelle
	liste.push(positionDeDepart);
	listeDistance.push(0);

	//On marque la position comme d�ja pass�e
	visite.insert(positionDeDepart);

	//On commence la boucle
	while (liste.empty() == false)
	{
		//On recup�re la position la plus lointaine ajout�e et on la supprime
		int distance = listeDistance.front();
		vector<int> positionActuelle = liste.front();
		listeDistance.pop();
		liste.pop();

		//On regarde tous les voisins de cette position, que l'on va explorer :
		//Tentative de mouvement vers le haut
		if (positionActuelle[1] > 0)
		{
			//On creer la position
			vector<int> newPosition{ positionActuelle[0], positionActuelle[1] - 1 };

			//Si on n'a pas deja visiter cette case
			if (visite.find(newPosition) == visite.end())
			{
				//On v�rifie si une barri�re se trouve au dessus
				if ((positionActuelle[0] == 0 && barrieresHorizontales[positionActuelle[0]][positionActuelle[1] - 1] == 0) || (positionActuelle[0] == 8 && barrieresHorizontales[positionActuelle[0] - 1][positionActuelle[1] - 1] == 0) || (positionActuelle[0] != 0 && positionActuelle[0] != 8 && barrieresHorizontales[positionActuelle[0]][positionActuelle[1] - 1] == 0 && barrieresHorizontales[positionActuelle[0] - 1][positionActuelle[1] - 1] == 0))
				{
					//On peut se rendre sur cette case
					//Si on a atteint note but :
					if (newPosition[1] == ligneAAtteindre)
						return distance + 1;
					//On l'ajoute � la liste
					liste.push(newPosition);
					listeDistance.push(distance + 1);
					visite.insert(newPosition);
				}
			}
		}

		//Tentative de mouvement vers le bas
		if (positionActuelle[1] < 8)
		{
			//On creer la position
			vector<int> newPosition{ positionActuelle[0], positionActuelle[1] + 1 };

			//Si on n'a pas deja visiter cette case
			if (visite.find(newPosition) == visite.end())
			{
				//On v�rifie si une barri�re se trouve au dessus
				if ((positionActuelle[0] == 0 && barrieresHorizontales[positionActuelle[0]][positionActuelle[1]] == 0) || (positionActuelle[0] == 8 && barrieresHorizontales[positionActuelle[0] - 1][positionActuelle[1]] == 0) || (positionActuelle[0] != 0 && positionActuelle[0] != 8 && barrieresHorizontales[positionActuelle[0]][positionActuelle[1]] == 0 && barrieresHorizontales[positionActuelle[0] - 1][positionActuelle[1]] == 0))
				{
					//On peut se rendre sur cette case
					//Si on a atteint note but :
					if (newPosition[1] == ligneAAtteindre)
						return distance + 1;
					//On l'ajoute � la liste
					liste.push(newPosition);
					listeDistance.push(distance + 1);
					visite.insert(newPosition);
				}
			}
		}

		//Tentative de mouvement vers la gauche
		if (positionActuelle[0] > 0)
		{
			//On creer la position
			vector<int> newPosition{ positionActuelle[0] - 1, positionActuelle[1] };

			//Si on n'a pas deja visiter cette case
			if (visite.find(newPosition) == visite.end())
			{
				//On v�rifie si une barri�re se trouve au dessus
				if ((positionActuelle[1] == 0 && barrieresVerticales[positionActuelle[0] - 1][positionActuelle[1]] == 0) || (positionActuelle[1] == 8 && barrieresVerticales[positionActuelle[0] - 1][positionActuelle[1] - 1] == 0) || (positionActuelle[1] != 0 && positionActuelle[1] != 8 && barrieresVerticales[positionActuelle[0] - 1][positionActuelle[1]] == 0 && barrieresVerticales[positionActuelle[0] - 1][positionActuelle[1] - 1] == 0))
				{
					//On peut se rendre sur cette case
					//On l'ajoute � la liste
					liste.push(newPosition);
					listeDistance.push(distance + 1);
					visite.insert(newPosition);
				}
			}
		}

		//Tentative de mouvement vers la droite
		if (positionActuelle[0] < 8)
		{
			//On creer la position
			vector<int> newPosition{ positionActuelle[0] + 1, positionActuelle[1] };

			//Si on n'a pas deja visiter cette case
			if (visite.find(newPosition) == visite.end())
			{
				//On v�rifie si une barri�re se trouve au dessus
				if ((positionActuelle[1] == 0 && barrieresVerticales[positionActuelle[0]][positionActuelle[1]] == 0) || (positionActuelle[1] == 8 && barrieresVerticales[positionActuelle[0]][positionActuelle[1] - 1] == 0) || (positionActuelle[1] != 0 && positionActuelle[1] != 8 && barrieresVerticales[positionActuelle[0]][positionActuelle[1]] == 0 && barrieresVerticales[positionActuelle[0]][positionActuelle[1] - 1] == 0))
				{
					//On peut se rendre sur cette case
					//On l'ajoute � la liste
					liste.push(newPosition);
					listeDistance.push(distance + 1);
					visite.insert(newPosition);
				}
			}
		}
	}

	return -1;
}
