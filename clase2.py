''' Problema 1: 
Area de un triangulo
Desarrolle un programa para calcular el area de un triangulo, cargando por teclado el valor
de la base, pero sabiendo que su altura al cuadrado de la base ( observar que la altura no es
dato... solo se indica la forma para calcularla de acuerdo a la base que si es un dato)'''

#Entradas

base = float(input('Ingrese el valor de la base:'))

#Procesos

altura = base**2
area = (base*altura)/2

#Salidas

print('El area del triangulo es: ',area)