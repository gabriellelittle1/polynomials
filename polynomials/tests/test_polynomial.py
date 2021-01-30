from polynomials import Polynomial
import pytest

def test_print():
    p = Polynomial((2,1,0,3))
    
    assert str(p) == "3x^3 + x + 2"

@pytest.mark.parametrize(
    "a, b, sub",
    ( ((0,), (0,1), (0, -1) ), 
    ( (2, 0, 3), (1, 2), (1, -2, 3) ),
    ( (4, 2), (10, 2, 4), (-6, 0, -4) ) )
)

def test_sub(a, b, sub):
    assert Polynomial(a) - Polynomial(b) == Polynomial(sub)
