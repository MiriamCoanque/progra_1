import json

def menu():
    print('''            
            A. Leer archivo JSON.
            B. Ordenar héroes por alguna de las claves numéricas (altura, peso y fuerza) de manera ascendente
            C. Guardar el listado ordenado en un CSV. Pedir el nombre del archivo al usuario.
            D. Salir''')
    opcion = input("Opcion: ").upper()
    return opcion

   
def parse_json(nombre:str,nombre_lista:str)->list:
    try:
        with open(nombre, "r") as archivo:
            resultado = json.load(archivo)

        return resultado[nombre_lista]
    except FileNotFoundError:
        print("Archivo no encontrado")
        return False

def mostrar_despedida():
    print("Ha elegido salir :)")



def generar_csv(nombre:str, lista:list):
    try:
        with open(nombre,"w") as archivo:
            archivo.write("Nombre, Identidad, Altura, Peso, Fuerza, Inteligencia")
            for heroes in lista:
                archivo.write({heroes["nombre"]},
                              {heroes["identidad"]},
                              {heroes["altura"]},
                              {heroes["peso"]},
                              {heroes["fuerza"]},
                              {heroes["inteligencia"]})
    except TypeError:
        print("No existe en la lista")
        return False
    
def guardar_archivo(nombre:str, contenido:str):
    try:
        with open(nombre, "w+") as archivo:
            archivo.write(contenido)
            print(f"Se creo el archivo: {nombre}")
            return True
    except TypeError:
        print(f"Error al crear el archivo: {nombre}")
        return False



def pedir_clave():
    while True:
        clave = input("Ingrese la clave numérica por la cual desea ordenar : ")
        if clave in ["altura", "peso", "fuerza"]:
            return clave
        else:
            print("Error")

def ordenar_por_clave(lista: list, clave: str):
    try:
        ordenado = sorted(lista, key=lambda heroe: heroe[clave])
        return ordenado
    except KeyError:
        print("La clave no existe")
        return lista
    
def mostrar_lista_ordenada(lista:list):
    print(lista)

def pedir_nombre():
    nombre = input("Ingrese el nombre: ")

    return nombre





