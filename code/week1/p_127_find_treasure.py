""" 
#127 Find Captain Redbeard's Hidden Treasure
Суть: найти точку глобального минимума через производную из полинома
Статус: решено

"""

def find_treasure(start_x: float) -> float:
    """
    d1 = 4*x**3 - 9*x**2
    roots = x**2(4*x - 9) => x1 = 0, x2 = 9/4
    d2 = 12*x**2 - 18*x
    d2 = 12 * 81/16 - 18 * 9/4 = 20.25

    """
    return 9/4
    