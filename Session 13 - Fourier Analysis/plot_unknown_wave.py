# plot_unknown_wave.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Read data from data file
file_name = "unknown_wave.csv"
file_path = Path(__file__).parent / file_name
data = np.genfromtxt(file_path, delimiter=",")

# unpack data
x_known, y_known = data.T

alpha = 10
beta = 3

t = np.linspace(0, 2 * np.pi, 1000)
y = 2 * np.sin(alpha * t) * np.cos(beta * t)

plt.figure(Path(__file__).name)
plt.title("QIS102 Task 13-03: Unknown Wave")
plt.plot(t, y_known, color="red", lw=2, label="Known Value")
plt.plot(t, y, label="Guessed curve")
plt.legend(loc="upper right")
plt.grid("on")
plt.show()
