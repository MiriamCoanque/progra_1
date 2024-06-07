'''Pedir al usuario que ingrese los datos de 5 alumnos y guardarlos en sus
respectivas listas. Validar el ingreso de datos según su criterio.
Datos:
nombre, sexo (f/m), nota (validar).
Una vez cargados los datos:
Mostrar el nombre del hombre con nota más baja
Mostrar el promedio de notas de las mujeres'''

lista_nombre = []
lista_sexo = []
lista_nota = []
bandera_nota_baja = True
nota_mas_baja = 10
contador_femenino = 0
acumulador_femenino = 0
promedio_femenino = 0

for i in range(5):
    nombre = input("Ingrese su nombre: ")

    sexo = input("Ingrese su sexo f/m: ")
    while sexo != "f" and sexo != "m":
        sexo = input("Ingrese su sexo f/m: ")

    nota = int(input("Ingrese su nota: "))
    while nota < 1 or nota > 10:
        nota = int(input("Error. Ingrese su nota: "))
    
    lista_nombre.append(nombre)
    lista_nota.append(nota)
    lista_sexo.append(sexo)

    if sexo == "m":
        if bandera_nota_baja == True or nota < nota_mas_baja:
            nota_mas_baja = nota
            nombre_nota_baja = nombre
            bandera_nota_baja = False
    else:
        contador_femenino +=1
        acumulador_femenino += nota
        promedio_femenino = acumulador_femenino / contador_femenino

if bandera_nota_baja == True:
    print("No hay alumnos masculinos")
else:
    print(f'El nombre del hombre con nota más baja es {nombre_nota_baja} y su nota es de: {nota_mas_baja}')

        
print(f'El promedio de la nota de las mujeres es de: {promedio_femenino}')




