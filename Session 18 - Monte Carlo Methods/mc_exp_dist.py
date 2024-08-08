# mc_parabola.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from numba import float64, vectorize

"Help from Dr. Biersach"


@vectorize([float64(float64, float64)], nopython=True)
def halton(n, p):
    h, f = 0, 1
    while n > 0:
        f = f / p
        h += (n % p) * f
        n = int(n / p)
    return h


def f(x, rate_p, y):
    return rate_p * np.exp(-rate_p * x) - y


def g(x, rate_p):
    return 1 - np.exp(-rate_p * x)


def main():
    dots = 500000
    rate_p = 90 / 60

    x = halton(np.arange(dots), 2)
    y = (halton(np.arange(dots), 3)) * 2

    d = f(x, rate_p, y)

    x_in = x[d <= 0.0]
    y_in = y[d <= 0.0]
    x_out = x[d > 0.0]
    y_out = y[d > 0.0]

    act = g(1, rate_p) - g(0, rate_p)
    # Sample area is (-2 to 2)x(0 to 5) = 20
    est = np.count_nonzero(d >= 0.0) / dots * 2
    err = np.abs((est - act) / act)

    print(f"dots = {dots:,}")
    print(f"act = {act:.6f}")
    print(f"est = {est:.6f}")
    print(f"err = {err:.5%}")

    act_x = np.linspace(0, 1, 1000)
    act_y = f(act_x, rate_p, 0)

    plt.figure(Path(__file__).name)
    plt.scatter(x_in, y_in, color="red", marker=".", s=0.5)
    plt.scatter(x_out, y_out, color="blue", marker=".", s=0.5)
    plt.plot(act_x, act_y, color="green", lw=2, label=r"$\lambda e^{-\lambda x}$")
    plt.title("$x=1-np.exp(-(landa)*x)$")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


main()
