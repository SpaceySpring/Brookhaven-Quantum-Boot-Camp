from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return np.sin(0.8 * x)


def g(x):
    return np.sin(0.5 * x)


def h(x):
    return f(x) * g(x)


def w_p(x):
    return (0.5) * (np.cos((0.8 * x) - (0.5 * x)) - np.cos((0.8 * x) + (0.5 * x)))


def main():
    # Plot formulas
    x = np.linspace(-3 * np.pi, 3 * np.pi, 100)
    plt.figure(Path(__file__).name)
    plt.plot(x, f(x), label="f(x)", color="black", lw=2)
    plt.plot(x, g(x), label="g(x)", color="red", lw=2)
    plt.plot(x, h(x), label="h(x)", color="blue", lw=2)
    plt.scatter(x, w_p(x), label="w_p(x)", edgecolor="grey", facecolor="none")

    # Defining plot
    plt.title("Werner formula")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend(loc="upper right")
    plt.grid()
    plt.show()


main()
