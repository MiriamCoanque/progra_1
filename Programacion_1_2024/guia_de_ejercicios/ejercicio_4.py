'''Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil
distinto a "Soltero", mostrar el siguiente mensaje: 'Es muy pequeño para NO
ser soltero.'''

edad = int(input("Ingrese su edad: "))

while edad < 1:
    print("Error")
    edad = int(input("Ingrese su edad: "))

estado_civil = input("Ingrese su estado civil: ")

if edad < 18 and estado_civil != "Soltero":
    print(f"Es muy pequeño para NO ser soltero")
else:
    print(f"Su edad es: {edad} y es {estado_civil}")




