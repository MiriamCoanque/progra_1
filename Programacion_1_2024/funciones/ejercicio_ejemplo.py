'''#PEDIR DOS NUMEROS Y MOSTRAR LA SUMA
#1)FUNCION SIN PARAMETROS NI RETORNOS
#2)FUNCION SIN PARAMETROS CON RETORNO
#3)FUNCION CON PARAMETROS SIN RETORNO
#4)FUNCION CON PARAMETROS CON RETORNO'''

'''#1)FUNCION SIN PARAMETROS NI RETORNOS

def funcion_sin_parametro_ni_retorno():
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese un numero: "))
    suma = num1 + num2
    resultado = print(f'El resultado de la suma es: {suma}')

funcion_sin_parametro_ni_retorno()'''


'''#2)FUNCION SIN PARAMETROS CON RETORNO

def funcion_sin_parametro_con_retorno():
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese un numero: "))
    suma = num1 + num2
    return suma

resultado = funcion_sin_parametro_con_retorno()
print(f'El resultado de la suma es: {resultado}')
'''


'''#3)FUNCION CON PARAMETROS SIN RETORNO

def funcion_con_parametros_sin_retorno(num_uno:int , num_dos:int)-> int:
    suma = num_uno + num_dos
    resultado = print(f'El resultado de la suma es: {suma}')

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))

funcion_con_parametros_sin_retorno(num1,num2)'''


#4)FUNCION CON PARAMETROS CON RETORNO

def funcion_con_parametros_con_retorno(num_uno:int , num_dos:int)-> int:
    suma = num_uno + num_dos
    return suma

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))

resultado = funcion_con_parametros_con_retorno(num1,num2)
print(f'El resultado de la suma es: {resultado}')

    







    