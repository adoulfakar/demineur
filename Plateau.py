import numpy
import pandas as pd


def getplateau():
    """
        :return plateau: Dataframe de 100 case (10 x 10). Les lignes sont représentées par des lettres (A, B,..., J) et
        les colonnes par des numéros (1, 2,..., 10).
    """

    arr = numpy.arange(100).reshape(10, 10)
    numpy.random.shuffle(arr)
    plateau_arr = numpy.ma.array(arr)
    plateau = pd.DataFrame(plateau_arr, columns=range(1, 11), index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
    return plateau

