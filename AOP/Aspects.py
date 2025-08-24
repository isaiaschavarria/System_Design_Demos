from termcolor import colored
from functools import wraps

def loggear(func):
    def wrapper(*args, **kwargs):
        print(colored(f"[LOG] Ejecutando proceso de logger con {args}", "green"))
        resultado = func(*args, **kwargs)
        print(colored(f"[LOG] Finalizó proceso de logger {func.__name__}", "green"))
        return resultado
    return wrapper

def requiere_autorizacion(func):
    def wrapper(usuario, *args, **kwargs):
        if not usuario.startswith("admin"):
            print(colored(f"El usuario '{usuario}' no tiene permisos para esta acción.", "red"))
            return 
        return func(usuario, *args, **kwargs)
    return wrapper
