def division_cabrera(a, b):
    """
    Devuelve el resultado de dividir 'a' entre 'b'.
    Si el divisor es 0, lanza una excepción ValueError.
    """
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b
