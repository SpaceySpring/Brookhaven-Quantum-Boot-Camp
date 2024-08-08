# epidemiology.py

from pathlib import Path

import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

"Help from chatGPT"


def model(time, state_vector, r, l, c):
    i_0, dI_dt = state_vector  # Unpacking the variables
    dI2_dt2 = -(r / l) * dI_dt - (1 / (l * c)) * i_0
    return [dI_dt, dI2_dt2]


def main():
    # Set model duration
    t_0, t_f = 0, 1  # time

    # Set simulation constants
    r = 0.1  # Ohms
    l = 0.01  # Henries
    c = 0.01  # Farads

    # Set initial conditions
    i_0 = 1  # Initial amp
    dI_dt_0 = 0  # Initial voltage

    # fmt: off
    sol = solve_ivp(model, (t_0, t_f), [i_0,dI_dt_0],
        max_step=0.001, args=(r, l, c))
    # fmt: on

    # Retrieve results of the solution
    t = sol.t
    I = sol.y[0]

    # Plot S-I-R compartment populations over time
    plt.figure(Path(__file__).name)
    plt.plot(t, I, lw=2, label="Susceptible")
    plt.title("RIC Circuit")
    plt.xlabel("Time (Sec)")
    plt.ylabel("Current (Amp)")
    plt.legend(loc="upper right")
    plt.axhline(y=0, color="lightgrey")
    plt.grid()
    plt.show()


main()
