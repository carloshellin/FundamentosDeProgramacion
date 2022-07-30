"""
    PROGRAMA: Geometría

    Tiempo consumido: 2 horas
"""

from math import sqrt
from collections import namedtuple
from libInterfaz import realPedido

tPunto = namedtuple('Punto', ['x', 'y', 'z'])

def distancia3D(x1, x2, y1, y2, z1, z2):
    """ float, float, float, float, float, float --> float
    OBJ: distancia en el espacio """
    return sqrt(((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2))

# PROBADOR
print('la distancia de 1.0, 1.0, 1.0 y 2.0, 2.0, 2.0 debe dar 1.73:', distancia3D(1.0, 2.0, 1.0, 2.0, 1.0, 2.0))

def distancia2D(x1, x2, y1, y2):
    """ float, float, float, float --> float
    OBJ: distancia en una superficie """
    return distancia3D(x1, x2, y1, y2, 0, 0)

# PROBADOR
print('la distancia de 1.0, 1.0, y 2.0, 2.0 debe dar 1.41:', distancia2D(1.0, 2.0, 1.0, 2.0))

def distanciaP(p1, p2):
    """ tPunto, tPunto --> float
    OBJ: distancia entre dos puntos """
    return distancia3D(p1.x, p2.x, p1.y, p2.y, p1.z, p2.z)

# PROBADOR
print('la distancia de los puntos 1.0, 1.0, y 2.0, 2.0 debe dar 1.73:', distanciaP(tPunto(1.0, 1.0, 1.0), tPunto(2.0, 2.0, 2.0)))

def puntoPedido(nombre):
    """ str --> tPunto
    OBJ: pide las coordenadas en centímetros de un punto en una habitacion 1*2*3 m """
    x = realPedido(0.0, 100.0, nombre + '.x = ')
    y = realPedido(0.0, 200.0, nombre + '.y = ')
    z = realPedido(0.0, 300.0, nombre + '.z = ')

    return tPunto(x, y, z)

# PROBADOR
print('el punto es (%.1f, %.1f, %.1f)' % (puntoPedido('P1')))


p1 = puntoPedido('P1')
p2 = puntoPedido('P2')

print('la distancia entre (%.2f, %.2f, %.2f) y (%.2f, %.2f, %.2f) es
%.2f metros' % (p1.x, p1.y, p1.z, p2.x, p2.y, p2.z, distanciaP(p1, p2)))
