""" 
#116 Derivative of a Polynomial
Суть: найти производную из полинома
Статус: решено

"""

def poly_term_derivative(c: float, x: float, n: float) -> float:
    return c * n * x ** (n-1)