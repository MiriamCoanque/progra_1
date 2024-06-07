'''Dadas las siguientes listas:
Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias
Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos",
"Base de Datos", "Ergonomia", "Naturaleza"]
Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]
Desarrollar una función que realice el ordenamiento de las listas por nombre de
manera ascendente, si el nombre es el mismo, debe ordenar por puntos de manera
descendente.'''

nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos","Base de Datos", "Ergonomia", "Naturaleza"]
puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]

for i in range(len(nombres)-1):
    for j in range(i+1 , len(nombres)):
        if nombres [i] > nombres [j]:
            auxiliar_nombre = nombres [i]
            auxiliar_puntos = puntos [i]

            nombres [i] = nombres [j]
            nombres [j] = auxiliar_nombre

            puntos [i] = puntos [j]
            puntos [j] = auxiliar_puntos

        elif nombres [i] == nombres [j]:
            if puntos [i] < puntos [j]:
                auxiliar_nombre = nombres [i]
                auxiliar_puntos = puntos [i]
                 
                nombres [i] = nombres [j]
                nombres [j] = auxiliar_nombre 

                puntos [i] = puntos [j]
                puntos [j] = auxiliar_puntos

for nombre, punto in zip(nombres, puntos): #combina y crea una tupla para tenerlos juntos
    print(f'{nombre}: {punto}')