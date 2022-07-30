"""****** BIBLIOTECA ESTADISTICA********
* V1.0                                 *
* Autor: Alumnos UAH   *
*FECHA 28/02/2018                      *
****************************************"""



from math import factorial


def total(p):
    """sec(numerico)-->numerico                                  
    OBJ: total de la población p
    PRE: """      
    t=0                      #t de total 
    for e in p:              #e de elemento. 
        t+=e                 #
    return t
    
cp=(1,2,3) #caso de prueba para todos los estadísticos
'''
#Probador
print('caso de prueba',cp,    'Total= ',total(cp))
'''

def media(p):
    """sec(numerico)-->float
    OBJ: media de la población p
    PRE: len(p)>0. requiere total()"""  
    return total(p)/float(len(p))

'''
#Probador
print('caso de prueba',cp,    'Media= ',media(cp))
'''

'''
def varianza(p): 
    """sec(numerico)-->float
    OBJ: varianza de la población p
    PRE: len(p)>0. media() definida"""
    t=0
    m=media(p)      
    for e in p:
        t+=(e-m)**2 
    return t/float(len(p))


#Probador
print('caso de prueba',cp,    'Varianza= ',varianza(cp))
'''

def varianza(p): 
    """sec(numerico)-->float
    OBJ: varianza de la población p
    PRE: len(p)>0. media() definida"""
    t=0
    for e in p:
        t+=e**2 
    return t/float(len(p))- media(p)**2       
'''
#Probador
print('caso de prueba',cp,    'Varianza= ',varianza(cp))
'''



def desv_tipica(p):
    """sec(numerico)-->float
    OBJ: desviación típica de la población p
    PRE: len(p)>0. varianza() definida"""
    from math import sqrt
    return sqrt(varianza(p))
'''
#Probador
print('caso de prueba',cp,    'desv= ',desv_tipica(cp))
'''

def coef_var(p):
    """sec(numerico)-->error, float
    OBJ: coeficiente de variación de la población p, error si media=0
    PRE: len(p)>0 desv_tipica() y media() definidas"""
    m=media(p)
    if m <=0.0001:     #nunca comparo float por == o != 
        error=True
        d=0
    else:
        error=False
        d=desv_tipica(p)/m
    return error, d

#ahora requiere dos casos de prueba
'''
#Probador
print('caso de prueba',cp,    'coeficiente variación= ',coef_var(cp))
print('caso de prueba',(-1,0,1),    'coeficiente variación= ',coef_var((-1,0,1)))
'''

def variacion(m,k):
    """int,int-->int
    OBJ: variaciones de m elementos tomados de k en k
    PRE factorial() definida.  m >=0, 0<=k>=m """
    return factorial(m)//factorial(m-k)

#Probador
'''m=4
k=2
print('Variaciones (',m,',',k,')= ',variacion(m,k))

'''
def combinacion(n,k):
    """Int,int-->int
    OBJ: combinacion de n elementos de k en k
    PRE:0<=k<=n variaciones y factorial definidos"""
    return variacion(n,k)//factorial(k)

'''
"""PROBADOR"""
print(combinacion(3,2))
'''

def permutacion(n):
    """int-->int
    OBJ: permutacion de n elementos
    PRE:n=>0 factorial() definida"""
    return factorial(n)

'''
"""PROBADOR"""
print(permutacion(4))
'''



""" Simulador de dado """



def dado_lanzado(n):
    """int-->int
    OBJ: lanza un dado de n caras
    PRE: 1<=n"""
    from random import randint
    return randint(1,n)

'''
"""PROBADOR"""
n=20               #veces
caras=6
print('lanzado',n,'veces: ',end='')
for cont in range (n):
    print(dado_lanzado(caras),end=',')

'''
