'''Desarrollar una función que inicialice una lista de 10 números en 0, pida
posición y número a guardar al usuario, lo guarde en una lista en la posición
solicitada aleatoriamente y la retorne. El programa principal debe invocar a la
función y mostrar por pantalla el retorno.'''

def pedir_guardar_y_modificar_lista():
    lista_numero = [0] * 10
    print(f'Lista sin modificar: {lista_numero}')
    posicion = int(input("Ingrese la posicion: "))
    while posicion < 0 or posicion > 9:
        posicion = int(input("Error, ingrese la posicion: "))

    numero = int(input("Ingrese el numero: "))

    lista_numero[posicion] = numero
    return lista_numero

resultado = pedir_guardar_y_modificar_lista()
print(f'Lista modificada: {resultado}')

