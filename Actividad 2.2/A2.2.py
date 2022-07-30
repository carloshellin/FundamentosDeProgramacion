"""
    PROGRAMA: simula 100, 1.000, 10.000 y 100.000 tiradas de un dado de n caras

    Tiempo consumido: 1 hora y 15 minutos
"""

from bibEstadistica import dado_lanzado, media, desv_tipica, coef_var

nCaras = 6

print('n_tirad', end='')
for i in range(nCaras):
    print('%8i' % (i + 1), end='')
print('   f_teorica   media   desv_tip   coef_var')

t = 10
for i in range(4):
    t *= 10
    fApariciones = (0,) * nCaras
    for j in range(t):
        cara = dado_lanzado(nCaras)
        fApariciones = fApariciones[:cara - 1] + (fApariciones[cara - 1] + 1,) \
                      + fApariciones[cara:]
        
    print('%7i' % t, end='')
    for fAparicion in fApariciones:
        print('%8i' % fAparicion, end='')
    print(' %8.2f  %8.2f  %8.2f  %8.2f' % (media(fApariciones),
                                           media(fApariciones),
                                           desv_tipica(fApariciones),
                                           coef_var(fApariciones)[1]))
