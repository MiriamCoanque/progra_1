'''Dadas las siguientes listas:
Nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
Desarrollar una función que realice el ordenamiento de las listas por nombre de
manera ascendente.'''

nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]


def ordenar_listas_ascendente(lista1:list,lista2:list):

    for i in range(len(lista1)-1):
        for j in range(i+1, len(lista1)):
            if lista1[i] > lista1[j]:
                auxiliar_lista1 = lista1[i]
                auxiliar_lista2 = lista2[i]

                lista1[i] = lista1[j]
                lista2[i] = lista2[j]

                lista1[j] = auxiliar_lista1
                lista2[j] = auxiliar_lista2           
    return lista1 ,  lista2


resultado_edades, resultado_nombres = ordenar_listas_ascendente(edades, nombres)

print(f'Edades ordenadas: {resultado_edades}')
print(f'Nombres ordenados: {resultado_nombres}')