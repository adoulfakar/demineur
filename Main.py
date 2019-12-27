""" import modules """

from DemineurPkg import Plateau, Mine, Game
import os
import pickle

# Check si le joueur a déja une partie sauvegardée
exists = os.path.isfile('savedData.txt')
if exists:
    with open('savedData.txt', 'rb') as savedData:
        unPickler = pickle.Unpickler(savedData)
        # Le unpickler va charger les objets selon l'ordre dans lequel ils ont été enregistrés
        plateau = unPickler.load()
        mines = unPickler.load()
        entered_cases = unPickler.load()
        Game.play(plateau, mines, entered_cases)
else:
    # Generer le plateau de jeu
    plateau = Plateau.getplateau()

    # print(plateau)
    while True:
        try:
            niveau = int(input("Selctionnez un niveau de jeu parmi les niveaux suivants : \n " +
                               "(debutant : 1; medium : 2; difficile :3; expert : 4) : "))
            if niveau not in [1, 2, 3, 4]:
                raise ValueError
            break
        except ValueError:
            print("Veuillez saisir une valeur numérique de 1 à 4")

    # Générer les cases contenant une mine
    mines = Mine.mines(niveau)
    # print(mines)

    # Une fois le plateau et les mines sont générés, nous lançons la partie
    Game.play(plateau, mines)





