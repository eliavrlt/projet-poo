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
        
    def de_double(resultats):
        if len(resultats) == 2:
            return resultats[0]==resultats[1]
        else:
            return False

    def joueur_suivant(self):
        """Passe la main au joueur suivant (sens horaire)."""
        pass

    def tour_joueur(self):
        """Déroule un tour complet du joueur courant."""
        pass
