'''Ingresar 5 números enteros, distintos de cero.
Informar:
a. Cantidad de pares e impares.
b. El menor número ingresado.
c. De los pares el mayor número ingresado.
d. Suma de los positivos.
e. Producto de los negativos.'''

i = 0
contador_par = 0
contador_impar = 0
numero_menor = 0
numero_mayor = 0
bandera_menor = True
bandera_mayor = True #la puedo poner con True
acumulador_positivos = 0
producto_negativo = 1

while i < 5: #si sé la cantidad de veces USO FOR "for i in range (0,5)"
    numero = int(input("Ingrese un numero entero distinto de cero: "))

    while numero == 0:
        print("Error, el numero debe ser distinto de cero")
        numero = int(input("Ingrese un numero entero distinto de cero: "))
    
    if bandera_menor == True or numero < numero_menor:
        numero_menor = numero
        bandera_menor = False

    if numero % 2 == 0:
        contador_par += 1
        if bandera_mayor == True or numero > numero_mayor:
            numero_mayor = numero
            bandera_mayor = False
    else:
        contador_impar += 1
    
    if numero > 0:
        acumulador_positivos += numero
    else:
        producto_negativo *= numero
   
      
    i += 1

print(f" La cantidad de numeros pares es: {contador_par} y la de impares es: {contador_impar}")
print(f"El numero menor encontrado es: {numero_menor}")
print(f"El numero mayor que es par es: {numero_mayor}")
print(f"La suma de numeros positivos da: {acumulador_positivos}")
print(f"El producto de los negativos es: {producto_negativo}")
    