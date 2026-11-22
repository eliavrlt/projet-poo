import random

class Partie:
    def __init__(self, joueurs, graine=None):
        self.joueurs = joueurs                # liste d'objets Joueur
        self.indice_courant = 0               # à qui le tour
        self.rng = random.Random(graine)      # hasard reproductible pour les tests

    def lancer_des(self, nb_des):
        """Lance nb_des dés et renvoie la liste des résultats."""
        resultats = []
        for i in range(nb_des):
            de = self.rng.randint(1,6) 
            resultats.append(de)
        return resultats 
        
    def de_double(self, resultats):
        if len(resultats) == 2:
            return resultats[0]==resultats[1]
        else:
            return False

    def joueur_suivant(self):
        """Passe la main au joueur suivant (sens horaire). Convention du projet : l'ordre de la liste self.joueurs est l'ordre des joueurs autour de la table, dans le sens horaire. Passer au joueur d'indice + 1 revient donc à passer au joueur suivant dans le sens horaire, comme l'impose la règle du jeu"""
        self.indice_courant = (self.indice_courant + 1)%len(self.joueurs) # L'opérateur % (modulo) donne le reste de la division par le nombre de joueurs : il ramène l'indice à 0 après le dernier joueur, ce qui fait boucler le tour.

    def tour_joueur(self):
        """Déroule un tour complet du joueur courant."""
        pass
