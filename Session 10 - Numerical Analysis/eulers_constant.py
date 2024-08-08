from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


def f(x):
    return np.log(np.log(1 / x))


def main():
    gamma = -(quad(f, 0, 1)[0])
    print(gamma)
    x = range(1, 52)
    gamma_log = gamma + np.log(x)  # noqa: F841
    print(gamma_log)
    HN = [0]
    for i in range(1, 51):
        eq = (1 / i) + HN[-1]
        HN.append(eq)
    print(HN)
    plt.figure(Path(__file__).name)
    plt.step(x,HN)
    plt.plot(x,gamma_log)
    plt.title("HN vs gamma log")
    plt.xlabel("x")
    plt.grid()
    plt.show()


main()


