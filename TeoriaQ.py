"""PRACTICA DE LA TEORIA CUANTICA
SANTIAGO FORERO YATE
CNYT
"""
import sistemas_cuanticos_cnyt as sc
import Libreria_numeros_complejos as nc
import math
import numpy as np


def cuatro2(biliar_matriz, ket, num):
    """resolucion del ejercicio 4.4.2

    :param biliar_matriz: matriz adyacent a la bola de billar
    :param ket: estado inicial
    """
    solution = sc.system_clikcs(biliar_matriz, ket, num)

    return solution


def cuatro1(matriz1, matriz2):
    """Resolucion del porblema 4.4.1

    :param matriz1: posible matriz unitaria
    :param matriz2: posible matriz unitaria

    :return: un booleano
    """
    if nc.unitaria(matriz1) and nc.unitaria(matriz2):
        product = nc.multiplicacion_matrices(matriz1, matriz2)
        if nc.unitaria(product):
            return True

    return False


def eingenvalues_vectors(matriz_ob):
    """funcion que calcula los valores y vectores propios de una matriz

    :param matriz_ob: observable
    :return: valores propios y vectores propios
    """
    matriz = np.array(matriz_ob)
    eingenvalues, eingenvectors = np.linalg.eig(matriz)

    return eingenvalues, eingenvectors


def generador_idn(matriz):
    """funcion que genera una matriz identidad

    :param matriz: lista en 2D
    :return: matriz identidad
    """
    midentidad = [[(0, 0) for j in range(len(matriz))] for i in range(len(matriz))]
    for i in range(len(midentidad)):
        for j in range(len(midentidad[0])):
            if i == j:
                midentidad[i][j] = (1, 0)
    print(midentidad)

    return midentidad


def mediaandvar(matriz_ob, estado):
    """Calcula la media y la varianza del observable en el estado dado

    :param matriz_ob: observavle
    :param estado: estado preparado
    :return: media y variancia
    """
    es_value = expected_value(matriz_ob, estado)
    if observables(matriz_ob):
        midentidad = generador_idn(matriz_ob)
        restador = nc.multiescalar_matrix(es_value, midentidad)
        restador = nc.inversa_add_matrizc(restador)
        delta = nc.suma_matricesc(matriz_ob, restador)
    delta_multi = nc.multiplicacion_matrices(delta, delta)
    variancia = expected_value(delta_multi, estado)

    return delta, variancia


def expected_value(matriz_ob, estado):
    """calcula el valor esperado despues de medir el sistema varias veces

    :param matriz_ob: observable
    :param estado: estado preparado
    :return: valor esperado
    """
    first_part = nc.accionmatriz_vector(matriz_ob, estado)
    value = nc.int_product(estado, first_part)
    m_value = nc.modulo_complejos(value)

    return (round(m_value, 1), 0)


def observables(matriz_ob):
    """ funcion que revisa si el observable ingresado es una matriz hermitiana

    :param matriz_ob: matriz posiblemente hermitiana
    :return: Booleana
    """
    return nc.hermitiana(matriz_ob)


def amplitud_tran(ket, ket1):
    """ función que calcula la amplitud de transcición

    :param ket: vector estado 1
    :param ket1: vector estado 2
    :return: amplitud de transición
    """
    transision = nc.int_product(ket1, ket)

    return transision


def prob_position(p, ket):
    """ función que determina la probabilidad de enccontrar una particula en una posición dada

    :param p: posición
    :param ket: vector estado
    :return: probabilidad
    """
    posisition_value = nc.modulo_complejos(ket[p]) ** 2
    magnitud_ket = 0
    for i in range(len(ket)):
        magnitud_ket += nc.modulo_complejos(ket[i]) ** 2
    magnitud_ket = math.sqrt(magnitud_ket)
    probabilidad = posisition_value / magnitud_ket ** 2

    return round(probabilidad, 3)
