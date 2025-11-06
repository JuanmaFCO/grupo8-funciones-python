# funciones/factorial_genez.py
def factorial(n):
    """
    Calcula el factorial de un número entero no negativo.
    """
    if n < 0:
        raise ValueError("El número debe ser no negativo")
    if n == 0:
        return 1
    return n * factorial(n - 1)