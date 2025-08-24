import asyncio
from termcolor import colored

async def leer_libro(usuario, duracion):
    print(colored(f"{usuario} empieza a leer un libro", 'green'))
    await asyncio.sleep(duracion)
    print(colored(f"{usuario} termina de leer el libro", 'green'))

async def dejar_comentario(usuario, duracion):
    print(colored(f"{usuario} empieza a escribir un comentario", 'cyan'))
    await asyncio.sleep(duracion)
    print(colored(f"{usuario} publica su comentario", 'cyan'))

async def main():
    await asyncio.gather(
        leer_libro("Usuario 1", 3),
        dejar_comentario("Usuario 2", 2),
    )

asyncio.run(main())
