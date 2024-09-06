"""
Ejercicio 5:

Escribe un programa que pida al usuario dos números y luego calcule su suma, resta, multiplicación y división.
"""
numeroUno = input('Ingresar el primer valor: ')
numeroDos = input('Ingresar el segundo valor: ')
temporalUno = int(numeroUno)
temporalDos = int(numeroDos)

resultado = temporalUno + temporalDos
print('El resultado de la suma es: ', resultado)

resultado = temporalUno - temporalDos
print('El resultado de la resta es: ', resultado)

resultado = temporalUno * temporalDos
print('El resultado de la multiplicación es: ', resultado)

resultado = temporalUno / temporalDos
print('El resultado de la división es: ', resultado)
