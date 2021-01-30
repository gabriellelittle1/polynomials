from polynomials import Polynomial
import pytest


@pytest.mark.parametrize(
    "a, d",
    ( ((0,), (0,)), 
    ( (2, 0, 3), (0, 6)),
    ( (4, 2), (2,) ) )
)

def test_deriv(a, d):
    assert Polynomial(deriv(a)) == Polynomial(d)
