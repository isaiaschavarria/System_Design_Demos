from multiprocessing import Process, Manager
import time
from termcolor import colored

def generar_recomendaciones(resultados):
    print(colored("Backend: Generando recomendaciones...", 'yellow'))
    time.sleep(4)
    resultados['recomendaciones'] = ['Item A', 'Item B', 'Item C']
    print(colored("Backend: Recomendaciones listas", 'yellow'))

def procesar_logs(resultados):
    print(colored("Backend: Procesando logs de uso...", 'green'))
    time.sleep(2)
    resultados['logs'] = ['Usuario1: Item A', 'Usuario2: Item C']
    print(colored("Backend: Logs procesados", 'green'))

def procesar_union(resultados):
    print(colored("Backend: Procesando unión de resultados...", 'cyan'))
    recomendaciones = resultados.get('recomendaciones', [])
    logs = resultados.get('logs', [])
    
    usados = [item for item in recomendaciones if any(item in log for log in logs)]
    print(colored(f"Backend: Ítems recomendados y usados: {usados}", 'cyan'))

if __name__ == '__main__':
    with Manager() as manager:
        resultados = manager.dict()

        p1 = Process(target=generar_recomendaciones, args=(resultados,))
        p2 = Process(target=procesar_logs, args=(resultados,))

        p1.start()
        p2.start()

        p1.join()
        p2.join()

        procesar_union(resultados)