"""
Ejercicio 3:
Escribe un programa que pida al usuario su edad y luego determine si es mayor o menor de edad.
"""
edad = input('Ingresar su edad: ')
temporal = int(edad)

if temporal >= 18:
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')