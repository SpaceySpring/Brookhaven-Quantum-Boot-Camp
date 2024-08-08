# plot3d_complex_sine.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import LinearLocator

"""Most of the code taken from Dr.Biersach"""

def f(x, y):
    return abs(np.sin(x+y*1j))


def main():
    x = np.linspace(-2.5, 2.5, 100)
    y = np.linspace(-1, 1, 100)
    x, y = np.meshgrid(x, y)
    z = f(x, y)

    plt.figure(Path(__file__).name)
    ax = plt.axes(projection="3d")

    surf = ax.plot_surface(x, y, z, cmap="coolwarm", lw=0, antialiased=False)
    plt.colorbar(surf, ax=ax, shrink=0.5)

    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter("{x:.02f}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    plt.show()


main()
