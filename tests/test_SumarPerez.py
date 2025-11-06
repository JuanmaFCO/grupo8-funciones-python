#tests/test_sumar.py
from funciones.sumarRamirez import sumar # type: ignore

def test_sumarRamirez():
 assert sumar(3, 5) == 8
 assert sumar(-2, 2) == 0