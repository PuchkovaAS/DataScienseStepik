import math

import numpy as np
from scipy.linalg import solve


def f(x):
    return math.sin(x / 5) * math.exp(x / 10) + 5 * math.exp(-x / 2)


def get_polynomials(m, p):
    b = np.array(list(map(f, m)))
    A = []
    for x in m:
        l = []
        for level in range(p, -1, -1):
            l.append(x ** level)
        A.append(l)
    A = np.array(A)
    return solve(A, b)


result1 = get_polynomials(np.array([1, 15]), 1)
print(result1)
