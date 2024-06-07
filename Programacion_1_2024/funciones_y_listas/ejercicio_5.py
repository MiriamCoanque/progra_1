'''Dadas las siguientes listas:
Nombres=["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Ped
ro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
Desarrollar una función que reciba por parámetro la lista de edades, busque a las
personas de menor edad (puede ser más de una) y las retorne. El programa
principal deberá mostrar nombre y edad de los menores.'''

nombres=["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

def buscar_persona_menor_con_dos_listas(lista_edades:list,lista_nombres)->tuple:

    bandera = True #la bandera es para tomar el 1er num como si fuera el mayor y de ahi empieza a compararlo con los otros
    for edad, nombre in zip(lista_edades,lista_nombres): #zip une listas y crea tuplas
        if bandera == True or edad < edad_menor:
            edad_menor = edad
            nombre_menor = nombre
            bandera = False

    return edad_menor , nombre_menor

menor_edad , menor_persona = buscar_persona_menor_con_dos_listas(edades,nombres)
print(f'La persona más joven es {menor_persona} y tiene {menor_edad}')    