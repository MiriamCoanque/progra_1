'''Ejercicio 3: Dadas las siguientes listas:
Estudiantes =
["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Anto
nio", "Eugenia", "Soledad", "Mario", "María"]
Apellidos =
[“Sosa”,”Gutierrez”,”Alsina”,”Martinez”,”Sosa”,”Ramirez”,”Perez”,”Lopez”,”Arregui”
,”Mitre”,”Andrade”,”Loza”,”Antares”,”Roca”,”Perez”]
Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]
Desarrollar una función que realice el ordenamiento de las listas por apellido de
manera ascendente, si el apellido es el mismo, debe ordenar por nombre de manera
ascendente, si el nombre también es el mismo, debe ordenar por nota de manera
descendente.'''

estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"]
apellidos = ["Sosa","Gutierrez","Alsina","Martinez","Sosa","Ramirez","Perez","Lopez","Arregui" ,"Mitre","Andrade","Loza","Antares","Roca","Perez"]
notas = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]

for i in range(len(apellidos)-1):
    for j in range(i+1 ,len(apellidos)):
        if apellidos [i] > apellidos [j]:

            auxiliar_apellidos = apellidos [i]
            apellidos [i] = apellidos [j]
            apellidos [j] = auxiliar_apellidos

            auxiliar_estudiantes = estudiantes [i]
            estudiantes [i] = estudiantes [j]
            estudiantes [j] = auxiliar_estudiantes

            auxiliar_notas = notas [i]
            notas [i] = notas [j]
            notas [j] = auxiliar_notas


        elif apellidos [i] == apellidos [j]:
            if estudiantes [i] > estudiantes [j]:

                auxiliar_estudiantes = estudiantes [i]
                estudiantes [i] = estudiantes [j]
                estudiantes [j] = auxiliar_estudiantes

                auxiliar_notas = notas [i]
                notas [i] = notas [j]
                notas [j] = auxiliar_notas

            elif estudiantes [i] == estudiantes [j]:
                if notas [i] < notas [j]:
                    auxiliar_notas = notas [i]
                    notas [i] = notas [j]
                    notas [j] = auxiliar_notas
            
for nombre, apellido, nota in zip(estudiantes, apellidos, notas): #combina y crea una tupla para tenerlos juntos
    print(f'{nombre} {apellido} : {nota}')

                