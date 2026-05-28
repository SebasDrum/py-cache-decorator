from typing import Callable


def cache(func: Callable) -> Callable:
    
    memoria = {}
    
    def wrapper(*args, **kwargs):

        clave = (args, tuple(sorted(kwargs.items())))

        if clave in memoria:
            print("Getting from cache")
            return memoria[clave]

        print("Calculating new result")
        resultado = func(*args, **kwargs)
        memoria[clave] = resultado
        return resultado

    return wrapper
