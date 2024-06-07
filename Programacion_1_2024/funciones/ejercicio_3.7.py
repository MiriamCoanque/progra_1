'''Realizar un programa que: asigne a las variables numero1 y numero2
los valores solicitados al usuario, valide los mismos entre 10 y 100, asigne a la
variable operacion el valor solicitado al usuario: 's'-sumar, 'r'-restar (validar),realice
la operación de dichos valores a través de una función. Mostrar el resultado por
pantalla.'''

def ingresar_numero():
    num = int(input("Ingrese un numero: "))
    return num

def validar_num_entre_rangos(numero:int)->int:
    while numero < 10 or numero > 100:
        print("Error, ingrese nuevamente: ")
        numero = ingresar_numero()
    return numero

def restar_numeros(num_uno:int , num_dos:int)-> int:
    resta = num_uno - num_dos
    return resta

def sumar_numeros(num_uno:int , num_dos:int)-> int:
    suma = num_uno + num_dos
    return suma

def validar_operacion(operacion:str) -> str:
    while operacion != "s" and operacion != "r":
        operacion = input("Error, ingrese nuevamente: ")
    return operacion

def operacion(num1:int , num2:int , operacion:str)->int:
    if operacion == 's':
        resultado = sumar_numeros(num1,num2)
    else:
        resultado = restar_numeros(num1,num2)
    
    return resultado

def mostrar_resultado(num1:int, num2:int):
    resultado = operacion(num1, num2,operacion_elegida)
    print(f"El resultado es: {resultado}")

def menu():
    print('''            
            1-Ingresar dato
            2-Validar dato
            3-Realizar operación
            4- Mostrar resultado
            5- Salir''')
    opcion = int(input("opcion: "))
    return opcion

bandera_primera_opcion = False
bandera_segunda_opcion = False
bandera_tercera_opcion = False
while True:
    opcion = menu()

    if opcion == 1:
        bandera_primera_opcion = True
        numero1 = ingresar_numero()
        numero2 = ingresar_numero()
    elif opcion == 2:
        if bandera_primera_opcion == False:
            print("Primero debe ingresar los numeros")
        else:           
            numero1 = validar_num_entre_rangos(numero1)
            numero2 = validar_num_entre_rangos(numero2)
            print("Numeros validados")
        
        bandera_segunda_opcion = True
    elif opcion == 3:
        if bandera_primera_opcion == False:
            print("Primero debe ingresar los numeros")
        elif bandera_segunda_opcion == False:
            print("Primero debe validar el numero antes de realizar la operacion")
        else:
            operacion_elegida = validar_operacion(input("Ingrese la operacion: "))
            print(f'Usted eligió: {operacion_elegida}')
       
        bandera_tercera_opcion = True
    elif opcion == 4:
        if bandera_primera_opcion == False:
            print("Primero debe ingresar los numeros")
        elif bandera_segunda_opcion == False:
            print("Primero debe validar los numeros antes de realizar la operacion")
        elif bandera_tercera_opcion == False:
            print("Debe realizar la operacion antes de mostrar el resultado")
        else:
            mostrar_resultado(numero1, numero2)

    else:
        print("Fin del programa :)")
        break