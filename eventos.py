import asyncio
from termcolor import colored

# Servicios que escuchan eventos
async def enviar_notificacion(usuario, evento):
    print(colored(f"[Notificador] Notificando a {usuario} sobre evento '{evento}'", 'yellow'))
    await asyncio.sleep(1)
    print(colored(f"[Notificador] Notificación enviada a {usuario}", 'yellow'))

async def registrar_log(usuario, evento):
    print(colored(f"[Logger] Registrando evento '{evento}' de {usuario}", 'cyan'))
    await asyncio.sleep(1)
    print(colored(f"[Logger] Evento registrado", 'cyan'))

# Función que genera el evento
async def leer_libro(usuario):
    print(colored(f"{usuario} está leyendo un libro...", 'green'))
    await asyncio.sleep(2)
    print(colored(f"{usuario} terminó de leer", 'green'))
    
    evento = "lectura_terminada"

    # Disparar eventos de forma que no bloquee el flujo del sistema
    tarea_notificacion = asyncio.create_task(enviar_notificacion(usuario, evento))
    tarea_log = asyncio.create_task(registrar_log(usuario, evento))

    print(colored(f"{usuario} siguió con otros procesos", 'green'))
    
    await asyncio.gather(tarea_notificacion, tarea_log)


asyncio.run(leer_libro("Usuario 1"))
