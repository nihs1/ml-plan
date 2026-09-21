"""
#79 Binomial Distribution Probability
# Суть: функция, находящая вероятность ровно k положительных случаев в n независимых испытаниях

"""

from math import factorial as fact

def binomial_probability(n: int, k: int, p: float) -> float:
    P = (fact(n) / (fact(k) * fact((n - k)))) * (p**k) * (1 - p)**(n - k)
    return P