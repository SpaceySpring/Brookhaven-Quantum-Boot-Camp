from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

"Dr.Biersach code modified"


def count_lattice_points():
    num_points = 0
    for x in range(-500, 500):
        for y in range(-500, 500):
            if abs(x**2 - y**2 - y + 1) <= 10 and abs(2 * x * y + x) <= 10:
                num_points += 1
    print(f"There are {num_points:,} lattice points")


def f(z):
    return z**2 + z * 1j + 1


def main():
    count_lattice_points()

    x = np.linspace(-4, 4, 1000)
    y = np.linspace(0, 2, 1000)
    x, y = np.meshgrid(x, y)
    z = f(x + y * 1j)

    plt.figure(Path(__file__).name)
    ax = plt.gca()
    pixel_size = 72 / ax.figure.dpi**2
    plt.scatter((np.real(z)), np.imag(z), marker="o", lw=0, s=pixel_size)
    plt.title(r"$f(z)=z^2+iz+1$")
    plt.xlabel("Real")
    plt.ylabel("imaginary")
    ax.set_aspect("equal")
    plt.show()


main()
