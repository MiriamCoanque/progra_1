'''Realizar una función con el siguiente Menú de Opciones:
A. Listar ordenado por Nombre. Lista todos los datos de cada superhéroe ordenados por Nombre de manera ascendente.
B. Listar Masculinos débiles. Recorrer la lista y determinar cuál es el superhéroe más débil de género M.
C. Cantidad por color de ojos. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
D. Listar por color de Pelo. Listar todos los superhéroes agrupados por color de pelo.
E. Listar inteligencia. Listar todos los superhéroes agrupados por tipo de inteligencia.
F. Listar Promedio. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género) los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino
G. Asignar IMC. Calcular el índice de masa corporal de cada superhéroe y guardarla en un nuevo campo. Se deberá hacer uso de una función lambda que asignará a cada superhéroe el IMC calculado.'''

from data_stark import lista_personajes
from biblioteca_stark1 import *


while True:
    opcion = menu()

    if opcion == "A":
        resultado = ordenar_lista_por_clave(lista_personajes, 'nombre', 'ascendente')
        mostrar_lista_ordenada(resultado)
        
    elif opcion == "B":
        resultado = encontrar_max_min_con_dos_claves(lista_personajes,"fuerza", "M", "min")
        mostrar_max_min(resultado)
    elif opcion == "C":
        conteo_color_ojos = cantidad_de_un_tipo(lista_personajes, "color_ojos")
        mostrar_cantidad_tipo(conteo_color_ojos)

    elif opcion == "D":
        agrupados_por_color_pelo = mostrar_lista_por_clave(lista_personajes, "color_pelo")
        mostrar_agrupados_color_pelo(agrupados_por_color_pelo)
    elif opcion =="E":
        agrupados_por_inteligencia = mostrar_lista_por_clave(lista_personajes, "inteligencia")
        mostrar_agrupados_inteligencia(agrupados_por_inteligencia)

    elif opcion == "F":
        personas_que_superan_promedio = listar_promedio(lista_personajes, 'fuerza', 'genero', 'F')
        mostrar_promedio(personas_que_superan_promedio)

    elif opcion == "G":
        lista_imc = calcular_imc(lista_personajes, "altura", "peso")
        mostrar_imc(lista_imc)
        
    elif opcion == "H":
        mostrar_despedida()
        break