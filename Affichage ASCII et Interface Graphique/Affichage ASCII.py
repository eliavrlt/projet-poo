
# Les dés en ASCII
# Les 3 lignes du milieu de chaque face (Chaque face est un tuple de 3 chaînes : rangée du haut, du milieu et du bas. Chaque chaîne fait exactement 7 caractères, espaces compris).
FACES_DES = {
    1: ("       ", "   o   ", "       "),
    2: ("     o ", "       ", " o     "),
    3: ("     o ", "   o   ", " o     "),
    4: (" o   o ", "       ", " o   o "),
    5: (" o   o ", "   o   ", " o   o "),
    6: (" o   o ", " o   o "," o   o ")}


class Affichage:
    
    def ligne_joueur(self, joueur, est_courant): #Renvoie une ligne de texte décrivant un joueur. est_courant : True si c'est le tour de ce joueur (il est alors marqué d'un ">"). Exemple : "> Traye | 3 pièces | Monuments : Gare"
        marque = ">" if est_courant else " "
        if len(joueur.monuments) == 0:
            monuments = "aucun"
        else:
            monuments = ", " .join(sorted(joueur.monuments)) #  sorted : ordre alphabétique, pour que l'affichage soit toujours le même (un set n'a pas d'ordre, ce qui ferait échouer les tests)
        return f"{marque} {joueur.nom} | {joueur.pieces} pièces | Monuments : {monuments}"
    
    def etat_joueurs(self, joueurs, indice_courant): # Renvoie le texte décrivant tous les joueurs, un par ligne. indice_courant : position, dans la liste, du joueur dont c'est le tour.
        lignes = []
        for i in range(len(joueurs)):
            est_courant = i == indice_courant
            lignes.append(self.ligne_joueur(joueurs[i], est_courant))
        return "\n".join(lignes)

    def texte_lancer(self, joueur, resultats):         # renvoie une phrase décrivant le lancer d'un joueur.
        mot = "dé" if len(resultats) == 1 else "dés"   # len(resultats) donne le nombre de dés, ce qui permet de choisir le singulier ou le pluriel
        return f"{joueur.nom} lance {len(resultats)} {mot} : {resultats} (total : {sum(resultats)})"




    def texte_tour(self, joueur, action, montant=None, carte=None, destinataire=None) : #  action : "debut", "gain", "achat", "paiement", "rejoue" ou "victoire". Lève une ValueError si l'action est inconnue.
        if action == "debut":
            return f"C'est au tour de {joueur.nom}."
        elif action == "gain":
            mot = "pièce" if montant ==1 else "pièces"
            return f"{joueur.nom} gagne {montant} {mot}."
        elif action == "achat":
            mot = "pièce" if montant == 1 else "pièces"
            return f"{joueur.nom} achète {carte} pour {montant} {mot}."
        elif action == "paiement":
            mot = "pièce" if montant == 1 else "pièces"
            return f"{joueur.nom} paie {montant} {mot} à {destinataire.nom}."
        elif action == "rejoue":
            return f"Double ! {joueur.nom} rejoue grâce au Parc d'attractions."
        elif action == "victoire":
            return f"{joueur.nom} a construit ses 4 monuments : victoire !"
        else: 
            raise ValueError(f"Action inconnue : {action}")

    def dessin_de(self, valeur):
        """Renvoie le dessin ASCII d'un dé (5 lignes), pour une valeur de 1 à 6."""
        bord = "+-------+"
        lignes = [bord]
        for ligne in FACES_DES[valeur]:
            lignes.append(f"|{ligne}|")     # entourer "ligne" d'une barre "|" de chaque côté
        lignes.append(bord)
        return "\n".join(lignes)
        
    def dessin_des(self, resultats):        # Renvoie le dessin ASCII de plusieurs dés côte à côte. resultats : la liste des valeurs, par exemple [6, 1].
        des = []
        for valeur in resultats:
            des.append(self.dessin_de(valeur).split("\n"))
        lignes = []
        for i in range(5):                  # on assemble les lignes 0 à 4, une par une
            morceaux = []
            for de in des:
                morceaux.append(de[i])           # la ligne numéro i de ce dé
            lignes.append("  ".join(morceaux))   # deux espaces entre les dés
        return "\n".join(lignes)
