'''La división de higiene está trabajando en un control de stock para productos sanitarios.
Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe
obtener los siguientes datos:
1. El tipo (validar "barbijo", "jabón" o "alcohol")
2. El precio: (validar entre 100 y 300)
3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000
unidades)
4. La marca y el Fabricante.

Se debe informar lo siguiente:
A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
B. Del ítem con más unidades, el fabricante.
C. Cuántas unidades de jabones hay en total.'''

bandera_caro = True
precio_mas_caro = 100
contador_barbijo_caro = 0
fabricante_barbijo_caro = ""
mayor_cantidad = 0
producto_mayor_cantidad = ""
cantidad_jabon = 0

for i in range(5):
    producto = input("Ingrese el producto ('barbijo'/'jabón'/'alcohol'): ")
    while producto != "barbijo" and producto != "jabón" and producto != "alcohol":
        producto = input("Error, ingrese 'barbijo', 'jabón' o 'alcohol': ")
    
    precio = int(input("Ingrese el precio (válido solo entre 100$ - 300$): "))
    while precio < 100 or precio > 300:
        precio = int(input("Error, ingrese el precio (válido solo entre 100$ - 300$): "))
    
    cantidad_unidades = int(input("Ingrese la cantidad de unidades: "))
    while cantidad_unidades <= 0 or cantidad_unidades > 1000:
        cantidad_unidades = int(input("Error, ingrese la cantidad de unidades: "))
    
    marca = input("Ingrese la marca: ")
    fabricante = input("Ingrese el fabricante: ")

    if producto == "barbijo":
        if bandera_caro == True or precio > precio_mas_caro:
            precio_mas_caro = precio
            bandera_caro = False
            contador_barbijo_caro = cantidad_unidades
            fabricante_barbijo_caro = fabricante

    if cantidad_unidades > mayor_cantidad:
        mayor_cantidad = cantidad_unidades
        producto_mayor_cantidad = producto
    
    if producto == "jabón":
        cantidad_jabon += cantidad_unidades

print(f"El barbijo más caro es {fabricante_barbijo_caro} y posee una cantidad de unidades de {contador_barbijo_caro}")
print(f"El producto con más unidades es: {producto_mayor_cantidad}")
print(f"La cantidad de jabones es de: {cantidad_jabon}")
