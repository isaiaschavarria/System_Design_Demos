from termcolor import colored

def leer_libro(usuario):
    print(colored(f"{usuario} empieza a leer un libro", 'green'))
    print(colored(f"{usuario} termina de leer el libro", 'green'))

def dejar_comentario(usuario):
    print(colored(f"{usuario} empieza a escribir un comentario", 'cyan'))
    print(colored(f"{usuario} publica su comentario", 'cyan'))

if __name__ == '__main__':
    leer_libro("Usuario 1"),
    dejar_comentario("Usuario 2")
