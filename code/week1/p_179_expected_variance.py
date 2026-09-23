"""

#179 Expected Value and Variance of an n-Sided Die
Суть: мат. ожидание и дисперсия результата броска кубика с n гранями

"""


def dice_statistics(n: int) -> tuple[float, float]:
	expected = float((n + 1)/2)
	variance = float(((n + 1)*(2*n + 1)/6) - ((n + 1)/2)**2)
	return expected, variance
	