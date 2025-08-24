class Libro:
    def __init__(self):
        self.disponible = True

    def prestar(self):
        # Precondición: el libro debe estar disponible
        assert self.disponible is True, "El libro no está disponible para préstamo."

        # Acción
        self.disponible = False
        print("Libro Prestado correctamente")

        # Postcondición: el libro ya no debe estar disponible
        assert self.disponible is False, "El estado del libro después del préstamo es incorrecto."


libro = Libro()

libro1 = libro.prestar()

libro2 = libro.prestar()

