
""" SCRIPT DE DÉMONSTRATION (hors des classes) : 
Programme qui lance une partie de Miniville en mode texte (affichage ASCII). 
Il utilise Partie (le moteur) et Affichage (le texte), mais n'est ni une classe ni un test.
Pour l'instant : 3 tours de démonstration, sans revenus ni achats (on attend
les classes Carte et Joueur du groupe). """

partie = Partie([Joueur("Traye"), Joueur("Elia")], graine=42)
affichage = Affichage()

for numero in range(1, 4):
    print(f"--- Tour {numero} ---")
    print(affichage.etat_joueurs(partie.joueurs, partie.indice_courant))
    joueur = partie.joueurs[partie.indice_courant]                                    # le joueur qui va jouer
    print(affichage.texte_tour(joueur, "debut"))
    resultats, total = partie.tour_joueur()
    print(affichage.texte_lancer(joueur, resultats))  




# petit programme provisoire qui fait jouer une partie de 3 tours

partie = Partie([Joueur("Traye"), Joueur("Elia")], graine=42)
partie.joueurs[0].monuments.update({"Gare", "Parc d'attractions"})   # pour tester le rejeu
affichage = Affichage()

for numero in range(1, 4):
    print(f"--- Tour {numero} ---")
    print(affichage.etat_joueurs(partie.joueurs, partie.indice_courant))
    joueur = partie.joueurs[partie.indice_courant]
    print(affichage.texte_tour(joueur, "debut"))
    resultats, total = partie.tour_joueur()
    print(affichage.texte_lancer(joueur, resultats))
    print(affichage.dessin_des(resultats))


    # Rejeu : même condition que dans tour_joueur
    if joueur.a_monument("Parc d'attractions") and partie.de_double(resultats):
        print(affichage.texte_tour(joueur, "rejoue"))

    input("Appuyez sur Entrée pour continuer...")
