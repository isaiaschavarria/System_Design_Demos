from prestar_libro import prestar_libro
from termcolor import colored

# Usuario autorizado
print(colored(f"\nIniciando proceso de prestar libro (admin_luis)", "green"))
prestar_libro("admin_luis", "LIBRO-123")

# Usuario no autorizado
print(colored(f"\nIniciando proceso de prestar libro (Juan)", "green"))
prestar_libro("Juan", "LIBRO-456")  # Lanzará PermissionError
