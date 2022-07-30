"""
    BIBLIOTECA: Estadística

    Tiempo consumido: 1 hora
"""

from math import sqrt
from random import randint

DADO_VECES = 20

def total(muestral):
    """ tupla --> int
    OBJ: total de un muestral
    """
    suma = 0;
    for i in muestral:
        suma += i
    return suma

# PROBADOR
print('caso de prueba (1, 2, 3) Total=', total((1, 2, 3)))

def media(muestral):
    """ tupla --> float
    OBJ: media aritmética de un muestral
    """
    return total(muestral) / len(muestral)

# PROBADOR
print('caso de prueba (1, 2, 3) Media=', media((1, 2, 3)))

def varianza(muestral):
    """ tupla --> float
    OBJ: varianza de un muestral
    """
    resultado = 0
    x = media(muestral)
    for i in muestral:
        resultado += total(((i - x) ** 2,)) / len(muestral)
    return resultado

# PROBADOR
print('caso de prueba (1, 2, 3) Varianza=', varianza((1, 2, 3)))

def desviacion(muestral):
    """ tupla-->float
    OBJ: desviación típica de un muestral
    """
    return sqrt(varianza(muestral))

# PROBADOR
print('caso de prueba (1, 2, 3) desviación típica=', desviacion((1, 2, 3)))

def coeficiente(muestral):
    """ tupla-->float
    OBJ: coeficiente de variación de un muestral
    """
    return desviacion(muestral) / media(muestral)

# PROBADOR
print('caso de prueba (1, 2, 3) coeficiente variacción=', coeficiente((1, 2, 3)))

def dado(n):
    """ int --> int
    OBJ: lanza un dado de n caras
    PRE: n > 0
    """
    return randint(1, n)

# PROBADOR
print('lanzado %d veces:' % (DADO_VECES), end='')
for i in range(DADO_VECES):
    print(dado(6), end=',')
