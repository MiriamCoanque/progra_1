'''Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su
sueldo para esa persona.'''

nombre = input("Ingrese su nombre: ")
sueldo = int(input("Ingrese su sueldo: "))

sueldo_con_aumento = sueldo + sueldo * 0.10

print(f'Su nombres es {nombre} y su sueldo con un aumento del 10% es: {sueldo_con_aumento} $')