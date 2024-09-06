"""
Ejercicio 4:
Crea un programa que pida al usuario un número y determine si es par o impar.
"""
numero = input('Ingresar número: ')
temporal = int(numero)

resultado = temporal % 2
if resultado == 0:
    print('El número es par')
else:
    print('El número es impar')