import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from funciones.sumarRamirez import sumar

def test_sumar():
    assert sumar(10, 5) == 15
    assert sumar(-1, 1) == 0
