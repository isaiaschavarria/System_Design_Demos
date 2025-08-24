"""Módulo de gestión de biblioteca: libros y usuarios."""

class Libro:
    """Representa un libro en la biblioteca."""

    def __init__(self, titulo, autor):
        """Inicializa el libro con título y autor."""
        self.titulo = titulo
        self.autor = autor
        self.prestado = False

    def prestar(self):
        """Marca el libro como prestado."""
        self.prestado = True

    def devolver(self):
        """Marca el libro como devuelto."""
        self.prestado = False


class Usuario:
    """Representa un usuario de la biblioteca."""

    def __init__(self, nombre):
        """Inicializa el usuario con nombre y lista de préstamos."""
        self.nombre = nombre
        self.prestamos = []

    def tomar_prestado(self, libro):
        """El usuario toma prestado un libro si está disponible."""
        if not libro.prestado:
            libro.prestar()
            self.prestamos.append(libro)

    def devolver_libro(self, libro):
        """Devuelve un libro si lo tiene en su lista de préstamos."""
        if libro in self.prestamos:
            libro.devolver()
            self.prestamos.remove(libro)
