'''Funciones:
1.Crear la función leer_json() que va a recibir el nombre y extensión de donde se ubica el
archivo a leer (Ruta absoluta o relativa), y también el nombre de la lista a leer por ejemplo en la
imagen anterior la lista está en la clave “heroes” Si el archivo existe deberia leer el archivo json
y retornar la lista obtenida.
Si el achivo no existe deberia retornar False (USAR EXCEPCIONES)
2. Crear la función generar_csv()
La función va a recibir el nombre y extensión del archivo csv de los superhéroes (Puede ser ruta
absoluta o relativa) y la lista de los mismos. Si la lista no está vacía la función deberá guardar
en un string la información en formato csv (separado con comas) con la cabecera
correspondiente.
Una vez generado el string debería usar la función del siguiente punto (3) para guardar ese string generado al archivo. Si la lista está vacía retornar False


3. Crear la función 'guardar_archivo' la cual recibirá por parámetro un string que indicará el
nombre con el cual se guardará el archivo junto con su extensión (ejemplo: 'archivo.csv') y
como segundo parámetro tendrá un string el cual será el contenido a guardar en dicho archivo.
Debe abrirse el archivo en modo escritura+, ya que en caso de no existir, lo creara y en caso de
existir, lo va a sobreescribir La función debera retornar True si no hubo errores, caso contrario
False (VALIDAR CON EXCEPCIONES), además en caso de éxito, deberá imprimir un
mensaje respetando el formato:
Se creó el archivo: nombre_archivo.csv
ATENCIÓN: Controlar las excepciones posibles en caso de presentarse alguna retornar false e
imprimir un mensaje que diga: ‘Error al crear el archivo: nombre_archivo’ Donde
nombre_archivo será el nombre que recibirá el archivo a ser creado, conjuntamente con su
extensión.
Menú de Opciones:
A. Leer archivo JSON.
B. Ordenar héroes por alguna de las claves numéricas (altura, peso y fuerza) de manera
ascendente
C. Guardar el listado ordenado en un CSV. Pedir el nombre del archivo al usuario.
D. Salir'''


from json import *
from biblioteca_stark2 import *


while True:
    opcion = menu()

    if opcion == "A":
        lista = parse_json("stark\data_stark.json","heroes")
    if opcion == "B":
        lista = parse_json("stark\data_stark.json", "heroes")
        clave = pedir_clave()
        lista_ordenada = ordenar_por_clave(lista, clave)
        mostrar_lista_ordenada(lista_ordenada)
    if opcion == "C":
        nombre = pedir_nombre()
        lista = parse_json("stark\data_stark.json", "heroes")
        generar_csv(nombre, lista)
        

    if opcion == "D":
        mostrar_despedida()
        break

'''def pedir_nombre():
    nombre = input("Ingrese el nombre: ")

    return nombre

def parse_json(nombre:str,nombre_lista:str)->list:
    try:
        with open(nombre, "r") as archivo:
            resultado = json.load(archivo)

        return resultado[nombre_lista]
    except FileNotFoundError:
        print("Archivo no encontrado")
        return False

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
        return False'''