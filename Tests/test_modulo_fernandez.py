# test/test_modulo_fernandez.py

from funciones.modulo_fernandez import modulo_fernandez

def test_modulo_fernandez():
    assert modulo_fernandez(10, 3) == 1
    assert modulo_fernandez(7, 0) is None
