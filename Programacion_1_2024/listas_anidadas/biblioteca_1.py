productos = [["botellas",3,[1,2]],
                   ["frascos",8,[1,4]],
                   ["fideos",4,[2,3]],
                   ["leches",3,[3,4]]

]


def verificar_nombre()->str: 
    nombre = input("Ingrese el nombre del producto: ")
    while not nombre.isalpha():
        nombre = input("Error, ingrese un nombre válido: ")
    return nombre

def verificar_producto()->int:
    cantidad = int(input("Ingrese la cantidad del producto: "))
    while cantidad < 1:
        cantidad = int(input("Error, ingrese una cantidad mayor a 1: "))

    fila = int(input("Ingrese la fila de la góndola: "))
    while fila < 1 or fila > 3:
        fila = int(input("Error, ingrese una fila entre 1 y 3: "))

    columna = int(input("Ingrese la columna de la góndola: "))
    while columna < 1 or columna > 5:
        columna = int(input("Error, ingrese una columna entre 1 y 5: "))
    
    return cantidad , fila , columna

def agregar_productos(productos:list):
    nombre = verificar_nombre()
    cantidad, fila, columna = verificar_producto()
    productos.append([nombre, cantidad, [fila, columna]])
    print("Producto agregado:", [nombre, cantidad, [fila, columna]])

def dar_de_baja_productos(productos:list):
    nombre = input("Ingrese el nombre del producto que desee dar de baja: ")
    i = 0
    for e_productos in productos:
        if e_productos [0] == nombre:
            productos.pop(i)
        else:
            i += 1
    print(productos)

def modificar_productos(productos:list):
    nombre = verificar_nombre()
    for e_productos in productos:       
        if e_productos[0] == nombre:
            cantidad, fila, columna = verificar_producto()
            e_productos[1] = cantidad
            e_productos[2] = [fila, columna]
            print("Producto modificado:", e_productos)
            break
    else:
        print("Producto no encontrado")
            

def listar_productos(productos:list):
    for e_productos in productos:
        print(f'nombre: {e_productos[0]} cantidad: {e_productos[1]} fila: {e_productos[2][0]} y columna: {e_productos[2][1]}')

def order_por_nombre(productos:list):        
    for i in range(len(productos)-1):
        for j in range(i+1,len(productos)):
            if productos[i][0] > productos[j][0]:
                auxiliar_producto = productos[i]
                productos[i] = productos[j]
                productos[j] = auxiliar_producto

    print(productos)    

def menu():
    print('''            
            1-Alta de productos (producto nuevo)
            2-Baja de productos (producto existente)
            3-Modificar productos (cantidad, ubicación)
            4-Listar productos
            5-Lista de productos ordenado por nombre
            6-Salir''')
    opcion = int(input("opcion: "))
    return opcion

