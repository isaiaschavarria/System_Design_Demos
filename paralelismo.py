from multiprocessing import Process
import time
from termcolor import colored

#En lenguajes como Python (con CPython), el GIL (Global Interpreter Lock) 
# puede limitar la ejecución real a un solo hilo a la vez (aunque hay excepciones como usar multiprocessing o C-extensions).
#En lenguajes como Java, C/C++, Rust, Go, el threading real puede 
# aprovechar múltiples núcleos efectivamente, incluyendo múltiples CPUs físicos.

def generar_recomendaciones():
    print(colored("Backend: Generando recomendaciones...", 'yellow'))
    time.sleep(4)
    print(colored("Backend: Recomendaciones listas", 'yellow'))

def procesar_logs():
    print(colored("Backend: Procesando logs de uso...", 'green'))
    time.sleep(2)
    print(colored("Backend: Logs procesados", 'green'))

if __name__ == '__main__':
    p1 = Process(target=generar_recomendaciones)
    p2 = Process(target=procesar_logs)

    p1.start()
    p2.start()

    p1.join()
    p2.join()