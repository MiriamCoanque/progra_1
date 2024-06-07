def menu():
    print('''            
            A. Listar ordenado por Nombre. Lista todos los datos de cada superhéroe ordenados por Nombre de manera ascendente.
            B. Listar Masculinos débiles. Recorrer la lista y determinar cuál es el superhéroe más débil de género M.
            C. Cantidad por color de ojos. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
            D. Listar por color de Pelo. Listar todos los superhéroes agrupados por color de pelo.
            E. Listar inteligencia. Listar todos los superhéroes agrupados por tipo de inteligencia.
            F. Listar Promedio. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género) los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino
            G. Asignar IMC. Calcular el índice de masa corporal de cada superhéroe y guardarla en un nuevo campo. Se deberá hacer uso de una función lambda que asignará a cada superhéroe el IMC calculado.
            H. Salir.''')
    opcion = input("opcion: ").upper()
    return opcion 



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
    

def encontrar_max_min_con_dos_claves(lista:list, clave1:str, clave2:str, valorclave2:str, tipo:str)->dict:
    '''Recibe la lista, la clave1 (atributo como fuerza), clave2 (atributo para filtrar como género)
    y tipo (min o max).'''
    
    retorno = -1
    if type(lista) == list and type(clave1) == str and type(clave2) == str and type(valorclave2) == str and type(tipo) == str and len(lista) > 0:
        lista_valor = []
        for personaje in lista:
            if clave2 in personaje and personaje[clave2] == valorclave2:
                lista_valor.append(personaje)

        max_min = lista_valor[0]
        for personaje in lista_valor[1:]:
            if tipo == "max" and personaje[clave1] > max_min[clave1]:
                max_min = personaje
            elif tipo == "min" and personaje[clave1] < max_min[clave1]:
                max_min = personaje

        retorno = max_min

    return retorno


def cantidad_de_un_tipo(lista, clave)->dict:
    ''''función: 
        contar la cantidad dependiendo la clave

        recibe: 
        lista que es la lista de donde contaré cada cosa especifica
        clave que es la clave que buscaré a contar
        
        retorna:
        devuelve un diccionario'''
    
    cantidad = {}
    
    if type(lista) == list and type(clave) == str and len(lista) > 0:
        for personaje in lista:
            if clave in personaje:
                if personaje[clave] in cantidad:
                    cantidad[personaje[clave]] += 1 #si existe sumo otro más
                else:
                    cantidad[personaje[clave]] = 1 #sino lo creo yo
    
    return cantidad

def mostrar_lista_por_clave(lista:list, clave:str)->dict:
    '''
    recibe:
        lista en la cual trabajaré
        clave con la cual buscaré en mi lista
    retorna:
        retorna un diccionario con mi clave que elijo y su valor
    '''
    dic_nuevo = {}

    if type(lista) == list and type(clave) == str and len(lista) > 0:
        for personaje in lista:
            if clave in personaje:
                if personaje[clave]:
                    valor = personaje[clave] #así es más practico
                else:
                    valor = "Desconocido"
                
                if valor not in dic_nuevo:
                    dic_nuevo[valor] = [] #sino está yo le creo una lista vacia para ponerlo
                    
                dic_nuevo[valor].append(personaje["nombre"])


        return dic_nuevo

def listar_promedio(lista:list, clave1:str, clave2:str,tipo:str)->list:
    '''
    funcion:
    mostrar personas que superen el promedio establecido por las claves
    recibe:
    lista: en la cual trabajaré
    clave1: el atributo fuerza
    clave2: el atributo genero
    retorna:
    los datos de las personas que superan el promedio de la clave1

    '''
    contador = 0
    acumulador = 0
    for persona in lista:
        if clave2 in persona:
            if persona[clave2] == tipo:
                 if clave1 in persona:
                     contador += 1
                     acumulador += int(persona[clave1]) #casteado a int porque es un str cono tal
 
    promedio = acumulador / contador
    personas_superan_promedio = []
    
    print(f"\tPERSONAJES CON FUERZA MAYOR AL PROMEDIO FEMENINO ({promedio:.2f} %)")
    
    for persona in lista:
        if clave1 in persona:
            if int(persona[clave1]) > promedio:
                personas_superan_promedio.append({"nombre": persona['nombre'], "genero": persona['genero'], "peso": persona['peso'], "fuerza": persona['fuerza']})
    return personas_superan_promedio  

def calcular_imc(lista: list, clave1: str, clave2: str) -> list:
    ''''
    función: 
    calcular el imc
    recibe:
    lista: en la cual trabajaré
    clave1: clave para obtener la altura
    clave2: clave para obtener el peso
    retorna: 
    lista de personajes su imc ya calculado
    '''
    calcular = lambda peso, altura: peso / (altura ** 2) # altura al cuadrado
    
    for persona in lista:
        persona["imc"] = round(calcular(float(persona[clave2]),float(persona[clave1]) / 100))#redondeo
        
    return lista

def mostrar_imc(lista:list):
    for persona in lista:
            print(f"Nombre: {persona['nombre']:<20}\tIMC: {persona['imc']}")

def mostrar_promedio(lista:list):
    for personaje in lista:
            print(f"Nombre: {personaje['nombre']:<20}\t Genero: {personaje['genero']:<10}\t Peso: {personaje['peso']:<25}\t Fuerza: {personaje['fuerza']:<10}") 

def mostrar_cantidad_tipo(lista:dict):
    for color_ojos, cantidad in lista.items():
            print(f"{color_ojos}: {cantidad}")   

def mostrar_agrupados_inteligencia(lista:dict):
    for inteligencia, personajes in lista.items():
            print(f"Inteligencia: {inteligencia}")

            for nombre in personajes:
                print(f"{nombre}")

def mostrar_agrupados_color_pelo(lista:dict):
    for color, personajes in lista.items():
            print(f"Color de pelo: {color}")
    
            for nombre in personajes:
                print(f"{nombre}")    


def mostrar_max_min(lista:dict):
    if lista != -1:
        print(lista["nombre"])
    else:
        print("Error")

def mostrar_lista_ordenada(lista:list):
    if lista is not None:
            for personaje in lista:
                print(personaje['nombre'])

def mostrar_despedida():
    print("Ha elegido salir :)")

        
    



