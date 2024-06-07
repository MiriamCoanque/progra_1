'''Dada la siguiente lista:
[82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
mostrar el número repetido'''

lista_num = [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
numeros_vistos = set() 

for e_lista in lista_num:
    if e_lista in numeros_vistos: #si mi elemento ya lo vi, lo muestro 
        print(f'num repetido: {e_lista}')
    else:
        numeros_vistos.add(e_lista) #sino lo agrego a set() el cual guarda cada uno SOlO 1 vez (no repetidos)

'''
for i range(len(lista)):
    for j range(elemento+1; len(lista)):
        if elemento [i] == elemento [j]:
            print(f'el repetido es: {elemento[i]}')
            break'''

        