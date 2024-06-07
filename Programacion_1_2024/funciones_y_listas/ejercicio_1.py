'''Desarrollar una función que pida 10 nombres de manera secuencial, los
guarde en una lista y la retorne. El programa principal debe invocar a la función y
mostrar por pantalla el retorno.'''

def pedir_nombres(cantidad:int):
    lista_nombres = []

    for i in range(cantidad):
        nombre = input("Ingrese su nombre: ")
        lista_nombres.append(nombre)
    
    return lista_nombres

cantidad = 3
print(f"Los nombres son: {pedir_nombres(cantidad)}")    




        
        
