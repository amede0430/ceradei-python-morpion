from joueur.py import demander_case, verifier_dispo_case

# Afficher plateau
def afficher_plateau(plateau):
    for ligne in plateau:
        print(" | ".join(ligne))
        print("-" * 9)
        
#Mise à jour de la grille après chaque tour
def mise_a_jour():
    while True:
        choix = demander_case()  # le groupe 2 va Demander à l'utilisateur de choisir une case

        if not verifier_dispo_case(plateau, choix):  # le groupe 2 va Vérifier si la case est valide
            continue
        
        ligne, colonne = divmod(choix, 3)
    
        # Mets à jour le plateau avec le symbole du joueur actuel
        plateau[ligne][colonne] = joueur_actuel #le groupe 2 va gérer l'alternance du joueur avec la variable  
        break
        
#Afficher message(victoi,nul)
def afficher_message(message):
    print(message)