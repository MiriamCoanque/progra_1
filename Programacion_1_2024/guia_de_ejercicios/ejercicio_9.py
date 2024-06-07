'''Dadas las siguientes listas:
edades = [25,36,18,23,45]
nombre = ["Juan","Ana","Sol","Mario","Sonia"]
y considerando que la posición en la lista corresponde a la misma persona,
mostrar el nombre de la persona más joven'''

edades = [25,36,18,23,45]
nombres = ["Juan","Ana","Sol","Mario","Sonia"]
edad_joven = edades[0]
nombre_joven = nombres[0]

for e_edades in range(len(edades)):
    if(edades[e_edades] < edad_joven):
        edad_joven = edades [e_edades]
        nombre_joven = nombres [e_edades]
                   
print("nobre más joven: ", nombre_joven)




