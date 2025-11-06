
# test_potenciaBenitez.py

from Funciones.potenciaBenitez import potencia

def test_potenciaBenitez():
    assert potencia(2, 3) == 8
    assert potencia(5, 0) == 1

