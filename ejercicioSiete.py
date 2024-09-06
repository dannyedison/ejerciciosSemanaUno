"""
Ejercicio 7:

Escribe un programa que pida al usuario dos números y luego determine cuál es el mayor.
"""

numeroUno = input('Ingresar el primer valor: ')
numeroDos = input('Ingresar el segundo valor: ')
temporalUno = int(numeroUno)
temporalDos = int(numeroDos)

if temporalUno > temporalDos:
    print('El numero mayor es: ', numeroUno)
elif temporalUno < temporalDos:
    print('El numero mayor es: ', numeroDos)
else:
    print('Los números son iguales ')
    