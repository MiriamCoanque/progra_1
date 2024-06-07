def validar_numero(desde:int, hasta:int)->int:
    '''pide por consola un numero dentro de los variables
    retorna ese numero'''
    numero = int(input("Ingrese un número: "))
    while numero < desde or numero > hasta:
        numero = int(input("Ingrese nuevamente: "))

    return numero

def opcion_continuar(respuesta: str) -> bool:
    return respuesta.lower() == 'si'



def pedir_y_guardar(cantidad:int)->list:
    '''recibe como parametro la cantidad de numeros que tendrá la lista
    valida los numeros y los agrega a la lista'''

    lista_num = []
    for i in range(cantidad):
        numeros = validar_numero(0, 1000)
        lista_num.append(numeros) 
        respuesta = input("Desea continuar? 'Si/No': ")
        if not opcion_continuar(respuesta):
            break
    return lista_num

'''ejemplo:

print("Lista de números:", pedir_y_guardar(5))'''


def ordenar_lista_por_clave(lista:list, clave:str,tipo:str):
    """
    función:
    ordenar por la clave dada de forma ascendente
    
    recibe:
    lista:lista de diccionarios a ordenar
    clave:clave por la cual se ordenará
    tipo: si es tipo ascendente o descendiente
    
    retorna: 
    lista de diccionarios ya ordenados
    """
  
    if tipo not in ["ascendente", "descendiente"]:
            print("Error, debe ordenar de forma ascendente o descendiente")
            return None

    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if tipo == "ascendente" and lista[i][clave] > lista[j][clave]:
                auxiliar = lista[i]
                lista[i] = lista[j]
                lista[j] = auxiliar

            elif tipo == "descendiente" and lista[i][clave] < lista[j][clave]:
                auxiliar = lista[i]
                lista[i] = lista[j]
                lista[j] = auxiliar

    return lista 

def calcular_max_min(lista:list, clave:str, tipo:str)->dict:
    '''recibe la lista, la clave con la que buscaré el min o max y el tipo
    por si es el min o max'''
    
    retorno = -1
    if type(lista) == type(list()) and type(clave) == str and len(lista) > 0:
        max_min = lista[0]
        for e_lista in lista:
            if tipo == "max" and e_lista[clave] > max_min[clave]:
                max_min = e_lista
            
            if tipo == "min" and e_lista[clave] < max_min[clave]:
                max_min = e_lista
        retorno = max_min
    return retorno

'''resultado = calcular_max_min(nombredelalista,porloquelobusco,siesmaxoomin)
if resultado == -1:
    print(error)
else:
    print(resultado) TODO ESTO ES OLO PARA UN MAX Y UN MIN'''    


def menu():
    print('''            
            1-
            2-
            3-
            4-Salir.''')
    opcion = int(input("opción: "))
    return opcion
def saludar():
    print("Bienvenido")

bandera_primera_opcion = False
while True:
    opcion = menu()
    if opcion == "1":
        bandera_primera_opcion == True
        saludar()
    elif opcion == "2":
        if bandera_primera_opcion == True:
            '''poner que sucede aqui'''
        else:
            print("Primero debe pasar por el punto 1")
    elif opcion == 3:
        pass