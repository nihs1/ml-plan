"""

#81 Poisson Distribution Probability Calculator
Суть: определить вероятность наступления события k раз в заданном интервале 

"""

import math

def poisson_probability(k, lam):
	val = (lam**k * 2.71828**(-lam)) / math.factorial(k)
	return round(val,5)