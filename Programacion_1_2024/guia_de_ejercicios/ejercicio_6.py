'''Utilizar For
Dada la siguiente lista:
[82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
mostrar el mayor.'''

lista_num = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
bandera = True #la bandera es para tomar el 1er num como si fuera el mayor y de ahi empieza a compararlo con los otros

for e_lista in lista_num:
    if bandera == True or e_lista > numero_mayor:
        numero_mayor = e_lista
        bandera = False

print(f'El numero mayor es: {numero_mayor}')