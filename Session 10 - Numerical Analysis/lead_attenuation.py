from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d  # Interpolation


def main():
    file_name = "lead_attenuation.csv"
    file_path = Path(__file__).parent / file_name
    # Note: this is NOT a CSV file and has no header row
    samples = np.genfromtxt(file_path, delimiter=",")  # Column separated by spaces
    energy, saf = samples.T  # Unpacking

    min_energy, max_energy = (
        np.min(energy),
        np.max(energy),
    )  # Creates the points for the curve
    energy_est = np.linspace(min_energy, max_energy, 1000)

    saf_f = interp1d(energy, saf, kind="cubic")  # Returns a interpolation function
    saf_est = saf_f(energy_est)  # Gets back array

    muE = saf_f(4.65)
    print(muE)
    N = 1 * np.exp(-muE * 2)
    print(N)
    print(f"{N:%}")

    plt.figure(Path(__file__).name)
    plt.scatter(energy, saf)

    plt.semilogy(energy_est, saf_est)

    plt.xlabel("Photon Energy [MeV]")
    plt.ylabel(r"Lead Shield’s Attenuation Factor")  # \; gives white space
    plt.title("Lead Attenuation Coefficient")
    plt.show()


main()
