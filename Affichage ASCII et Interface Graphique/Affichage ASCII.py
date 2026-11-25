
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
            est_courant = i == indice_courant
            lignes.append(self.ligne_joueur(joueurs[i], est_courant))
        return "\n".join(lignes)

    def texte_lancer(self, joueur, resultats):    # renvoie une phrase décrivant le lancer d'un joueur.
        mot = "dé" if len(resultats) == 1 else "dés"
        return f"{joueur.nom} lance {len(resultats)} {mot} : {resultats} (total : {sum(resultats})"



    # à verifier avec Claude : étape 5
    def texte_tour(self, joueur, action, montant=None, carte=None, destinataire=None) :
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
        else: 
            raise ValueError("Action inconnue")
        
