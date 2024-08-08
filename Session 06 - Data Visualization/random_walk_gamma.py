from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.special import gamma

"""these are my corrections with help of Dr. Biersach"""
# Number of dimensions
d = 2

# Walks increase in length from 1 to max_steps
max_steps = 25

# Number of times a walk of each length is repeated to find its average
N = 20_000

print("This may take up to 30 seconds . . .")
steps = np.linspace(1, max_steps, 100)
distances = (np.sqrt(2 * N / steps) * (gamma((steps + 1) / 2)) / gamma(steps / 2)) ** 2

plt.figure(Path(__file__).name, figsize=(12, 5))

ax = plt.subplot(1, 2, 1)
ax.plot(steps, distances)
ax.set_title(f"Uniform Random Walk on {d}-D Unit Lattice")
ax.set_xlabel("Number of Steps")
ax.set_ylabel("Mean Final Distance")

plt.show()
