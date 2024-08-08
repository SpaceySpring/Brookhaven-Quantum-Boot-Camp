from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

"Modified code from Dr. Biersach"


def f(x):
    return 1 / (1 + x**2)


# Power Series for f(x)
# See https://www.youtube.com/watch?v=pADUvK6bcW4
def p_f(x, num_terms):
    y = 0.0
    for n in range(num_terms):
        y += (-(x**2)) ** n  # this would be out i!
    return y


def main():
    # Plot exact formula
    x = np.linspace(-1.5, 1.5, 1000)
    plt.figure(Path(__file__).name)
    plt.plot(x, f(x), label="Exact")

    # Plot power series with increasing number of terms
    v = np.vectorize(p_f, excluded=("num_terms"))
    for n in range(2, 8):
        plt.plot(x, v(x, num_terms=n), label=f"{n} terms")

    # Defining plot
    plt.title("Runge's Phenomenon (Witch of Agnesi)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.ylim(-2, 2)
    plt.axvline(1.0, color="black", linestyle="--", lw=2)
    plt.axvline(-1.0, color="black", linestyle="--", lw=2)
    plt.legend(loc="lower center")
    plt.grid()
    plt.show()


main()
