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
        """Renvoie True si on a lancé 2 dés de même valeur (un double)."""
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
        
    def paiements(self, total):
        """Cartes rouges: le joueur actuel paie les autres, dans le sens inverse des aiguilles d'une montre."""
        n = len(self.joueurs)
        for i in range(1, n):
            indice = (self._indice_courant -i) % n
            proprietaire = self._joueurs[indice]
            for carte in proprietaire.ville.etablissements:
                if isinstance(carte, Rouge) and carte.est_active(total, False):       # isinstance(carte, Rouge) veut dire « cette carte est-elle une carte rouge ? ». On l'utilise parce que les trois couleurs n'ont pas la même signature d'appliquer_effet, donc on s'adapte à chacune sans lui demander de changer.
                    carte.appliquer_effet(proprietaire, self.joueur_actuel )

    def revenus(self, total):
        """ cartes bleues (tous les joueurs) puis vertes (joueur actuel) : revenus de la banque."""
        # cartes bleues: elles rapportent à leur propriétaire, quelque soit le joueur qui a lancé
        for joueur in self.joueurs:
            for carte in joueur.ville.etablissements:
                if isinstance(carte, Bleu) and carte.est_active(total, joueur == self.joueur_actuel):
                    carte.appliquer_effet(joueur)
                    
        # cartes vertes: seulement pour le joueur dont c'est le tour
        for carte in self.joueur_actuel.ville.etablissements:
            if isinstance(carte, Vert) and carte.est_active(total, True):
                carte.appliquer_effet(self.joueur_actuel)
         
    def tour_joueur(self):           # relancer : simule le choix du joueur de relancer ses dés. Cette option n'a d'effet que si le joueur possède la Tour radio (règle du livret : "une fois par tour, vous pouvez choisir de relancer vos dés")
        """Déroule un tour complet du joueur courant."""
        joueur = self.joueur_actuel # le joueur courant

        nb_des = 1
        if joueur.ville.a_monument("Gare"):
            nb_des = 2
        resultats = self.lancer_des(nb_des)     # lancer nb_des dé avec lancer_des
       
        if joueur.ville.a_monument("Tour radio") and self.souhaite_relancer():
            resultats = self.lancer_des(nb_des) # Le nouveau lancer REMPLACE l'ancien : une variable ne garde qu'une seule valeur à la fois, donc l'ancien résultat est oublié, même s'il était meilleur. C'est le nouveau qui compte pour la suite.

        total = sum(resultats)      # additionner les dés avec sum(...)
        self.paiements(total)       # Effets des cartes : d'abord les paiements, puis les revenus
        self.revenus(total)
        self.achat_cartes()         # l'achat

        # Parc d'attractions : un double fait rejouer, donc on ne passe pas la main
        rejoue = False
        if joueur.ville.a_monument("Parc d'attractions") and self.de_double(resultats):
            rejoue = True          # donc on ne change pas d'indice courant et on reste sur le meme joueur, ça rejoue pour le meme joueur
        if not rejoue:             # "not" inverse : si ce n'est pas le cas     
            self.joueur_suivant()  
    
        return resultats, total


    # --- Achat de cartes (écrit par ma camarade) ---


    def souhaite_acheter(self) -> bool:
        """Demande au joueur s'il veut acheter une carte."""
        reponse = input("Souhaitez-vous acheter une carte ? (1 = Oui, 0 = Non) : ")
        return reponse == "1"

    def achat_cartes(self):
        """Fait acheter une carte (établissement ou monument) au joueur actuel. Renvoie True si l'achat a eu lieu, False sinon."""
        if not self.souhaite_acheter():
            return False

        nom = input("Quelle carte souhaitez-vous acheter ? ")   # attention à l'orthographe
        joueur = self.joueur_actuel

        # Cas 1 : un établissement (il est dans la réserve)
        if nom in self._reserve._cartes:
            if not self._reserve.est_disponible(nom):
                print("Cette carte n'est plus disponible.")
                return False

            carte = self._reserve._cartes[nom]["objet"]   # pour connaître son coût
            prix = carte.cout

            if joueur.argent >= prix:        # on vérifie AVANT de payer
                joueur.payer(prix)
                carte = self._reserve.prendre_carte(nom)
                joueur.ville.ajouter_carte(carte)
                return True

            print("Le joueur n'a pas assez d'argent")
            return False

        # Cas 2 : un monument (il est déjà dans la ville, à l'état « non construit »)
        else:
            for monument in joueur.ville.monuments:
                if monument.nom == nom:
                    if monument.construit:
                        print("Monument déjà construit")
                        return False

                    if joueur.argent >= monument.cout:
                        joueur.payer(monument.cout)
                        monument.construire()
                        return True

                    print("Pas assez d'argent")
                    return False

            print("Ce monument n'existe pas.")
            return False
