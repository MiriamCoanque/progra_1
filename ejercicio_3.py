'''Ejercicio 3: Desarrollar una función “char_at” que recibe una cadena y un número.
Se debe retornar el caracter en la posición indicada por el número si ésta es válida.
**IMPORTANTE: **Las posiciones de los caracteres en un string van del 0 hasta el
<número de caracteres> - 1.'''

def char_at(cadena: str, numero: int) -> str:
    if numero < 0 or numero >= len(cadena):
        return "Posición inválida"
    else:
        return cadena[numero]


cadena = input("Ingrese una cadena: ")
numero = int(input("Ingrese un numero: "))
print("El caracter es:", char_at(cadena, numero))