'''Crear una función que muestre por pantalla el número que recibe
como parámetro.'''

def mostrar_num(num_1:int)->int:
    resultado = print(f"El numero es: {num_1}")

numero = int(input("Ingrese un numero: "))
mostrar_num(numero)