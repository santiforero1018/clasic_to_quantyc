""" Libreria simulación de lo clasico a lo cuantico
Santiago Forero Yate
CNYT

"""


import math
import Libreria_numeros_complejos as nc


def interferencias(matriz):
    """funcion que regresa las interferencias de un sistema

    :param matriz: matriz de un sistema de rendijas
    :return: matriz de interferencias
    """
    matriz_interfe = []
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            tempo = 0
            for l in range(len(matriz[i])):
                tempo1 = matriz[i][k] * matriz[k][j] + tempo
                if tempo1 == tempo and (matriz[i][j] != 0 or matriz[j][i] != 0):
                    matriz_interfe += [[i,j]]

    return matriz_interfe



def multi_rendijas(matriz, vector, clicks):
    """ función que multiplica una matriz por si misma y devuelve el vector estado despues de una cierta cantidad
    de clicks

    :param matriz: matriz adyacente al sistema
    :param vector: vector estado inicial
    :param clicks: cantidad de clicks
    :return: vector estado despues de los clicks
    """
    matriz_prod = nc.multiplicacion_matrices(matriz, matriz)
    vector_est = system_clikcs(matriz_prod, vector, clicks)

    return vector_est


def probabilistic_ad_matrix(matrix, frac):
    """ funcion que permite ingresar fracionarios a las entradas de una matriz booleana

    :param matrix: matriz booleana
    :param frac: numeros fraccionarios a rremplazar
    :return: matriz propabilistica
    """
    k = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                matrix[i][j] = frac[k]
                k += 1

    return matrix


def Boolean_ad_matrix(first_vertex, mov_vertex):
    """crea una matriz adyacente booleana

    :param first_vertex: vertices iniciales
    :param mov_vertex: vertices a donde llegan los vertices iniciales
    :return:matriz adyacente booleana
    """
    matriz_ad = [[(0, 0) for j in range(len(first_vertex))] for i in range(len(mov_vertex))]
    for i in range(len(first_vertex)):
        for j in range(len(mov_vertex)):
            if i == j:
                matriz_ad[mov_vertex[j]][first_vertex[i]] = (1,0)

    return matriz_ad


def system_clikcs(matriz_ad, vector, number):
    """determina el vector estado despues de una cierta cantidad de clicks

    :param matriz_ad: matriz adyacente al sistema
    :param vector: vector estado
    :param number: cantidad de clikcs
    :return: vector estado despues de number clicks
    """
    i = 0
    while i < number:
        vector_cl = nc.accionmatriz_vector(matriz_ad, vector)
        vector = vector_cl
        i += 1

    return vector
