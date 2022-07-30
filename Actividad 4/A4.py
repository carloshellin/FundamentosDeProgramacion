"""
    PROGRAMA: Gestión administrativa de una empresa

    Tiempo consumido: 2 hora y 45 minutos
"""

from recordclass import recordclass
from datetime import date
from random import randint
from libInterfaz import centrarRotulo, enteroPedido, dniPedido, cadCompuestaPedida, limpiaCadena

tEmpleado = recordclass('Empleado', 'dni, nombre, email, pagos')

def esAlfa(cad):
        """ str --> bool
        OBJ: cadena de texto cad es alfabético? """
        es = True
        for c in cad:
                if not 'a' <= c <= 'z' and not 'A' <= c <= 'Z':
                        es = False
        return es

# PROBADOR
#print('abcd debe dar True:', esAlfa('abcd'))
#print('ABCD debe dar True:', esAlfa('ABCD'))
#print('abcd1 debe dar False:', esAlfa('abcd1'))

def esNum(cad):
        """ str --> bool
        OBJ: cadena de texto cad es un número? """
        es = True
        
        for c in cad:
                if not '0' <= c <= '9' and not c == '-' and not c == ',':
                        es = False

        if '-' in cad and cad[0] != '-':
                es = False
        
        return es

# PROBADOR
#print('1234 debe dar True:', esNum('1234'))
#print('-1234 debe dar True:', esNum('-1234'))
#print('1234,5 debe dar True:', esNum('1234,5'))
#print('1234a debe dar False:', esNum('1234a'))
#print('1-234 debe dar False:', esNum('1-234'))

def esAlfaNum(cad):
        """ str --> bool
        OBJ: cadena de texto cad es alfabético o un número? """
        return esAlfa(cad) or esNum(cad)

# PROBADOR
#print(esAlfaNum('abcd'))

def divide(cad, sep):
        """ str, str --> lista
        OBJ: cadena de texto cad se divide por el separador sep """
        resultado = ['']
        pos = 0
        for c in cad:
                if c == sep:
                        resultado.append('')
                        pos += 1
                else:
                        resultado[pos] += c
                
        return resultado

# PROBADOR
#print('prueba@gmail.com se divide por el @:', divide('prueba@gmail.com', '@'))

def reemplaza(cad, viejo, nuevo):
        """ str, str, str --> str
        OBJ: reemplaza en la cadena de texto cad el carácter viejo por nuevo
        """
        for i in range(len(cad)):
                if cad[i] == viejo:
                        cad = cad[:i] + nuevo + cad[i + 1:]

        return cad

# PROBADOR
#print('100,0 debe cambiar a 100.0:', reemplaza('100,0', ',', '.'))

def total(sec):
        """ sec(float) --> float
        OBJ: total de la secuencia sec """      
        t = 0
        for i in sec:
                t += i
        return t

# PROBADOR
#print('(1, 2, 3) debe dar 6:', total((1, 2, 3)))

def ordenacionBurbuja(lista):
        """ lista --> nada
        OBJ: ordena por el método de la burbuja """
        for i in range(len(lista) - 1, 0, - 1):
                for j in range(i):
                        if lista[j] > lista[j + 1]:
                                temp = lista[j + 1]
                                lista[j+ 1] = lista[j]
                                lista[j] = temp

# PROBADOR
#print('[3, 1, 2] debe dar [1, 2, 3]:', ordenacionBurbuja([3, 1, 2]))

def esEmail(cad):
        """ str --> bool
        OBJ: cadena de texto cad es email? """
        es = False
        cad = divide(cad, '@')
        if len(cad) == 2:
                dominio = divide(cad[1], '.')
                if len(dominio) == 2:
                        es = len(cad[0]) > 0 and esAlfaNum(cad[0]) \
                             or '.' in cad[0] or '_' in cad[0] \
                             and 2 <= len(dominio[0]) <= 5 \
                             and 2 <= len(dominio[1]) <= 3
        return es

# PROBADOR
#print('prueba@gmail.com debe dar True:', esEmail('prueba@gmail.com'))
#print('prue.ba@gmail.com debe dar True:', esEmail('prue.ba@gmail.com'))
#print('prue_ba@gmail.com debe dar True:', esEmail('prue_ba@gmail.com'))
#print('prueba@gmailcom debe dar False:', esEmail('prueba@gmailcom'))
#print('pruebagmail.com debe dar False:', esEmail('pruebagmail.com'))

def emailPedido():
        """ nada --> str
        OBJ: pide email al usuario """
        email = ''
        while not esEmail(email):
                email = input('introduzca email:')
        return email

# PROBADOR
#print(emailPedido())

def importePedido():
        """ nada --> float
        OBJ: pide importe al usuario con coma para los céntimos """
        importe = ' '
        while not esNum(importe):
                importe = input('Importe:')
        importe = reemplaza(importe, ',', '.')

        return float(importe)

# PROBADOR
#print(importePedido())

def existeEmpleado(dni):
        """ str --> bool, int
        OBJ: True si existe empleado con dni y devuelve su posicion
        PRE: empleados definido """
        existe = False
        pos = 0
        for i in range(len(empleados)):
                if empleados[i].dni == dni:
                        existe = True
                        pos = i
        return existe, pos

# PROBADOR
#print(existeEmpleado(22918759H))

def altaEmpleado():
        """ nada --> nada
        OBJ: alta a un empleado
        PRE: empleados definido """
        existe = True
        while existe:
                dni = dniPedido()
                existe = existeEmpleado(dni)[0]
                if existe:
                        print('Ya existe un empleado con ese DNI')
                        
        nombre = limpiaCadena(cadCompuestaPedida('introduzca nombre completo:'))
        email = emailPedido()
        
        empleados.append(tEmpleado(dni, nombre, email, (0.0,)))
        ordenacionBurbuja(empleados)

# PROBADOR
#altaEmpleado()

def pagoEmpleado():
        """ nada --> nada
        OBJ: pago a un empleado
        PRE: empleados definido """
        existe = False
        while not existe:
                dni = dniPedido()
                existe, pos = existeEmpleado(dni)
        importe = importePedido()
        empleados[pos].pagos += (importe,)

# PROBADOR
#pagoEmpleado()

def resumenActual():
        """ nada --> nada
        OBJ: Resumen actual ordenada por nombre
        PRE: empleados definido """
        print('RESUMEN ACTUAL')
        fechaHoy = date.today()
        print('Fecha %i/%i/%i' % (fechaHoy.day, fechaHoy.month, fechaHoy.year))
        print('%s %28s %20s %20s' % ('Nombre', 'DNI', 'email', 'Total'))
        lista = []
        for empleado in empleados:
                lista.append((empleado.nombre, empleado.dni, empleado.email, empleado.pagos))
        ordenacionBurbuja(lista)
        for elem in lista:
                totalPagos = "%0.2f" % total(elem[3])
                print('%-29s%9s%29s%12s' % (elem[0],
                                            elem[1],
                                            elem[2],
                                            reemplaza(str(totalPagos), '.', ',')))

# PROBADOR
#resumenActual()

def menorIngreso():
        """ nada --> nada
        OBJ: pinta DNI del empleado con menor ingreso
        PRE: empleados definido """
        totales = [0] * len(empleados)
        for i in range(len(empleados)):
               totales[i] = [total(empleados[i].pagos), empleados[i].dni]
        ordenacionBurbuja(totales)
        print('Menores ingresos:', totales[0][1])

# PROBADOR
#menorIngreso()
        
def muestraEmpleado():
        """ nada --> nada
        OBJ: Muestra un empleado sabido su DNI
        PRE: empleados definido """
        existe = False
        while not existe:
                dni = dniPedido()
                existe, pos = existeEmpleado(dni)
        print('%s  %s  %s  %s' % (empleados[pos].nombre,
                                  empleados[pos].dni,
                                  empleados[pos].email,
                                  empleados[pos].pagos))

# PROBADOR
#muestraEmpleado()

def enviaEmail():
        """ nada --> nada
        OBJ: envia emails a todos los empleados con el total de sus cobros
        PRE: empleados definido """
        
        # NOTA:
        # Se ha decidido comentar este código para que no de error al mandar
        # emails pero que sirva de ejemplo de cómo sería enviaEmail()
        #import smtplib

        #titulo = 'Total de sus cobros hasta la actualidad'

        # Datos correo de la empresa
        #username = 'empresa@gmail.com'
        #password = 'contraseña'

        # Enviando correos
        #servidor = smtplib.SMTP('smtp.gmail.com:587')
        #servidor.starttls()
        #servidor.login(username, password)
        
        #for empleado in empleados:
                #cabecera = 'From: %s\n' % username
                #cabecera += 'To: %s\n' % empleado.email
                #cabecera += 'Subject: %s\n\n' % titulo
                #msg = "El total de sus cobros son: %i" % (total(empleado.pagos))
                #servidor.sendmail(username, empleado.email, cabecera + msg)
                
        #servidor.quit()
        
        print('Hecho')

# PROBADOR
#enviaEmail()

def amigoInvisible():
        """ nada --> nada
        OBJ: sortea el amigo invisible
        PRE: empleados definido """

        participantes = empleados.copy()
        reciben = []
        for empleado in empleados:
                distinto = False
                while not distinto:
                        pos = randint(0, len(participantes) - 1)
                        if empleado.dni != participantes[pos].dni \
                           or len(participantes) == 1:
                                distinto = True
                reciben.append(participantes[pos].dni)
                participantes.remove(participantes[pos])
                
        print('Regala\t\tRecibe')
        for i in range(len(reciben)):
                print('%s\t%s' % (empleados[i].dni, reciben[i]))
        
        
# PROBADOR
#amigoInvisible()

def pintaMenu():
	""" nada --> nada
	OBJ: pinta el menú de gestión administrativa """
	centrarRotulo('GESTIÓN ADMINISTRATIVA', '=')
	print('1.- Dar alta a un empleado')
	print('2.- Apuntar pago a un empleado')
	print('3.- Mostrar lista ordenada por nombre')
	print('4.- Mostrar empleado con el menor importe en el año')
	print('5.- Mostrar datos de un empleado')
	print('6.- Enviar email a todos los empleados con el total de cobros')
	print('7.- Amigo invisible')
	print('8.- Salir')
	print('\t Teclee la opción deseada:')

# PROBADOR
#pintaMenu()

empleados = []
# PROBADOR
#empleados = [tEmpleado('22918759H', 'Martinez Lopez Jose Carlos', 'jcml@gmail.com', (500.0, -400.0, -100.0)),
#             tEmpleado('99999999X', 'Alvarez Juan', 'miEmail@yahoo.es', (2000.0, 999.27)),
#             tEmpleado('8888888Y', 'Martinez Lopez Ana', 'elSuyo@ministerio.org', (3000.0, 333.98))]

opciones = ('altaEmpleado()', 'pagoEmpleado()', 'resumenActual()',
            'menorIngreso()', 'muestraEmpleado()', 'enviaEmail()',
            'amigoInvisible()', '0')

opcion = 0
while opcion != len(opciones):
        pintaMenu()
        opcion = enteroPedido(1, len(opciones), '')
        eval(opciones[opcion - 1])
