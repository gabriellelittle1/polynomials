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

@pytest.mark.parametrize(
    "a, b, prod",
    ( ((0,), (0,1), (0,0) ), 
    ( (2, 0, 3), (1, 2), (2, 4, 3, 6)),
    ( (4, 2), (10, 2, 4), (40, 28, 20, 8) )))

def test_mult(a, b, prod):
    assert Polynomial(a)*Polynomial(b) == Polynomial(prod)

@pytest.mark.parametrize(
    "a, b, pow",
    ( ((3, 4, 5, 6), 1, (3, 4, 5, 6) ), 
    ( (5, 2), 4, (625, 1000, 600, 160, 16)),
    ( (0, 0, 3), 5, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 243 ))))

def test_pow(a, b, pow):
    assert Polynomial(a)**b == Polynomial(pow)

@pytest.mark.parametrize(
    "a, b, fx",
    ( ((3, 4, 5, 6), 1, 18), 
    ( (5, 2), 4, 13),
    ( (3,), 5, 3)))
    

def test_call(a, b, fx):
    assert Polynomial(a).__call__(b)==fx
    



