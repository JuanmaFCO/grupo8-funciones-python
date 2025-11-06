from funciones.factorial_genez import factorial

def test_factorial_cero():
    assert factorial(0) == 1

def test_factorial_uno():
    assert factorial(1) == 1

def test_factorial_cinco():
    assert factorial(5) == 120

def test_factorial_numero_grande():
    assert factorial(10) == 3628800

def test_factorial_negativo():
    try:
        factorial(-1)
        assert False, "Debería haber lanzado ValueError"
    except ValueError:
        assert True
