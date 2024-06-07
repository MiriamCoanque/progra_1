'''Realizar un programa en donde se puedan utilizar los prototipos de la
función Restar en sus 4 combinaciones.
1_ Restar1(int, int)->int:
2_ Restar2()->int:
3_ Restar3(int, int):
4_ Restar4():'''


def menu():
    print('''            
            1-Restar1(int, int) ->int
            2-Restar2()->int
            3-Restar3(int, int)
            4-Restar4()
            5- Salir''')
    opcion = int(input("opcion: "))
    return opcion

def ingresar_numero():
    num = int(input("Ingrese un numero: "))
    return num

def restar_con_parametros_con_retorno(num_uno:int , num_dos:int)-> int:
    resta = num_uno - num_dos
    return resta

def restar_sin_parametro_con_retorno():
    num1 = ingresar_numero()
    num2 = ingresar_numero()
    resta = num1 - num2
    return resta

def restar_con_parametros_sin_retorno(num_uno:int , num_dos:int)-> int:
    resta = num_uno - num_dos
    resultado = print(f'El resultado de la resta es: {resta}')

def restar_sin_parametro_ni_retorno():
    num1 = ingresar_numero()
    num2 = ingresar_numero()
    resta = num1 - num2
    resultado = print(f'El resultado de la resta es: {resta}')


while True:
    opcion = menu()

    if opcion == 1:
        num1 = ingresar_numero()
        num2 = ingresar_numero()

        resultado = restar_con_parametros_con_retorno(num1,num2)
        print(f'El resultado es: {resultado}')
    elif opcion == 2:
        resultado = restar_sin_parametro_con_retorno()
        print(f'El resultado de la resta es: {resultado}')
    elif opcion == 3:
        num1 = ingresar_numero()
        num2 = ingresar_numero()

        resultado = restar_con_parametros_sin_retorno(num1,num2)
    elif opcion == 4:
        restar_sin_parametro_ni_retorno()
    elif opcion == 5:
        print("Fin del programa :)")
        break
'''importar listas -> en el 7 de funciones y listas, tenemos una funcion.py// tenemos nuestras funciones
poniamos from NOMBRE import *
no se nos dio funciones, sino listas
hacemos
lista_personas import *
lista_nombres = nombre -> para poder utilizarlo


'''