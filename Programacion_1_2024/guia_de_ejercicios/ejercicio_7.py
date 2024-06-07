'''Dada la siguiente lista:
[82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
mostrar solo los números pares.'''

lista_num = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]

for e_lista in lista_num:
    if e_lista % 2 == 0:
        numero_par = e_lista
        print(f'Número par: {numero_par}')