""" import modules """

from random import randint


def mines(niveau):
    """
    :param niveau: niveau de jeu selectionne
    :return mines_list: liste de mines selon le niveau de jeu en entree
    """
    mines_list = []
    # Boucle for pour valoriser la liste avec niveau * valeurs aleatoires
    for i in range(0, niveau):
        # Generer un entier entre 0 et 99
        mine = randint(0, 99)
        mines_list.append(mine)
    return mines_list
