'''Ejercicio 2-Armar el siguiente menú de opciones:
1-Alta de productos (producto nuevo)
2-Baja de productos (producto existente)
3-Modificar productos (cantidad, ubicación)
4-Listar productos
5-Lista de productos ordenado por nombre
6-Salir'''

from biblioteca_1 import *

alta_producto = False

while True:
    opcion = menu()

    if opcion == 1:
        
        agregar_productos(productos)
        alta_producto = True

    elif opcion == 2:
        if alta_producto == False:
            print("Error, debe primero dar de alta un producto")
        else:
            dar_de_baja_productos(productos)

    elif opcion == 3:
        if alta_producto == False:
            print("Error, debe primero dar de alta un producto")
        else:
            modificar_productos(productos)
  
    elif opcion == 4:
        listar_productos(productos)

    elif opcion == 5:
        order_por_nombre(productos)
        
    elif opcion == 6:
        print("Ha elegido 'Salir' :)")
        break
    



   

