'''Pedir una edad. Informar si la persona es mayor de edad (más de 18 años),
adolescente (entre 13 y 17 años) o niño (menor a 13 años).'''

edad = int(input("Ingrese su edad: "))

while edad < 1:
    print("Error")
    edad = int(input("Ingrese su edad: "))

if edad > 18:
    print("Eres mayor de edad")
elif edad < 13:
    print("Eres un niño")
else:
    print("Eres un adolescente")