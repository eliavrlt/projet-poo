import random


# En attendant que la classe Joueur soit définitivement créé, on utilise en reférence la classe suivante : 
class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.pieces = 3              # chaque joueur démarre avec 3 pièces
        self.monuments = set()       # noms des monuments construits, vide au départ

    def a_monument(self, nom):
        """Renvoie True si le joueur a construit ce monument."""
        return nom in self.monuments


class Partie:
    def __init__(self, joueurs, graine=None):
        self._joueurs = joueurs                # liste d'objets Joueur
        self._indice_courant = 0               # à qui le tour
        self._rng = random.Random(graine)      # hasard reproductible pour les tests
        self._reserve = Reserve()              # une reserve

    @property
    def joueurs(self):
        return self._joueurs

    @property
    def indice_courant(self):
        return self._indice_courant

    @property
    def joueur_actuel(self):
        """Le joueur dont c'est le tour."""
        return self._joueurs[self._indice_courant]
        

    def lancer_des(self, nb_des):
        """Lance nb_des dés et renvoie la liste des résultats."""
        resultats = []
        for _ in range(nb_des):
            de = self._rng.randint(1, 6) 
            resultats.append(de)
        return resultats 
        
    def de_double(self, resultats):
        if len(resultats) == 2:
            return resultats[0]==resultats[1]
        else:
            return False

    def joueur_suivant(self):
        """Passe la main au joueur suivant (sens horaire). Convention du projet : l'ordre de la liste self.joueurs est l'ordre des joueurs autour de la table, dans le sens horaire. Passer au joueur d'indice + 1 revient donc à passer au joueur suivant dans le sens horaire, comme l'impose la règle du jeu"""
        self._indice_courant = (self._indice_courant + 1)%len(self.joueurs) # L'opérateur % (modulo) donne le reste de la division par le nombre de joueurs : il ramène l'indice à 0 après le dernier joueur, ce qui fait boucler le tour.

    def souhaite_relancer(self):
        """Demande au joueur s'il relance ses dés (Tour radio)."""
        reponse = input("Souhaitez-vous relancer et supprimer votre ancien jet ? (1 = Oui, 0 = Non) : ")
        return reponse == "1"
         
    def tour_joueur(self):           # relancer : simule le choix du joueur de relancer ses dés. Cette option n'a d'effet que si le joueur possède la Tour radio (règle du livret : "une fois par tour, vous pouvez choisir de relancer vos dés")
        """Déroule un tour complet du joueur courant."""
        joueur = self.joueur_actuel # le joueur courant

        nb_des = 1
        if joueur.ville.a_monument("Gare"):
            nb_des = 2
        resultats = self.lancer_des(nb_des)     # lancer nb_des dé avec lancer_des
       
        if joueur.ville.a_monument("Tour radio") and self.souhaite_relancer():
            resultats = self.lancer_des(nb_des) # Le nouveau lancer REMPLACE l'ancien : une variable ne garde qu'une seule valeur à la fois, donc l'ancien résultat est oublié, même s'il était meilleur. C'est le nouveau qui compte pour la suite.

        rejoue = False
        if joueur.ville.a_monument("Parc d'attractions") and self.de_double(resultats):
            rejoue = True # donc on ne change pas d'indice courant et on reste sur le meme joueur, ça rejoue pour le meme joueur
        if not rejoue:             # "not" inverse : si ce n'est pas le cas
            self.joueur_suivant()
    
        total = sum(resultats)      # additionner les dés avec sum(...)
        return resultats, total
