from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

# Number of trials
n = 1000

# Array of integers from 0 to n (inclusive)
r_values = np.arange(n + 1)


# the given parameters p= 1, p= 2, p= 5
dist1 = (
    np.sqrt(2 / 3.14)
    * (r_values) ** 2
    / 1**3
    * (np.exp((-((r_values) ** 2)) / (2 * 1**2)))
)
dist2 = (
    np.sqrt(2 / 3.14)
    * (r_values) ** 2
    / 2**3
    * (np.exp((-((r_values) ** 2)) / (2 * 2**2)))
)
dist3 = (
    np.sqrt(2 / 3.14)
    * (r_values) ** 2
    / 5**3
    * (np.exp((-((r_values) ** 2)) / (2 * 5**2)))
)

# Use matplotlib bar plot to show each r_value
# with its associated probability of occurrence
plt.figure(Path(__file__).name)
plt.plot(r_values, dist1, label="p = 1", linewidth=5)
plt.plot(r_values, dist2, label="p = 2", linewidth=5)
plt.plot(r_values, dist3, label="p = 5", linewidth=5)
plt.title(f"Binomial Distribution (n={n} trials)")
plt.xlim(0, 20)
plt.ylim(0, 0.6)
plt.xlabel("Number of Successes")
plt.ylabel("Probability")
ax = plt.gca()
ax.legend(loc="upper right")
ax.xaxis.set_major_locator(MultipleLocator(5))
plt.show()

"""Modified code from Dr. Biersach"""
