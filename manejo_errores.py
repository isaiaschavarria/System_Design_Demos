from termcolor import colored

def descargar_libro(nombre_libro):
    try:
        if nombre_libro != "El Quijote":
            raise FileNotFoundError(f"No se encontró el libro '{nombre_libro}'")
        
        print(colored(f"Descargando '{nombre_libro}'...", 'green'))
    except FileNotFoundError as e:
        print(colored(f"Error: {e}", 'red'))
    except Exception as e:
        print(colored(f"Error inesperado: {e}", 'red'))
    else:
        print(colored("Descarga completada exitosamente", 'green'))
    finally:
        print(colored("Proceso de descarga finalizado\n", 'blue'))

descargar_libro("Harry Potter")
descargar_libro("El Quijote")
