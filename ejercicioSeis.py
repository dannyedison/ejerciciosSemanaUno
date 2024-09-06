"""
Ejercicio 6:
Crea un programa que pida al usuario su calificación y luego imprima el mensaje "Aprobado" si la 
calificación es mayor o igual a 70, o "Reprobado" si la calificación es menor que 70.
"""

calificacion = input('Ingresar su calificación: ')
temporal = int(calificacion)

if temporal >= 70:
    print('Aprobado')
else:
    print('Reprobado')