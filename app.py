# comentario

"""
comentario
multi linea
"""

print('Hola mundo!!')

datoUno = 10
datoDos = 20
datoTres ='Hola'
datoCuatro = 10.5

print(type(datoUno))

if datoUno==10:
    if datoDos>15:
        pass
    print(datoUno)

suma = datoUno + datoDos
print('La suma es', datoUno)

print(type(datoTres))
print(type(datoCuatro))

dato = input('Ingrese un numero')
print(type(dato))
temporal= int(dato)
if temporal == 9:
    print(temporal)

edad = 17
if edad >= 16:
    print('Eres mayor de edad')
elif edad == 15:
    print(15)
elif edad == 16:
    print(16)
elif edad == 17:
    print(17)
else:
    print('Eres menor de edad')


    n1 = int(input('Ingrese número 1: '))
n2 = int(input('Ingrese número 2: '))

respuesta = n1 + n2
respuesta += 50


#para evitar las comas, se inicia fon f

print(f'El resultado {respuesta} y es de tipo {type(respuesta)}') 

print('respuesta suma: ', respuesta)


# pass permite completar el código

if respuesta > 200:
    pass

if respuesta > 200:
    print('Es mayor de 200')
elif respuesta >= 100 and respuesta <= 150:
    print('esta entre 100 y 150')
else:
    print('No es mayor a 200')

#con tecla Ctrl + } para comentar