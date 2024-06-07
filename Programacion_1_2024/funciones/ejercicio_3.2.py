'''Crear una función que pida el ingreso de un número y lo retorne.'''

def ingresar_numero():
    num = int(input("Ingrese un numero: "))
    return num

resultado = ingresar_numero()
print(f'El numero ingresado es: {resultado}')