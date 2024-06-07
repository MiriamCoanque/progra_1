'''Ejercicio 1: Se trabajará con el archivo estudiantes.py
Realizar una función con el siguiente Menú de Opciones:

1-Listar los alumnos por orden ascendente de apellido, si se repite,
ordenar por nombre. Mostrar legajo, nombre, apellido y edad
2-Obtener el promedio de notas para cada estudiante
3-Listar legajo, nombre, apellido y edad de los estudiantes que cursan el
programa de “Ingenieria en Informatica”
4-Obtener un promedio de edad de los estudiantes. Mostrar nombre y
apellido
5-Informar el alumno con mayor pomedio de notas. Mostrar nombre y
apellido
6-Listar nombre y apellido de los alumnos que forman el grupo “Club de
Informática” con sus respectivos promedios
7-Listar legajo, nombre, apellido y programas que cursan los alumnos
más jóvenes.'''

from estudiantes import *
from biblioteca_1 import *


while True:
    opcion = menu()

    if opcion == 1:
        listar_alumnos_ascendente(estudiantes)
        
          
    if opcion == 2:
        promedio = promediar_notas(estudiantes)
        print(f"El promedio de las notas es: {promedio:.2f}")

    if opcion == 3:
        listar_estudiantes_inge_informatica(estudiantes)
    if opcion == 4:
        listar_edad_joven(estudiantes)
    if opcion == 5:
        mayor_promedio_notas(estudiantes)
    if opcion == 6:
        listar_por_grupo_con_promedio(estudiantes)
    if opcion == 7:
        listar_edad_joven_con_programa(estudiantes)
    if opcion == 8:
        print("Ha elegido salir :)")
        break