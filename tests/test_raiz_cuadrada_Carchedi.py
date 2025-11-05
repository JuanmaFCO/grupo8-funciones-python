import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from funciones.raiz_cuadrada_Carchedi import raiz_cuadrada

def test_raiz_cuadrada():
    assert raiz_cuadrada(25) == 5.0
    assert raiz_cuadrada(100) == 10.0
