'''Crear una función que permita determinar si un número es par o no. La
función retorna “True” en caso afirmativo y “False en caso contrario. Probar en el
programa principal realizando la invocación o llamada.'''

def comprobar_par_impar(num:int)-> int:
    if num % 2 == 0:
        return True
    else:
        return False
    
numero = int(input("Ingrese un numero: "))
resultado = comprobar_par_impar(numero)

print(f'El numero {numero} es: {resultado}')