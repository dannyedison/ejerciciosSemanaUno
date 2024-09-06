"""
Ejercicio 9:
Escribe un programa que pida al usuario un 
número y luego imprima la tabla de multiplicar de ese número hasta el 10.
"""

numero = input('Ingresar un valor: ')
temporal = int(numero)

print('El resultado es: ')

n = 11
for i in range(n):
    print(i,' * ',numero,' = ',i*temporal )

