
class Affichage:
    
    def ligne_joueur(self, joueur, est_courant): #Renvoie une ligne de texte décrivant un joueur. est_courant : True si c'est le tour de ce joueur (il est alors marqué d'un ">"). Exemple : "> Traye | 3 pièces | Monuments : Gare"
        marque = ">" if est_courant else " "
        if len(joueur.monuments) == 0:
            monuments = "aucun"
        else:
            monuments = " , " .join(sorted(joueur.monuments)) #  sorted : ordre alphabétique, pour que l'affichage soit toujours le même (un set n'a pas d'ordre, ce qui ferait échouer les tests)
        return f"{marque} {joueur.nom} | {joueur.pieces} pièces | Monuments : {monuments}"
    
    def etat_joueurs(self, joueurs, indice_courant): # Renvoie le texte décrivant tous les joueurs, un par ligne. indice_courant : position, dans la liste, du joueur dont c'est le tour.
        lignes = []
        for i in range(len(joueurs)):
            est_courant =
