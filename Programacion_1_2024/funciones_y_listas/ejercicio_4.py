'''Desarrollar una función que reciba por parámetro, una lista de números
y un número especificado. La misma debe buscar el número especificado en la lista
y retornar “True” si existe.'''

def buscar_numero_en_lista(lista_num:list, num:int)->bool:

    return num in lista_num

lista = [1,23,6,18,22,45,64,71,9]
num = [2]


print(buscar_numero_en_lista(lista,num))