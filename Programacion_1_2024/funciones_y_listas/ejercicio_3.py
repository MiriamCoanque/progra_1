'''Desarrollar una función que pida 10 números dentro de un rango
especificado, validar los números solicitados dentro de ese rango, guardar en una
lista y retornarla. El programa principal debe invocar a la función y mostrar por
pantalla el retorno.'''

def pedir_num_dentro_de_rangos(rango1:int, rango2:int):
    lista_numero = []
    for i in range(10):
        numero = int(input("Ingrese un numero: "))

        while numero < rango1 or numero > rango2:
            numero = int(input(f"Error, ingrese nuevamente entre ({rango1} - {rango2}): "))

        lista_numero.append(numero)

    return lista_numero

resultado = pedir_num_dentro_de_rangos(1, 10)

print(f'Los numeros: {resultado}')
