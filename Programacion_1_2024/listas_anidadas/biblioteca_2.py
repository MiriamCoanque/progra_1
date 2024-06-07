estanteria = [["to12", 65, [1, 1]] , ["to16", 86, [1, 2]], ["to20", 65, [1, 3]], ["to25",45, [1, 4]],
              ["to30", 68, [2, 1]], ["to35", 73, [2, 2]], ["to40", 85, [2, 3]], ["to45", 89, [2, 4]],
              ["ta4", 58, [3, 1]], ["ta5", 48, [3, 2]], ["ta6", 64, [3, 3]], ["ta7", 96, [3, 4]],
              ["ta8", 36, [4, 1]], ["ta10", 72, [4, 2]], ["ta12", 78, [4, 3]], ["ta14", 71, [4, 4]]

]

def reponer_mercaderia(estanteria:list):
    
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad a reponer: "))
    while cantidad < 1:
        cantidad = int(input("Error, ingrese la cantidad de nuevo: "))

    for e_estanteria in estanteria:
        if e_estanteria [0] == nombre:
            e_estanteria [1] += cantidad
            print(f'Producto actualizado: {e_estanteria}')
            break


def vender_producto(estanteria:list):
    nombre = input("Ingrese el nombre de producto: ")
    cantidad = int(input("Ingrese la cantidad a vender: "))

    while cantidad < 1:
        cantidad = int(input("Error, ingrese la cantidad de nuevo: "))

    for e_estanteria in estanteria:
        if e_estanteria [0] == nombre:
            if e_estanteria [1] >= cantidad:
                e_estanteria [1] -= cantidad
                print(f'Producto actualizado luego de venderlo: {e_estanteria}')
                break
                
            else:
                print("No hay suficiente producto para vender")

def listar_producto(estanteria:list):
    for e_estanteria in estanteria:
        print(f'Nombre:{e_estanteria[0]} cantidad: {e_estanteria[1]} fila: {e_estanteria[2][0]} caja: {e_estanteria[2][1]}')



def menu():
    print('''            
            1-Reponer mercadería (productos existentes)
            2-Vender mercadería (producto existente, solo si alcanza el stock)
            3-Listar inventario
            4-Salir ''')
    
    opcion = int(input("opcion: "))
    return opcion