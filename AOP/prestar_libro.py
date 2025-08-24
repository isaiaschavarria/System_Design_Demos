
from Aspects import loggear, requiere_autorizacion
from termcolor import colored


@requiere_autorizacion
@loggear
def prestar_libro(usuario, libro_id):
    print(colored(f"{usuario} ha prestado el libro {libro_id}", "green"))
