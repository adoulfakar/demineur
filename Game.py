""" import modules """

import numpy
import pandas as pd
import pickle
import os

""" la methode play lance la partie de jeu """


def play(plateau, mines, entered_cases=None):
    """
    :param plateau: tableau de 100 cases (10*10) contenant des nombres de 0 a 99
    :param mines: n mines generees aleatoirement selon le niveau de jeu selectionne
    :param entered_cases: les cases deja saisies
    :return:
    """
    while True:
        try:
            n_ligne = input("Saisissez un caractère représentant une ligne : ")
            if not n_ligne or n_ligne not in "abcdefjhij":
                raise TypeError
            break
        except TypeError:
            print("Veuillez saisir un caractère parmi les lettres (a,b,..,j)")

    while True:
        try:
            n_colonne = int(input("Saisissez un numero de colonne : "))
            if not n_colonne or n_colonne not in range(1, 11):
                raise ValueError
            break
        except ValueError:
            print("Veuillez saisir un numero parmi (1,2,..,10)")

    # Verifier si la case choisie ne contient pas une mine
    if plateau.get(n_colonne)[n_ligne] in mines:
        print('Vous etes tombé sur une mine, Game Over!')
        print('Votre score final est de : ' + str(numpy.sum(entered_cases)) + ' points.')
        os.remove('savedData.txt')

    # Verifier si la case choisie n'a pas encore ete choisie
    elif entered_cases and plateau.get(n_colonne)[n_ligne] in entered_cases:
        print("case deja choisie, saisissez d'autres coordonnees.")
        # Si c'est le cas on demande au joueur de resaisir d'autres cooronnees
        play(plateau, mines, entered_cases)
    else:
        # case choisie ne contenant pas de mine a demasquer
        case_to_unmask = plateau.get(n_colonne)[n_ligne]

        if entered_cases is None:
            entered_cases = []
        # Ajouter la case choisie à la liste des cases déja selectionnées
        entered_cases.append(int(case_to_unmask))

        # Cette fonction renvoie une liste 2D de booleans a True dans des cases correspondant aux cases deja choisies
        # Cette liste est utilisee pour construire le mask du plateau
        masked_arr = numpy.isin(plateau, entered_cases, invert=True)
        # Convertir la liste des masks en Dataframe
        masked_df = pd.DataFrame(masked_arr, columns=range(1, 11),
                                  index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

        # pandas.DataFrame.mask renvoie le dataframe en entrée avec ses valeurs masquées
        # selon le df défini dans l'argument cond
        new_plateau_df = plateau.mask(cond=masked_df, other="--")

        print(new_plateau_df)
        print('Votre score est de : ' + str(numpy.sum(entered_cases)) + ' points.')

        # Enegistrer la partie
        with open('savedData.txt', 'wb') as savedData:
            pickler = pickle.Pickler(savedData)
            pickler.dump(plateau)
            pickler.dump(mines)
            pickler.dump(entered_cases)

        # Relancer un nouveau tour
        play(plateau, mines, entered_cases)
