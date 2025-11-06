import pytest
from funciones.divisionCabrera import division_cabrera

def test_division_cabrera():
    assert division_cabrera(10, 2) == 5
    assert division_cabrera(-9, 3) == -3
    assert division_cabrera(7.5, 2.5) == 3

    # Verifica que se lance la excepción al dividir por cero
    with pytest.raises(ValueError):
        division_cabrera(5, 0)
