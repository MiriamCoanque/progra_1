'''Especializar la función del punto 3.1 y 3.2 para que valide el número en
un rango determinado pasado por parámetro “desde”-“hasta”.'''

def ingresar_numero():
    num = int(input("Ingrese un numero: "))
    return num

def mostrar_error_numero():
    dato_ingresado = int(input("Error, ingrese nuevamente: "))
    return dato_ingresado

def validar_num(desde:int, hasta:int)-> int:

    numero = ingresar_numero()
    while numero < desde or numero > hasta:
        numero = mostrar_error_numero()

    return numero

def mostrar_num(desde_aqui:int, hasta_aqui:int)->int:
    resultado = validar_num(desde_aqui,hasta_aqui)
    print(f'El numero es: {resultado}')

desde = 1
hasta = 100

mostrar_num(desde,hasta)


