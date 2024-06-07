'''Ejercicio 1: Desarrollar una función que reciba una letra y una cadena.
Debe retornar las veces que la letra está incluida en el texto.'''

def retornar_por_cant_de_veces(letra:str,cadena:str)->int:
    contador = 0
    for char in cadena:
        if char == letra:
            contador += 1
    return contador


cadena = "hola como estas"
letra = "o"
resultado = retornar_por_cant_de_veces(letra, cadena)
print(f'cantidad de letras: {resultado}') 




    