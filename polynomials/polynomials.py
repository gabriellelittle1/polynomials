from numbers import Number, Integral

class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):

        return len(self.coefficients) - 1
    
    def __str__(self):

        terms = []
        coefs = self.coefficients

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1]==1 else coefs[1]}x")

        terms += [f"{'' if c ==1 else c}x^{d}"
                    for d,c in enumerate(coefs[2:], start = 2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __eq__(self, other):

        return self.coefficients == other.coefficients

    def __add__(self, other):
        if isinstance(other,Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a,b in zip(self.coefficients, other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]
            
            return Polynomial(coefs)
       
        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0]+other,) + self.coefficients[1:])
        
        else: 
            return NotImplemented      

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other,Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a - b for a,b in zip(self.coefficients[0:common], other.coefficients[0:common]))
            ocoefs = tuple(0 for i in range(common))
            ocoefs += tuple(-1*c for c in other.coefficients[common:])
            coefs += self.coefficients[common:] + ocoefs[common:]
    
            
            return Polynomial(coefs)
       
        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0]-other,) + self.coefficients[1:])
        
        else: 
            return NotImplemented

    def __rsub__(self, other):
        return other - self

    def __mul__(self, other):
        degree = self.degree()+other.degree()
        mult = [0 for i in range(degree+1)]


        if isinstance(other, Polynomial):
            for i in range(self.degree()+1):
                for j in range(other.degree()+1):
                    mult[i+j] += self.coefficients[i]*other.coefficients[j]
            mult = tuple(mult)
            return Polynomial(mult)

        elif isinstance(other, Number):
            coefs = tuple(other*a for a in self.coefficients)
            return Polynomial(coefs)

        else:
            return NotImplemented
    
    def __rmul__(self, other):
        return self*other

    def __pow__(self, num):
        if isinstance(num, Integral):
            vec = [0 for i in range(num)]
            vec[0] = self
            for i in range(1,num):
                vec[i] = self*vec[i-1]
                
            return vec[num-1]
        else:
            return NotImplemented

    def __call__(self, x):
        fx = 0
        for i in range(len(self.coefficients)):
            fx += self.coefficients[i]*x**i
        return fx









