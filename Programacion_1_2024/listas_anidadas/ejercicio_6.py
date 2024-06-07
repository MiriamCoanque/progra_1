'''Ejercicio 6-Armar el siguiente menú de opciones:
1- Reponer mercadería (productos existentes)
2- Vender mercadería (producto existente, solo si alcanza el stock)
3- Listar inventario
5- Salir'''
from biblioteca_2 import *


while True:
    opcion = menu()

    if opcion == 1:
        reponer_mercaderia(estanteria)

    elif opcion == 2:
        vender_producto(estanteria)

    elif opcion == 3:
        listar_producto(estanteria)

    elif opcion == 4:
        print("Ha elegido 'Salir' :)")
        break