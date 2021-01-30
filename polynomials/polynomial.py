from .polynomials import Polynomial


def deriv(poly):
    polylist = list(poly.coefficients)
    for i in range(len(poly)):
        polylist[i] = i*poly[i]
    newpolycoef = tuple(polylist.pop())
    return Polynomial(newpolycoef)


    

        
        