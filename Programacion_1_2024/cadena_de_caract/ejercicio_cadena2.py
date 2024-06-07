'''Ejercicio 2: Desarrollar una función que reciba una cadena y dos índices.
Se debe retornar la cadena que va entre las posiciones indicadas por los índices.
Si las posiciones no son válidas se debe informar.'''

def verificar_posiciones(cadena:str,indice1:int,indice2:int)->str:
    if indice1 < 1 or indice2 >= len(cadena) or indice1 >= indice2:
        return "posición no encontrada"
    
    sub_cadena = cadena[indice1:indice2+1]
    return sub_cadena
    

cadena = "parangaricutirimicuaro"
indice1 = 3
indice2 = 7

print(verificar_posiciones(cadena, indice1, indice2))
