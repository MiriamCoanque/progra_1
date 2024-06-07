'''Ejemplo: Clase para representar un Libro
Crear una clase Libro que tenga las características títuto, autor y año de publicación. Del libro se
debe poder obtener información, mostrando por mensaje todos sus datos. Se debe crear la clase
e implementarla.'''

class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año
    
    def informacion_libro(self):
        print(f"Titulo de libro: {self.titulo}, Autor: {self.autor}, Fecha de publicación: {self.año}")

libro = Libro(titulo = 'Nombre original', autor = 'Pepe', año = 1999)

libro.informacion_libro()
        