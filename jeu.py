print("BIENVENUE DANS LE JEU DU MORPION !!!")
def afficher_plateau(plateau):
    for ligne in plateau:
        print(" | ".join(ligne))
        print("-" * 9)
grille = [[" " for _ in range(3)] for _ in range(3)]
afficher_plateau(grille)
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

def check_winner(board, player):
   
    for row in board:
        if all(cell == player for cell in row):
            return True

  
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

  
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def board_full(board):
    return all(cell != " " for row in board for cell in row)
joueur_actuel = "X"
while True:
    try:
            print(f"Tour du joueur {joueur_actuel}")
            pos = int(input("Entrez un numéro de case (1-9) : "))

            if pos not in range(1, 10):
                print("Numéro invalide. Choisissez un chiffre entre 1 et 9.")
                continue
            ligne, colonne = convertir_position(pos)
            if coup_valide(grille, pos):
                grille[ligne][colonne] = joueur_actuel  # Place le symbole du joueur
                afficher_plateau(grille)
                if check_winner(grille,joueur_actuel):
                    print(f'Félicitations {joueur_actuel} vous avez gagné')
                    break
                if board_full(grille):
                    print("Personne n'a gagné. Félicitations à vous deux!!!")
                    break
                joueur_actuel = changer_joueur(joueur_actuel)  # Change de joueur
            else:
                print("Case déjà occupée. Veuillez réessayer.")
    except ValueError:
        print("Entrée invalide. Veuillez entrer un chiffre.")
