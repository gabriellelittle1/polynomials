from polynomials import Polynomial, deriv
import pytest


@pytest.mark.parametrize(
    "a, d",
    ( (Polynomial((0,)), Polynomial((0,))), 
    ( Polynomial((2, 0, 3)), (Polynomial((0, 6)))),
    ( Polynomial((4, 2)), Polynomial((2,)) ) )
)

def test_deriv(a, d):
    assert deriv(a) == d
