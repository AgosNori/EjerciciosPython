'''Problema 1:
Descuento en medicinas
Calcular el descuento y el monto a pagar por un medicamento 
cualquiera en una farmacia( cargar por teclado el precio del mismo )
sabiendo que todos los medicamentos tienen un descuento del 35%
Mostrar el precio actual, el monto del descuento y el monto final a pagar'''


# entradas
precio_actual = float(input('Porfavor ingrese el precio actual del medicamento: '))

#procesos
descuento = precio_actual * 0.35
precio_final = precio_actual-descuento

#salidas
print('El precio original del medicamento: ',precio_actual)
print('Descuento del 35%: ',descuento)
print('El precio final: ',precio_final)


'''Problema 2:
Realiza un programa que nos permita ingresar el precio de lista de un articulo, y nos muestre:
precio de venta al contado (10% de descuento)
precio de venta con tarjeta (5% de recargo)'''

#entradas
pre_list = float(input('ingrese el precio de lista del articulo: '))

#procesos
contado = pre_list-pre_list*10/100
tarjeta = pre_list*pre_list*5/100

#salidas

print('El precio de contado es: ',contado)
print('El precio con tarjeta es: ',tarjeta)

'''Problema 3: 
La dirección de la carrera de ingenieria en sistemas de la utn de cba, necesita
un programa que permita cargar el nombre de un estudiante de quinto año, el nombre 
profesor responsable de la practica profesional supervisada de ese estudiante, y el 
promedio general ( con decimales) del estudiante en su carrera. Una vez cargados los
datos, se pide simplemente mostrarlos en la consola de salida a modo de verificación, 
pero de forma que el nombre del practicante vaya precedido de la cadena "est." 
y el nombre del profesor se preceda con "prof.". el promedio del alumno debe mostrarse redondeado, 
sin decimales , en formato entero.
'''

#entradas
est = input('Ingrese el nombre del estudiante: ')
prof = input('Ingrese el nombre del profesor a cargo: ')
prom = float(input('Ingrese el promedio del estudiante: '))

#procesos
datos = (est,prof,prom)

#salidas
print('est: ',datos[0],'prof: ',datos[1],'prom: ',str(round(datos[2])))

'''problema 4:
juego de adivinanza'''
print('Adivina mi idioma favorito')
print('-------------------------')
i = ('italiano')
print('Ayuditas')
print('Contiene la letra ',i[2],'dos veces')
print('Cantidad de letras: ',len(i))
print('termina con la letra: ',i[7])

i_ingresada = input('Adivinaste cual es: ?')
if (i_ingresada == i):
    print('ganaste') 
else:
    print('perdiste')