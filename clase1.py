'''CLASE 1'''

#Salida por consola

# print('Hola Mundo')

#Solicitaremos al usuario que ingrese su nombre y luego imprimimos un saludo

# nombre = input('Porfavor ingrese su nombre: ')
# print('Hola',nombre)

'''Problema 1: 
Se conoce la cantidad de horas que trabaja un empleado en una fabrica, mas el importe que percibe por cada hora 
trabajada, ademas del nombre del empleado.
Se pide caluclar el importe final del sueldo que el empleado debera cobrar y mostrar el nombre del empleado y el 
importe final del sueldo que se calculo.'''

#Entrada

h_trabajadas = int(input('Porfavor ingrese la cantidad de horas trabajadas: '))
precio_hora = float(input('Porfavor ingrese el importe por hora: '))
nombre = input('Porfavor ingrese el nombre del empleado: ')

#Procesos

sueldo = h_trabajadas * precio_hora

#Salidas

print('El empleado',nombre,'tendra un sueldo de ',sueldo)

'''Problema 2:
Se requiere calcular la suma de dos numeros. Se pide generar la siguiente salida impresa:
El resultado de la suma de los dos numeros.
Para ello usted dispone de las siguientes entradas:
Numero 1 (n1): identifica el primer numero
Numero 2 (n2): identificar el segundo numero'''

#Entradas

n1 = int(input('Porfavor ingrese el primer numero: '))
n2 = int(input('Porfavor ingrese el segundo numero: '))

#Procesos

suma = n1 + n2

#Salidas

print('El resultado de la suma es igual a: ',suma)

'''Problema 3:
Desarrolle un programa para calcular el area de un triangulo, cargando por teclado el valor
de la base, pero sabiendo que su altura es igual al cuadrado de la base'''

#Entradas 

base = float(input('Porfavor ingrese la base del triangulo: '))

#Procesos 

altura = base ** 2
area = (base * altura)/2

#Salidas 

print('El area del triangulo:', area)

'''Problema 4:
Una persona necesita informacion relacionado con el desempeño de su automovil. Se pide generar 
las siguientes salidas impresas:
La cantidad de litros consumidos.
Para ello usted dispone de las siguientes entradas:
Kilometros(km): representa los KM recorridos por el vehiculo.
Precio(pr): representa el precio de combustible por litro.
Kilometros Litro(kmL): representa los km recorridos por cada litro.'''

#Entradas

km= float(input('Porfavor ingrese la cantidad de km a recorrer: '))
pr = float(input('Porfavor ingrese el precio del combustible por litro: '))
kmL= float(input('Porfavor ingrese el rendimiento por litro: '))

#Procesos

litros_cons = km /kmL
gastos = litros_cons * pr

#Salidas

print('Los litros consumidos: ',litros_cons, 'el gasto calculado es: ',gastos)

'''Problema 5: 
Desarrollar un programa que declare dos variables enteras, le asigne valores arbitrarios y luego muestre su suma, diferencia y producto'''

#Entradas

n1= 10
n2 = 5

#Procesos

suma = n1+n2
diferencia = n1 - n2
producto = n1*n2

#Salidas

print('El resultado de la suma es: ',suma)
print('El resultado de la diferencia es: ',diferencia)
print('El resultado del prodcuto es: ',producto)


'''Problema 6: 
Desarrollar un programa que le solicite al usuario su año de nacimiento. A continuacion, calcular e imprimir la edad que tendra el
usuario a fin de año'''

#Entradas

año_nac= int(input('Porfavor ingrese su año de nacimiento: '))

#Procesos 

edad = 2023 - año_nac

#Salidas

print('El usuario tendra a fin de año ',edad)

'''Problema 7:
Un mini mercado de nuestra ciudad necesita obtener informacion relacionada con el stock de 3 articulos de los productos que comercializa.
Se pide generar la siguiente salida impresa:
El importe total en concepto de ventas de cada articulo.
El importe total de los tres artculos considerados.
Para ello usted dispone de las siguientes entradas:
Cantidad Vendida Art1 (cant1): representa la cantidad vendida del articulo 1.
Precio Venta Art1 (pre1): representa el precio de venta del articulo 1.
Cantidad vendida Art2 (cant2): representa la cantidad vendida del articulo 2.
Precio Venta Art2 (pre2): representa el precio de venta del articulo 2.
Cantidad Vendida Art3 (cant3) : representa la cantidad vendida del articulo 3.
Precio Venta Art3 (pre3): representa el precio de venta del articulo 3.'''

#Entradas

#Articulo 1

cant1 = int(input('Porfavor ingrese la cantidad vendida del articulo 1: '))
pre1 = float(input('Porfavor ingrese el precio del articulo 1: '))

#Articulo 2

cant2 = int(input('Porfavor ingrese la cantidad vendida del articulo 2: '))
pre2 = float(input('Porfavor ngrese el precio del articulo 2: '))

#Articulo 3

cant3 = int(input('Porfavor ingrese la cantidad vendida del articulo 3: '))
pre3 = float(input('Porfavor ingres el precio del articulo 3: '))

#Procesos

imp_art1 = cant1 *pre1
imp_art2 = cant2 * pre2
imp_art3 = cant3 * pre3

total_imp = imp_art1 + imp_art2 + imp_art3

#Salidas

print('El importe total del articulo 1 es: ',imp_art1)
print('El importe total del articulo 2 es: ',imp_art2)
print('El importe total del articulo 3 es: ',imp_art3)
print('El importe total de los tres articulos es: ',total_imp)

'''Problema 8:
El observatorio metereologico necesita obtener informacion relacionada con la variacion de temperaturas en distintos momentos del dia.
Se pide generar la siguiente salida impresa:
La temperatura promedio del dia.
Para ello usted dispone de las siguientes entradas:
Temperatura 1 (t1): representa la temperatura tomada en hs de la mañana
Temperatura 2 (t2): representa la temperatura tomada en hs de la tarde
Temperatura 3 (t3): representa la temperatura tomada en hs de la noche'''

#Entradas

t1 = float(input('Porfavor ingrese la temperatura tomada en hs de la mañana: '))
t2 = float(input('Porfavor ingrese la temperatura tomada en hs de la tarde: '))
t3 = float(input('Porfavor ingrese la temperatura tomada en hs de la noche: '))

#Procesos

temp_prom = (t1+t2+t3)/3

#Salidas

print('La temperratura promedio durante el dia es: ', temp_prom)

'''Problema 9:
Ingresar los votos obtenidos por dos candidatos en una eleccion e informar el porcentaje obtenido para cada uno'''

#Entradas

votos_can1= int(input('Porfavor ingrese la cantidad de votos para el candidato 1: '))
votos_can2 = int(input('Porfavor ingrese la cantidad de votos para el candidato 2: '))

#Procesos

total = votos_can1+ votos_can2
porc_can1 = (votos_can1 * 100)/total
porc_can2 = (votos_can2 *100 )/total

#Salidas

print('El porcentaje obtenido para el candidato 1 es: ', porc_can1 ,'%')
print('El porcentaje obtenido para el candidato 2 es: ', porc_can2 ,'%')


'''Problema 10: 
Un vehiculo parte de la ciudad de Rio Grande y se dirige a Ushuaia, por la ruta, la distancia aproximada entre ambas
ciudades es de 200km. El vehiculo se desplaza a una velocidad promedio de 80km/h. Desarrolle un programa
que calcule el tiempo total en horas que demora ese vehiculo en llegar a ushuaia. De nuevo, no es necesario
convertir a horas, minutos y segundos, exprese el resultado como un numero real.
'''

#Entradas

velo_prom = 80

#Procesos

horas = 200 / velo_prom

#Salidas

print('La cantidad de horas que tarda en ir desde Rio Grande a Ushuaia es de: ',horas)