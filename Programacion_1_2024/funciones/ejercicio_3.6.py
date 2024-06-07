'''Realizar un programa que: asigne a la variable numero1 un valor
solicitado al usuario, valide el mismo entre 10 y 100, realice un descuento del 5% a
dicho valor a través de una función llamada realizarDescuento(). Mostrar el resultado
por pantalla. Atención: pueden reutilizarse funciones ya creadas.'''

def menu():
    print('''            
            1-Ingresar dato
            2-Validar dato
            3-Realizar descuento
            4- Salir''')
    opcion = int(input("opcion: "))
    return opcion

def ingresar_numero():
    num = int(input("Ingrese un numero: "))
    return num

def validar_num(numero:int)->int:
    while numero < 10 or numero > 100:
        print("Error, ingrese nuevamente: ")
        numero = ingresar_numero()
    return numero

def realizar_descuento(num):
    descuento = num * 0.05
    resultado = num - descuento
    return resultado


while True:
    opcion = menu()

    if opcion == 1:
        numero = ingresar_numero()
    elif opcion == 2:
        numero = validar_num(numero)
        print("Numero validado")
    elif opcion == 3:
        resultado_descuento = realizar_descuento(numero)
        print(f"El resultado con descuento es: {resultado_descuento}")
    elif opcion == 4:
        print("Fin del programa :)")
        break


