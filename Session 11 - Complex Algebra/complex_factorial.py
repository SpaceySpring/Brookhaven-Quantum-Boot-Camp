# oscillating_integrand.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

"code from Dr. Biersach"


def f(x):
    return np.exp(-x) * np.cos(np.log(x))


def g(x):
    return np.exp(-x) * np.sin(np.log(x))


def main():
    integral_f = quad(f, 0, 1000)[0]
    integral_g = quad(g, 0, 1000)[0]

    factorial = complex(integral_f, integral_g)

    print(f"i! = {factorial:.4f}")


main()
