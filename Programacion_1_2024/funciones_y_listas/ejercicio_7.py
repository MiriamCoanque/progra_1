'''Una startup desea analizar las estadísticas de los usuarios de su sitio de
compras on-line recientemente lanzado al mercado para ello necesita un programa
que le permita acceder a los datos relevados.

Realizar una función con el siguiente Menú de Opciones:

1-Importar listas
2-Listar los datos de los usuarios de México
3-Listar los nombre, mail y teléfono de los usuarios de Brasil
4-Listar los datos del/los usuario/s más joven/es
5-Obtener un promedio de edad de los usuarios
6-De los usuarios de Brasil, listar los datos del usuario de mayor edad
7-Listar los datos de los usuarios de México y Brasil cuyo código postal
sea mayor a 8000
8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40
años.'''

from listas_personas import *

def menu():
    print('''            
            1- Importar listas
            2- Listar los datos de los usuarios de México
            3- Listar los nombre, mail y teléfono de los usuarios de Brasil
            4- Listar los datos del/los usuario/s más joven/es
            5- Obtener un promedio de edad de los usuarios
            6- De los usuarios de Brasil, listar los datos del usuario de mayor edad
            7- Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000
            8- Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años.
            9- Salir''')
    opcion = int(input("opcion: "))
    return opcion

def mostrar_todos_los_datos():
    for i in range(len(nombres)):
        print(f"Nombre: {nombres[i]}\tEdad: {edades[i]}\tTelefono: {telefonos[i]:<15}\tMail: {mails[i]:<20}\tRegion: {region[i]:<10}\tDirección: {address[i]}\tCodigo Postal: {postalZip[i]}")

def listar_brasil():
    for i in range(len(country)):
        if country[i] == "Brazil":
            print(f"Nombre: {nombres[i]}\tTelefono: {telefonos[i]}\tMail: {mails[i]}")


def listar_mexico():
    for i in range(len(country)):
        if country[i] == "Mexico":
            print(f"Nombre: {nombres[i]}\tEdad: {edades[i]}\tTelefono: {telefonos[i]:<15}\tMail: {mails[i]:<20}\tRegion: {region[i]:<10}\tDirección: {address[i]}\tCodigo Postal: {postalZip[i]}")

def listar_mas_joven():
    mas_joven = edades[0]
    for e_edades in range(len(edades)):
        if edades[e_edades] < mas_joven:
            mas_joven = edades[e_edades]
    
    for i in range(len(edades)):
        if edades[i] == mas_joven:
            print(f"Nombre: {nombres[i]}\tEdad: {edades[i]}\tTelefono: {telefonos[i]}\tMail: {mails[i]}\tRegion: {region[i]}\tDirección: {address[i]}\tCodigo Postal: {postalZip[i]}")

def promediar_personas():
    contador = 0
    acumulador = 0
    for e_edades in range(len(edades)):
        contador += 1
        acumulador += e_edades
      
    promedio = acumulador / contador
    print(f"El promedio de edad es de: {promedio}")

def mostrar_mayor_brasil():
    for i in range(len(country)):
        if country[i] == "Brazil":
            mayor_edad = edades[0]
            for e_edades in range(len(edades)):
                if edades[e_edades] > mayor_edad:
                    mayor_edad = edades[e_edades]
            for i in range(len(edades)):
                if edades[i] == mayor_edad:
                    print(f"Nombre: {nombres[i]}\tEdad: {edades[i]}\tTelefono: {telefonos[i]}\tMail: {mails[i]}\tRegion: {region[i]}\tDirección: {address[i]}\tCodigo Postal: {postalZip[i]}")
                    
def mostrar_codigoPostal_mayor_a_8000():
    
    for i in range(len(country)):
        if (country[i] == "Brazil" or country[i] == "Mexico") and postalZip[i] > 8000:
            print(f"Nombre: {nombres[i]}\tEdad: {edades[i]}\tTelefono: {telefonos[i]}\tMail: {mails[i]}\tRegion: {region[i]}\tDirección: {address[i]}\tCodigo Postal: {postalZip[i]}")

def mostrar_italianos_mayores_a_40():
    
    for i in range(len(country)):
        if country[i] == "Italy" and edades[i] > 40:
            print(f"Nombre: {nombres[i]}\tTelefono: {telefonos[i]}\tMail: {mails[i]}")

def mostrar_despedida():
    print("Adios :)")
    
while True:
    opcion = menu()
    if opcion == 1:
        mostrar_todos_los_datos()
    if opcion == 2:
        listar_mexico()
    if opcion == 3:
        listar_brasil()
    if opcion == 4:
        listar_mas_joven() 
    if opcion == 5:
        promediar_personas()
    if opcion == 6:
        mostrar_mayor_brasil()
    if opcion == 7:
        mostrar_codigoPostal_mayor_a_8000() 
    if opcion == 8:
        mostrar_italianos_mayores_a_40()
    if opcion == 9:
        mostrar_despedida()
        break
    