"""********************************************************************
*                      biblioteca: libInterfaz                        *
*OBJ: agrupa facilidades para la interfaz de usuario                  *
*     centrarRotulo (rotulo,signo,tamVentana=76)                      *
*     enteroPedido (min,max,msg)                                      *
*     realPedido (min,max, msg)                                       *
********************************************************************"""

def centrarRotulo (rotulo,signo,tamVentana=76):
    """str,str,[int]-->[]
    OBJ: centra rótulo, subrayado con signo en ventana de tamaño 
        indicado,+ linea encima y debajo
    PRE: len(rotulo)<=tamVentana<=150"""
    tam = len(rotulo)
    lado = (tamVentana-tam)//2-1 #-1 xq print deja blanco entre argum
    print ()
    print(' '*lado,rotulo)
    print(' '*lado,'='*tam)
    print()

#centrarRotulo ('Aplicación de combinatoria','*') 

def enteroPedido (mini,maxi, msg):
    """ int,int, str-->int
    OBJ: pide entero a usuario entre mini y maxi, mostrando msg
    PRE: mini<=maxi                                           """

    pedir = True
    while  pedir or not (mini<=n<=maxi):
        try:
            n = int(input(msg))
            pedir = False
        except:print('debe ser un entero. ', end='')        
    return n
'''
#Probador
min = 1
max = 12
print(enteroPedido(min,max,'mes entre '+str(min)+' y '+str(max)+': '))
'''

def realPedido (mini,maxi,msg):
    """float, float, str -->float
    OBJ: pide real a usuario, entre min y max, mostrando msg    """

    pedir = True
    while  pedir or not (mini<=n<=maxi):
        try:
            n = float(input(msg))
            pedir = False
        except:print('debe ser un real. ', end='')
            
    return n
'''
print(realPedido(min,max,'real entre '+str(min)+' y '+str(max)+': '))
'''


"""gestion DNI de españoles                                     """

def esDNI(dni):
    """str-->bool
    OBJ: dni es un dni válido?      """
    COD_VERIFICACION= 'TRWAGMYFPDXBNJZSQVHLCKE' #encapsulo constante,
                                               #xq es específica de este subprog 
    long = len(dni) 
    try:
        numero=int(dni[:long-1]) 
        #el DNI de Franco era el 1
        es = 2<=long<=9 and COD_VERIFICACION[numero%23]== dni[long-1].upper()
    except:es = False
    return es

#PROBADOR
#print (esDNI('23232323t'))

def dniPedido():
    dni='   '
    while not esDNI(dni):
        dni = input('introduzca DNI:')
    dni=' '*(9-len(dni))+dni #Ajusto a 9 caracteres
    dni = dni[:8]+dni[8].upper()
    return dni

#PROBADOR
#print(dniPedido())

def cadCompuestaPedida(msg):
    '''cad-->cad
    OBJ: pide a usuario cadena con solo letras y espacios, al menos 2 palabras'''
    pedir = True
    while pedir: 
        cad = input(msg)
        aux= cad.split()
        pedir= len(aux)<2
        #print(pedir,aux)
        for pal in aux:
            pedir = pedir or not pal.isalpha()
            #print(pedir, pal.isalpha())
    return cad
#print(cadCompuestaPedida('combre completo: '))

#5)
def limpiaCadena(cad):
    '''cad-->cad
    OBJ: devuelve cad, eliminados espacios en blanco de delante detras,
    deja solo uno entre palabras. Primera letra de cada palabra Mayúscula,
    resto minúscula''' 
    aux=''
    tam=len(cad)
    i=0
    while i<tam:
        while i<tam and cad[i] ==' ': i+=1
        if i<tam:
            
            aux+=' '+cad[i].upper()
            i+=1
        while i<tam and cad[i] !=' ':
            aux+=cad[i].lower()
            i+=1
    return aux[1:]

#Probador
'''
sucia=' HoLa   mUndo '
print(sucia, len(sucia))
limpia= limpiaCadena(sucia)
print(limpia, len(limpia))
    
'''


"""en esta biblioteca tambien tienen cabida
contraseñaPedida
cuentaBancariaPedida

Todo loQueSeaPedido, excepto que se agrupe con su tipo (por ejemplo tFecha

esAlfa
esNum
limpiar pantalla
y un largo etc"""


