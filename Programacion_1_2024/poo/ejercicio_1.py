'''Ejemplo: Clase simple
Crear una clase Persona que tenga las características nombre y edad. La persona debe poder
mostrar un mensaje saludando presentándose con su nombre y edad. Se debe crear la clase e
implementarla.'''

class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")


juan = persona(nombre="ASDFGHJKL", edad=11111)

juan.saludar() 
    