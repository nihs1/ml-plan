"""

#184 Empirical Probability Mass Function (PMF)
Суть: вероятность по выборке и исходам


"""


def empirical_pmf(samples):
    nondup = set(samples)
    amo = [samples.count(i) for i in nondup]
    probalites = [el/len(samples) for el in amo]

    return list(zip(nondup, probalites))