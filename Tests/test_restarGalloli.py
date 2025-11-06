#tests/test_restar.py

from funciones.restarGalloli import restar

def test_restar():
 assert restar(10, 4) == 6
 assert restar(5, 10) == -5