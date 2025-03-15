def convertir_position(pos):
    """Convertit un numéro de case (1-9) en coordonnées (ligne, colonne)."""
    return (pos - 1) // 3, (pos - 1) % 3

def coup_valide(grille, pos):
    """Vérifie si la case est vide et valide."""
    ligne, colonne = convertir_position(pos)
    return grille[ligne][colonne] == " "

def changer_joueur(joueur):
    """Alterner entre les joueurs X et O."""
    return "O" if joueur == "X" else "X"

# Initialisation
grille = [[" " for _ in range(3)] for _ in range(3)]
joueur_actuel = "X"

# Boucle du jeu
while True:
    print(f"Tour du joueur {joueur_actuel}")

    try:
        pos = int(input("Entrez un numéro de case (1-9) : "))

        if pos not in range(1, 10):
            print("Numéro invalide. Choisissez un chiffre entre 1 et 9.")
            continue  # Redemande la saisie
        ligne, colonne = convertir_position(pos)
        if coup_valide(grille, pos):
            grille[ligne][colonne] = joueur_actuel  # Place le symbole du joueur
            joueur_actuel = changer_joueur(joueur_actuel)  # Change de joueur
        else:
            print("Case déjà occupée. Veuillez réessayer.")

    except ValueError:
        print("Entrée invalide. Veuillez entrer un chiffre.")
